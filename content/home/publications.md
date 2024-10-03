---
# An instance of the Pages widget.
# Documentation: https://wowchemy.com/docs/page-builder/

#how to update https://wowchemy.com/docs/content/publications/, i.e pip3 install -U academic, academic import --bibtex static/publications.bib, and then correct weird characters, otherwise it won't load
widget: pages

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 50

title: Publications
subtitle: ''

content:
  # Filter on criteria
  filters:
    folders:
      - publication
    tag: ''
    category: ''
    publication_type: ''
    author: ''
    exclude_featured: false
    exclude_future: false
    exclude_past: false
  # Choose how many pages you would like to display (0 = all pages)
  count: 3
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc
design:
  # Choose a view for the listings:
  view: citation
  columns: '2'
---

I would never keep everything here up to date, so for an up-to-date list, instead look at the amazing [NASA/ADS](https://ui.adsabs.harvard.edu/search/fq=%7B!type%3Daqp%20v%3D%24fq_database%7D&fq_database=(database%3Aastronomy%20OR%20database%3Aphysics)&q=((author%3A%22Jespersen%2C%20Christian%20K.%22%20or%20author%3A%22Kragh%20Jespersen%2C%20Christian%22)%20AND%20year%3A2020-)&sort=date%20desc%2C%20bibcode%20desc&p_=0) service. Sometimes, web services track my name as "Kragh Jespersen, Christian", sometimes as "Jespersen, Christian Kragh" (the correct form), and sometimes as "Jespersen, Christian K.", so I recommend using the above link to get correct results.