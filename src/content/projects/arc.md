---
title: ARC — Advanced Raid Check
subtitle: A clearer picture before the pull.
summary: A World of Warcraft addon that helps raid leaders see who is ready and what is missing before a group encounter.
tags: [Lua, WoW API, Event-driven tools]
status: Release available
repository: https://github.com/Interacti0n/ARC-Advanced-Raid-Check
release: https://github.com/Interacti0n/ARC-Advanced-Raid-Check/releases/latest
image: images/arc-demo.png
imageWidth: 854
imageHeight: 446
imageAlt: ARC demo roster showing player readiness, consumables, equipment, and a summary of confirmed issues.
imageCaption: ARC demo interface with temporary sample roster data. Screenshot provided by the project author.
order: 3
---

## The problem

Raid readiness involves more than a single ready-check response. Equipment, specializations, consumables, buffs, and player-reported data all contribute to understanding whether a group is prepared.

## The resulting tool

ARC combines those signals in a roster view with readiness verdicts. It also provides targeted player checks and raid-session reports covering attendance, encounters, activity, and loot. Its interface supports English, Slovak, and Czech.

## My contribution

Most implementation is AI-generated. I guide development through task instructions and feedback, manually try the addon, and report visual issues. I am learning to understand the generated code and the reasons behind its behavior.

## How the project is structured

### Modules with distinct responsibilities

Core state, gear rules, inspection, interface, localization, and sessions live in separate Lua modules. Runtime dependencies are optional; ElvUI styling is detected when available.

### Treat missing data carefully

Inspection cannot provide every remote value. ARC supplements it with peer reports, validates sender identity, limits report freshness, and distinguishes unavailable information from a failed check. Some compatibility-sensitive checks are skipped with explanatory tooltips when data cannot be verified.

### Preserve compatibility

Stable saved-variable and communication identifiers preserve existing settings and peer compatibility. Incremental, idempotent schema migrations update persisted data without discarding unknown fields or session history.

## Scope and limitations

ARC targets the legacy MoP 5.4.8 client. Remote private data requires a compatible peer report. Client-specific behavior and unavailable inspection data remain important limits; the repository documents the in-game release verification process.

[Read the user guide](https://github.com/Interacti0n/ARC-Advanced-Raid-Check/blob/main/docs/USER_GUIDE.md) · [Explore the architecture](https://github.com/Interacti0n/ARC-Advanced-Raid-Check/blob/main/docs/ARCHITECTURE.md)

