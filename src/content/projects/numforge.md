---
title: NumForge
subtitle: Precise calculations, from a C core to interactive tools.
summary: A mathematics project built around a C17 core, with tools for precise calculations, graphs, equations, and matrices.
tags: [C17, CMake, Mathematics]
status: In development
repository: https://github.com/Interacti0n/NumForge
release: https://github.com/Interacti0n/NumForge/releases/latest
image: images/numforge-calculator-2026-10.webp
imageWidth: 1440
imageHeight: 900
imageAlt: NumForge calculator evaluating 1/3 + 1/6 as the exact fraction 1/2, with function library and calculation history.
imageCaption: Calculator showing an exact fraction result. Development screenshot from the project documentation, captured 27 October 2026.
order: 1
featured: true
---

## What it does

NumForge is my main personal software project: a mathematics platform with a standalone C library, an expression engine, and command-line and browser tools. It explores exact arithmetic and calculations beyond fixed-width numeric types.

For example, `1/3 + 1/6` produces the exact reduced fraction `1/2`. Calculations such as `sqrt(2)` use configurable precision. Exact results and approximations are distinguished within the project's resource limits.

## My contribution

Most implementation is AI-generated. I guide the work through task instructions and feedback, manually try the application, and report visual issues. I study the generated code and explanations to understand how and why it works.

## What you can explore

- A scientific calculator with exact fractions, variables, and confirmed history.
- Function graphs, equation solving, and a matrix editor.
- Unit conversions and dimensional quantities.
- A C library and expression engine, plus an experimental Python adapter built from source.

## How the project is structured

The interfaces reuse a C17 mathematical core. JavaScript handles browser presentation and requests. The numeric library and optional expression engine can be consumed independently of the applications.

The repository documents automated testing and integration checks alongside the source.

## Current scope

The project is in development. Features in current source can differ from published release packages; consult the release notes and SDK guide before choosing a download. The Python adapter is experimental, and approximate calculations have documented accuracy limits.

[Explore the project and examples](https://github.com/Interacti0n/NumForge#readme) · [Testing documentation](https://github.com/Interacti0n/NumForge/blob/main/docs/TESTING.md) · [SDK guide](https://github.com/Interacti0n/NumForge/blob/main/docs/guides/SDK.md)
