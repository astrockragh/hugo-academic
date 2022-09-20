---
title: Learning Baryonic Physics from Complete Merger Histories @DAWN Copenhagen

event: DAWN Cake Talk

location: Niels Bohr Institute

summary: I will introduce a new Machine Learning based model for mapping between dark matter and galaxies, called Mangrove. I'll show improvements in both precision and speed compared to other similar methods, and discuss how Mangrove opens up new avenues for efficiently learning from simulations.

abstract: "Efficiently mapping between baryonic properties and dark matter is a major challenge in astrophysics. 
Although semi-analytic models (SAMs) and hydrodynamical simulations have made impressive advances in reproducing galaxy observables across cosmologically significant volumes, both still require significant computation times, and are hard to succinctly analyze, representing a barrier to many applications. Graph Neural Networks (GNNs) have recently proven to be the natural choice for learning physical relations. Among the most inherently graph-like structures found in astrophysics are the dark matter merger trees that encode the evolution of dark matter halos. In this cake talk I will introduce a new, graph-based emulator framework, Mangrove, and show that it emulates the galactic stellar mass, cold gas mass and metallicity, instantaneous and time-averaged star formation rate, and black hole mass with scatters two times lower than other methods across a simulation box of side length 75 Mpc/h in 40 seconds, 4 orders of magnitude faster than a SAM and 9 orders of magnitude faster than a hydro simulation. I’ll also show how Mangrove allows for quantification of the dependence of galaxy properties on merger history, making it possible to learn about the simulations on a new level. I will also compare Mangrove results to the current state of the art in emulating the dark matter - galaxy connection and show significant improvements for all target properties. 
Mangrove is publicly available at https://github.com/astrockragh/Mangrove.
"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2022-08-18"
# date_end: "2030-06-01T15:00:00Z"#
all_day: false
draft: false
# Schedule page publish date (NOT talk date).
publishDate: "2022-03-29T00:00:00Z"

authors: []
tags: [invited]

# Is this a featured talk? (true/false)
featured: true

image:
  caption: 'Logo for our model, Mangrove'
  focal_point: Right

url_code: "https://github.com/astrockragh/Mangrove"
url_pdf: ""
url_slides: ""
url_video: ""

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects:
- Mangrove
---
<!-- 
{{% callout note %}}
Click on the **Slides** button above to view the built-in slides feature.
{{% /callout %}}

Slides can be added in a few ways:

- **Create** slides using Wowchemy's [*Slides*](https://wowchemy.com/docs/managing-content/#create-slides) feature and link using `slides` parameter in the front matter of the talk file
- **Upload** an existing slide deck to `static/` and link using `url_slides` parameter in the front matter of the talk file
- **Embed** your slides (e.g. Google Slides) or presentation video on this page using [shortcodes](https://wowchemy.com/docs/writing-markdown-latex/).

Further event details, including [page elements](https://wowchemy.com/docs/writing-markdown-latex/) such as image galleries, can be added to the body of this page. -->
