---
title: Learning Baryonic Physics from Complete Merger Histories

event: "Graduate Student talk series"

location: Brown University, Providence RI

summary: For the first time ever, we show that it is possible to use full merger histories to emulate SAMs with Machine Learning.

abstract: "Efficiently mapping baryonic physics onto dark matter represents one of the major challenges of the current cosmological paradigm. Even as Semi-Analytical Models (SAMs) and hydrodynamical simulations have made impressive advances in reproducing key observables across cosmologically significant volumes, there is significant tension between the predictions of these two methods, and the increases in simulation volume has meant that simulation times are now of order $10^8$ CPU hours. However, with recent advances in Machine Learning (ML), key quantities of these simulations can now be reproduced in seconds. Graph Neural Networks (GNNs) have proven to be the natural choice for learning physical relations, and among the most inherently graph-like structures found in astrophysics are the merger trees that encode the evolution of dark matter haloes, which are used by SAMs to simulate baryonic physics. I’ll discuss how SAMs can be emulated precisely and quickly with a GNN for several different baryonic quantities of interest, and how this method offers key advantages over other ML methods in analyzing the interdependence between assembly history and the baryonic properties of galaxies. 

"

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2022-04-05"
# date_end: "2030-06-01T15:00:00Z"#
all_day: false
draft: false
# Schedule page publish date (NOT talk date).
publishDate: "2022-03-29T00:00:00Z"

authors: []
tags: []

# Is this a featured talk? (true/false)
featured: true

image:
  caption: 'True-Predicted plot when using our model (left), and the traditional Abundance Matching approach (right), for regressing stellar mass'
  focal_point: Right

url_code: "https://github.com/astrockragh/GraphMerge"
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
- GraphMerge
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
