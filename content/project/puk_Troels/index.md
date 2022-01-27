---
title: Classifying - particles from the ATLAS detector for detector calibration
summary: We go through several low - to medium level Machine Learning algorithms and optimize their performance for a classifying - particles, both in simulation and real data
tags:
- Machine Learning
- Particle Physics
date: "2022-01-25T00:00:00Z"
draft: false
featured: false

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: XGBoost ecision boundary for two parameters in the ATLAS dataset
  focal_point: Smart

links:
url_code: "https://github.com/astrockragh/troels_projekt"
# url_pdf: "/project/puk_troels/PUK_med_Troels.pdf" #need to ask the guys

slides: ""

---
This project was done in collaboration with [Jonas Vinther](https://github.com/Vinther901), [Johann Bock Severin](https://github.com/JohannSeverin) and [Jakob H. Schauser](https://github.com/JakobSchauser). Check out their GitHubs!

In most branches of physics, new discoveries are made by identifying som signal peak upon a background of noise. In High Energy Physics, this could be the peak of a new particle found amongst the almost uncountable amount of collisions happening every second the Large Hadron Collider is running. Only a few collisions actually produce the particles we search for, so finding and quantifying small peaks is the cornerstone of making the actual discovery. This makes it crucial to be able to classify which detections are part of the actual signal, and which are not. In this project we employed a range of statistical methods and machine learning algorithms to get the best estimate of the masses of $V^0$ - particles, in both simulated data and real data.

![Signal in simulation and data for normal fit. The background is fitted with a third degree polynomial and a double Gaussian is used on the peak.](/project/puk_troels/Truesimplefits.png)

As can be seen in the top figure, among some of the methods tried were simply doing some linear cuts in the feature space, found by simple annealing, using Fisher's discriminant analysis, a simple decision tree and XGBoost, which ended up being the method of choice. We ended up getting an accuracy of 99.7% for classyfing signal and background.