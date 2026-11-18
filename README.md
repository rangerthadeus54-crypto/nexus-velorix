# NEXUS VELORIX event feed

This project builds the static site from `Retchan.py` and serves `/api/events` as a Vercel serverless function. The function requests current and upcoming esports matches from PandaScore; it does not expose the provider token to browsers.

## Configure and deploy

1. Create a PandaScore account and confirm that its data coverage and plan include the games you want to list.
2. In Vercel project settings, add the provider token as the `PANDASCORE_TOKEN` environment variable for the deployment environments you use. Never put this token in `Retchan.py`, generated HTML, or source control.
3. Deploy this folder as the Vercel project. `vercel.json` runs `build_site.py` to generate `public/index.html`; Vercel serves `api/events.js` at `/api/events`.
4. Visit `/api/events` on the deployed site to verify the feed. A missing token, provider error, or unsupported page is returned as an explicit HTTP error.

The page refreshes its event listings every five minutes and supports pagination. PandaScore coverage is limited to esports matches it tracks; it is not a universal source for every game, casual in-game event, or official organizer announcement. Verify event details with the organizer before relying on them.

The leaderboard includes a local preview using proposed match scoring (3 points per win, 1 per draw, 0 per loss) and Division 9-to-1 thresholds. These are examples only; scores are not saved, verified, or included in shared standings until trusted storage and result review are configured. The $10,000 USD prize pool shown on the page is an unconfirmed proposal, not a funded reward or payout offer.

## Configure Supabase authentication

1. Create a Supabase project and copy its project URL and **publishable/anon key** into `public/supabase-config.js`. These browser values are public; never put a `service_role` or secret key in this file.
2. In Supabase Auth settings, add the deployed site URL and `/sign-in.html` to the allowed redirect URLs. Configure the email provider and any OAuth/SMS providers you plan to offer. Apple and phone sign-in remain unavailable until their Supabase providers are configured.
3. Use Supabase Auth's built-in user store for sign-in. Do not enable profile, party, lobby, or chat storage until its database schema, row-level security policies, and moderation process have been reviewed. The related controls remain clickable, but clearly report that nothing was saved or sent while those features are disconnected. Community invite requests open an email to the organizer.
4. `public/terms.html` and `public/privacy.html` are starter drafts. Have the site operator verify the actual data practices and obtain jurisdiction-appropriate legal review before launch.

The site is static, so the Supabase project URL and publishable/anon key are delivered to browsers by design. Supabase row-level security—not secrecy of the anon key—must protect database data. The event provider token remains server-side in the `PANDASCORE_TOKEN` Vercel environment variable.

### Passkey sign-in

The sign-in page uses Supabase Auth's experimental passkey support from `@supabase/supabase-js` 2.105.0. In the Supabase Dashboard, open **Authentication → Passkeys**, enable passkey authentication, and configure the relying-party display name, bare domain ID, and allowed HTTPS origin(s) for the deployed site. Use `localhost` for local development. Choose the relying-party ID carefully; changing it invalidates passkeys registered for the previous domain. Users must first sign in to a confirmed account to create a passkey; they can then choose **Sign in with a passkey**. Biometrics, device PINs, and security-key operations stay with the authenticator and are not sent to the site.
