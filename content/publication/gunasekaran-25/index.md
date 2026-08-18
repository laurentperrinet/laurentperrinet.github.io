--- 
title: A Predictive Approach to Enhance Time-Series Forecasting
authors:
- Skye Gunasekaran
- Assel Kembay
- Hugo Ladret
- Rui-Jie Zhu
- Laurent U Perrinet
- Omid Kavehei
- Jason Eshraghian
date: '2025-08-29'
publishDate: '2024-12-23T13:47:40.425008Z'
publication_types:
- manuscript
abstract: 'Accurate time-series forecasting is essential across a multitude of scientific
  and industrial domains, yet deep learning models often struggle with challenges
  such as capturing long-term dependencies and adapting to drift in data distributions
  over time. We introduce Future-Guided Learning, an approach that enhances time-series
  event forecasting through a dynamic feedback mechanism inspired by predictive coding.
  Our approach involves two models: a detection model that analyzes future data to
  identify critical events and a forecasting model that predicts these events based
  on present data. When discrepancies arise between the forecasting and detection
  models, the forecasting model undergoes more substantial updates, effectively minimizing
  surprise and adapting to shifts in the data distribution by aligning its predictions
  with actual future outcomes. This feedback loop, drawing upon principles of predictive
  coding, enables the forecasting model to dynamically adjust its parameters, improving
  accuracy by focusing on features that remain relevant despite changes in the underlying
  data. We validate our method on a variety of tasks such as seizure prediction in
  biomedical signal analysis and forecasting in dynamical systems, achieving a 40%
  increase in the area under the receiver operating characteristic curve (AUC-ROC)
  and a 10% reduction in mean absolute error (MAE), respectively. By incorporating
  a predictive feedback mechanism that adapts to data distribution drift, Future-Guided
  Learning offers a promising avenue for advancing time-series forecasting with deep
  learning.'
doi: 10.1038/s41467-025-63786-4
links:
- name: URL
  url: https://www.nature.com/articles/s41467-025-63786-4
- name: Code
  url: https://github.com/SkyeGunasekaran/FutureGuidedLearning
- name: PDF
  url: https://www.nature.com/articles/s41467-025-63786-4.epdf
- name: arXiv
  url: https://arxiv.org/abs/2410.15217
- name: HAL
  url: https://hal.science/hal-05293576
tags:
- predictive-coding
categories:
- Computational Neuroscience
- Education
- NeuroAI & Machine Learning
projects: []
---

The lead author, Jason Eshragian, speaks most clearly about it: 

For the amount of compute they burn, transformers are pretty bad at time-series data analysis. Which is pretty unsurprising if your objective is to predict the next token, one step at a time. 

Brains, on the other hand, are predictive machines. Think of your daily commute to work. On Day 1, your brain was probably in overdrive to make sure you're not late, taking in all of your environment. On Day 1000, you're on full autopilot, barely burning mental energy unless something unexpected - like a major accident - forces you to adjust. 

That's predictive coding in action: the brain continuously compares its expectations (no traffic) to reality (flipped car damn), then updates only when surprised.

Skye Gunasekaran has spent the past couple of years integrating this principle into Future-Guided Learning, where a "future" model guides a "past" forecasting model, dynamically minimizing surprise when reality deviates from predictions. 

In our preprint, we show how drawing upon neuroscience-inspired ideas actually helps in time-series forecasting with deep learning. Efficiency isn't the only win from the brain; it's also pretty damn good at organizing long-range time-series information. 

https://www.linkedin.com/feed/update/urn:li:activity:7378797683425296385/
https://bsky.app/profile/laurentperrinet.bsky.social/post/3m26xgwaisc2t
https://neuromatch.social/@laurentperrinet/115303186807684381

