---
title: "Post-doc Market II: Modelling the Stochasticity in the Market"
subtitle:

# Summary for listings and search engines
summary: The postdoctoral job market is one of the major challenges anyone wishing to work in academia must face. To gain insights into the dynamics of the market, we can model, fit, and simulate the market. These simulations let us answer a few hard questions.

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

One of the most common answers I got from my mentors when I asked: "how many applications should I send?", was, "there is no way of knowing, the market is just very stochastic". Of course, being a statistician at heart, I immediately followed up with questions about the order of magnitude of the stochasticity. No one really knew, exact that it is **very** stochastic. This made sense to me - after all, I would not know how to pick the best out of N applicants with any certainty. Professors are of course better, but it seems natural that ranking candidates is hard. However, presenting the fact that committee evaluation must be a very noisy process to more senior professors, I was soon given another confusing piece of information. All professors that I spoke to were quite adamant that they are actually very good at ranking applicants, which seemingly contradicts the claim of high stochasticity in postdoc hiring decisions. I was very skeptical of this, since it seemed to me a way of justifying their own success. As explained [in this video](https://www.youtube.com/watch?v=3LopI4YeC4I), professors are likely to overestimate just how much of a role skills plays in these decisions, since nobody successful likes to believe that their good fortunes are largely determined by luck.  

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

!! Figure (scatter plot, with postdocs and students covered differently)

What a mess! So even if individual committees are not very stochastic, the market still looks very stochastic from the POV of any applicant. This is a key take-away point from this exercise.

`The appearance of high stochasticity can persist even in the limit where any individual committees is minimally stochastic` 

So both of the things that I was told early, which seemed inconsistent with one another, that a) the market should be viewed as very stochastic and that b) professors/committees are actually quite good (or at least, consistent) at ranking people, turned out to be true at the same time! This behaviour largely persists because of the fact that both $$ N_applicants > N_positions $$, and $$ N_applications>> N_positions $$. Expand on this part here Claude, maybe expand on this using marriage market theory where $$ N_applicants \approx N_positions $$ and how there, stable pairings can be found. This also mirrors the case of astronaut selections, link this amazing [veritasium video](https://www.youtube.com/watch?v=3LopI4YeC4I). You should read the transcript to inform the background for this article.

Now let's color each point by the round that they got accepted in - this will uncover a pretty significant source of where a lot of this apparent scatter comes from - many very good people act as corks in the flow of jobs in the first round, making a lot of unexpected things happen with time. 

!!Figure (scatter plot, coloured by acceptance round)

I think that this highlights something that I got to see firsthand here at Princeton - first, that offers tend to cluster quite strongly, and second, that many very good people end up with a large amount of waitlist offers, and then get many offers once the market starts to loosen up post-round 1. We can try to see how this works by also plotting the median, and inter-quartile, ranks of people binned by number of offers received in round 1, 2, and 3 (in three separate axes, in three columns). 

!! Put this figure here

So many really great applicants end up getting put through the painful experience of having to wait months after months to then get several offers.

Okay, but now that we have the model in place, we can start to really test it a little more. Running a single market gives us a very stochastic outcome (again, despite committees being coherent in their rankings), but if we run the market 100 times, we can build up heatmaps of the average number of offers received by applicant rank and number of applications sent.

!!Heatmap figure

This is instructive - the 5% best applicants are essentially guaranteed to get an offer, even if they only apply a small amount of times. However, for an applicant to get many offers, they really have to both be very good, and send a lot of applications. We also see that once you get down to the 10th-30th percentile, the number of applications does really start to matter. We can try to quantify this and finally answer the question that sparked this entire post

# How many applications should I send?

So in truth, the question that I will answer is a little more specified.

### If I believe that I am roughly ranked at given percentile, how many applications should I send to have an X percent chance of getting at least one offer?

The clean way to do this is by injecting candidates into the job market. We can modify our simulation code to do this, and then inject a candidate with a pre-determined number of applications to send, as well as a pre-determined global rank. Since we are just injecting one applicant out of ~1000, the dynamics of the job market will not be disturbed. We can then run the market a couple hundred times, and see how well our injected candidates fare, i.e., how often do they get **at least one offer**, as a function of how many applications they send. The results can be seen below, and it is my hope that this table can be of some use to future applicants

!! The table

I think that the safest use of this table is to try to get one of your advisors or mentors to guess at your ranking. Add 5% for safety, and then use that column to estimate how many applications to send. Of course, when you do ask your mentors, remember that it is your global ranking, out of the roughly 1000 students that will graduate in a given year, that you care about. So top 5% corresponds to top 50 and so on, which may give you a better way of phrasing the question both to others and to yourself. 

## What if the job market were different?

!Running a few tests with half the positions available or double the students, and one with double the positions available, or half the amount of students applying and making the scatter plots in four separate axes, arranged in a square pattern.

!Running a test with close to zero stochasticity in the Mallows model, and one with a lot of stochasticity, and making the scatter plots in two separate axes, arranged horizontally.

# Final take-aways

I think that the biggest take-away from this exercise is that the main determinant really is global ranking, much more than number of applications sent. This is uplifting - as an applicant, you really do benefit mostly from doing more scientific work, instead of spending all too much time sending more applications. It also goes directly contrary to a piece of advice I got quite a lot "applications are a lottery, and you just have to make sure that you buy enough lottery tickets".

It's very important across this post that the global ranking system is a toy model, and that real rankings are driven by a lot of biases that come into the perception of the "real" ranking. What this exercise in part shows, is that whatever biases exist in any one committee, must also exist in any other committee.