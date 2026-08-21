# Thistle Flooring

Public website for Thistle Flooring — premium vinyl, laminate, hardwood, and carpet sourcing & installation.

## Local development

```bash
npm start
```

Opens on [http://localhost:3000](http://localhost:3000). Railway sets `PORT` automatically in production.

## Deploy on Railway (from GitHub)

1. Push this repo to GitHub (already done if you cloned `Rthistle-Data/thistle-flooring`).
2. Go to [railway.app](https://railway.app) and sign in with GitHub.
3. **New Project → Deploy from GitHub repo**.
4. Select **thistle-flooring**.
5. Railway detects Node, runs `npm start`, and binds `$PORT`.
6. Open the service → **Settings → Networking → Generate domain**.

That’s the live site. Add a custom domain in the same Networking panel when you have one.

### Quote form → Gmail

The contact form posts to `/api/quote` and emails **thistleflooringinstalls@gmail.com**. It does not open the visitor’s mail app.

Add this Railway variable (Variables tab on the service):

| Variable | Value |
|---|---|
| `GMAIL_USER` | `thistleflooringinstalls@gmail.com` |
| `GMAIL_APP_PASSWORD` | Google App Password (not the normal Gmail password) |
| `QUOTE_TO` | `thistleflooringinstalls@gmail.com` |

Create the App Password:

1. Sign in to the Thistle Flooring Google account.
2. Turn on [2-Step Verification](https://myaccount.google.com/signinoptions/two-step-verification) if it isn’t on.
3. Open [App passwords](https://myaccount.google.com/apppasswords).
4. Create a password for “Mail” / “Thistle Flooring website”.
5. Paste the 16-character password into `GMAIL_APP_PASSWORD` on Railway (no spaces).
6. Redeploy.

Reply in Gmail goes to the customer, because the quote uses their address as Reply-To.

Health check: `GET /health` returns `ok`.

## Pages

| URL | File |
|---|---|
| `/` | Homepage |
| `/services` | Vinyl ($3/sq ft vinyl click), laminate, hardwood, carpet |
| `/winter-special` | Winter Hibernation Special — free carpet tear-out |
| `/kitchen-revival` | Express Kitchen Floor Revival — $500 + material |
| `/gallery` | Project photography |
| `/contact` | Quote request |

## Contact

- Email: thistleflooringinstalls@gmail.com
- Phone (text only): (587) 594-8169

## Project layout

```
server.mjs          Static site + POST /api/quote
mail.mjs            Sends quote requests through Gmail
railway.toml        Railway build & health check
nixpacks.toml       Node 22 on Railway
assets/             Optimized gallery + brand images
_build_pages.py     Regenerates HTML from the shared template
```

Source job photos stay in local `pictures/` (not deployed). Regenerating pages:

```bash
python3 _build_pages.py
```
