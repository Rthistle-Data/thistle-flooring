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
server.mjs          Production static server (zero dependencies)
railway.toml        Railway build & health check
nixpacks.toml       Node 22 on Railway
assets/             Optimized gallery + brand images
_build_pages.py     Regenerates HTML from the shared template
```

Source job photos stay in local `pictures/` (not deployed). Regenerating pages:

```bash
python3 _build_pages.py
```
