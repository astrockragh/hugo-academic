---
title: Galaxy Physics at Cosmic Dawn from Clustering
summary: Numerous models have been proposed to explain the unexpected wealth of galaxies at Cosmic Dawn revealed by JWST. These models are all tuned to reproduce the abundance of galaxies, requiring new measures to figure out which ones are actually right. An obvious candidate for these constraints come from clustering, but to do so with JWST requires innovating methodology. Here I show how clustering can be measured from pure-parallel JWST surveys, and how it gives us a unique handle on why galaxies seem to not be going through a wild and bursty teenage phase.
tags:
- Galaxies
- Observations
date: "2026-02-26T00:00:00Z"
draft: false
featured: true

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: A randomly picked PANORAMIC pointing
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
<!-- https://www.youtube.com/watch?v=Ewn_zA0xm5Y -->

Now a section on how these are all tuned to reproduce the luminosity or stellar mass functions starting from halo masses (the halo mass function HMF being the only thing we have down theoretically)

#### Some quick terminology definitions

When we talk about bursty star formation, the terms highly variable star formation, or stochastic star formation are often used interchangably. Because we are not consistent with these choices in the litterature, I will likewise use them interchangably. However, I do want to note that things can be bursty or highly variable without being stochastic. Stochastic is how we usually make the models we have right now, but there are many ways of making something variable without making it stochastic.

# So how can we know which model is right? Clustering!

Section on how we can measure clustering and why clustering is so constraining for galaxy physics.

## The traditional method - Halo Occupation Distribution

See Paquereau+ 2025 for the application in COSMOS-Web. "Given a random galaxy in a location, the 2-point correlation function describes the probability that another galaxy will be found within a given distance." (I want some kind of demonstration figure/video)

<!-- <iframe width="700" height="440" frameborder="0" loading="lazy" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; web-share" allowfullscreen src="https://commons.wikimedia.org/wiki/File:Two-point-correlation-function-astronomy.webm?embedplayer=true" /> -->
<video width="640" height="480" controls>
  <source src="Two-point-correlation-function-astronomy_trimmed.mp4" type="video/mp4">
</video>

However, JWST is almost perfectly constructed to not be able to measure correlation functions well, due to the small field of view. That's because correlation functions require continuous large volumes surveyed. Only one survey really allows us to do so, the COSMOS-Web survey. Include a description of the COSMOS-Web survey (area, depths, combination with cosmos_2020) 

![The footprint of the COSMOS survey](/project/measuring_clustering_cosmic_variance/COSMOS_footprint.png)

## The new method - Cosmic Variance

While JWST is ideally unsuited for 2 point correlation functions and classical clustering analyses, we just need to be a little creative and come up with new ways of measuring clustering. Our new method leverages another consequence of high clustering --- that the number counts of galaxies between different fields vary increasingly with increasing clustering amplitudes. This clustering-induced field-to-field variance is known as **cosmic variance**, and it is something [I have worked on extensively](https://astrockragh.github.io/project). In short, it makes the amount of galaxies in a given field more dispersed, so that some fields are basically empty, whereas others host enormous amounts of galaxies. You can see a demonstration of how increasing clustering variance gives a higher two-point function amplitude and more dispersed number counts in simulated fields in the Figure below.

<!-- --- Figure showing two-point correlation functions, Number count histograms and simulated fields for 3 different clustering strengths. -->
![A demonstration figure showing how clustering can be measured in many different ways](/project/measuring_clustering_cosmic_variance/galaxy_simulation_v3_4.png)


Therefore, if we have enough sampled fields, we can directly **measure** the clustering amplitude. One thing that is worth noting is that the above Figure is just for demonstration, if you want to actually make , your fields need to be so spatially separated that they are **independent**. Luckily, JWST __IS__ ideally suited to this kind of observation through what is called the pure-parallel observing mode. Essentially, the telescope can operate more than two different instruments at the same time, and parallel mode simply means that we ask for our best camera for high-redshift science, NIRCAM, to be opened while another primary instrument is in use. The [PANORAMIC survey](https://panoramic-jwst.github.io/), is exactly this kind of survey! Below you can see the nice PANORAMIC logo and how the different pointings are spatially distributed across the sky.

![PANORAMIC logo](/project/measuring_clustering_cosmic_variance/PANORAMIC_logo.png)
![Overview of the PANORAMIC pointings](/project/measuring_clustering_cosmic_variance/PANORAMIC_footprint.png)

Because of the survey strategy, we now have __independent__ fields spread all over the sky, perfect for doing the kind of science we want to do! You can also see a randomly sampled PANORAMIC pointing at the top of the article!

#### Technical Notes - The model, the likelihood function, and what we are actually fitting

This section will touch on the formal and mathematical aspects of how to fit for the cosmic variance from a set of fields. Feel free to skip if you are looking for the scientific interpretation of our results! To get to the results we need

- a set of k fields with a set of associated galaxy number counts $\{N_0, N_1, ..., N_k\}$. These should be completeness-corrected before you start doing anything!
- a distribution characterized by a mean and variance ($\mu, \sigma^2$). The distribution has to fulfill a few conditions
  1. It has to approximate the Poisson distribution in the limit of $\sigma^2 \rightarrow \mu$, the appropriate distribution when no clustering is present.
  2. It has to allow for $\sigma$ to be set independently in $\mu$, allowing $\sigma$ to encode the clustering strength at a fixed mean number density.
  3. It has to be strictly positive

  A few different distributions fulfill these conditions, but the two best are the Gamma distribution and the Negative Binomial. Using either of these is fine, and it does not impact the results we get. I typically use the Gamma, but it does not matter.

- A likelihood function to 

- A way of fitting. Since $\mu$ and $\sigma$ are non-linearly related, the ideal way is to use an MCMC chain. This can be implemented using the amazing ```emcee``` package. One can prove that for a Maximum Likelihood Estimator, cosmic variance is always biased high  (see Jespersen et al., 2025a find the link to cite my paper), and although I have not proven that it is not when using MCMC, I suspect that it will fix the issue.

#### Relationship to other concepts - are we just reinventing old ideas?

For example, Coles and Jones 1991 (https://articles.adsabs.harvard.edu/pdf/1991MNRAS.248....1C), for generating log-normal fields, and saying that one can derive galaxy biases from these fields. (This paper also contains a great ssection on how to simulate realistic galaxy fields given some clustering amplitude/structure!)

This also should include the book by Peebles 1980 and the Adelberger et al. 1998 paper on the Counts-in-Cells statistics of clustered galaxy fields.

Newman and Scott 1952 https://articles.adsabs.harvard.edu/pdf/1952ApJ...116..144N where it is established that the counts-in-cells of galaxies has a super-Poissonian variance due to clustering from gravity.

Void probability functions are another spin on exactly this same thing, but of course the inverse.

One-point statistics for constraining cosmology by Cora Uhlemann's recent work (e.g., [this nice paper from 2020](https://ui.adsabs.harvard.edu/abs/2020MNRAS.495.4006U/abstract)). One-point/counts-in-cells functions are apparently really good at constraining the neutrino mass!

And [this wonderful paper by Brant Robertson](https://ui.adsabs.harvard.edu/abs/2010ApJ...716L.229R/abstract) which quite literally suggests the exact same thing that we ended coming up. It is an amazing paper, and made a lot of the points that we ended up fumbling our way to. E.g., you need to compare to simulations, for these small fields analytic theory does not work very well, you're biased low if you do the same thing by chopping up continuous fields, many great things! Overall I just love this paper, and the method has been severely underrated and underutilized. 

Other papers worth mentioning are López-Sanjuan et al. 2015 (https://www.aanda.org/articles/aa/pdf/2015/10/aa26731-15.pdf) and Cameron et al. 2019 (https://academic.oup.com/mnras/article/483/2/1922/5173113), which also measure galaxy clustering amplitudes using the cosmic variance/counts-in-cells method in the ALHAMBRA and BoRG surveys, respectively. 

So what is the novelty for us? Well, we push the highest-z applications from z~2 to z~10, giving the first ever z ≥ 10 measurement of the galaxy clustering amplitude, and it is the first time that this method has been used with JWST. Furthermore, we find some really interesting tensions that I'll show now!

# So now, what do we then actually measure in the real Universe?

So now we have two independent methods for measuring clustering, which can be applied to two independent datasets. That means that we should be able to combine any conclusions drawn from these analyses. Let's take a look at what we get!

## Traditional clustering method

Below, I show the results that we derived [using a traditional HOD approach in the COSMOS-Web survey](https://ui.adsabs.harvard.edu/abs/2025A%26A...702A.163P/abstract). There is a lot of information on this plot, so let us take a look at the most important parts.

1. Our measurements are shown in as filled circles with errorbars connected by solid lines. Each colour shows a different mass bin.
2. The relevant model comparison is to look at the dashed (bursty star formation model) and dash-dotted (no burstiness) lines. These are also calculated per mass bin, so compare only data and model lines with the same colour.
3. Focus specifically on the dark green measurements at z~9, it is easy to see the tension between our measurement and the bursty model, as well as the near-perfect agreement between the measurements and the model with no burstiness.

[Figure showing the measured clustering amplitude in COSMOS-Web](/project/measuring_clustering_cosmic_variance/COSMOS_clustering_results.png)

The cyan measurements are also interesting, but here, the model comparson is less obvious, and the measurements more doubtful, although the clustering is still consistently high.

In total, at z~9, we get a tension between the data and the bursty model of $\approx 3 \sigma$. This is substantial and exciting, but it did not fully convince me at first. I did not feel certain that it was not some weird model systematic that was driving these results, although the signal that we got was pretty clear. That motivated my second direction for constraining clustering. 

## Cosmic Variance method

<!-- The cosmic variance method is a much more model-free way of measuring clus -->
As decribed [above](#the-new-method---cosmic-variance), we must always jointly fit for both the mean and variance when we fit for the cosmic variance. That means that we always get two-dimensional contours in number density - clustering amplitude space. This is what you can see in the figure below, along with the pre-JWST expectation clearly marked in red. The question is then how we can move to the higher-than-expected abundance of galaxies without lowering the clustering amplitude. That's because a higher galaxy abundance usually comes associated with lower-mass systems, which are less strongly clustered.

![Model measurement with pre-JWST UniverseMachine theory](/project/measuring_clustering_cosmic_variance/annotated_measurement.png)

So let's take a look at some of these potential models. I want to specifically highlight 
1. the bursty star formation model that you have already heard a lot about, and 
2. a model that one of favourite collaborators, [Rachel Somerville](https://www.simonsfoundation.org/people/rachel-somerville/), introduced, which scales the star formation efficiency with halo mass (**D**ensity **M**odulated **S**tar **F**ormation **E**fficiency, DMSFE), so that higher mass systems preferentially form the galaxies we see.

Below, you see how these models can move us across the number density - clustering contours, and while there is no insane difference between them, the bursty model systematically underpredicts the clustering amplitude relative to the Somerville/DMSFE model. 

![Bursty model on contours](/project/measuring_clustering_cosmic_variance/cosmic_variance_sig_UV_withmodel.png)
![DMSFE model on contours](/project/measuring_clustering_cosmic_variance/cosmic_variance_SFE_somerville_medium_withmodel.png)

Because the differences are systematic, we can aggregate the results across the three bins we have to actually get a consistent and somewhat strong result. This is what is shown in the below figure, where we also tested out many other models, as well as variations on the above models (each model class has a letter, variations are numbered).

![Cosmic variance model constraints](/project/measuring_clustering_cosmic_variance/model_constraints_v1.png)

So in total, between the bursty and DMSFE models, we find that burstiness is disfavoured at the $\approx 2 \sigma$ level. Again, on its own it is not very impressive. In physics we do not take $2 \sigma$ this to be definitive, but merely suggestive of tension. This reflects the fact that we are making a very model-independent statement (any time we are not using a very specific model, it tends to lower the significance of finding), and that we simply do not (for the time being) have that much data in this novel and exciting early Universe regime.

#### Why are you measuring a galaxy bias of 100??

One thing that surprised me a bit once we mapped our measured cosmic variance values to a galaxy bias (i.e., how much more clustered galaxies are than dark matter, $b_g = \sigma_{CV}/\sigma_{DM}$), we find very high values on the order of 100. This worried us quite a lot, since bias values closer to 1 are much more normal. However, two things are in effect:
1. At high redshift, galaxies are inherently more biased, with bias values on the order of 10 being expected. So this gets us half the way.
2. Our fields are quite small, meaning that we are not measuring the typical _linear_ bias, but instead a _non-linear_ bias, which boosts the bias. We tested if this really was the case in the ```UniverseMachine``` simulation, and as you can see in the figure below, we would have gotten the same bias as the usual clustering studies if each our fields was (roughly) a square degree in size. However, our fields are only around 1/500th of that size, which is why the values are so weird.

![Mapping from CV to HOD/linear bias](/project/measuring_clustering_cosmic_variance/CV_to_HOD_bias_field_size.png)

## Putting both tests together

Because we now have two tests, based on two different sets of assumptions, applied to two different datesets, we can easily combine them to get the joint significance! For this, we can either just combine the Gaussian tensions directly, or we can use something called [Fisher's Method](https://en.wikipedia.org/wiki/Fisher%27s_method), which implicitly accounts lightly for the [look-elsewhere effect](https://en.wikipedia.org/wiki/Look-elsewhere_effect). That is what the plot below shows for the DMSFE and bursty models. 

![Total model constraints](/project/measuring_clustering_cosmic_variance/model_constraints_cosmos_and_panoramic_fisher_with_annotation.png)


Here we see that the total preference for a non-bursty model is between 3.5-3.8 $\sigma$, depending on our way of aggregating the probabilities. That means that we are already getting close to the 4 $\sigma$ threshold that [in medicine](https://nursing.ucalgary.ca/research/nursing-research-office/data-analysis/quantitative) would be called ```"Extremely strong evidence against the null hypothesis"```. This is maybe a little stronger than I am willing to put it, but the point stands: 4 $\sigma$ is significant.

# What does this mean for galaxy physics?

So in the end, the otherwise very popular bursty model seems fairly ruled out. Galaxies in the early Universe cannot be very bursty, i.e., galaxies do not go through a "wild teenage phase". Instead, **galaxy growth must tightly follow the growth of their host dark matter halos**. We also find that the efficiency of star formation must scale with the mass of the host halo.

# What now?

There are some obvious next steps for this kind of analysis. The first line is of course to get more high-z data (preferably pure parallel), validate and use our methods in both the high and low redshift regimes, and to redo the analysis of separate galaxy classes.

The second is to reconcile our clustering measurements (which disfavour high stochasticity) with the fact that early galaxy spectra _look_ quite bursty. Let's tackle the two in turn.

### Improving our methodology and measurements

JWST will continue on being an incredible discovery machine, and PANORAMIC is not the only pure parallel survey out there. We should all combine our forces and pool our data to get incredible 

Another thing is that we need to extend and validate the framework at lower redshift, so that we can also connect clustering at all redshifts, measured from both of these independent methods. This is also a great way of validating all of these different things. We should remember that these tools are either in their infancy (cosmic variance) or have never been deeply tested (not even in simulations) at these redshifts.

### Reconciling different kinds of measurements

Aspen conference, we are two sections of the community studying burstiness/stochasticity, and we are in complete disagreement and kinda disjoint. One section believes in measuring the UV/star formation stochasticity from ratios between H-$\alpha$ and UV luminosities, and are completely convinced that burstiness is a major factor, whereas the ones of doing clustering are completely convinced that it cannot be bursty. I really want to explore this more in future work, to see if there is a way of fitting both things into the same framework (something about halo formation scatter and that I don't have a full understanding of what goes into the UV/H-$\alpha$ results). Shoutout to Daniel Stark who really pressed me on this and inspired me to aim a little higher.

There has already been some early work here. For example Julian's (Muñoz) paper (should clarify that I love the paper, and that I think that this is definitely the way forward). Here, it seems to claim that clustering doesn't matter, and cannot be measured if it is just halo mass dependent, but we disagree quite strongly, and we have a lot of nice updated clustering measurement compared to what is used in that work. I'll be visiting UT Austin in the fall, and I am so looking forward to figuring this out along with Julian.

## Public Code?

I am very sorry to say ***not yet***, but once the paper is officially accepted, I plan to release the full analysis code on [my GitHub](https://github.com/astrockragh/), including a demo notebook with simulated data! I unfortunately cannot share collaboration-reduced data myself, but I will make the methodology as accessible as possible. On that note, please reach out to me if you have any questions, or if you would like help setting up a similar clustering measurement.

---
