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
categories: []
date: 2023-09-27
draft: false
featured: false
grants:
- polychronies
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2023-07-21 13:12:04+02:00
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/perrinet-23-icann/
projects: []
publication: '*ICANN Special Session on Recent Advances in Spiking Neural Networks*'
publication_types:
- '2'
publishDate: '2023-07-21T11:12:04.721342Z'
subtitle: ''
tags: []
title: Accurate Detection of Spiking Motifs by Learning Heterogeneous Delays of a Spiking Neural Network
url_pdf: https://laurentperrinet.github.io/publication/perrinet-23-icann/
---

* Will be presented at the [special session on Recent Advances in Spiking Neural Networks at this year's ICANN 2023 conference](https://e-nns.org/icann2023/wp-content/uploads/sites/7/2023/04/ICANN2023-ASNN-CfP.pdf).

* This theoretical implements the objectives set up in this review: {{< cite page="/publication/grimaldi-22-polychronies" view="4" >}}
