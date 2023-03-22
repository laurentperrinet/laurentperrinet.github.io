---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Learning heterogeneous delays of spiking neurons for motion detection
subtitle: ''
summary: ''
authors:
- Antoine andd Perrinet, Laurent U Grimaldi
tags: []
categories: []
date: '2023-01-27'
lastmod: 2023-03-22T16:35:38+01:00
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
publishDate: '2023-03-22T15:35:38.869745Z'
publication_types:
- '1'
abstract: 'The response of a biological neuron depends largely on the precise timing
  of presynaptic spikes that reach the basal dendritic tree. However, most neuronal
  models do not take advantage of this minute temporal dimension, especially in exploiting
  the variety of synaptic delays on the dendritic tree. A notable exception is the
  polychronization model, a recurrent model of spiking neurons including fixed and
  random heterogeneous delays and in which the weights are learned using Spike-Time
  Dependent Plasticity. The output raster plot displays repeated activations of prototypical
  spiking motifs called Polychronous Groups. Importantly, these motifs seem to be
  highly relevant in experimental neuroscience. Here, by extending the model of~[3],
  we develop a spiking neural network model for the efficient detection of PGs: By
  defining the generation of the raster plot as a probabilistic combination of PGs,
  we build and train the network in order to optimize the inversion of this generative
  model. '
publication: '*GDR Vision, Toulouse, 2023*'
links:
- name: URL
  url: https://gdr-vision-2023.sciencesconf.org/browse?forward-action=index&forward-controller=browse&docid=442297&lang=en
---

* see a follow-up as journal paper: {{< cite page="/publication/grimaldi-22-bc" view="4" >}}
* presented at [GDR vision 2023 2022](https://gdr-vision-2023.sciencesconf.org/) January 2023 in Toulouse, France
