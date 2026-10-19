# Puberty101.com

Independent, plain-language puberty education for teens, parents and educators. Static site, hosted free on GitHub Pages.

- 18 in-depth guides (`content/articles/*.md`)
- 6 interactive tools (`/tools/`)
- Lead generation: Starter Kit (parents), 4-step school request, newsletter, exit-intent modal
- Monetization: Google AdSense (`ca-pub-6620975821265271`), sponsorships, donations, contests
- Strategy and the phase-wise build prompt: [`BUILD-PROMPT.md`](BUILD-PROMPT.md)

## Build
```
pip install markdown
python3 build/build.py
```
Edit content in `content/articles/`, layout in `build/layout.py`, pages in `build/pages.py`, tools in `build/tools.py`. The build writes HTML to the repo root.

## Deploy
GitHub → Settings → Pages → Deploy from branch `main` / root. Custom domain: `puberty101.com` (see `CNAME`).

## Trademark notice
Puberty101.com is an independent publication, not affiliated with any organization, product or trademark using the name "Puberty 101" or similar. See `disclaimer.html`.
