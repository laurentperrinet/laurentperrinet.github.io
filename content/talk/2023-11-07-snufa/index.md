---
# Documentation: https://wowchemy.com/docs/managing-content/
title: Accurate Detection of Spiking Motifs by Learning Heterogeneous Delays of a Spiking Neural Network
subtitle: ''
summary: 'Recently, there has been growing interest in exploring the hypothesis that neural activity conveys information through precise spiking motifs. To investigate this hypothesis, various algorithms have been proposed to detect such motifs in spiking activity recorded from populations of neurons. In this study, we present a detection model that takes the form of logistic regression combined with temporal convolution. A key advantage of this model is its differentiability, which allows us to formulate a gradient descent on any appropriate loss. We prove its efficiency on synthetic data for which the ground truth is available to use supervised learning. However, this ground truth information is not available for neurobiological data, where a self-learning procedure is required. We show that a contrastive learning method can recover the synthetically generated spiking motifs without knowing the ground truth. In the future, we aim to extend this method to real neurobiological data to explore and detect spiking motifs in a more natural and biologically relevant context.'
authors:
- Laurent U Perrinet
tags: []
categories: []
date: '2023-11-07'
lastmod: 2023-09-10T17:59:14+02:00
featured: false
draft: false
slides: "2023-11-07-snufa"

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
publishDate: '2023-11-06T15:59:14.546901Z'
publication_types:
- '1'
abstract: ''
publication: '*SNUFA: Spiking Neural networks as Universal Function Approximators*'
---

* Poster Session at https://snufa.net/2023/
* https://snufa.net/2023/abstracts/laurent-perrinet-accurate.html
* code: https://github.com/laurentperrinet/2023-09-27_HDSNN-ICANN


