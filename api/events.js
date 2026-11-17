const { getEventPage } = require("../events-provider.cjs");

module.exports = async function eventsHandler(request, response) {
	response.setHeader("Content-Type", "application/json; charset=utf-8");
	response.setHeader("X-Content-Type-Options", "nosniff");
	response.setHeader("Cache-Control", "no-store");

	if (request.method !== "GET") {
		response.setHeader("Allow", "GET");
		return response.status(405).json({ error: "Only GET requests are supported." });
	}

	try {
		const page = request.query?.page ?? new URL(request.url, "https://localhost").searchParams.get("page");
		const feed = await getEventPage(page);
		response.setHeader("Cache-Control", "public, s-maxage=300, stale-while-revalidate=60");
		return response.status(200).json(feed);
	} catch (error) {
		const statusCode = Number.isInteger(error.statusCode) ? error.statusCode : 502;
		return response.status(statusCode).json({
			error: error.message || "The live event feed could not be loaded."
		});
	}
};
