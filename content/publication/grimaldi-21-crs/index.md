---
# Documentation: https://wowchemy.com/docs/managing-content/

title: From event-based computations to a bio-plausible Spiking Neural Network
subtitle: ''
summary: ''
authors:
- Antoine Grimaldi
- Victor Boutin
- Sio-Hoi Ieng
- Ryad Benosman
- Laurent U Perrinet
tags:
- '"efficient coding"'
- '"event-based vision"'
- '"homeostasis"'
- '"neuromorphic hardware"'
- '"online classification"'
categories: []
date: '2021-02-26'
lastmod: 2021-10-12T12:44:34+02:00
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
publishDate: '2021-10-12T10:44:33.992162Z'
publication_types:
- '1'
abstract: ' We propose a neuromimetic online classifier for always-on digit recognition. To achieve this, we extend an existing event-based algorithm which introduced novel
  spatio-temporal features: time surfaces. Built from asynchronous events acquired
  by a neuromorphic camera, these time surfaces allow to code the local dynamics of
  a visual scene and create an efficient hierarchical event-based pattern recognition
  architecture. Its formalism was previously adapted in the computational neuroscience
  domain by showing it may be implemented using a Spiking Neural Network (SNN) of
  leaky integrate-and-fire models and Hebbian learning. Here, we add an online classification
  layer using a multinomial logistic regression which is compatible with a neural
  implementation. A decision can be taken at any arbitrary time by taking the $argmax$ of the probability values associated to each class. We extend the parallel
  with computational neuroscience by demonstrating that this classification layer
  is also equivalent to a layer of spiking neurons with a Hebbian-like learning mechanism.
  Our method obtains state-of-the-art performances on the N-MNIST dataset and we show
  that it is robust to both spatial and temporal jitter. As a summary, we were able
  to develop a neuromimetic SNN model for online digit classification. We aim at pursuing
  the study of this architecture for natural scenes and hope to offer insights on
  the efficiency of neural computations, and in particular how mechanisms of decision-making
  may be formed.'
publication: '*Champalimaud Research Symposium (CRS21)*'
url_pdf: https://laurentperrinet.github.io/publication/grimaldi-21-crs/
---
