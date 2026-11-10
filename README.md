# StellarGrok: a Quarto blog

A Quarto blog for posts that mix Markdown, Python, R and Mermaid diagrams, styled with
the Optimizely-inspired brand kit. Netlify builds and hosts it straight from the GitHub repo.

```
├── _quarto.yml            site config: navbar, theme, freeze
├── index.qmd              home: hero, section tiles, latest posts
├── blog.qmd               all posts, filterable by category
├── about.qmd              about page
├── sections/              one landing page per section (a mini blog each)
│   ├── ai.qmd  data.qmd  art.qmd  leadership.qmd  other.qmd
├── posts/
│   ├── _metadata.yml      defaults for every post (author, toc, freeze)
│   ├── ai/  data/  art/  leadership/  other/
│   │   └── YYYY-MM-DD-slug/index.qmd
├── _freeze/               cached code results. COMMIT THIS.
├── assets/
│   ├── theme.scss         brand theme (colours, fonts, cards, hero, 3D headline)
│   ├── fonts.css + fonts/ free fonts (OFL)
│   ├── StellarGrok.py      matplotlib style   -> StellarGrok.use()
│   ├── theme_StellarGrok.R ggplot2 theme      -> theme_StellarGrok(), scale_*_StellarGrok()
│   ├── svg/               illustrations, decor, icons
│   └── images/            social sharing image
├── scripts/new_post.py    create a post skeleton
├── netlify.toml + package.json   Netlify build: Quarto plugin, publish _site/
├── netlify.toml
├── requirements.txt / install.R
└── StellarGrok.Rproj      open in RStudio if you prefer
```

## 1. One-time setup on your machine

1. Install Quarto from [quarto.org/docs/get-started](https://quarto.org/docs/get-started/).
   This template was tested with Quarto **1.11.9**, and Netlify pins the same version in `netlify.toml`.
2. Set up Python:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Set up R: `Rscript install.R`
4. Preview the site: `quarto preview`

## 2. Writing a post

```bash
python scripts/new_post.py ai "What I learned building an agent"          # Python post
python scripts/new_post.py data "Tidy Tuesday: coffee prices" --r         # R post
```

This creates `posts/<section>/<date>-<slug>/index.qmd` with `draft: true`. Drafts show in
`quarto preview` but are left out of the published site. Remove that line when the post is ready.

* **Section:** the folder decides which section page lists the post. Keep the first category
  the same as the section name (`AI`, `Data`, `Art`, `Leadership`, `Other`) so filtering on
  the blog page works.
* **Card image:** `image:` in the front matter. Use an illustration from `assets/svg/illustrations/`
  or put a `thumbnail.png` in the post folder.
* **Diagrams:** add a ```` ```{mermaid} ```` block. It picks up the brand colours automatically.
* **3D headline:** in raw HTML or a Markdown span, `[big results]{.extrude}`.
* **One language per post.** Python posts use `jupyter: python3`, and R posts just use `{r}` chunks.
  To mix the two, use `reticulate` from R.

## 3. Publishing

Code only runs on your machine. `quarto render` saves the results in `_freeze/`, and Netlify
re-uses them, so Netlify never needs Python or R.

```bash
quarto render              # runs any changed posts, updates _freeze/
git add . && git commit -m "New post: …"
git push                   # Netlify installs Quarto, renders and deploys
```

If you forget to render first, the Netlify build fails on that post instead of publishing a broken page.

### How the Netlify build works

* `netlify.toml` sets the publish folder to `_site`, pins `QUARTO_VERSION`, and enables the
  official `@quarto/netlify-plugin-quarto` plugin (listed in `package.json`).
* The plugin installs Quarto and runs `quarto render` during the build. The `command` in
  `netlify.toml` is a placeholder that overrides any older build command saved in the Netlify UI.
* Branches and pull requests get Netlify deploy previews if they're enabled for the site.
* After upgrading Quarto locally, update `QUARTO_VERSION` in `netlify.toml` to match.

### Post thumbnails in lists (on/off)

Post lists (home, All posts, section pages) show **no thumbnails** by default, so you don't need to
find an image for every post. Keep an `image:` line in a post's front matter anyway when you have a
good one: it's used for link previews on LinkedIn and elsewhere.

To bring thumbnails back, add `image` to the start of the `fields:` line in `index.qmd`,
`blog.qmd` and each file in `sections/`:

```yaml
  fields: [image, date, title, description, categories, reading-time]
  image-height: 84px
```

The styles for both layouts are already in `assets/theme.scss`, so nothing else needs changing.

## 4. Customising

| What | Where |
|---|---|
| Site name, navbar, footer, social links | `_quarto.yml` |
| Colours, fonts, card and hero styling | `assets/theme.scss` (palette at the top) |
| Home page hero text and section tiles | `index.qmd` |
| Section blurbs and hero colours | `sections/*.qmd` |
| Chart colours | `assets/StellarGrok.py`, `assets/theme_StellarGrok.R` |
| Default author and TOC | `posts/_metadata.yml` |

**Adding or removing a section:** create or delete `posts/<name>/`, create or delete
`sections/<name>.qmd` (copy an existing one), and update the Blog menu in `_quarto.yml` and the
tile in `index.qmd`.

**Running code on the server instead:** Netlify's build image can't run R or Python reliably; if you ever need that, render in GitHub Actions and deploy the `_site` folder instead of using the plugin, and set
`freeze: false` in `posts/_metadata.yml`. Builds get slower, but you no longer need to commit `_freeze/`.
