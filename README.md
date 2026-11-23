# Developer portfolio

A small static Astro portfolio for Jakub Bartošovič with a dark navy/purple design, NumForge, TwinStar Progress, and ARC case studies, and GitHub Pages deployment support. Project summaries are grounded in repository documentation and the live applications. TwinStar Progress links to its public website; its source repository is private.

## Local development

Requires Node.js 22.12+ (Node 24 also works).

```sh
npm install
npm run dev
npm run check
npm run build
npm run preview
```

## Personalize

- `src/data/profile.ts`: public name, role, GitHub, LinkedIn, email, skills. Empty contact links are omitted rather than pointing at fake accounts.
- `src/content/projects/*.md`: project descriptions, status, tags, optional `repository`, `release`, and `website` URLs, and detailed case study text.
- `src/pages/index.astro`: introduction and background copy; add dates and responsibilities when confirmed.
- `src/styles/global.css`: colors and layout. Add `data-theme="red"` to the `<html>` element in `src/layouts/Layout.astro` for the alternative red accent.
- `public/social.svg` and `public/social.png`: editable vector and raster social sharing image.
- `src/pages/resume.astro`: résumé from confirmed facts, with print styling.
- `public/jakub-bartosovic-resume.pdf`: one-page downloadable CV. Regenerate with `scripts/build_resume.py` using Python + ReportLab + pypdf; it uses Windows Arial fonts. Keep its facts aligned with the résumé page.
- `public/images/numforge-calculator-2026-10.webp` (NumForge documentation capture, 27 October 2026) and `public/images/arc-demo.png` (supplied by the author): project screenshots. ARC shows demo roster data. `public/images/twinstar-progress-2026-11.webp` is a live website capture from 23 November 2026. All screenshots support click-to-enlarge overlays capped at 80% of the viewport.

## GitHub Pages and your GitHub profile

These are two separate repositories:

1. **Website:** create `Interacti0n.github.io` in your GitHub account, put this project there on branch `main`, and choose **GitHub Actions** in Settings → Pages. The included workflow installs, checks, builds, and deploys. Your site will be `https://Interacti0n.github.io/`.
2. **Profile README:** create a public repository named exactly `Interacti0n`. Copy `docs/github-profile-README.md` to that repository as `README.md` after publishing the site. This text appears on your GitHub profile. Add the portfolio URL to your profile's website field too.

A differently named website repository also works: the workflow obtains the correct base path from GitHub Pages. For local production-path verification, set `SITE_URL` and `BASE_PATH` before building. No account credentials or tokens belong in site source.

## Before publishing

Review public facts and contact links. Add employment dates or new responsibilities only when confirmed. Review the social sharing image and all external links.

The site has no backend or client-side framework. Fonts use Google Fonts with local system fallbacks. Content and assets render as static HTML/CSS. Deployment remains unconfigured until connected to your GitHub repository.
