---
title: 'Feature detection using spikes : the greedy approach'
date: 2004-07-01
authors:
- Laurent U Perrinet
abstract: A goal of low-level neural processes is to build an efficient code extracting
  the relevant information from the sensory input. It is believed that this is implemented
  in cortical areas by elementary inferential computations dynamically extracting
  the most likely parameters corresponding to the sensory signal. We explore here
  a neuro-mimetic feed-forward model of the primary visual area (V1) solving this
  problem in the case where the signal may be described by a robust linear generative
  model. This model uses an over-complete dictionary of primitives which provides
  a distributed probabilistic representation of input features. Relying on an efficiency
  criterion, we derive an algorithm as an approximate solution which uses incremental
  greedy inference processes. This algorithm is similar to 'Matching Pursuit' and
  mimics the parallel architecture of neural computations. We propose here a simple
  implementation using a network of spiking integrate-and-fire neurons which communicate
  using lateral interactions. Numerical simulations show that this Sparse Spike Coding
  strategy provides an efficient model for representing visual data from a set of
  natural images. Even though it is simplistic, this transformation of spatial data
  into a spatio-temporal pattern of binary events provides an accurate description
  of some complex neural patterns observed in the spiking activity of biological neural
  networks.
featured: false
categories:
- Biological Neuroscience
- Computational Neuroscience
tags:
- bayesian-modelling
- primary-visual-cortex
- sparse-coding
- spiking-neural-networks
publication: '*Journal of Physiology-Paris*'
publication_types:
- article-journal
doi: 10.1016/j.jphysparis.2005.09.012
links:
- name: URL
  url: https://doi.org/10.1016/j.jphysparis.2005.09.012
- name: arXiv
  url: https://arxiv.org/abs/q-bio/0611003
grants:
- facets
---
