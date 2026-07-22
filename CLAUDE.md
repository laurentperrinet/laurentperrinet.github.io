# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Site Overview

- **Description**: The website of Laurent Perrinet, an academic in computational neuroscience.
- **Content**: It details all his production, including publications, talks, slides, and more. 
- **Note**: I like to link related content together (e.g., linking a talk to its corresponding paper).

## Build & Development Commands

- **Local Development**: `make test` (runs `hugo server --disableFastRender`) or `npm run dev`
- **Clean Hugo Modules**: `make clean`
- **Update Theme/Dependencies**: `make update` (runs `sh update_hugoblox.sh`)
- **Deploy to GitHub Pages**: `make gitpages` (commits and pushes changes to `main`, optionally with a custom message via `MESSAGE="your message"`)

## Architecture & Content Structure

This is a [Hugo](https://gohugo.io/) site using the [Hugo Blox Builder](https://hugoblox.com/) (formerly Academic CV template). The site is organized by content types located in the `content/` directory:

- **Authors**: `content/authors/` contains profile pages for researchers and collaborators.
- **Publications**: `content/publication/` holds research papers and their metadata.
- **Talks**: `content/talk/` stores information about presentations and talks.
- **Projects**: `content/project/` hosts project showcases.
- **Posts/Events**: `content/post/` (or other taxonomies like `events`) contains blog posts or site updates.

The configuration is primarily managed via:
- `config/_default/hugo.yaml`: General Hugo configuration.
- `config/_default/params.yaml`: Site-specific parameters (appearance, SEO, features).

## Deployment

The site is deployed to GitHub Pages. The deployment process can be triggered manually via the `make gitpages` command or automatically through GitHub Actions workflows defined in `.github/workflows/`.
