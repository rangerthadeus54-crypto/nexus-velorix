const assert = require("node:assert/strict");
const test = require("node:test");
const { getEventPage } = require("../events-provider.cjs");
const eventsHandler = require("../api/events.js");

function createResponse() {
	return {
		headers: {},
		statusCode: 200,
		body: null,
		setHeader(name, value) {
			this.headers[name] = value;
		},
		status(code) {
			this.statusCode = code;
			return this;
		},
		json(body) {
			this.body = body;
			return this;
		}
	};
}

test("requires a server-side provider token", async () => {
	const previousToken = process.env.PANDASCORE_TOKEN;
	delete process.env.PANDASCORE_TOKEN;
	try {
		await assert.rejects(getEventPage(1), (error) => error.statusCode === 503);
	} finally {
		if (previousToken === undefined) delete process.env.PANDASCORE_TOKEN;
		else process.env.PANDASCORE_TOKEN = previousToken;
	}
});

test("returns live and future scheduled events, excluding past fixtures", async () => {
	const previousToken = process.env.PANDASCORE_TOKEN;
	const previousFetch = global.fetch;
	const requests = [];
	process.env.PANDASCORE_TOKEN = "test-token";
	global.fetch = async (url, options) => {
		requests.push({ url: new URL(url), options });
		const isRunning = new URL(url).pathname.endsWith("/running");
		const payload = isRunning
			? [{
				id: 51,
				status: "running",
				name: "Live final",
				scheduled_at: new Date(Date.now() - 60_000).toISOString(),
				videogame: { name: "Fortnite" },
				opponents: [{ opponent: { name: "Team A" } }, { opponent: { name: "Team B" } }],
				streams_list: [{ official: true, raw_url: "https://stream.example/live" }]
			}]
			: [
				{
					id: 52,
					status: "not_started",
					name: "Upcoming final",
					scheduled_at: new Date(Date.now() + 60 * 60_000).toISOString(),
					videogame_title: { name: "VALORANT" },
					tournament: { name: "Regional Cup" }
				},
				{
					id: 53,
					status: "not_started",
					name: "Past fixture",
					scheduled_at: new Date(Date.now() - 60_000).toISOString(),
					videogame: { name: "Minecraft" }
				}
			];
		return { ok: true, json: async () => payload };
	};

	try {
		const result = await getEventPage(2);
		assert.deepEqual(result.events.map((event) => event.id), ["51", "52"]);
		assert.equal(result.events[0].isLive, true);
		assert.equal(result.events[0].officialStream, "https://stream.example/live");
		assert.equal(result.events[1].game, "VALORANT");
		assert.equal(result.events[1].competition, "Regional Cup");
		assert.equal(requests.length, 2);
		assert.ok(requests.every(({ options }) => options.headers.Authorization === "Bearer test-token"));
		assert.ok(requests.every(({ url }) => url.searchParams.get("page") === "2"));
	} finally {
		global.fetch = previousFetch;
		if (previousToken === undefined) delete process.env.PANDASCORE_TOKEN;
		else process.env.PANDASCORE_TOKEN = previousToken;
	}
});

test("rejects page numbers outside the provider paging limit", async () => {
	await assert.rejects(getEventPage(11), (error) => error.statusCode === 400);
});

test("Vercel endpoint reports missing provider configuration as an error", async () => {
	const previousToken = process.env.PANDASCORE_TOKEN;
	delete process.env.PANDASCORE_TOKEN;
	const response = createResponse();
	try {
		await eventsHandler({ method: "GET", url: "/api/events?page=1", query: { page: "1" } }, response);
		assert.equal(response.statusCode, 503);
		assert.match(response.body.error, /PANDASCORE_TOKEN/);
		assert.equal(response.headers["Cache-Control"], "no-store");
	} finally {
		if (previousToken === undefined) delete process.env.PANDASCORE_TOKEN;
		else process.env.PANDASCORE_TOKEN = previousToken;
	}
});

test("Vercel endpoint rejects non-GET requests", async () => {
	const response = createResponse();
	await eventsHandler({ method: "POST", url: "/api/events" }, response);
	assert.equal(response.statusCode, 405);
	assert.equal(response.headers.Allow, "GET");
});
