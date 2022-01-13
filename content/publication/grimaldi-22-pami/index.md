---
# Documentation: https://wowchemy.com/docs/managing-content/

title: A Robust Event-Driven Approach to Always-on Object Recognition
subtitle: ''
summary: ''
authors:
- Antoine Grimaldi
- Victor Boutin
- Sio-Hoi Ieng
- Ryad Benosman
- Laurent U Perrinet
tags:
- efficient coding
- event-based vision
- homeostasis
- neuromorphic hardware
- online classification
categories: []
date: '2022-01-13'
lastmod: 2022-01-13T15:27:10+01:00
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
publishDate: '2022-01-13T14:27:10.142244Z'
publication_types:
- '2'
abstract: 'We propose a neuromimetic architecture able to perform always-on pattern
  recognition. To achieve this, we extended an existing event-based algorithm [1],
  which introduced novel spatio-temporal features as a Hierarchy Of Time-Surfaces
  (HOTS). Built from asynchronous events acquired by a neuromorphic camera, these
  time surfaces allow to code the local dynamics of a visual scene and to create an
  efficient event-based pattern recognition architecture. Inspired by neuroscience,
  we extended this method to increase its performance. Our first contribution was
  to add a homeostatic gain control on the activity of neurons to improve the learning
  of spatio-temporal patterns [2]. A second contribution is to draw an analogy between
  the HOTS algorithm and Spiking Neural Networks (SNN). Following that analogy, our
  last contribution is to modify the classification layer and remodel the offline
  pattern categorization method previously used into an online and event-driven one.
  This classifier uses the spiking output of the network to define novel time surfaces
  and we then perform online classification with a neuromimetic implementation of
  a multinomial logistic regression. Not only do these improvements increase consistently
  the performances of the network, they also make this event-driven pattern recognition
  algorithm online and bio-realistic. Results were validated on different datasets:
  DVS barrel [3], Poker-DVS [4] and N-MNIST [5]. We foresee to develop the SNN version
  of the method and to extend this fully event-driven approach to more naturalistic
  tasks, notably for always-on, ultra-fast object categorization.'
publication: '*TechRxiv*'
doi: 10.36227/techrxiv.18003077.v1
links:
- name: URL
  url: https://www.techrxiv.org/articles/preprint/A_robust_event-driven_approach_to_always-on_object_recognition/18003077/1
---
