---
title: TwinStar Progress
subtitle: From raid results to searchable rankings.
summary: A live website for comparing guild progress, fastest boss kills, and heroic kill counts across three TwinStar game realms.
tags: [React, TypeScript, SQLite, Cloudflare Pages]
status: Live website
website: https://twinstar-progress.pages.dev/
image: images/twinstar-progress-2026-11.webp
imageWidth: 1440
imageHeight: 900
imageAlt: TwinStar Progress showing Siege of Orgrimmar guild rankings, realm navigation, raid filters, and heroic boss progress.
imageCaption: Live Helios guild rankings captured on 23 November 2026. Rankings change as new data is published. TwinStar branding and World of Warcraft artwork belong to their respective owners.
order: 2
---

## What it is for

Players want to compare their guild’s raid progress, find fast boss kills, and see how active other groups are. TwinStar Progress brings those views into one searchable website for Helios, Perses, and Proudmoore.

## What visitors can do

- Browse progress, speedkill, and heroic kill-count rankings by realm and raid.
- Switch between 10-player and 25-player heroic results, and guild or boss views.
- Search for a guild and explore its recorded encounters.
- Use the interface in English, Czech, or Slovak, with light and dark themes.

## My contribution

This is an AI-assisted personal project. As with my other projects, I guide the work through instructions and feedback, manually try the interface, and report visual issues. I am learning how the generated code connects the interface, stored data, and published results.

## How the project works

The interface uses **React and TypeScript**. A separate import process collects raid records into **SQLite**, then exports data for the static website hosted on **Cloudflare Pages**. Scheduled publishing updates the public snapshot without requiring a database request for every visitor.

The project gives me a practical setting for learning about data processing, filtering and presenting records, and keeping a deployed application up to date.

## Current scope

The website is publicly accessible; the source repository is private. Rankings reflect the latest successfully published data, rather than a real-time feed. Coverage depends on the available source records and successful imports. The interface displays when the data was last updated.

[Explore the live website](https://twinstar-progress.pages.dev/)
