---
title: The optical and infrared are connected
summary: Galaxies are often modelled as disjoint composites of distinct spectral components, implying that different wavelength ranges are only weakly correlated. **They are not**. We construct a data-driven model to predict infrared emission from optical spectra, achieving almost lossless predictions. Traditional fitting methods are incapable of making predictions, being biased by model misspecifications.
tags:
- Machine Learning
- Galaxies
- Observations
date: "2025-06-06T00:00:00Z"
draft: false
featured: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: The Milky Way seen across different wavelengths
  focal_point: Center

links:

- icon: github
  icon_pack: fas
  name: GitHub
  url: https://github.com/astrockragh/evs_clustering

- icon: book
  icon_pack: fas
  name: NASA/ADS
  url: https://ui.adsabs.harvard.edu/abs/2025arXiv250303816J/abstract

- icon: quote-left
  icon_pack: fas
  name: Cite
  url: https://ui.adsabs.harvard.edu/abs/2025arXiv250303816J/exportcitation

url_pdf: "https://arxiv.org/pdf/2503.03816"

slides: ""

---

# Explaining the masses of ultra-massive "universe-breaking" galaxies

What do you do when observations break your theory?

That’s the situation galaxy physics has faced since the JWST started discovering both extremely distant galaxies, along with **ultra-massive, quiescent galaxies** at redshifts 3–5 — galaxies more massive than our Milky Way, already completely quenched just 1 billion years after the Big Bang. We have struggled to explain how these galaxies could form stars so rapidly and shut off star formation this early. Theories have invoked extreme star formation efficiencies (close to 100%!), very exotic feedback mechanisms, or even modifications to our well-tested ΛCDM-cosmology. This has all come from statistical analyses of an idealized distribution of galaxies by total mass, the stellar mass function (SMF), using a technique called **Extreme Value Statistics (EVS)**, which is designed to ask the question:

---
If I 
---

#### But what if we’ve just been asking the wrong question?

## 🌌 The Real Question: Where Are These Galaxies Found?

Every single one of these ultra-massive, quiescent galaxies — including those in the **JWST EXCELS sample** — lives in a **cosmic overdensity**, regions with significantly more galaxies than average. And yet, most theoretical predictions have treated these galaxies as if they live in average environments.

That’s like estimating the height of the tallest person *in the world* by looking at a single average village. You're going to be surprised.

📷 **\[INSERT 3D plot of spectroscopic galaxies showing overdensities – e.g., Figure 1 from paper]**

---

## 🔥 The EVS Trick That Changes Everything

This paper introduces an extended version of EVS that includes a galaxy’s **environment** — specifically, the overdensity it lives in — when estimating the expected maximum stellar mass. Instead of marginalizing over environments (which dilutes everything), we condition on the known fact that the galaxy is in an extreme region.

How?

1. **Estimate the volume** of the overdensity using 3D redshift-space distributions.
2. **Compute how rare** such an overdensity is in the full survey — i.e., the **density percentile** `u_δ`.
3. **Construct a stellar mass function (SMF)** that depends on `u_δ`. More overdense = more high-mass galaxies.
4. Use EVS on this **overdensity-dependent SMF** to compute the distribution of the **most massive galaxy**.

📷 **\[INSERT Figure 2 from paper – ideal demo of how SMF(u\_δ) leads to P(M\_max|N\_δ)]**

---

## 🎯 The Result: They're Not So Impossible After All

When we apply this method to three galaxies in the UDS field — including the infamous PRIMER-EXCELS-109760 and ZF-UDS-7329 — the tension with theoretical models *drops dramatically*.

* Under the standard EVS (ignoring environment), some galaxies were **5–6σ** above expectation. Alarming!
* When we **condition on overdensity**, this drops to **\~2σ** or even **zero**.
* You don’t need 100% star formation efficiency anymore. The pre-JWST \~10% value works fine.

📷 **\[INSERT side-by-side comparison of mass-redshift contours, e.g., Figure 3]**

---

## 💥 So… Was This a Crisis? Or a Misunderstanding?

Let’s be blunt. Much of the tension arose not because the models were fundamentally wrong, but because we were comparing the rarest galaxies in the universe to average expectations.

By conditioning on where these galaxies actually live — **the most overdense regions of the sky** — we reconcile theory and observation without invoking extreme physics.

It’s a small shift in logic. But a huge step in understanding.

---

## 🛠 Want to Try This Yourself?

We've released the full code for environment-conditioned EVS on [GitHub](https://github.com/astrockragh/evs_clustering), including a \[demo notebook]\(link to demo). It’s simple, transparent, and powerful — just like the best statistics.

📷 **\[INSERT gif from the demo notebook showing SMF evolution with clustering strength]**

---

## 🚀 Why This Matters for Galaxy Evolution

* We now have a **physically-motivated way** to model massive galaxy formation without stretching SFE or tweaking dark matter.
* We **connect large-scale structure and galaxy properties** in a statistical framework.
* Future clustering-calibrated SMFs (from JWST or Euclid) can **predict the expected outliers**, not just describe the mean.

This is not the end of the mystery — but it’s the **beginning of the right question**.

---

*Want to know how rare your favorite massive galaxy really is? Plug it into the code and find out.*

---

Let me know if you'd like help turning this into HTML, Jekyll, or LaTeX for your academic site.

