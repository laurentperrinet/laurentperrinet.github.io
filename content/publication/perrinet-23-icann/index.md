---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Accurate detection of spiking motifs in multi-unit raster plots
subtitle: ''
summary: ''
authors:
- Laurent U Perrinet
tags: []
categories: []
date: '2023-01-01'
lastmod: 2023-07-21T13:12:04+02:00
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
publishDate: '2023-07-21T11:12:04.721342Z'
publication_types:
- '2'
abstract: Recently, there has been growing interest in the hypothesis that information
  can be carried within neural activity by precise spiking motifs. As a result, there
  have been several recent proposals for algorithms to detect such motifs in the Spiking
  Unit Activity (SUA) of populations of neurons. In this study, we introduce a detection
  model as an inversion of a generative model of raster plot synthesis. From this
  model, an optimal detection procedure is derived. This takes the form of a logistic
  regression coupled with a temporal convolution. Since this model is differentiable,
  we derive a supervised learning method in the form of gradient descent on the loss
  function of an auto-encoder model. We evaluate the ability of this model to detect
  spiking motifs in synthetic data. This learning method is able to recover the synthetically
  generated spiking motifs, and we plan to extend this method to neurobiological data
  as well.
publication: '*ICANN Special Session on Recent Advances in Spiking Neural Networks*'
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/keating-perrinet-23-icann/
---
