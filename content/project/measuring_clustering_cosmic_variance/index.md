---
title: Constraining galaxy physics at Cosmic Dawn with Cosmic Variance 
summary: Numerous models have been proposed to explain the unexpected wealth of galaxies at Cosmic Dawn revealed by JWST. These models are all tuned to reproduce the abundance of galaxies, requiring new measures to figure out which ones are actually right. An obvious candidate for these constraints come from clustering, but to do so with JWST requires innovating methodology. Here I show how clustering can be measured from pure-parallel JWST surveys, and how it gives us a unique handle on why galaxies seem to not be going through a wild and bursty teenage phase.
tags:
- Galaxies
- Observations
date: "2026-02-26T00:00:00Z"
draft: true
featured: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: Galaxies in the EXCELS survey, along with identified overdensities and extreme galaxies
  focal_point: Center

links:

# - icon: github
#   icon_pack: fas
#   name: GitHub
#   url: https://github.com/astrockragh/evs_clustering

- icon: book
  icon_pack: fas
  name: NASA/ADS
  url: https://ui.adsabs.harvard.edu/abs/2025arXiv251214212W/abstract

- icon: quote-left
  icon_pack: fas
  name: Cite
  url: https://ui.adsabs.harvard.edu/abs/2025arXiv251214212W/exportcitation

url_pdf: "https://arxiv.org/pdf/2512.14212"

slides: ""

---

Insert some overview and hyperlinks to the different sections here

# The physics of galaxies in the baby Universe

State-of-the-field, ultra high redshfit galaxy abundances being a tough thing to reproduce theoretically. (below is figure 11 from https://arxiv.org/pdf/2505.11263, cite this)

![A figure showing the observed luminosity function along with pre- and post-JWST models](/project/measuring_clustering_cosmic_variance/NaiduPrePostJWST.png)

What models have been proposed so far to mitigate this. Focus on the most popular ones, meaning the bursty star formation and the feedback free model, which appropriate links and citations (for example https://arxiv.org/pdf/2305.02713, https://arxiv.org/pdf/2303.04827).

![A figure showing the consequences of bursty star formation](/project/measuring_clustering_cosmic_variance/bursty_star_formation_guochao.png)

Now a section on how these are all tuned to reproduce the luminosity or stellar mass functions starting from halo masses (the halo mass function HMF being the only thing we have down theoretically)

# So how can we know which model is right? Clustering!

Section on how we can measure clustering

## The traditional method - Halo Occupation Distribution

See Paquereau+ 2025 for the application in COSMOS-Web. "Given a random galaxy in a location, the 2-point correlation function describes the probability that another galaxy will be found within a given distance." (I want some kind of demonstration figure/video)

However, JWST is almost perfectly constructed to not be able to measure correlation functions well, due to the small field of view. That's because correlation functions require continuous large volumes surveyed. Only one survey really allows us to do so, the COSMOS-Web survey. Include a description of the COSMOS-Web survey (area, depths, combination with cosmos_2020) 

![The footprint of the COSMOS survey](/project/measuring_clustering_cosmic_variance/COSMOS_footprint.png)

## The new method - Cosmic Variance

While JWST is ideally unsuited for 2 point correlation functions and classical clustering analyses, we just need to be a little creative and come up with new ways of measuring clustering. Our new method leverages another consequence of high clustering --- that the number counts of galaxies between different fields vary increasingly with increasing clustering amplitudes. This clustering-induced field-to-field variance is known as **cosmic variance**, and it is something I have worked on extensively (references)

Figure showing two-point correlation functions, Number count histograms and simulated fields for 3 differnt clustering strengths.

Therefore, if we have enough sampled independent fields, we can .... . Luckily, JWST __IS__ ideally suited to this kind of observation through what is called the pure-parallel observing mode. 

![PANORAMIC logo](PANORAMIC_logo.png)
![Overview of the PANORAMIC pointings](PANORAMIC_footprint.png)

#### The Likelihood Function


## The Real Question: Where Are These Galaxies Found?

Every single one of these beautiful, ultra-massive, quiescent galaxies lives in an **overdensity**, regions with significantly more galaxies than average. The overdensities reflect the fact that galaxies **cluster**, i.e., they are not randomly distributed on the sky. However, until now,theoretical predictions have treated these galaxies as if they live in average, unclustered, environments.

That’s like estimating the wealth of the richest person *in the world* by starting from the mean and spread in a random city. You're going to be surprised, because wealth, just like galaxies, clusters quite strongly, with clustered environments producing both extreme wealth and galaxies. You can see that either in the Figure at the top of this post or in the video below, where on of our galaxies of interest is marked in blue

<video controls width="100%">
  <source src="/project/most_massive_environment/zoom_tour.mp4" type="video/mp4">
</video>

#### It is clear that our galaxy is in the middle of a very dense part of the Universe!

---

## The Insight That Changes Everything

This paper introduces an extended version of EVS that includes a galaxy’s **environment** — specifically, the overdensity it lives in — when estimating the expected maximum stellar mass. Instead of marginalizing over environments (which dilutes everything), we condition on the known fact that the galaxy is in an extreme region. How?

1. **Estimate the volume** of the overdensity using 3D redshift-space distributions.
2. **Compute how overdense** such a volume could reasonably be expected to in the full survey — i.e., the distribution of **density percentile** `u_δ` given that we can fit N subvolumes of the same size as the overdensity into our survey.
3. **Construct stellar mass functions (SMF)** that depends on `u_δ`. More overdense = more galaxies, especially at high masses.
4. Convolve the normal EVS estimates for each **overdensity-dependent SMF** with the distribution of possible overdensities given a certain volume to compute the distribution of the most massive galaxy **given that it exists in the most extreme overdensity in that survey** with a given volume.

You can see how our `P(Maximum mass)` estimates change as a function on the number of total overdensities of a given volume we sample below

<video controls width="100%">
  <source src="/project/most_massive_environment/0_phimax.mp4" type="video/mp4">
</video>

In a way this is the compliment to [another one of my papers on massive galaxies in a clustered Universe](https://astrockragh.github.io/project/most_massive_jwst/), where we instead of **conditioning** on environment like here, marginalize out our lack of knowledge of the environment. For many galaxies, especially at ultra-high redshift, *we do not know their environments*, so there, the above conditioning steps would be inappropriate!

---

## The Result: They're Not So Impossible After All

When we apply this method to the three most extreme galaxies in the [EXCELS survey](https://ui.adsabs.harvard.edu/abs/2024MNRAS.534..325C/abstract) — including the infamous ZF-UDS-7329 galaxy — the tension with theoretical models *drops dramatically*.

* Under the standard EVS (ignoring environment and using normal star formation efficiencies), some galaxies were at a model tension of almost **6σ**, and combining all three, we get a total of **9σ**!! Alarming!
* When we **condition on overdensity**, this drops to **\~3σ** for the most extreme galaxy. So the galaxy is still extreme, but within acceptable limits. Remember that we could invoke higher star formation efficiency, but it is not that necessary now.
* You don’t need 100% star formation efficiency anymore. The pre-JWST \~10-20% values works just fine!

This is all summarized in the below Figure, where you can see the mass histories of the galaxies in dotted blue. The alleviated tension is immediately obvious!

![Main Figure from the paper](combined_updated_SBF_Finkelstein_fiducial_legend_reverse_order_referee_v2.png)

---

## So… Was This Really a Crisis? Or a Misunderstanding?

Let’s be blunt. Much of the tension arose not because the models were fundamentally wrong, but because we were comparing the rarest galaxies in the universe to average expectations. By conditioning on where these galaxies actually live — **the most overdense regions of the sky** — we reconcile theory and observation without invoking extreme physics.

It’s a small shift in logic, but a sizable step in understanding.

In a way, [this reflects the thoughts of the original discover of the extreme ZF-UDS-7329, Karl Glazebrook](https://ui.adsabs.harvard.edu/abs/2024Natur.628..277G/abstract), who suggested that we may be missing something about halo physics that makes dark matter collapse faster early on --- a seemingly radical idea. However, this is actually exactly what happens in extreme overdensities, halos collapse earlier and grow faster than in average areas, so in a way, Prof. Glazebrook was right!

---

## 🛠 Want to Try This Yourself?

We've released the full code for environment-conditioned EVS on [GitHub](https://github.com/astrockragh/evs_clustering), including a demo notebook!

---

## 🚀 Why This Matters for Galaxy Evolution

* We now have a **physically-motivated way** to model massive galaxy formation without stretching SFE or tweaking dark matter in new ways.
* We **connect large-scale structure and galaxy masses** in a statistical framework. Clustering is **always** important. One of the important next steps is measuring the amplitude of clustering at these redshifts, but this is something that I am currently working on!

This is not the end of the mystery — but it’s the **beginning of the asking right question**.
