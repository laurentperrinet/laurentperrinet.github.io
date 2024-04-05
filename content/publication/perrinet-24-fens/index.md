---
# Documentation: https://docs.hugoblox.com/managing-content/

title: Accurate Detection of Spiking Motifs in Neurobiological Data by Learning Heterogeneous
  Delays of a Spiking Neural Network
subtitle: ''
summary: ''
authors:
- Laurent U Perrinet
tags: []
categories: []
date: '2024-06-27'
lastmod: 2024-04-05T10:22:08+02:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-04-05T08:22:04.452494Z'
publication_types:
- '1'
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
publication: '*FENS Forum 2024*'
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/perrinet-24-fens/
---
