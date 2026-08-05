---
abstract: Recently, interest has grown in exploring the hypothesis that neural activity
  conveys information through precise spiking motifs. To investigate this phenomenon,
  various algorithms have been proposed to detect such motifs in Single Unit Activity
  (SUA) recorded from populations of neurons. In this study, we present a novel detection
  model based on the inversion of a generative model of raster plot synthesis. Using
  this generative model, we derive an optimal detection procedure that takes the form
  of logistic regression combined with temporal convolution. A key advantage of this
  model is its differentiability, which allows us to formulate a supervised learning
  approach using a gradient descent on the binary cross-entropy loss. To assess the
  model's ability to detect spiking motifs in synthetic data, we first perform numerical
  evaluations. This analysis highlights the advantages of using spiking motifs over
  traditional firing rate based population codes. We then successfully demonstrate
  that our learning method can recover synthetically generated spiking motifs, indicating
  its potential for further applications. In the future, we aim to extend this method
  to real neurobiological data, where the ground truth is unknown, to explore and
  detect spiking motifs in a more natural and biologically relevant context.
authors:
- Laurent U Perrinet
date: 2023-09-27
doi: 10.1007/978-3-031-44207-0_31
draft: false
featured: false
grants:
- polychronies
image:
  caption: ''
  focal_point: Smart
  preview_only: false
lastmod: 2023-07-21 13:12:04+02:00
links:
- name: Code
  url: https://github.com/laurentperrinet/2023-09-27_HDSNN-ICANN
- name: arXiv
  url: https://arxiv.org/abs/2307.11555

publication: '*ICANN Special Session on Recent Advances in Spiking Neural Networks*'
publication_types:
- inproceedings
publishDate: '2023-07-21T11:12:04.721342Z'
slides: 2023-09-27_icann
subtitle: ''
title: Accurate Detection of Spiking Motifs by Learning Heterogeneous Delays of a
  Spiking Neural Network
tags:
- predictive-coding
- spiking-neural-networks
categories:
- Computational Neuroscience
- NeuroAI & Machine Learning
- Outreach & Public Engagement
- Theoretical Neuroscience
projects:
- ''
---






* paper presented during the [32nd International Conference on Artificial Neural Networks (ICANN 2023)](https://e-nns.org/icann2023/)
* Will be presented at the [special session on Recent Advances in Spiking Neural Networks at this year's ICANN 2023 conference](https://e-nns.org/icann2023/wp-content/uploads/sites/7/2023/04/ICANN2023-ASNN-CfP.pdf)
* This theoretical implements the objectives set up in this review: {{< cite page="/publication/grimaldi-22-polychronies" view="4" >}}
* The code is available on [GitHub](https://github.com/laurentperrinet/2023-09-27_HDSNN-ICANN)
