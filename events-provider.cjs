const API_BASE = "https://api.pandascore.co";
const PAGE_SIZE = 100;
const MAX_PAGE = 10;
const CACHE_TTL_MS = 5 * 60 * 1000;
const pageCache = new Map();

function feedError(message, statusCode) {
	const error = new Error(message);
	error.statusCode = statusCode;
	return error;
}

function parsePage(value) {
	const page = Number(value ?? 1);
	if (!Number.isInteger(page) || page < 1 || page > MAX_PAGE) {
		throw feedError(`Page must be a whole number from 1 to ${MAX_PAGE}.`, 400);
	}
	return page;
}

function httpsUrl(value) {
	if (typeof value !== "string") return null;
	try {
		const url = new URL(value);
		return url.protocol === "https:" ? url.href : null;
	} catch {
		return null;
	}
}

function normalizeMatch(match, isLive) {
	if (!match || typeof match !== "object") return null;
	const id = match.id ?? match.slug;
	if (id === undefined || id === null) return null;

	const startTime = Date.parse(match.scheduled_at);
	if (!isLive && (!Number.isFinite(startTime) || startTime <= Date.now())) return null;

	const opponents = Array.isArray(match.opponents)
		? match.opponents
			.map((entry) => entry?.opponent?.name)
			.filter((name) => typeof name === "string" && name.trim())
		: [];
	const officialStream = Array.isArray(match.streams_list)
		? match.streams_list.find((stream) => stream?.official === true && httpsUrl(stream.raw_url))
		: null;

	return {
		id: String(id),
		game: match.videogame_title?.name || match.videogame?.name || "Other game",
		competition: match.tournament?.name || match.serie?.full_name || match.league?.name || "Esports competition",
		name: match.name || (opponents.length ? opponents.join(" vs ") : "Scheduled match"),
		startAt: Number.isFinite(startTime) ? new Date(startTime).toISOString() : null,
		isLive,
		officialStream: officialStream ? httpsUrl(officialStream.raw_url) : null
	};
}

async function fetchMatches(kind, page, token) {
	const url = new URL(`${API_BASE}/matches/${kind}`);
	url.searchParams.set("page", String(page));
	url.searchParams.set("per_page", String(PAGE_SIZE));
	url.searchParams.set("sort", "scheduled_at");

	const controller = new AbortController();
	const timeout = setTimeout(() => controller.abort(), 8000);
	let response;
	try {
		response = await fetch(url, {
			headers: {
				Accept: "application/json",
				Authorization: `Bearer ${token}`
			},
			signal: controller.signal
		});
	} catch (error) {
		if (error.name === "AbortError") {
			throw feedError("PandaScore did not respond before the request timed out.", 504);
		}
		throw feedError("Could not reach PandaScore. Try again shortly.", 502);
	} finally {
		clearTimeout(timeout);
	}

	if (!response.ok) {
		throw feedError(`PandaScore returned HTTP ${response.status}. Check the server-side token and provider access.`, 502);
	}

	let matches;
	try {
		matches = await response.json();
	} catch {
		throw feedError("PandaScore returned an unreadable response.", 502);
	}
	if (!Array.isArray(matches)) {
		throw feedError("PandaScore returned data in an unexpected format.", 502);
	}
	return matches;
}

async function getEventPage(pageValue) {
	const page = parsePage(pageValue);
	const token = process.env.PANDASCORE_TOKEN;
	if (typeof token !== "string" || !token.trim()) {
		throw feedError("The live feed is not configured. Add PANDASCORE_TOKEN as a Vercel server-side environment secret.", 503);
	}

	const cached = pageCache.get(page);
	if (cached && cached.expiresAt > Date.now()) return cached.data;

	const [runningMatches, upcomingMatches] = await Promise.all([
		fetchMatches("running", page, token.trim()),
		fetchMatches("upcoming", page, token.trim())
	]);
	const byId = new Map();
	runningMatches.forEach((match) => {
		const normalized = normalizeMatch(match, true);
		if (normalized) byId.set(normalized.id, normalized);
	});
	upcomingMatches.forEach((match) => {
		const normalized = normalizeMatch(match, false);
		if (normalized && !byId.has(normalized.id)) byId.set(normalized.id, normalized);
	});

	const events = [...byId.values()].sort((left, right) => {
		if (left.isLive !== right.isLive) return left.isLive ? -1 : 1;
		return (left.startAt || "").localeCompare(right.startAt || "");
	});
	const data = {
		provider: "PandaScore",
		page,
		hasMore: runningMatches.length === PAGE_SIZE || upcomingMatches.length === PAGE_SIZE,
		limitReached: page === MAX_PAGE &&
			(runningMatches.length === PAGE_SIZE || upcomingMatches.length === PAGE_SIZE),
		updatedAt: new Date().toISOString(),
		events
	};
	pageCache.set(page, { data, expiresAt: Date.now() + CACHE_TTL_MS });
	return data;
}

module.exports = { getEventPage };
