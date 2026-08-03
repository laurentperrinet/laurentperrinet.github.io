---
abstract: Recently, there has been an increase in interest in exploring the hypothesis
  that neural activity conveys information through precise spiking motifs. To investigate
  this phenomenon, several algorithms have been proposed to detect such motifs in
  Single Unit Activity recorded from populations of neurons. Based on the inversion
  of a generative model of raster plot synthesis, we present a novel detection model.
  This model derives an optimal detection procedure in the form of logistic regression
  combined with temporal convolution. Its differentiability allows for a supervised
  learning approach using gradient descent on the binary cross-entropy loss. To assess
  the model's ability to detect spiking motifs in synthetic data, numerical evaluations
  are performed. This analysis emphasizes the benefits of utilizing spiking motifs
  instead of traditional firing rate-based population codes. Our learning method was
  able to successfully recover synthetically generated spiking motifs, indicating
  its potential for further applications. In the future, we aim to extend this method
  to real neurobiological data, where the ground truth is unknown, to explore and
  detect spiking motifs in a more natural and biologically relevant context.
authors:
- Laurent U Perrinet
categories: ["Computational Neuroscience", "NeuroAI & Machine Learning"]
date: 2024-06-27
draft: false
featured: false
grants:
- polychronies
image:
  caption: ''
  focal_point: Smart
  preview_only: false
lastmod: 2024-04-05 10:22:08+02:00
links:
- name: Code
  url: https://github.com/laurentperrinet/2024-06-26_Perrinet24FENS
- name: URL
  url: https://laurentperrinet.github.io/publication/perrinet-24-fens/

publication: '*Proceedings of the FENS Forum 2024*'
publication_types:
- inproceedings
publishDate: '2024-04-05T08:22:04.452494Z'
subtitle: ''
tags: ["predictive-coding", "spiking-neural-networks", "neuromorphic-computing"]
title: Accurate Detection of Spiking Motifs in Neurobiological Data by Learning Heterogeneous
  Delays of a Spiking Neural Network
---
* see accompanying papers
 * for neural data: {{< cite page="/publication/perrinet-23-icann" view="4" >}}
 * for event-based cameras: {{< cite page="/publication/grimaldi-23-bc" view="4" >}}
