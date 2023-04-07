---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Convolutional Sparse Coding is improved by heterogeneous uncertainty modeling
subtitle: ''
summary: ''
authors:
- Hugo Ladret
- Laurent U Perrinet
tags:
- sparse
- coding
- convolutional
- natural
- images
- uncertainty
categories: []
date: '2023-05-05'
lastmod: 2023-04-07T12:45:44+02:00
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
publishDate: '2023-04-07T10:45:44.753196Z'
publication_types:
- '1'
abstract: Aleatoric uncertainty characterizes the variability of features found in
  natural images, and echoes the epistemic uncertainty ubiquitously found in computer
  vision models. We explore this ”uncertainty in, uncertainty out” relationship by
  generating convolutional sparse coding dictionaries with parametric epistemic uncertainty.
  This improves sparseness, resilience and reconstruction of natural images by providing
  the model a way to explicitly represent the aleatoric uncertainty of its input.
  We demonstrate how hierarchical processing can make use of this scheme by training
  a deep convolutional neural network to classify a sparse-coded CIFAR10 dataset,
  showing that encoding uncertainty in a sparse code is as efficient as using conventional
  images, with additional beneficial computational properties. Overall, this work
  empirically demonstrates the advantage of partitioning epistemic uncertainty in
  sparse coding algorithms.
publication: '*ICLR 2023 SNN Workshop*'
---
