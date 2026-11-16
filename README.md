# Cognitive Forge — Engineering tutorials

Published with Jekyll and GitHub Pages at https://cognitiveforge630.github.io/cognitiveforge.github.io/.

Tutorial001 contains eight illustrated C0 Lagrange Hex8/Hex27/Hex64 lessons and Appendix A1 preserving HexahedronMomentDocs. The previous research landing page is retained in Git history.

## Local preview

```powershell
bundle install
bundle exec jekyll serve --baseurl /cognitiveforge.github.io
```

Open http://127.0.0.1:4000/cognitiveforge.github.io/.

## Comments

A discussion box is present on every content page. To activate posting:

1. Enable Discussions in this public GitHub repository.
2. Install the Giscus GitHub app for this repository, then configure it at https://giscus.app/.
3. Copy the repository ID and category ID into `giscus` in `_config.yml`, select the matching category, and set `enabled: true`.
4. Commit and push. Discussions use each page's pathname so lessons remain separate.

No comment credentials or fabricated IDs are included. Set `comments: false` in an individual page's front matter to hide its box.

## Analytics

The shared default layout includes the GoatCounter script exactly once per content page. The endpoint is https://cognitiveforge.goatcounter.com/count. GoatCounter records each visited URL path separately; the account dashboard is https://cognitiveforge.goatcounter.com/.

Localhost and private-network visits are ignored by GoatCounter by default. Browser blocking or disabled JavaScript may prevent counts. No API key is needed for the public tracking script.

## Publishing

Push this Jekyll source to `main`. In repository Settings → Pages, choose **Deploy from a branch**, branch **main**, folder **/(root)**. GitHub Pages builds the site; do not commit `_site/`.

Appendix A1 includes an unchanged downloadable source snapshot. All page URLs include the configured project base path. `sitemap.xml` lists the content pages automatically.
