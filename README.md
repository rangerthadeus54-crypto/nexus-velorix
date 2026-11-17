# NEXUS VELORIX event feed

This project builds the static site from `Retchan.py` and serves `/api/events` as a Vercel serverless function. The function requests current and upcoming esports matches from PandaScore; it does not expose the provider token to browsers.

## Configure and deploy

1. Create a PandaScore account and confirm that its data coverage and plan include the games you want to list.
2. In Vercel project settings, add the provider token as the `PANDASCORE_TOKEN` environment variable for the deployment environments you use. Never put this token in `Retchan.py`, generated HTML, or source control.
3. Deploy this folder as the Vercel project. `vercel.json` runs `build_site.py` to generate `public/index.html`; Vercel serves `api/events.js` at `/api/events`.
4. Visit `/api/events` on the deployed site to verify the feed. A missing token, provider error, or unsupported page is returned as an explicit HTTP error.

The page refreshes its event listings every five minutes and supports pagination. PandaScore coverage is limited to esports matches it tracks; it is not a universal source for every game, casual in-game event, or official organizer announcement. Verify event details with the organizer before relying on them.

The leaderboard includes a local preview using proposed match scoring (3 points per win, 1 per draw, 0 per loss) and Division 9-to-1 thresholds. These are examples only; scores are not saved, verified, or included in shared standings until trusted storage and result review are configured. The $10,000 USD prize pool shown on the page is an unconfirmed proposal, not a funded reward or payout offer.
