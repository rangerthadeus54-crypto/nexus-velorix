HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>NEXUS VELORIX — Gaming Community</title>
	<style>
		:root {
			color-scheme: dark;
			--page: #071326;
			--surface: #0c1e39;
			--surface-raised: #10284a;
			--border: #1d4773;
			--text: #f3f8ff;
			--muted: #b7c9e2;
			--blue: #2584ff;
			--cyan: #20d3e8;
			--purple: #a78bfa;
		}

		* { box-sizing: border-box; }

		body {
			margin: 0;
			font-family: system-ui, sans-serif;
			color: var(--text);
			background:
				radial-gradient(ellipse at 12% 0%, rgba(37, 132, 255, 0.2), transparent 34rem),
				radial-gradient(ellipse at 88% 8%, rgba(32, 211, 232, 0.12), transparent 30rem),
				var(--page);
		}

		header, main, footer {
			width: min(100% - 2rem, 1000px);
			margin: auto;
		}

		header {
			display: flex;
			justify-content: space-between;
			align-items: center;
			gap: 1rem;
			padding: 1.25rem 0;
		}

		.logo { display: grid; color: var(--cyan); font-size: 1.3rem; }
		.logo strong { font-weight: 800; letter-spacing: 0.04em; }
		.logo span { color: var(--muted); font-size: 0.8rem; font-weight: 600; }

		nav a {
			color: #d6e8ff;
			text-decoration: none;
		}

		nav { display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 0.5rem 1rem; }
		nav a:hover, nav a:focus-visible { color: var(--cyan); }

		.page-layout {
			display: grid;
			grid-template-columns: 220px minmax(0, 1fr);
			gap: 1.5rem;
			align-items: start;
			width: min(100% - 2rem, 1200px);
			margin: 0 auto;
		}

		.sidebar {
			position: sticky;
			top: 1rem;
			display: grid;
			gap: 0.4rem;
			padding: 1rem;
			border: 1px solid var(--border);
			border-radius: 0.75rem;
			background: rgba(12, 30, 57, 0.94);
		}

		.sidebar h2 { margin: 0 0 0.4rem; font-size: 1rem; }
		.sidebar a {
			padding: 0.65rem 0.75rem;
			border-radius: 0.45rem;
			color: #d6e8ff;
			text-decoration: none;
		}
		.sidebar a:hover, .sidebar a:focus-visible {
			color: var(--cyan);
			background: var(--surface-raised);
		}
		.page-layout main { width: 100%; margin: 0; }

		.hero {
			margin: 2rem 0;
			padding: 4rem 2rem;
			text-align: center;
			border-radius: 1rem;
			border: 1px solid #2862a2;
			background: linear-gradient(135deg, #123f82, #0b1b38 72%);
			box-shadow: 0 18px 48px rgba(0, 7, 22, 0.35);
		}

		.hero h1 { font-size: clamp(2rem, 6vw, 3.5rem); margin: 0 0 1rem; }
		.hero p { color: #d5e5fb; }
		h2 { color: #e2f1ff; }

		.button {
			display: inline-block;
			margin-top: 1rem;
			padding: 0.8rem 1.2rem;
			border-radius: 0.5rem;
			border: 1px solid #51c9f3;
			color: #fff;
			background: linear-gradient(115deg, #176de0, #087fbd 58%, #087e91);
			text-decoration: none;
			font-weight: 700;
			box-shadow: 0 6px 16px rgba(0, 88, 192, 0.2);
		}

		.button:hover, .button:focus-visible {
			background: linear-gradient(115deg, #328bff, #08a9d1 58%, #0ba8a3);
		}

		.button[aria-disabled="true"] {
			border-color: #3b506b;
			background: #23364e;
			cursor: not-allowed;
		}

		.cards {
			display: grid;
			grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
			gap: 1rem;
			margin: 1.5rem 0 3rem;
		}

		.card {
			padding: 1.25rem;
			border: 1px solid var(--border);
			border-radius: 0.75rem;
			background: linear-gradient(150deg, var(--surface-raised), var(--surface) 72%);
			box-shadow: 0 10px 26px rgba(0, 7, 22, 0.24);
			transition: border-color 150ms ease, transform 150ms ease;
		}

		.card:hover { border-color: #378ed1; transform: translateY(-2px); }
		.card h3 { color: #91d5ff; }
		.card p { color: #c6d6eb; line-height: 1.5; }

		.price { color: #8eeeff; font-size: 1.5rem; font-weight: 700; }
		.price span { color: var(--muted); font-size: 0.9rem; font-weight: 400; }
		.membership-status { color: #c3d4eb; }

		.login-panel {
			max-width: 680px;
			margin: 2rem auto 3rem;
		}

		.login-panel form {
			display: grid;
			gap: 0.75rem;
			margin: 1rem 0;
		}

		.login-panel label { display: grid; gap: 0.35rem; color: #cfe2fa; }
		.login-panel input {
			width: 100%;
			padding: 0.7rem;
			border: 1px solid #31547b;
			border-radius: 0.4rem;
			color: var(--text);
			background: #07162b;
		}

		.login-panel button.button { cursor: pointer; }
		.login-panel button:disabled { cursor: not-allowed; opacity: 0.6; }

		.server-submit-form {
			display: grid;
			gap: 0.75rem;
			margin: 1.5rem 0;
			padding: 1.25rem;
			border: 1px solid var(--border);
			border-radius: 0.75rem;
			background: linear-gradient(150deg, var(--surface-raised), var(--surface) 72%);
		}

		.server-submit-form label { display: grid; gap: 0.35rem; color: #cfe2fa; }
		.server-submit-form input {
			width: 100%;
			padding: 0.65rem;
			border: 1px solid #31547b;
			border-radius: 0.4rem;
			color: var(--text);
			background: #07162b;
		}

		.feature-form {
			display: grid;
			gap: 0.75rem;
			margin: 1rem 0;
		}

		.feature-form label { display: grid; gap: 0.35rem; color: #cfe2fa; }
		.feature-form input, .feature-form textarea {
			width: 100%;
			padding: 0.65rem;
			border: 1px solid #31547b;
			border-radius: 0.4rem;
			color: var(--text);
			background: #07162b;
		}

		.birth-date-fields {
			display: grid;
			grid-template-columns: repeat(3, minmax(0, 1fr));
			gap: 0.75rem;
		}

		.feature-form button:disabled { cursor: not-allowed; opacity: 0.6; }
		.feature-notice { color: #c5daf4; }
		.feature-notice[data-error="true"] { color: #fca5a5; }

		.toolbar {
			display: flex;
			flex-wrap: wrap;
			gap: 0.75rem;
			margin: 1rem 0;
		}

		.toolbar label { display: grid; gap: 0.35rem; color: #cfe2fa; }
		select {
			min-width: 12rem;
			padding: 0.65rem;
			border: 1px solid #31547b;
			border-radius: 0.4rem;
			color: var(--text);
			background: #0a1c35;
		}

		.tag {
			display: inline-block;
			padding: 0.25rem 0.55rem;
			border-radius: 999px;
			border: 1px solid #2d78a9;
			color: #b9f4ff;
			background: linear-gradient(110deg, #124783, #16426b);
			font-size: 0.85rem;
		}

		.card[hidden] { display: none; }
		.game-feed { margin-top: 2rem; }
		.game-feed-heading {
			display: flex;
			justify-content: space-between;
			align-items: end;
			gap: 1rem;
		}
		.game-feed-kicker {
			margin-bottom: 0.35rem;
			color: var(--cyan);
			font-size: 0.75rem;
			font-weight: 800;
			letter-spacing: 0.14em;
			text-transform: uppercase;
		}
		.game-feed-heading h2 { margin: 0; font-size: clamp(1.7rem, 4vw, 2.4rem); }
		.game-feed-heading p { max-width: 42rem; color: var(--muted); line-height: 1.55; }
		.game-feed-count {
			flex: 0 0 auto;
			padding: 0.6rem 0.85rem;
			border: 1px solid var(--border);
			border-radius: 999px;
			color: #b9f4ff;
			background: rgba(16, 40, 74, 0.8);
			font-size: 0.9rem;
			font-weight: 700;
		}
		.game-feed-toolbar {
			display: grid;
			grid-template-columns: minmax(180px, 1fr) minmax(160px, 0.7fr) auto auto;
			align-items: end;
			gap: 0.75rem;
			margin: 1.25rem 0 0.5rem;
			padding: 1rem;
			border: 1px solid var(--border);
			border-radius: 0.75rem;
			background: rgba(12, 30, 57, 0.84);
		}
		.game-feed-toolbar label { display: grid; gap: 0.35rem; color: #cfe2fa; font-size: 0.9rem; }
		.game-feed-toolbar input, .game-feed-toolbar select {
			width: 100%;
			min-width: 0;
			padding: 0.65rem 0.75rem;
			border: 1px solid #31547b;
			border-radius: 0.45rem;
			color: var(--text);
			background: #07162b;
			font: inherit;
		}
		.game-feed-toolbar input:focus-visible, .game-feed-toolbar select:focus-visible,
		.game-feed-toolbar button:focus-visible, .game-favorite:focus-visible {
			outline: 2px solid var(--cyan);
			outline-offset: 2px;
		}
		.game-feed-actions, .game-view-switch {
			display: flex;
			align-items: center;
			gap: 0.4rem;
		}
		.game-feed-toolbar button {
			min-height: 42px;
			padding: 0.55rem 0.75rem;
			border: 1px solid #31547b;
			border-radius: 0.45rem;
			color: #d6e8ff;
			background: #10284a;
			font: inherit;
			font-weight: 700;
			cursor: pointer;
		}
		.game-feed-toolbar button[aria-pressed="true"] {
			border-color: var(--cyan);
			color: #061326;
			background: var(--cyan);
		}
		.game-feed-result { min-height: 1.5rem; color: var(--muted); font-size: 0.9rem; }
		.game-feed-empty {
			padding: 2rem;
			border: 1px dashed var(--border);
			border-radius: 0.75rem;
			color: var(--muted);
			text-align: center;
		}
		.game-card {
			position: relative;
			overflow: hidden;
			padding: 0;
		}
		.game-art-wrap {
			position: relative;
			overflow: hidden;
			aspect-ratio: 16 / 8;
			background: #10284a;
		}
		.game-art {
			display: block;
			width: 100%;
			height: 100%;
			object-fit: cover;
			transition: transform 220ms ease;
		}
		.game-card:hover .game-art { transform: scale(1.04); }
		.game-card-content { padding: 1rem 1.15rem 1.15rem; }
		.game-card-heading {
			display: flex;
			justify-content: space-between;
			align-items: center;
			gap: 0.5rem;
		}
		.game-card-heading h3 { margin: 0.65rem 0 0.35rem; }
		.game-card-content p { margin-bottom: 0; }
		.game-favorite {
			flex: 0 0 auto;
			width: 2.25rem;
			height: 2.25rem;
			border: 1px solid var(--border);
			border-radius: 50%;
			color: #c6d6eb;
			background: #07162b;
			font-size: 1.2rem;
			cursor: pointer;
		}
		.game-favorite[aria-pressed="true"] { border-color: #fda4af; color: #fda4af; }
		.cards--list { grid-template-columns: 1fr; }
		.cards--list .game-card { display: grid; grid-template-columns: minmax(190px, 0.8fr) minmax(0, 1fr); }
		.cards--list .game-art-wrap { height: auto; min-height: 0; aspect-ratio: 16 / 8; }
		.cards--list .game-card-content { align-self: center; padding: 1.25rem; }
		@media (max-width: 760px) {
			.game-feed-toolbar { grid-template-columns: repeat(2, minmax(0, 1fr)); }
			.game-feed-actions, .game-view-switch { justify-content: flex-start; }
		}
		@media (max-width: 520px) {
			.game-feed-heading { align-items: flex-start; flex-direction: column; }
			.game-feed-toolbar { grid-template-columns: minmax(0, 1fr); }
			.cards--list .game-card { grid-template-columns: minmax(0, 1fr); }
			.cards--list .game-art-wrap { height: auto; min-height: 0; aspect-ratio: 16 / 8; }
		}
		@media (prefers-reduced-motion: reduce) {
			.game-art, .card { transition: none; }
		}
		table { width: 100%; border-collapse: collapse; color: var(--muted); }
		th, td { padding: 0.65rem; border-bottom: 1px solid var(--border); text-align: left; }

		footer {
			padding: 1.5rem 0;
			color: #9fb5d0;
			border-top: 1px solid var(--border);
			text-align: center;
		}

		@media (max-width: 600px) {
			header { align-items: flex-start; flex-direction: column; gap: 0.75rem; }
			nav { display: flex; flex-wrap: wrap; gap: 0.5rem 0.9rem; }
			nav a { margin-left: 0; }
		}

		@media (max-width: 760px) {
			.page-layout { grid-template-columns: minmax(0, 1fr); }
			.sidebar {
				position: static;
				display: flex;
				flex-wrap: wrap;
				gap: 0.25rem;
			}
			.sidebar h2 { flex: 0 0 100%; }
		}
	</style>
</head>
<body>
	<header>
		<div class="logo">
			<strong>NEXUS VELORIX</strong>
			<span>Play, Win and Teamwork</span>
		</div>
		<nav aria-label="Main navigation">
			<a href="sign-in.html">Sign in / Join</a>
		</nav>
	</header>

	<div class="page-layout">
		<aside class="sidebar" aria-label="Community sections">
			<h2>Community</h2>
			<a href="#parties">Parties &amp; lobbies</a>
			<a href="#communities">Communities</a>
			<a href="#chat">Chats</a>
			<a href="#games">Games</a>
			<a href="#teammates">Find teammates</a>
			<a href="#upcoming-events">Live events</a>
			<a href="sign-in.html">Sign in / Join</a>
		</aside>

	<main>
		<section class="hero" id="about">
			<h1>Play together. Level up.</h1>
			<p>Find teammates, join events, and meet your next favorite gaming crew.</p>
			<a class="button" href="sign-in.html">Sign in or create an account</a>
		</section>

		<section id="games" class="game-feed" aria-labelledby="game-feed-title">
			<div class="game-feed-heading">
				<div>
					<p class="game-feed-kicker">Discover your next squad</p>
					<h2 id="game-feed-title">Game feed</h2>
					<p>Browse featured games, save favorites, and find people to play with. Player counts are not live. Additional multiplayer picks are inspired by <a href="https://store.steampowered.com/charts/mostplayed" target="_blank" rel="noopener noreferrer">Steam's most-played chart</a>; rankings vary by platform.</p>
				</div>
				<span class="game-feed-count" id="game-feed-count">18 featured games</span>
			</div>
			<div class="game-feed-toolbar" aria-label="Game feed controls">
				<label for="game-search">Search games
					<input id="game-search" type="search" placeholder="Try a game or genre">
				</label>
				<label for="game-filter">Filter by game
					<select id="game-filter">
						<option value="all">All games</option>
						<option value="fortnite">Fortnite</option>
						<option value="roblox">Roblox</option>
						<option value="minecraft">Minecraft</option>
						<option value="free-fire">Free Fire</option>
						<option value="call-of-duty">Call of Duty</option>
						<option value="counter-strike-2">Counter-Strike 2</option>
						<option value="dota-2">Dota 2</option>
						<option value="delta-force">Delta Force</option>
						<option value="rust">Rust</option>
						<option value="pubg-battlegrounds">PUBG: BATTLEGROUNDS</option>
						<option value="call-of-duty-warzone">Call of Duty: Warzone</option>
						<option value="need-for-speed">Need for Speed</option>
						<option value="apex-legends">Apex Legends</option>
						<option value="rocket-league">Rocket League</option>
						<option value="fc-26">EA SPORTS FC 26</option>
						<option value="efootball">eFootball</option>
						<option value="gta-6">GTA 6</option>
						<option value="other">Other games</option>
					</select>
				</label>
				<label for="game-sort">Sort
					<select id="game-sort">
						<option value="featured">Featured</option>
						<option value="alphabetical">A to Z</option>
					</select>
				</label>
				<div class="game-feed-actions">
					<button id="game-favorites-toggle" type="button" aria-pressed="false">Favorites <span id="game-favorite-count">0</span></button>
					<div class="game-view-switch" role="group" aria-label="Game feed layout">
						<button id="game-view-grid" type="button" aria-pressed="true">Grid</button>
						<button id="game-view-list" type="button" aria-pressed="false">List</button>
					</div>
				</div>
			</div>
			<p id="game-feed-result" class="game-feed-result" role="status" aria-live="polite"></p>
			<p id="game-feed-empty" class="game-feed-empty" hidden>No games match these filters. Try another search or clear Favorites.</p>
			<div class="cards" id="game-feed-cards">
				<article class="card game-card" data-game="fortnite">
					<span class="tag">Battle royale</span>
					<h3>Fortnite</h3>
					<p>Team up for casual matches, creative experiences, and community tournaments.</p>
				</article>
				<article class="card game-card" data-game="roblox">
					<span class="tag">Social &amp; creative</span>
					<h3>Roblox</h3>
					<p>Find friends to explore experiences and build together.</p>
				</article>
				<article class="card game-card" data-game="minecraft">
					<span class="tag">Sandbox</span>
					<h3>Minecraft</h3>
					<p>Share survival, building, and creative-mode sessions.</p>
				</article>
				<article class="card game-card" data-game="free-fire">
					<span class="tag">Mobile</span>
					<h3>Free Fire</h3>
					<p>Connect with squadmates for quick mobile matches.</p>
				</article>
				<article class="card game-card" data-game="call-of-duty">
					<span class="tag">Action</span>
					<h3>Call of Duty</h3>
					<p>Find teammates for multiplayer and other community game modes.</p>
				</article>
				<article class="card game-card" data-game="counter-strike-2">
					<span class="tag">Tactical shooter</span>
					<h3>Counter-Strike 2</h3>
					<p>Team up for tactical matches and community tournaments.</p>
				</article>
				<article class="card game-card" data-game="dota-2">
					<span class="tag">MOBA</span>
					<h3>Dota 2</h3>
					<p>Find teammates for strategy, roles, and coordinated matches.</p>
				</article>
				<article class="card game-card" data-game="delta-force">
					<span class="tag">Tactical shooter</span>
					<h3>Delta Force</h3>
					<p>Coordinate squads for tactical and extraction modes.</p>
				</article>
				<article class="card game-card" data-game="rust">
					<span class="tag">Survival</span>
					<h3>Rust</h3>
					<p>Find a group for survival, base building, and server play.</p>
				</article>
				<article class="card game-card" data-game="pubg-battlegrounds">
					<span class="tag">Battle royale</span>
					<h3>PUBG: BATTLEGROUNDS</h3>
					<p>Squad up and find teammates for battle royale matches.</p>
				</article>
				<article class="card game-card" data-game="call-of-duty-warzone">
					<span class="tag">Battle royale</span>
					<h3>Call of Duty: Warzone</h3>
					<p>Find a squad for battle royale and Resurgence matches.</p>
				</article>
				<article class="card game-card" data-game="need-for-speed">
					<span class="tag">Racing</span>
					<h3>Need for Speed</h3>
					<p>Connect with racers for online races and car meets.</p>
				</article>
				<article class="card game-card" data-game="apex-legends">
					<span class="tag">Squad-based</span>
					<h3>Apex Legends</h3>
					<p>Find a squad and plan your next drop.</p>
				</article>
				<article class="card game-card" data-game="rocket-league">
					<span class="tag">Sports</span>
					<h3>Rocket League</h3>
					<p>Pair up for casual games and community competitions.</p>
				</article>
				<article class="card game-card" data-game="fc-26">
					<span class="tag">Football</span>
					<h3>EA SPORTS FC 26</h3>
					<p>Find players for football matches and community competitions.</p>
				</article>
				<article class="card game-card" data-game="efootball">
					<span class="tag">Football</span>
					<h3>eFootball</h3>
					<p>Connect with players for online matches and community events.</p>
				</article>
				<article class="card game-card" data-game="gta-6">
					<span class="tag">Action &amp; adventure</span>
					<h3>GTA 6</h3>
					<p>Discuss the game and find community members interested in playing.</p>
				</article>
				<article class="card game-card" data-game="other">
					<span class="tag">Your choice</span>
					<h3>More games welcome</h3>
					<p>We can feature more games as the community grows. Suggest a title when you <a href="mailto:rangerthadeus54@gmail.com?subject=Suggest%20a%20game">contact us</a>.</p>
				</article>
			</div>
		</section>

		<section id="profiles">
			<h2>Gamer Profiles</h2>
			<p class="feature-notice">Profiles will show only a display name, games, region, and availability. Email and phone details stay private.</p>
			<div class="card">
				<p class="membership-status">Profile controls are available, but profiles cannot be saved until Supabase storage and row-level security are configured.</p>
				<form id="profile-form" class="feature-form">
					<label for="profile-name">Display name
						<input id="profile-name" type="text" minlength="2" maxlength="32" required>
					</label>
					<label for="profile-games">Favorite games
						<input id="profile-games" type="text" placeholder="Choose games">
					</label>
					<label for="profile-region">Region
						<select id="profile-region" required>
							<option value="">Select a region</option>
							<option>North America</option><option>South America</option>
							<option>Europe</option><option>Asia</option>
							<option>Oceania</option><option>Africa</option>
						</select>
					</label>
					<button class="button" type="submit">Save profile</button>
					<p id="profile-save-status" class="feature-notice" role="status" aria-live="polite"></p>
				</form>
			</div>
		</section>

		<section id="teammates">
			<h2>Find Teammates</h2>
			<p class="membership-status">Search for players by game and region after profiles are enabled.</p>
			<div class="toolbar">
				<label for="teammate-game">Game
					<select id="teammate-game">
						<option>All games</option><option>Fortnite</option><option>Roblox</option>
						<option>Minecraft</option><option>Free Fire</option><option>Call of Duty</option>
						<option>Counter-Strike 2</option><option>Dota 2</option><option>Delta Force</option>
						<option>Rust</option><option>PUBG: BATTLEGROUNDS</option>
						<option>Call of Duty: Warzone</option><option>Need for Speed</option>
						<option>EA SPORTS FC 26</option><option>eFootball</option><option>GTA 6</option>
					</select>
				</label>
				<label for="teammate-region">Region
					<select id="teammate-region">
						<option>All regions</option><option>North America</option>
						<option>South America</option><option>Europe</option>
						<option>Asia</option><option>Oceania</option><option>Africa</option>
					</select>
				</label>
				<label for="teammate-hardware">Hardware
					<select id="teammate-hardware">
						<option>All hardware</option><option>PlayStation</option><option>Xbox</option>
						<option>PC</option><option>Nintendo</option><option>Mobile</option><option>Other</option>
					</select>
				</label>
			</div>
			<p id="teammate-results-status" class="card membership-status" role="status" aria-live="polite">Filters are available, but no teammate profiles are connected yet. Nothing is searched or saved.</p>
		</section>

		<section id="parties">
			<h2>Parties &amp; Lobbies</h2>
			<p class="membership-status">Find a party, coordinate a lobby, and team up around your favorite games.</p>
			<div class="card">
				<p class="membership-status">Party listings are not connected yet. Create and join controls stay available, but no parties or invites are saved.</p>
				<a class="button" href="sign-in.html">Sign in to join the community</a>
				<button class="button" id="create-party-button" type="button">Create or join a party/lobby</button>
				<p id="party-action-status" class="feature-notice" role="status" aria-live="polite"></p>
			</div>
		</section>

		<section id="chat">
			<h2>Game Chat</h2>
			<p class="membership-status">Chat controls are available. Messages are not sent or stored until Supabase storage, access policies, and moderation are configured.</p>
			<div class="card">
				<label for="chat-game">Game channel
					<select id="chat-game">
						<option>Choose a game</option><option>Fortnite</option><option>Roblox</option>
						<option>Minecraft</option><option>Free Fire</option><option>Call of Duty</option>
						<option>Counter-Strike 2</option><option>Dota 2</option><option>Delta Force</option>
						<option>Rust</option><option>PUBG: BATTLEGROUNDS</option>
						<option>Call of Duty: Warzone</option><option>Need for Speed</option>
						<option>EA SPORTS FC 26</option><option>eFootball</option><option>GTA 6</option>
					</select>
				</label>
				<p id="chat-status" class="feature-notice" role="status" aria-live="polite">No messages. Chat is not connected.</p>
				<form id="chat-form" class="feature-form">
					<label for="chat-message">Message
						<textarea id="chat-message" maxlength="500" rows="3" required></textarea>
					</label>
					<button class="button" type="submit">Send message</button>
				</form>
				<p class="feature-notice">Public messages will need reporting and moderation before chat can launch.</p>
			</div>
		</section>

		<section id="leaderboards">
			<h2>Leaderboards and Divisions</h2>
			<p class="membership-status">The shared leaderboard is not connected yet. This page can preview proposed match points, but it does not save, verify, or publish scores.</p>
			<div class="card">
				<h3>Proposed match points</h3>
				<p>Win: 3 points. Draw: 1 point. Loss: 0 points. An organizer must verify real results before they count on an official leaderboard.</p>
			</div>
			<div class="card">
				<h3>Score and division preview</h3>
				<form id="score-calculator" class="feature-form">
					<label for="score-game">Game
						<select id="score-game" required>
							<option>Fortnite</option><option>Roblox</option><option>Minecraft</option>
							<option>Free Fire</option><option>Call of Duty</option>
							<option>Counter-Strike 2</option><option>Dota 2</option><option>Delta Force</option>
							<option>Rust</option><option>PUBG: BATTLEGROUNDS</option>
							<option>Call of Duty: Warzone</option><option>Need for Speed</option>
							<option>Apex Legends</option><option>Rocket League</option><option>EA SPORTS FC 26</option>
							<option>eFootball</option><option>GTA 6</option><option>Other game</option>
						</select>
					</label>
					<div class="birth-date-fields">
						<label for="score-wins">Wins
							<input id="score-wins" type="number" min="0" max="10000" step="1" required>
						</label>
						<label for="score-draws">Draws
							<input id="score-draws" type="number" min="0" max="10000" step="1" required>
						</label>
						<label for="score-losses">Losses
							<input id="score-losses" type="number" min="0" max="10000" step="1" required>
						</label>
					</div>
					<button class="button" type="submit">Calculate preview</button>
				</form>
				<p id="score-preview-result" class="feature-notice" role="status" aria-live="polite">Preview only; scores are not saved or published.</p>
			</div>
			<div class="card">
				<h3>Division progression (proposed)</h3>
				<p>Example thresholds only; they are not official season rules.</p>
				<table>
					<thead><tr><th>Division</th><th>Points</th></tr></thead>
					<tbody>
						<tr><th scope="row">Division 9</th><td>0-24</td></tr>
						<tr><th scope="row">Division 8</th><td>25-49</td></tr>
						<tr><th scope="row">Division 7</th><td>50-74</td></tr>
						<tr><th scope="row">Division 6</th><td>75-99</td></tr>
						<tr><th scope="row">Division 5</th><td>100-124</td></tr>
						<tr><th scope="row">Division 4</th><td>125-149</td></tr>
						<tr><th scope="row">Division 3</th><td>150-174</td></tr>
						<tr><th scope="row">Division 2</th><td>175-199</td></tr>
						<tr><th scope="row">Division 1</th><td>200+</td></tr>
					</tbody>
				</table>
			</div>
			<div class="card">
				<h3>Official leaderboard</h3>
				<p class="membership-status">No verified results are available. Supabase score storage, access rules, and result review must be configured before real standings can appear.</p>
				<table>
					<thead><tr><th>Game</th><th>Player</th><th>Points</th><th>Division</th><th>Status</th></tr></thead>
					<tbody><tr><td colspan="5">No verified leaderboard entries yet.</td></tr></tbody>
				</table>
			</div>
		</section>

		<section id="news">
			<h2>Community News</h2>
			<p class="membership-status">No news posts yet. News will be added after community submissions are reviewed.</p>
			<div class="card">
				<p class="feature-notice">Community news is not connected to a publishing system.</p>
				<a href="mailto:rangerthadeus54@gmail.com?subject=NEXUS%20VELORIX%20news%20submission">Suggest a news post</a>
			</div>
		</section>

		<section id="upcoming-events">
			<h2>Upcoming Live Events</h2>
			<p class="membership-status">Live esports schedules are provided by PandaScore. Coverage varies by game and competition; the game organizer remains the authoritative source for event details.</p>
			<div class="toolbar">
				<label for="event-game-filter">Filter by game
					<select id="event-game-filter">
						<option value="all">All games</option>
					</select>
				</label>
				<button class="button" id="event-refresh" type="button">Refresh events</button>
			</div>
			<p id="event-feed-status" class="feature-notice" role="status" aria-live="polite">Connecting to the live event feed...</p>
			<div id="event-feed-list" class="cards"></div>
			<button class="button" id="event-load-more" type="button" hidden>Load more events</button>
			<div class="card">
				<span class="tag">Proposed only</span>
				<h3>Event reward target</h3>
				<p>A $10,000 USD prize pool is an unconfirmed proposal, not a funded prize or payout offer. No event or eligibility rules have been announced.</p>
			</div>
			<form id="event-submission-form" class="server-submit-form">
				<h3>Suggest an upcoming event</h3>
				<label for="event-game">Game
					<select id="event-game" required>
						<option value="">Choose a game</option>
						<option>Fortnite</option>
						<option>Roblox</option>
						<option>Minecraft</option>
						<option>Free Fire</option>
						<option>Call of Duty</option>
						<option>Counter-Strike 2</option>
						<option>Dota 2</option>
						<option>Delta Force</option>
						<option>Rust</option>
						<option>PUBG: BATTLEGROUNDS</option>
						<option>Call of Duty: Warzone</option>
						<option>Need for Speed</option>
						<option>Apex Legends</option>
						<option>Rocket League</option>
						<option>EA SPORTS FC 26</option>
						<option>eFootball</option>
						<option>GTA 6</option>
						<option>Other game</option>
					</select>
				</label>
				<label for="event-name">Event name
					<input id="event-name" type="text" maxlength="120" required>
				</label>
				<label for="event-start">Start date and time (your local time)
					<input id="event-start" type="datetime-local" required>
				</label>
				<label for="event-link">Official event or organizer link
					<input id="event-link" type="url" placeholder="https://..." required>
				</label>
				<button class="button" type="submit">Email event for review</button>
				<p id="event-submission-status" class="membership-status" role="status" aria-live="polite"></p>
			</form>
		</section>

		<section id="communities">
			<h2>Popular Gaming Communities</h2>
			<p class="membership-status">Community invite links are not connected yet. Use an active request button to ask the organizer for a verified invite.</p>
			<div class="cards">
				<article class="card"><h3>Fortnite</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20a%20Fortnite%20community%20invite">Request invite</a></article>
				<article class="card"><h3>Roblox</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20a%20Roblox%20community%20invite">Request invite</a></article>
				<article class="card"><h3>Minecraft</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20a%20Minecraft%20community%20invite">Request invite</a></article>
				<article class="card"><h3>Free Fire</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20a%20Free%20Fire%20community%20invite">Request invite</a></article>
				<article class="card"><h3>Call of Duty</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20a%20Call%20of%20Duty%20community%20invite">Request invite</a></article>
				<article class="card"><h3>EA SPORTS FC 26</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20an%20EA%20SPORTS%20FC%2026%20community%20invite">Request invite</a></article>
				<article class="card"><h3>eFootball</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20an%20eFootball%20community%20invite">Request invite</a></article>
				<article class="card"><h3>GTA 6</h3><p>Verified invite link not provided yet.</p><a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Request%20a%20GTA%206%20community%20invite">Request invite</a></article>
			</div>
		</section>

		<section id="tournaments">
			<h2>Upcoming Tournaments</h2>
			<p class="membership-status">No dates are confirmed. These are proposed formats, not scheduled tournaments.</p>
		<section class="cards">
			<article class="card">
				<span class="tag">Fortnite · proposed</span>
				<h3>Squad Showdown</h3>
				<p>Team-based tournament idea. Schedule and entry details are not set.</p>
				<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Fortnite%20tournament%20interest">Ask about this event</a>
			</article>
			<article class="card">
				<span class="tag">Minecraft · proposed</span>
				<h3>Build Challenge</h3>
				<p>Community build competition idea. Schedule and entry details are not set.</p>
				<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Minecraft%20tournament%20interest">Ask about this event</a>
			</article>
			<article class="card">
				<span class="tag">Any game</span>
				<h3>Suggest a tournament</h3>
				<p>Tell us which game and format you would like to play.</p>
				<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Tournament%20suggestion">Send a suggestion</a>
			</article>
		</section>
		</section>

		<section id="servers">
			<h2>Servers around the world</h2>
			<p class="membership-status">No game server links have been provided yet. Submit a community invite for review; submissions are emailed to the organizer and are not published automatically.</p>
			<form id="server-submission-form" class="server-submit-form">
				<label for="server-game">Game
					<select id="server-game" required>
						<option value="">Choose a game</option>
						<option>Fortnite</option>
						<option>Roblox</option>
						<option>Minecraft</option>
						<option>Free Fire</option>
						<option>Call of Duty</option>
						<option>Counter-Strike 2</option>
						<option>Dota 2</option>
						<option>Delta Force</option>
						<option>Rust</option>
						<option>PUBG: BATTLEGROUNDS</option>
						<option>Call of Duty: Warzone</option>
						<option>Need for Speed</option>
						<option>EA SPORTS FC 26</option>
						<option>eFootball</option>
						<option>GTA 6</option>
						<option>Other (include the title in the server name)</option>
					</select>
				</label>
				<label for="server-region">Region
					<select id="server-region" required>
						<option value="">Choose a region</option>
						<option>North America</option>
						<option>South America</option>
						<option>Europe</option>
						<option>Asia</option>
						<option>Oceania</option>
						<option>Africa</option>
					</select>
				</label>
				<label for="server-name">Server or community name
					<input id="server-name" type="text" maxlength="100" required>
				</label>
				<label for="server-invite">Invite or server link (include https://)
					<input id="server-invite" type="url" placeholder="https://..." required>
				</label>
				<button class="button" type="submit">Email server listing for review</button>
				<p id="server-submission-status" class="membership-status" role="status" aria-live="polite"></p>
			</form>
			<div class="toolbar">
				<label for="region-filter">Filter by region
					<select id="region-filter">
						<option value="all">All regions</option>
						<option value="north-america">North America</option>
						<option value="south-america">South America</option>
						<option value="europe">Europe</option>
						<option value="asia">Asia</option>
						<option value="oceania">Oceania</option>
						<option value="africa">Africa</option>
					</select>
				</label>
			</div>
			<div class="cards">
				<article class="card server-card" data-region="north-america">
					<h3>North America</h3><p>Meet players across the US, Canada, and nearby time zones.</p>
					<a href="mailto:rangerthadeus54@gmail.com?subject=North%20America%20community%20hub">Ask for the community link</a>
				</article>
				<article class="card server-card" data-region="south-america">
					<h3>South America</h3><p>Connect with players across South American time zones.</p>
					<a href="mailto:rangerthadeus54@gmail.com?subject=South%20America%20community%20hub">Ask for the community link</a>
				</article>
				<article class="card server-card" data-region="europe">
					<h3>Europe</h3><p>Find teammates across Europe and nearby regions.</p>
					<a href="mailto:rangerthadeus54@gmail.com?subject=Europe%20community%20hub">Ask for the community link</a>
				</article>
				<article class="card server-card" data-region="asia">
					<h3>Asia</h3><p>Meet players across Asian regions and time zones.</p>
					<a href="mailto:rangerthadeus54@gmail.com?subject=Asia%20community%20hub">Ask for the community link</a>
				</article>
				<article class="card server-card" data-region="oceania">
					<h3>Oceania</h3><p>Find gaming friends in Australia, New Zealand, and nearby areas.</p>
					<a href="mailto:rangerthadeus54@gmail.com?subject=Oceania%20community%20hub">Ask for the community link</a>
				</article>
				<article class="card server-card" data-region="africa">
					<h3>Africa</h3><p>Connect with gamers across African regions.</p>
					<a href="mailto:rangerthadeus54@gmail.com?subject=Africa%20community%20hub">Ask for the community link</a>
				</article>
			</div>
		</section>

		<section id="membership">
			<h2>Membership</h2>
			<p class="membership-status">Membership requests go to rangerthadeus54@gmail.com. The USD prices below are set, but live subscription checkout is not connected on this static page.</p>
			<aside class="card" aria-label="Payment setup status">
				<h3>Payment options</h3>
				<p>Stripe and PayPal can offer their supported card methods, including Visa and Mastercard; Google Pay and Apple Pay depend on provider, account, domain, and device eligibility. Prices are in USD.</p>
				<p><strong>Checkout is not active.</strong> A secure backend connected to Stripe and PayPal must be deployed before these plans can accept payments.</p>
			</aside>
			<div class="cards">
				<article class="card">
					<h3>Weekly</h3>
					<p class="price">$1.49 <span>/ week</span></p>
					<p>Supporter. Champion membership is $2.99/week. USD.</p>
					<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Weekly%20membership%20subscription">Ask about weekly</a>
				</article>
				<article class="card">
					<h3>Monthly</h3>
					<p class="price">$4.99 <span>/ month</span></p>
					<p>Supporter. Champion membership is $9.99/month. USD.</p>
					<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Monthly%20membership%20subscription">Ask about monthly</a>
				</article>
				<article class="card">
					<h3>Yearly</h3>
					<p class="price">$49.99 <span>/ year</span></p>
					<p>Supporter. Champion membership is $99.99/year. USD.</p>
					<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Yearly%20membership%20subscription">Ask about yearly</a>
				</article>
			</div>
			<p class="membership-status">Free Player membership is also available. <a href="mailto:rangerthadeus54@gmail.com?subject=Free%20player%20membership">Request it by email</a>.</p>
		</section>

		<section id="join" class="hero">
			<h2>Ready to join us?</h2>
			<p>Send a membership or community question to the organizer.</p>
			<a class="button" href="mailto:rangerthadeus54@gmail.com?subject=Gaming%20community%20membership">
				Email the community
			</a>
		</section>

		<section id="report" class="login-panel">
			<h2>Report Suspicious Activity</h2>
			<p class="membership-status">Report scams, suspicious links, harassment, impersonation, cheating, or other concerns for organizer review.</p>
			<div class="card">
				<p class="feature-notice">Submitting opens your email app and sends a report to the community organizer. Reports are not monitored live. Do not include passwords, verification codes, full payment-card details, or other sensitive information.</p>
				<form id="activity-report-form" class="feature-form">
					<label for="report-category">Report category
						<select id="report-category" required>
							<option value="">Choose a category</option>
							<option>Scam or fraud</option>
							<option>Suspicious link</option>
							<option>Harassment or threats</option>
							<option>Impersonation</option>
							<option>Cheating or botting</option>
							<option>Other suspicious activity</option>
						</select>
					</label>
					<label for="report-game">Game or community
						<select id="report-game" required>
							<option value="">Choose a game</option>
							<option>Fortnite</option><option>Roblox</option><option>Minecraft</option>
							<option>Free Fire</option><option>Call of Duty</option>
							<option>Counter-Strike 2</option><option>Dota 2</option><option>Delta Force</option>
							<option>Rust</option><option>PUBG: BATTLEGROUNDS</option>
							<option>Call of Duty: Warzone</option><option>Need for Speed</option>
							<option>EA SPORTS FC 26</option><option>eFootball</option><option>GTA 6</option>
							<option>Other</option>
						</select>
					</label>
					<label for="report-username">Reported username (optional)
						<input id="report-username" type="text" maxlength="100">
					</label>
					<label for="report-details">What happened?
						<textarea id="report-details" maxlength="2000" rows="5" required></textarea>
					</label>
					<label for="report-evidence">Evidence link (optional; do not upload private information)
						<input id="report-evidence" type="url" placeholder="https://...">
					</label>
					<button class="button" type="submit">Email report for review</button>
					<p id="report-status" class="membership-status" role="status" aria-live="polite"></p>
				</form>
			</div>
		</section>
	</main>
	</div>

	<footer>
		<p>© 2026 NEXUS VELORIX. All rights reserved.</p>
		<p>A community for gamers · <a href="#report">Report suspicious activity</a> · <a href="terms.html">Terms and conditions</a> · <a href="privacy.html">Privacy policy</a> · <a href="mailto:rangerthadeus54@gmail.com">Contact the organizer</a></p>
	</footer>
	<script>
		const gameFilter = document.querySelector("#game-filter");
		const gameSearch = document.querySelector("#game-search");
		const gameSort = document.querySelector("#game-sort");
		const gameFeedCards = document.querySelector("#game-feed-cards");
		const gameFeedResult = document.querySelector("#game-feed-result");
		const gameFeedEmpty = document.querySelector("#game-feed-empty");
		const gameFeedCount = document.querySelector("#game-feed-count");
		const gameFavoriteCount = document.querySelector("#game-favorite-count");
		const favoritesToggle = document.querySelector("#game-favorites-toggle");
		const gameCards = Array.from(document.querySelectorAll(".game-card"));
		const originalGameOrder = new Map(gameCards.map((card, index) => [card, index]));
		const favoriteGameIds = new Set();
		const artworkThemes = {
			"fortnite": ["#2069bc", "#111945", "#68e5ff", "F"],
			"roblox": ["#d8314c", "#31182e", "#ffe4e8", "R"],
			"minecraft": ["#36a76a", "#143a2f", "#b7f47c", "M"],
			"free-fire": ["#ed6a25", "#512319", "#ffd166", "FF"],
			"call-of-duty": ["#78834c", "#1a2824", "#e7d6a0", "COD"],
			"counter-strike-2": ["#d68a36", "#352a23", "#ffda8a", "CS2"],
			"dota-2": ["#bd493b", "#351b20", "#ffb27b", "D2"],
			"delta-force": ["#6e8d55", "#1b3130", "#d0e58c", "DF"],
			"rust": ["#bd6339", "#3b2822", "#ffc27c", "R"],
			"pubg-battlegrounds": ["#c59b3c", "#393323", "#ffe29a", "PUBG"],
			"call-of-duty-warzone": ["#697a52", "#182822", "#d5d9a1", "WZ"],
			"need-for-speed": ["#d94c3e", "#321c2a", "#ffb16b", "NFS"],
			"apex-legends": ["#bd493b", "#302238", "#ffbd72", "A"],
			"rocket-league": ["#168bc2", "#122653", "#63eeff", "RL"],
			"fc-26": ["#159b74", "#123a43", "#a9ffd9", "FC"],
			"efootball": ["#2783c9", "#142651", "#85e0ff", "eF"],
			"gta-6": ["#d64b83", "#34204d", "#ffc7a6", "VI"],
			"other": ["#6459c8", "#222052", "#d5ccff", "+"]
		};
		const svgNamespace = "http://www.w3.org/2000/svg";

		function addArtworkElement(parent, name, attributes = {}) {
			const element = document.createElementNS(svgNamespace, name);
			Object.entries(attributes).forEach(([attribute, value]) => {
				element.setAttribute(attribute, value);
			});
			parent.append(element);
			return element;
		}

		function createGameArtwork(card, index) {
			const [startColor, endColor, accentColor, mark] =
				artworkThemes[card.dataset.game] || artworkThemes.other;
			const title = card.querySelector("h3").textContent.trim();
			const originalChildren = Array.from(card.children);
			const tag = card.querySelector(".tag");
			const heading = card.querySelector("h3");
			const artwork = document.createElement("div");
			artwork.className = "game-art-wrap";
			const content = document.createElement("div");
			content.className = "game-card-content";
			const headingRow = document.createElement("div");
			headingRow.className = "game-card-heading";
			const favoriteButton = document.createElement("button");
			favoriteButton.className = "game-favorite";
			favoriteButton.type = "button";
			favoriteButton.setAttribute("aria-pressed", "false");
			favoriteButton.setAttribute("aria-label", `Add ${title} to favorites`);
			favoriteButton.textContent = "♡";
			headingRow.append(heading, favoriteButton);
			card.replaceChildren(artwork, content);
			if (tag) content.append(tag);
			content.append(headingRow);
			originalChildren
				.filter((child) => child !== tag && child !== heading)
				.forEach((child) => content.append(child));

			const svg = document.createElementNS(svgNamespace, "svg");
			svg.setAttribute("xmlns", svgNamespace);
			svg.setAttribute("viewBox", "0 0 720 320");
			const gradientId = `game-art-gradient-${index}`;
			const defs = addArtworkElement(svg, "defs");
			const gradient = addArtworkElement(defs, "linearGradient", {
				id: gradientId, x1: "0", y1: "0", x2: "1", y2: "1"
			});
			addArtworkElement(gradient, "stop", { offset: "0%", "stop-color": startColor });
			addArtworkElement(gradient, "stop", { offset: "100%", "stop-color": endColor });
			addArtworkElement(svg, "rect", { width: "720", height: "320", fill: `url(#${gradientId})` });
			addArtworkElement(svg, "circle", {
				cx: "548", cy: "96", r: "112", fill: accentColor, opacity: "0.22"
			});
			addArtworkElement(svg, "path", {
				d: "M0 270 145 174 260 246 390 120 520 230 650 150 720 194V320H0Z",
				fill: "#071326", opacity: "0.48"
			});
			addArtworkElement(svg, "path", {
				d: "M0 291 174 222 312 278 470 200 590 263 720 218V320H0Z",
				fill: endColor, opacity: "0.72"
			});
			const markText = addArtworkElement(svg, "text", {
				x: "548", y: "216", fill: "#fff", opacity: "0.24",
				"font-family": "system-ui, sans-serif", "font-size": mark.length > 2 ? "82" : "126",
				"font-weight": "900", "text-anchor": "middle"
			});
			markText.textContent = mark;
			const titleText = addArtworkElement(svg, "text", {
				x: "34", y: "68", fill: "#fff",
				"font-family": "system-ui, sans-serif", "font-size": "27",
				"font-weight": "800", "letter-spacing": "2"
			});
			titleText.textContent = title.toUpperCase();
			const image = document.createElement("img");
			image.className = "game-art";
			image.alt = `Stylized ${title} game artwork`;
			image.loading = "lazy";
			image.src = `data:image/svg+xml;charset=utf-8,${encodeURIComponent(
				new XMLSerializer().serializeToString(svg)
			)}`;
			artwork.append(image);
		}

		const gameFeedGrid = document.querySelector("#game-view-grid");
		const gameFeedList = document.querySelector("#game-view-list");
		gameCards.forEach((card, index) => {
			createGameArtwork(card, index);
			const favoriteButton = card.querySelector(".game-favorite");
			favoriteButton.addEventListener("click", () => {
				const gameId = card.dataset.game;
				if (favoriteGameIds.has(gameId)) {
					favoriteGameIds.delete(gameId);
				} else {
					favoriteGameIds.add(gameId);
				}
				const isFavorite = favoriteGameIds.has(gameId);
				favoriteButton.setAttribute("aria-pressed", String(isFavorite));
				favoriteButton.setAttribute(
					"aria-label",
					`${isFavorite ? "Remove" : "Add"} ${card.querySelector("h3").textContent.trim()} ${isFavorite ? "from" : "to"} favorites`
				);
				favoriteButton.textContent = isFavorite ? "♥" : "♡";
				renderGameFeed();
			});
		});

		function renderGameFeed() {
			const query = gameSearch.value.trim().toLocaleLowerCase();
			const favoritesOnly = favoritesToggle.getAttribute("aria-pressed") === "true";
			const visibleCards = gameCards.filter((card) => {
				const matchesGame = gameFilter.value === "all" || card.dataset.game === gameFilter.value;
				const matchesSearch = card.textContent.toLocaleLowerCase().includes(query);
				const matchesFavorites = !favoritesOnly || favoriteGameIds.has(card.dataset.game);
				return matchesGame && matchesSearch && matchesFavorites;
			});
			visibleCards.sort((left, right) => gameSort.value === "alphabetical"
				? left.querySelector("h3").textContent.localeCompare(right.querySelector("h3").textContent)
				: originalGameOrder.get(left) - originalGameOrder.get(right));
			visibleCards.forEach((card) => gameFeedCards.append(card));
			gameCards.forEach((card) => { card.hidden = !visibleCards.includes(card); });
			gameFavoriteCount.textContent = String(favoriteGameIds.size);
			gameFeedCount.textContent = `${visibleCards.length} of ${gameCards.length} games`;
			gameFeedResult.textContent = `${visibleCards.length} ${visibleCards.length === 1 ? "game" : "games"} shown`;
			gameFeedEmpty.hidden = visibleCards.length > 0;
		}

		[gameFilter, gameSearch, gameSort].forEach((control) => {
			control.addEventListener(control === gameSearch ? "input" : "change", renderGameFeed);
		});
		favoritesToggle.addEventListener("click", () => {
			const showFavorites = favoritesToggle.getAttribute("aria-pressed") !== "true";
			favoritesToggle.setAttribute("aria-pressed", String(showFavorites));
			renderGameFeed();
		});
		gameFeedGrid.addEventListener("click", () => {
			gameFeedCards.classList.remove("cards--list");
			gameFeedGrid.setAttribute("aria-pressed", "true");
			gameFeedList.setAttribute("aria-pressed", "false");
		});
		gameFeedList.addEventListener("click", () => {
			gameFeedCards.classList.add("cards--list");
			gameFeedGrid.setAttribute("aria-pressed", "false");
			gameFeedList.setAttribute("aria-pressed", "true");
		});
		renderGameFeed();

		const regionFilter = document.querySelector("#region-filter");

		regionFilter.addEventListener("change", () => {
			document.querySelectorAll(".server-card").forEach((card) => {
				card.hidden = regionFilter.value !== "all" && card.dataset.region !== regionFilter.value;
			});
		});

		document.querySelector("#profile-form").addEventListener("submit", (event) => {
			event.preventDefault();
			document.querySelector("#profile-save-status").textContent =
				"Supabase profile storage is not connected. Your profile was not saved.";
		});

		["#teammate-game", "#teammate-region", "#teammate-hardware"].forEach((selector) => {
			document.querySelector(selector).addEventListener("change", () => {
				document.querySelector("#teammate-results-status").textContent =
					"Filters are active, but no teammate profiles are connected. No search was sent.";
			});
		});

		document.querySelector("#create-party-button").addEventListener("click", () => {
			document.querySelector("#party-action-status").textContent =
				"Party and lobby storage is not connected. Nothing was created or joined.";
		});

		document.querySelector("#chat-form").addEventListener("submit", (event) => {
			event.preventDefault();
			document.querySelector("#chat-status").textContent =
				"Chat is not connected. Your message was not sent or saved.";
		});

		document.querySelector("#server-submission-form").addEventListener("submit", (event) => {
			event.preventDefault();
			const game = document.querySelector("#server-game").value;
			const region = document.querySelector("#server-region").value;
			const name = document.querySelector("#server-name").value.trim();
			const invite = document.querySelector("#server-invite").value.trim();
			const subject = encodeURIComponent(`Game server listing: ${game} - ${region}`);
			const body = encodeURIComponent(
				`Game: ${game}\nRegion: ${region}\nServer/community: ${name}\nInvite link: ${invite}\n`
			);
			document.querySelector("#server-submission-status").textContent =
				"Your email app will open. The listing will not appear on the site until reviewed and added.";
			window.location.href = `mailto:rangerthadeus54@gmail.com?subject=${subject}&body=${body}`;
		});

		document.querySelector("#activity-report-form").addEventListener("submit", (event) => {
			event.preventDefault();
			const category = document.querySelector("#report-category").value;
			const game = document.querySelector("#report-game").value;
			const username = document.querySelector("#report-username").value.trim() || "Not provided";
			const details = document.querySelector("#report-details").value.trim();
			const evidence = document.querySelector("#report-evidence").value.trim() || "Not provided";
			const subject = encodeURIComponent(`Community safety report: ${category}`);
			const body = encodeURIComponent(
				`Category: ${category}\nGame/community: ${game}\nReported username: ${username}\n\nDetails:\n${details}\n\nEvidence link: ${evidence}\n`
			);
			document.querySelector("#report-status").textContent =
				"Your email app will open. The report is sent only if you send the email.";
			window.location.href = `mailto:rangerthadeus54@gmail.com?subject=${subject}&body=${body}`;
		});

		const eventStartInput = document.querySelector("#event-start");
		const localDateTime = new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
			.toISOString()
			.slice(0, 16);
		eventStartInput.min = localDateTime;
		document.querySelector("#event-submission-form").addEventListener("submit", (event) => {
			event.preventDefault();
			const game = document.querySelector("#event-game").value;
			const name = document.querySelector("#event-name").value.trim();
			const start = eventStartInput.value;
			const link = document.querySelector("#event-link").value.trim();
			if (new Date(start).getTime() <= Date.now()) {
				document.querySelector("#event-submission-status").textContent =
					"Choose a future event date and time.";
				return;
			}
			const timeZone = Intl.DateTimeFormat().resolvedOptions().timeZone || "local time";
			const subject = encodeURIComponent(`Upcoming event suggestion: ${game} - ${name}`);
			const body = encodeURIComponent(
				`Game: ${game}\nEvent: ${name}\nStart: ${start} (${timeZone})\nOfficial event/organizer link: ${link}\n`
			);
			document.querySelector("#event-submission-status").textContent =
				"Your email app will open. The event will not appear on the site until it is reviewed and added.";
			window.location.href = `mailto:rangerthadeus54@gmail.com?subject=${subject}&body=${body}`;
		});

		const hardwareInputs = document.querySelectorAll('input[name="profile-hardware"]');
		hardwareInputs.forEach((input) => {
			input.addEventListener("change", () => {
				const selected = Array.from(hardwareInputs)
					.filter((option) => option.checked)
					.map((option) => option.value);
				document.querySelector("#hardware-selection-status").textContent = selected.length
					? `Selected: ${selected.join(", ")}. This selection is not saved yet.`
					: "No hardware selected. Selections are not saved until Supabase profile storage is configured.";
			});
		});

		const scoreCalculator = document.querySelector("#score-calculator");
		const scorePreviewResult = document.querySelector("#score-preview-result");
		const divisionThresholds = [
			{ division: "Division 1", minimum: 200 },
			{ division: "Division 2", minimum: 175 },
			{ division: "Division 3", minimum: 150 },
			{ division: "Division 4", minimum: 125 },
			{ division: "Division 5", minimum: 100 },
			{ division: "Division 6", minimum: 75 },
			{ division: "Division 7", minimum: 50 },
			{ division: "Division 8", minimum: 25 },
			{ division: "Division 9", minimum: 0 }
		];
		scoreCalculator.addEventListener("submit", (event) => {
			event.preventDefault();
			const wins = Number(document.querySelector("#score-wins").value);
			const draws = Number(document.querySelector("#score-draws").value);
			const losses = Number(document.querySelector("#score-losses").value);
			if (
				![wins, draws, losses].every(Number.isSafeInteger) ||
				[wins, draws, losses].some((value) => value < 0 || value > 10000)
			) {
				scorePreviewResult.textContent = "Enter whole, non-negative match totals.";
				scorePreviewResult.dataset.error = "true";
				return;
			}
			const points = wins * 3 + draws;
			const division = divisionThresholds.find((tier) => points >= tier.minimum);
			const game = document.querySelector("#score-game").value;
			scorePreviewResult.textContent =
				`${game}: ${points} proposed points (${division.division}). Record: ${wins} wins, ${draws} draws, ${losses} losses. Preview only; this score is not saved or verified.`;
			scorePreviewResult.dataset.error = "false";
		});

		const eventFeedStatus = document.querySelector("#event-feed-status");
		const eventFeedList = document.querySelector("#event-feed-list");
		const eventGameFilter = document.querySelector("#event-game-filter");
		const eventRefreshButton = document.querySelector("#event-refresh");
		const eventLoadMoreButton = document.querySelector("#event-load-more");
		let loadedEvents = [];
		let nextEventPage = 1;
		let hasMoreEvents = false;
		let eventFeedLoading = false;
		let eventFeedHasLoaded = false;

		function renderLiveEvents() {
			eventFeedList.replaceChildren();
			const selectedGame = eventGameFilter.value;
			const visibleEvents = loadedEvents.filter((item) =>
				selectedGame === "all" || item.game === selectedGame
			);
			if (visibleEvents.length === 0) {
				const emptyMessage = document.createElement("p");
				emptyMessage.className = "card feature-notice";
				emptyMessage.textContent = loadedEvents.length
					? "No loaded events match this game filter."
					: eventFeedHasLoaded
						? "No events are currently listed by the provider for this selection."
						: "Event listings will appear here when the live feed responds.";
				eventFeedList.append(emptyMessage);
				return;
			}

			visibleEvents.forEach((item) => {
				const card = document.createElement("article");
				card.className = "card";

				const badge = document.createElement("span");
				badge.className = "tag";
				badge.textContent = `${item.isLive ? "LIVE NOW" : "UPCOMING"} · ${item.game}`;

				const title = document.createElement("h3");
				title.textContent = item.competition || "Esports event";

				const match = document.createElement("p");
				match.textContent = item.name || "Scheduled match";

				const start = document.createElement("p");
				start.textContent = item.startAt
					? new Date(item.startAt).toLocaleString()
					: "Start time not published";

				const attribution = document.createElement("a");
				attribution.href = "https://www.pandascore.co/";
				attribution.target = "_blank";
				attribution.rel = "noopener noreferrer";
				attribution.textContent = "Source: PandaScore";

				card.append(badge, title, match, start, attribution);
				if (item.officialStream) {
					const stream = document.createElement("a");
					stream.href = item.officialStream;
					stream.target = "_blank";
					stream.rel = "noopener noreferrer";
					stream.textContent = "Official stream";
					card.append(stream);
				}
				eventFeedList.append(card);
			});
		}

		async function loadEventPage(reset = false) {
			if (eventFeedLoading) return;
			const requestedPage = reset ? 1 : nextEventPage;
			eventFeedLoading = true;
			eventRefreshButton.disabled = true;
			eventLoadMoreButton.disabled = true;
			eventFeedStatus.textContent = "Loading scheduled matches from PandaScore...";
			try {
				const response = await fetch(`/api/events?page=${requestedPage}`);
				const result = await response.json();
				if (!response.ok) {
					throw new Error(result.error || `Event feed returned HTTP ${response.status}.`);
				}
				if (!Array.isArray(result.events) || result.page !== requestedPage) {
					throw new Error("The event feed returned an invalid response.");
				}

				const updatedEvents = reset ? [] : [...loadedEvents];
				const existingIds = new Set(updatedEvents.map((item) => item.id));
				result.events.forEach((item) => {
					if (item && typeof item.id === "string" && !existingIds.has(item.id)) {
						existingIds.add(item.id);
						updatedEvents.push(item);
					}
				});
				loadedEvents = updatedEvents;
				nextEventPage = result.page + 1;
				hasMoreEvents = result.hasMore === true && result.limitReached !== true;
				eventFeedHasLoaded = true;

				const gameNames = [...new Set(loadedEvents.map((item) => item.game).filter(Boolean))]
					.sort((left, right) => left.localeCompare(right));
				const selectedGame = eventGameFilter.value;
				eventGameFilter.replaceChildren(new Option("All games", "all"));
				gameNames.forEach((game) => eventGameFilter.add(new Option(game, game)));
				eventGameFilter.value = gameNames.includes(selectedGame) ? selectedGame : "all";
				renderLiveEvents();

				const updatedAt = new Date(result.updatedAt).toLocaleTimeString();
				eventFeedStatus.textContent = `Loaded ${loadedEvents.length} provider-listed event${loadedEvents.length === 1 ? "" : "s"}. Updated ${updatedAt}. Times are shown in your local timezone.`;
				if (result.limitReached) {
					eventFeedStatus.textContent += " The provider page limit was reached.";
				}
				eventFeedStatus.dataset.error = "false";
				eventLoadMoreButton.hidden = !hasMoreEvents;
			} catch (error) {
				eventFeedStatus.textContent = loadedEvents.length
					? `Could not refresh the live event feed; previously loaded events are still shown. ${error.message}`
					: `Could not load the live event feed: ${error.message}`;
				eventFeedStatus.dataset.error = "true";
			} finally {
				eventFeedLoading = false;
				eventRefreshButton.disabled = false;
				eventLoadMoreButton.disabled = false;
			}
		}

		eventGameFilter.addEventListener("change", renderLiveEvents);
		eventRefreshButton.addEventListener("click", () => loadEventPage(true));
		eventLoadMoreButton.addEventListener("click", () => loadEventPage());
		loadEventPage(true);
		window.setInterval(() => loadEventPage(true), 5 * 60 * 1000);
	</script>
</body>
</html>'''

if __name__ == "__main__":
		print(HTML)
