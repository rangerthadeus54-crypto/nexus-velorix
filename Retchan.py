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

		.login-panel .consent-label { display: flex; align-items: flex-start; }
		.login-panel .consent-label input { width: auto; margin: 0.25rem 0.5rem 0 0; }
		.login-panel button.button { cursor: pointer; }
		.login-panel button:disabled { cursor: not-allowed; opacity: 0.6; }
		.login-actions { display: flex; flex-wrap: wrap; gap: 0.5rem; }
		.auth-message { min-height: 1.5rem; color: #8fe6ff; }
		.auth-message[data-error="true"] { color: #fca5a5; }

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

		.platform-options {
			display: flex;
			flex-wrap: wrap;
			gap: 0.5rem 1rem;
			padding: 0.9rem;
			border: 1px solid var(--border);
			border-radius: 0.5rem;
		}

		.platform-options legend { padding: 0 0.35rem; color: #cfe2fa; }
		.platform-options label { display: flex; align-items: center; gap: 0.4rem; }
		.platform-options input { width: auto; margin: 0; padding: 0; border: 0; background: transparent; }

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
	</style>
</head>
<body>
	<header>
		<div class="logo">
			<strong>NEXUS VELORIX</strong>
			<span>Play, Win and Teamwork</span>
		</div>
		<nav aria-label="Main navigation">
			<a href="#games">Games</a>
			<a href="#profiles">Profiles</a>
			<a href="#teammates">Find teammates</a>
			<a href="#chat">Chat</a>
			<a href="#leaderboards">Leaderboards</a>
			<a href="#news">News</a>
			<a href="#upcoming-events">Live events</a>
			<a href="#communities">Communities</a>
			<a href="#tournaments">Tournaments</a>
			<a href="#report">Report activity</a>
			<a href="#membership">Membership</a>
			<a href="#login">Sign in</a>
			<a href="#join">Join</a>
		</nav>
	</header>

	<main>
		<section class="hero" id="about">
			<h1>Play together. Level up.</h1>
			<p>Find teammates, join events, and meet your next favorite gaming crew.</p>
			<a class="button" href="#login">Sign in or create an account</a>
		</section>

		<section id="login" class="login-panel">
			<h2>Sign in to NEXUS VELORIX</h2>
			<p class="membership-status">Sign in with email and password, an email link, Apple, or phone verification.</p>
			<p id="auth-message" class="auth-message" role="status" aria-live="polite">
				Firebase sign-in needs your web app configuration before it can be used.
			</p>
			<div class="card">
				<form id="email-password-form">
					<label for="auth-email">Email address
						<input id="auth-email" type="email" autocomplete="email" required>
					</label>
					<label for="auth-password">Password
						<input id="auth-password" type="password" autocomplete="current-password" minlength="6" required>
					</label>
					<div class="login-actions">
						<button class="button" type="submit" value="signin">Sign in with email</button>
						<button class="button" type="submit" value="signup">Create account</button>
						<button class="button" id="password-reset" type="button">Reset password</button>
					</div>
				</form>

				<form id="email-link-form">
					<label for="email-link-address">Email link sign-in
						<input id="email-link-address" type="email" autocomplete="email" required>
					</label>
					<button class="button" type="submit">Send sign-in link</button>
				</form>

				<form id="email-link-complete-form" hidden>
					<label for="email-link-complete-address">Confirm the email address that received the link
						<input id="email-link-complete-address" type="email" autocomplete="email" required>
					</label>
					<button class="button" type="submit">Complete email sign-in</button>
				</form>

				<button class="button" id="apple-sign-in" type="button">Continue with Apple</button>

				<form id="phone-form">
					<label for="phone-number">Phone number (include country code)
						<input id="phone-number" type="tel" autocomplete="tel" placeholder="+15551234567" pattern="^\+[1-9][0-9]{1,14}$" required>
					</label>
					<label class="consent-label">
						<input id="sms-consent" type="checkbox" required>
						I agree to receive a verification text; message and data rates may apply.
					</label>
					<div id="recaptcha-container"></div>
					<button class="button" type="submit">Send verification code</button>
				</form>

				<form id="phone-code-form" hidden>
					<label for="phone-code">SMS verification code
						<input id="phone-code" type="text" inputmode="numeric" autocomplete="one-time-code" required>
					</label>
					<button class="button" type="submit">Verify code and sign in</button>
				</form>

				<p class="membership-status">Phone sign-in uses SMS verification and requires an authorized HTTPS domain and allowed Firebase SMS regions. Firebase may process phone numbers for abuse prevention; message and data rates may apply.</p>
				<div id="signed-in-panel" hidden>
					<p>Signed in as <span id="signed-in-user"></span>.</p>
					<button class="button" id="sign-out" type="button">Sign out</button>
				</div>
			</div>
		</section>

		<section id="age-verification" class="login-panel" hidden>
			<h2>Age check</h2>
			<p class="membership-status">NEXUS VELORIX requires members to be 13 or older. Enter your display name and birth date. This is a self-declaration, not identity verification.</p>
			<p class="feature-notice">Your birth date is used only for the age calculation and is not saved. Only your display name, eligibility result, and check time are stored.</p>
			<div class="card">
				<form id="age-verification-form" class="feature-form">
					<label for="age-display-name">Display name
						<input id="age-display-name" type="text" autocomplete="nickname" minlength="2" maxlength="32" required>
					</label>
					<div class="birth-date-fields">
						<label for="birth-day">Day
							<input id="birth-day" type="number" min="1" max="31" inputmode="numeric" required>
						</label>
						<label for="birth-month">Month
							<input id="birth-month" type="number" min="1" max="12" inputmode="numeric" required>
						</label>
						<label for="birth-year">Year
							<input id="birth-year" type="number" min="1900" inputmode="numeric" required>
						</label>
					</div>
					<button class="button" type="submit">Verify age</button>
				</form>
				<p id="age-check-result" class="auth-message" role="status" aria-live="polite"></p>
			</div>
		</section>

		<section id="hardware-selection" class="login-panel" hidden>
			<h2>Select Your Gaming Hardware</h2>
			<p class="membership-status">Choose all platforms you play on. This panel appears after sign-in and the age check.</p>
			<div class="card">
				<fieldset class="platform-options">
					<legend>Gaming hardware</legend>
					<label><input type="checkbox" name="profile-hardware" value="PlayStation"> PlayStation</label>
					<label><input type="checkbox" name="profile-hardware" value="Xbox"> Xbox</label>
					<label><input type="checkbox" name="profile-hardware" value="PC"> PC</label>
					<label><input type="checkbox" name="profile-hardware" value="Nintendo"> Nintendo</label>
					<label><input type="checkbox" name="profile-hardware" value="Mobile"> Mobile</label>
					<label><input type="checkbox" name="profile-hardware" value="Other"> Other</label>
				</fieldset>
				<p id="hardware-selection-status" class="feature-notice" role="status" aria-live="polite">Selections are not saved until Firebase profile storage is configured.</p>
			</div>
		</section>

		<section id="games" class="game-feed" aria-labelledby="game-feed-title">
			<div class="game-feed-heading">
				<div>
					<p class="game-feed-kicker">Discover your next squad</p>
					<h2 id="game-feed-title">Game feed</h2>
					<p>Browse featured games, save favorites, and find people to play with. Player counts are not live.</p>
				</div>
				<span class="game-feed-count" id="game-feed-count">12 featured games</span>
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
						<option value="valorant">VALORANT</option>
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
				<article class="card game-card" data-game="valorant">
					<span class="tag">Tactical</span>
					<h3>VALORANT</h3>
					<p>Meet players for coordinated, competitive matches.</p>
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
				<p class="membership-status">No community profiles are available yet. Firebase configuration and Firestore security rules are required for shared profiles.</p>
				<form class="feature-form">
					<label for="profile-name">Display name
						<input id="profile-name" type="text" maxlength="32" disabled>
					</label>
					<label for="profile-games">Favorite games
						<input id="profile-games" type="text" placeholder="Choose games after setup" disabled>
					</label>
					<label for="profile-region">Region
						<select id="profile-region" disabled>
							<option>Select a region</option>
							<option>North America</option><option>South America</option>
							<option>Europe</option><option>Asia</option>
							<option>Oceania</option><option>Africa</option>
						</select>
					</label>
					<button class="button" type="button" disabled>Save profile — setup required</button>
				</form>
			</div>
		</section>

		<section id="teammates">
			<h2>Find Teammates</h2>
			<p class="membership-status">Search for players by game and region after profiles are enabled.</p>
			<div class="toolbar">
				<label for="teammate-game">Game
					<select id="teammate-game" disabled>
						<option>All games</option><option>Fortnite</option><option>Roblox</option>
						<option>Minecraft</option><option>Free Fire</option><option>Call of Duty</option>
						<option>EA SPORTS FC 26</option><option>eFootball</option><option>GTA 6</option>
					</select>
				</label>
				<label for="teammate-region">Region
					<select id="teammate-region" disabled>
						<option>All regions</option><option>North America</option>
						<option>South America</option><option>Europe</option>
						<option>Asia</option><option>Oceania</option><option>Africa</option>
					</select>
				</label>
				<label for="teammate-hardware">Hardware
					<select id="teammate-hardware" disabled>
						<option>All hardware</option><option>PlayStation</option><option>Xbox</option>
						<option>PC</option><option>Nintendo</option><option>Mobile</option><option>Other</option>
					</select>
				</label>
			</div>
			<p class="card membership-status">No teammate profiles to show yet. Sign-in and Firestore setup are required.</p>
		</section>

		<section id="chat">
			<h2>Game Chat</h2>
			<p class="membership-status">Public game channels are planned. Chat is inactive until Firebase and Firestore rules are configured.</p>
			<div class="card">
				<label for="chat-game">Game channel
					<select id="chat-game" disabled>
						<option>Choose a game</option><option>Fortnite</option><option>Roblox</option>
						<option>Minecraft</option><option>Free Fire</option><option>Call of Duty</option>
						<option>EA SPORTS FC 26</option><option>eFootball</option><option>GTA 6</option>
					</select>
				</label>
				<p class="feature-notice" role="status">No messages. Chat is not connected.</p>
				<form class="feature-form">
					<label for="chat-message">Message
						<textarea id="chat-message" maxlength="500" rows="3" disabled></textarea>
					</label>
					<button class="button" type="button" disabled>Send — setup required</button>
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
							<option>Free Fire</option><option>Call of Duty</option><option>VALORANT</option>
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
				<p class="membership-status">No verified results are available. Firebase score storage, access rules, and result review must be configured before real standings can appear.</p>
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
						<option>VALORANT</option>
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
			<p class="membership-status">Join links have not been provided yet. Submit verified invites through the server directory for review.</p>
			<div class="cards">
				<article class="card"><h3>Fortnite</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>Roblox</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>Minecraft</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>Free Fire</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>Call of Duty</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>EA SPORTS FC 26</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>eFootball</h3><p>Community invite link pending.</p></article>
				<article class="card"><h3>GTA 6</h3><p>Community invite link pending.</p></article>
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

	<footer>
		<p>© 2026 NEXUS VELORIX. All rights reserved.</p>
		<p>A community for gamers · <a href="#report">Report suspicious activity</a> · <a href="mailto:rangerthadeus54@gmail.com">Contact the organizer</a></p>
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
			"valorant": ["#d84055", "#431c39", "#ff9aa6", "V"],
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
					: "No hardware selected. Selections are not saved until Firebase profile storage is configured.";
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
	<script type="module">
		import { initializeApp } from "https://www.gstatic.com/firebasejs/13.3.0/firebase-app.js";
		import {
			createUserWithEmailAndPassword,
			getAuth,
			getRedirectResult,
			isSignInWithEmailLink,
			onAuthStateChanged,
			OAuthProvider,
			RecaptchaVerifier,
			sendPasswordResetEmail,
			sendSignInLinkToEmail,
			signInWithEmailAndPassword,
			signInWithEmailLink,
			signInWithPhoneNumber,
			signInWithRedirect,
			signOut
		} from "https://www.gstatic.com/firebasejs/13.3.0/firebase-auth.js";
		import {
			doc,
			getDoc,
			getFirestore,
			serverTimestamp,
			setDoc
		} from "https://www.gstatic.com/firebasejs/13.3.0/firebase-firestore.js";

		const firebaseConfig = {
			apiKey: "",
			authDomain: "",
			projectId: "",
			appId: ""
		};
		const authMessage = document.querySelector("#auth-message");
		const authControls = document.querySelectorAll("#login input, #login button");
		const configReady = Object.values(firebaseConfig).every((value) => value.trim() !== "");

		function showAuthMessage(message, isError = false) {
			authMessage.textContent = message;
			authMessage.dataset.error = String(isError);
		}

		if (!configReady) {
			authControls.forEach((control) => { control.disabled = true; });
			showAuthMessage("Add your Firebase web app configuration to enable sign-in.", true);
		} else {
			const app = initializeApp(firebaseConfig);
			const auth = getAuth(app);
			const db = getFirestore(app);
			let recaptchaVerifier;
			let phoneConfirmation;

			if (isSignInWithEmailLink(auth, window.location.href)) {
				const completionForm = document.querySelector("#email-link-complete-form");
				completionForm.hidden = false;
				document.querySelector("#email-link-form").hidden = true;
				document.querySelector("#email-link-complete-address").value =
					sessionStorage.getItem("emailForSignIn") || "";
				showAuthMessage("Enter the email address that received your sign-in link.");
			}

			document.querySelector("#email-password-form").addEventListener("submit", async (event) => {
				event.preventDefault();
				const email = document.querySelector("#auth-email").value.trim();
				const password = document.querySelector("#auth-password").value;
				try {
					if (event.submitter?.value === "signup") {
						await createUserWithEmailAndPassword(auth, email, password);
						showAuthMessage("Account created and signed in.");
					} else {
						await signInWithEmailAndPassword(auth, email, password);
						showAuthMessage("Signed in successfully.");
					}
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			document.querySelector("#password-reset").addEventListener("click", async () => {
				const email = document.querySelector("#auth-email").value.trim();
				if (!email) {
					showAuthMessage("Enter your email address first to request a password reset.", true);
					return;
				}
				try {
					await sendPasswordResetEmail(auth, email);
					showAuthMessage("Password reset email sent.");
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			document.querySelector("#email-link-form").addEventListener("submit", async (event) => {
				event.preventDefault();
				const email = document.querySelector("#email-link-address").value.trim();
				const continueUrl = new URL(window.location.pathname, window.location.origin).href;
				try {
					await sendSignInLinkToEmail(auth, email, {
						url: continueUrl,
						handleCodeInApp: true
					});
					sessionStorage.setItem("emailForSignIn", email);
					showAuthMessage("Sign-in link sent. Check your email to continue.");
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			document.querySelector("#email-link-complete-form").addEventListener("submit", async (event) => {
				event.preventDefault();
				const email = document.querySelector("#email-link-complete-address").value.trim();
				try {
					await signInWithEmailLink(auth, email, window.location.href);
					sessionStorage.removeItem("emailForSignIn");
					history.replaceState(null, document.title, window.location.pathname);
					showAuthMessage("Signed in successfully.");
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			document.querySelector("#apple-sign-in").addEventListener("click", async () => {
				const provider = new OAuthProvider("apple.com");
				provider.addScope("email");
				provider.addScope("name");
				try {
					await signInWithRedirect(auth, provider);
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			const phoneForm = document.querySelector("#phone-form");
			const phoneButton = phoneForm.querySelector("button");
			const localHostnames = ["localhost", "127.0.0.1"];
			const phoneDomainReady =
				window.location.protocol === "https:" &&
				!localHostnames.includes(window.location.hostname);
			if (!phoneDomainReady) {
				phoneButton.disabled = true;
				showAuthMessage("Deploy this site on an authorized HTTPS domain to use phone sign-in.");
			}

			phoneForm.addEventListener("submit", async (event) => {
				event.preventDefault();
				if (!phoneDomainReady) {
					showAuthMessage("Phone sign-in requires an authorized HTTPS domain.", true);
					return;
				}
				try {
					recaptchaVerifier ??= new RecaptchaVerifier(auth, "recaptcha-container", {});
					phoneConfirmation = await signInWithPhoneNumber(
						auth,
						document.querySelector("#phone-number").value.trim(),
						recaptchaVerifier
					);
					document.querySelector("#phone-code-form").hidden = false;
					showAuthMessage("Verification code sent by SMS. Enter it below.");
				} catch (error) {
					await recaptchaVerifier?.clear();
					recaptchaVerifier = undefined;
					showAuthMessage(error.message, true);
				}
			});

			document.querySelector("#phone-code-form").addEventListener("submit", async (event) => {
				event.preventDefault();
				if (!phoneConfirmation) {
					showAuthMessage("Request an SMS verification code first.", true);
					return;
				}
				try {
					await phoneConfirmation.confirm(document.querySelector("#phone-code").value.trim());
					showAuthMessage("Phone verified and signed in.");
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			document.querySelector("#sign-out").addEventListener("click", async () => {
				try {
					await signOut(auth);
					showAuthMessage("Signed out.");
				} catch (error) {
					showAuthMessage(error.message, true);
				}
			});

			const ageSection = document.querySelector("#age-verification");
			const ageForm = document.querySelector("#age-verification-form");
			const ageResult = document.querySelector("#age-check-result");
			const hardwareSection = document.querySelector("#hardware-selection");
			const birthYearInput = document.querySelector("#birth-year");
			birthYearInput.max = String(new Date().getFullYear());

			function calculateAge(day, month, year, today = new Date()) {
				if (
					!Number.isInteger(day) || !Number.isInteger(month) || !Number.isInteger(year) ||
					year < 1900 || month < 1 || month > 12 || day < 1 || day > 31
				) {
					return null;
				}
				const birthDate = new Date(year, month - 1, day);
				if (
					birthDate.getFullYear() !== year ||
					birthDate.getMonth() !== month - 1 ||
					birthDate.getDate() !== day ||
					birthDate > new Date(today.getFullYear(), today.getMonth(), today.getDate())
				) {
					return null;
				}
				let age = today.getFullYear() - year;
				if (
					today.getMonth() + 1 < month ||
					(today.getMonth() + 1 === month && today.getDate() < day)
				) {
					age -= 1;
				}
				return age;
			}

			ageForm.addEventListener("submit", async (event) => {
				event.preventDefault();
				const user = auth.currentUser;
				if (!user) {
					ageResult.textContent = "Sign in before completing the age check.";
					return;
				}

				const displayName = document.querySelector("#age-display-name").value.trim();
				const day = Number(document.querySelector("#birth-day").value);
				const month = Number(document.querySelector("#birth-month").value);
				const year = Number(birthYearInput.value);
				const age = calculateAge(day, month, year);
				if (displayName.length < 2 || age === null) {
					ageResult.textContent = "Enter a valid display name and birth date.";
					ageResult.dataset.error = "true";
					return;
				}
				document.querySelector("#birth-day").value = "";
				document.querySelector("#birth-month").value = "";
				birthYearInput.value = "";
				try {
					await setDoc(doc(db, "userProfiles", user.uid), {
						displayName,
						ageEligible: age >= 13,
						ageCheckedAt: serverTimestamp()
					}, { merge: true });
					ageForm.reset();
					if (age >= 13) {
						ageForm.hidden = true;
						hardwareSection.hidden = false;
						ageResult.textContent = "Age check passed. Your birth date was not saved.";
						document.querySelector("#signed-in-user").textContent = displayName;
					} else {
						hardwareSection.hidden = true;
						ageResult.textContent = "You must be at least 13 to use this community.";
					}
					ageResult.dataset.error = String(age < 13);
				} catch (error) {
					ageResult.textContent = error.message;
					ageResult.dataset.error = "true";
				}
			});

			onAuthStateChanged(auth, async (user) => {
				const signedInPanel = document.querySelector("#signed-in-panel");
				signedInPanel.hidden = !user;
				ageSection.hidden = !user;
				hardwareSection.hidden = true;
				if (user) {
					document.querySelector("#signed-in-user").textContent =
						user.displayName || user.email || user.phoneNumber || user.uid;
					try {
						const profile = await getDoc(doc(db, "userProfiles", user.uid));
						const ageEligible = profile.exists() && profile.data().ageEligible === true;
						hardwareSection.hidden = !ageEligible;
						ageForm.hidden = ageEligible;
						ageResult.textContent = ageEligible
							? "Age check complete. Your birth date is not stored."
							: "Complete the age check to continue.";
						ageResult.dataset.error = "false";
						if (ageEligible && profile.data().displayName) {
							document.querySelector("#signed-in-user").textContent = profile.data().displayName;
						}
					} catch (error) {
						hardwareSection.hidden = true;
						ageForm.hidden = false;
						ageResult.textContent = error.message;
						ageResult.dataset.error = "true";
					}
				}
			}, (error) => {
				showAuthMessage(error.message, true);
			});

			getRedirectResult(auth).catch((error) => {
				showAuthMessage(error.message, true);
			});
		}
	</script>
</body>
</html>'''

if __name__ == "__main__":
		print(HTML)
