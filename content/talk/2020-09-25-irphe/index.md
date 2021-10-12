---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Understanding natural vision using deep predictive coding
subtitle: ''
summary: ''
authors:
- Laurent U Perrinet
tags: []
categories: []
date: '2020-09-25'
lastmod: 2021-10-12T12:44:44+02:00
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
publishDate: '2021-10-12T10:44:44.847897Z'
publication_types:
- '1'
abstract: Building models which efficiently process images is a great source of inspiration
  to better understand the processes which underly our visual perception. I will present
  some classical models stemming from the Machine Learning community and propose some
  extensions inspired by Nature. For instance, Sparse Coding (SC) is one of the most
  successful frameworks to model neural computations at the local scale in the visual
  cortex. It directly derives from the efficient coding hypothesis and could be thought
  of as a competitive mechanism that describes visual stimulus using the activity
  of a small fraction of neurons. At the structural scale of the ventral visual pathways,
  feedforward models of vision (CNNs in the terminology  of deep learning) take into
  account neurophysiological observations and provide as of today the most successful
  framework for object recognition tasks. Nevertheless, these models do not leverage
  the high density of feedback and lateral interactions observed in the visual cortex.
  In particular, these connections are known to integrate contextual and attentional
  modulations to feedforward signals. The Predictive Coding (PC) theory has been proposed
  to model top-down and bottom-up interaction between cortical regions. We will here
  introduce a model combining Sparse Coding and Predictive Coding in a hierarchical
  and convolutional architecture. Our model, called Sparse Deep Predictive Coding
  (SDPC), was trained on several different databases including faces and natural images.
  We analyze the SPDC from a computational and a biological perspective and we combine
  neuroscientific evidence with machine learning methods to analyze the impact of
  recurrent processing at both the neural organization and representational levels.
  These results from the SDPC model additionally demonstrate that neuro-inspiration
  might be the right methodology to design more powerful and more robust computer
  vision algorithms.
publication: "*Séminaire à l'Institut de Recherche sur les Phénomènes Hors Équilibre*"
url_pdf: https://laurentperrinet.github.io/talk/2020-09-25-irphe
---
