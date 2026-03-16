---
title: "Post-doc Market II: Modelling the Stochasticity in the Market"
subtitle:

# Summary for listings and search engines
summary: The postdoctoral job market is one of the major challenges to any finishing graduate student wishing to continue in academia. Here I want to provide some lessons learned and personal reflections for both other and my future self.

# Link this post with a project
projects: []

# Date published
date: "2026-03-14T00:00:00Z"

# Date updated
lastmod: "2026-03-14T00:00:00Z"

# Is this an unpublished draft?
draft: true

# Show this page in the Featured widget?
featured: false

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
image:
  caption: ''
  focal_point: ""
  placement: 2
  preview_only: false

---

This is a blog post about the job market, second of two. It has been inspired by my frustration in not knowing how many applications would be reasonable to send. Of course one wants to send enough applications to elevate ones chances of getting a position, but sending applications is a huge time investment, so the trade-off has to be considered carefully. I for one ended up spending essentially half a year of full time effort on my applications, [as you can read about in another post](https://astrockragh.github.io/post/postdoc_experience1/), which, given how it turned out, was probably a bit too much.

One of the most common answers I got from my mentors when I asked: "how many applications should I send?", was, "there is no way of knowing, the market is just very stochastic". Of course, being a statistician at heart, I immediately followed up with questions about the order of magnitude of the stochasticity. No one really knew, exact that it is **very** stochastic. This made sense to me - after all, I would not know how to pick the best out of N applicants with any certainty. Professors are of course better, but it seems natural that ranking candidates is hard. However, presenting the fact that committee evaluation must be a very noisy process to more senior professors, I was soon given another confusing piece of information. All professors that I spoke to were quite adamant that they are actually very good at ranking applicants, which seemingly contradicts the claim of high stochasticity in postdoc hiring decisions. 

Of course, there are ways that both can be true at the same time. To see how, let's consider how decisions in any one committee is made (according to the Princeton faculty). A candidate's vector of skills (e.g., technical skill, creativity, writing, ability to work with others), is projected onto a committee-specific vector encoding what that committee values. Of course, two things then contribute to selection noise (from the POV of the applicant):
1. The committee has imperfect knowledge of the skill vector
2. Different committees are searching for different things

The Senior people with whom I talked claimed that 2. is the main source of what we applicants perceive as stochasticity. However, for us applicants, it matters less where the noise comes from, we just want to know how noisy the entire process actually is. 

### This is the question I have set out to answer. 

# So how stochastic is the postdoctoral job market?

In order to measure the stochasticity in the job market, we first have to make a forward model of the job market. To that end, let's first get some basic statistics about the job market out of the way. (lift from notebook)

So now we need a way of turning these facts into a realistic model of the job market. For Claude, here I need a description of the model, (especially the Mallows model), as it is implemented in code. I want prestige histograms by position type, plots showing the postdoc skill distribution versus that of students, and any more ideas you may have.

Be very careful when describing how we do the skills and rankings, and that there is no inherent best/worst applicant, but we are putting up this toy-model to gain some insights. Drop a little, all models are wrong but some are useful, and link+foreshadow the results and how they will be presented (for a given rank, here is how many applications you should send to be N% sure to get at least one position). Also make sure to describe the round structure, and ask for a printout of one round with verbose = 1 (so round by round summaries).

Now, we can calibrate this code against the outcomes of this and previous Princeton cohorts in terms of the distribution of the number of offers, assuming, that the 4-10 graduating Princeton PhD are randomly drawn from withing the top 20% of those who apply. What we get is that there is indeed some stochasticity in the market, but not as much as I would have thought at all. The stochasticity level (and uncertainties) roughly corresponds to committees, on average, being able to recover the global ranking of a student to within 8 $\pm$ 3 places. I should note that the errors are quite assymmetric, so I actually can only get a 3 $\sigma$ "detection" of any stochasticity existing, but the market being highly stochastic is strongly ruled out. Hats off to the professors, they must be quite well-aligned in what they are looking for in us applicants.

So, then, why does everybody then say that everything is so stochastic. Well let's run the job-market once, and plot the rank of the position versus the rank of the student who ended up accepting the job. 
!! Figure (scatter plot)
What a mess.