---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Learning hetero-synaptic delays of Spiking Neurons for motion detection
subtitle: ''
summary: ''
authors:
- Antoine Grimaldi
- Laurent U Perrinet
tags:
- efficient coding
- event-based vision
- homeostasis
- neuromorphic hardware
- online classification
categories: []
date: '2022-06-29'
lastmod: 2022-05-20T13:42:38+02:00
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
publishDate: '2022-05-20T11:42:36.747953Z'
publication_types:
- '1'
abstract: The response of a biological neuron depends on the precise timing of afferent
  spikes. This temporal aspect of the neuronal code is essential in understanding
  information processing in neurobiology and applies particularly well to the output
  of neuromorphic hardware such as event-based cameras. However, most artificial neuronal
  models do not take advantage of this minute temporal dimension. Inspired by this
  neuroscientific observation, we develop a model for the efficient detection of temporal
  spiking motifs based on a layer of neurons with hetero-synaptic delays. Indeed,
  the connectivity of the dendritic tree allows to discriminate between different
  temporal sequences, and we show that this can be formalized as a time-invariant
  logistic regression which can be trained using labelled data. We apply this model
  to solve the specific computer vision problem of motion detection and demonstrate
  its application to synthetic nature videos transformed into event streams similar
  to the output of event-based cameras. In particular, we quantify how its accuracy
  can vary with the total computational load. This end-to-end event-driven computational
  brick could help improve the performance of future spiking neural network (SNN)
  solutions currently used in neuromorphic chips.
publication: '*Proceedings of AREADNE*'
links:
- name: URL
  url: https://areadne.org/
---
