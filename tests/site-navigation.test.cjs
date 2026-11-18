const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");

const root = path.resolve(__dirname, "..");
const source = fs.readFileSync(path.join(root, "Retchan.py"), "utf8");
const home = source.match(/HTML = r'''([\s\S]*?)'''/)[1];
const signIn = fs.readFileSync(path.join(root, "public", "sign-in.html"), "utf8");

test("home page sidebar links to party lobbies, communities, and chat", () => {
	assert.match(home, /<a href="#parties">Parties &amp; lobbies<\/a>/);
	assert.match(home, /<a href="#communities">Communities<\/a>/);
	assert.match(home, /<a href="#chat">Chats<\/a>/);
	assert.match(home, /<section id="parties">/);
});

test("sign-in is a separate Supabase page and links the policies", () => {
	assert.doesNotMatch(home, /<section id="login"/);
	assert.match(home, /href="sign-in\.html"/);
	assert.ok(signIn.indexOf('id="title-screen"') < signIn.indexOf('id="sign-in-options"'));
	assert.match(signIn, /id="sign-in-options"[^>]*hidden/);
	assert.match(signIn, /id="open-sign-in"/);
	assert.match(signIn, /supabase\.auth\.signInWithPassword/);
	assert.match(signIn, /auth: \{ experimental: \{ passkey: true \} \}/);
	assert.match(signIn, /id="passkey-sign-in"[^>]*data-passkey/);
	assert.match(signIn, /id="register-passkey"[^>]*data-passkey/);
	assert.match(signIn, /<div id="signed-in-panel" hidden>[\s\S]*?id="register-passkey"/);
	assert.match(signIn, /supabase\.auth\.signInWithPasskey\(\)/);
	assert.match(signIn, /supabase\.auth\.registerPasskey\(\)/);
	assert.match(signIn, /terms\.html/);
	assert.match(signIn, /privacy\.html/);
	assert.ok(fs.existsSync(path.join(root, "public", "terms.html")));
	assert.ok(fs.existsSync(path.join(root, "public", "privacy.html")));
});

test("community, chat, teammate, and party controls stay enabled with clear feedback", () => {
	for (const sectionId of ["profiles", "teammates", "parties", "chat"]) {
		const section = home.match(new RegExp(`<section id="${sectionId}"[\\s\\S]*?</section>`));
		assert.ok(section, `expected #${sectionId} section`);
		assert.doesNotMatch(section[0], /\sdisabled(?:\s|>|=)/);
	}
	assert.match(home, /id="profile-save-status"/);
	assert.match(home, /id="teammate-results-status"/);
	assert.match(home, /id="party-action-status"/);
	assert.match(home, /id="chat-status"/);
	assert.match(home, /id="create-party-button"/);
	assert.match(home, /href="mailto:[^"]+Request%20a%20Fortnite%20community%20invite/);
});

test("game feed replaces VALORANT with requested and relevant multiplayer titles", () => {
	assert.doesNotMatch(home, /valorant/i);
	const cards = [...home.matchAll(/<article class="card game-card" data-game="([^"]+)">/g)];
	assert.equal(cards.length, 18);

	for (const game of [
		"Counter-Strike 2",
		"Dota 2",
		"Delta Force",
		"Rust",
		"PUBG: BATTLEGROUNDS",
		"Call of Duty: Warzone",
		"Need for Speed"
	]) {
		assert.ok(home.includes(`<h3>${game}</h3>`), `missing feed card for ${game}`);
	}

	const gameFilter = home.match(/<select id="game-filter">([\s\S]*?)<\/select>/)[1];
	for (const gameId of [
		"counter-strike-2",
		"dota-2",
		"delta-force",
		"rust",
		"pubg-battlegrounds",
		"call-of-duty-warzone",
		"need-for-speed"
	]) {
		assert.ok(gameFilter.includes(`value="${gameId}"`), `missing filter option for ${gameId}`);
	}
	assert.match(home, /store\.steampowered\.com\/charts\/mostplayed/);
});
