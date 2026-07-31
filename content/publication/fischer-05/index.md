---
abstract: Low-level perceptual computations may be understood in terms of efficient
  codes (Simoncelli and Olshausen, 2001, Annual Review of Neuroscience 24 1193-216).
  Following this argument, we explore models of representation for natural static
  images as a way to understand the processing of information in the primary visual
  cortex. This representation is here based on a generative linear model of the synthesis
  of images using an over-complete multi-resolution dictionary of edges. This transform
  is implemented using log-Gabor filters and permits an exact reconstruction of any
  image. However, this linear representation is redundant and since to any image may
  correspond different representations, we explore more efficient representations
  of the image. The problem is stated as an ill-posed inverse problem and we compare
  first different known strategies by computing the efficiency of the solutions given
  by Matching Pursuit (Perrinet, 2004, IEEE Trans. Neural Networks 15 1164-75) and
  sparse edge coding (Fischer, in press, Trans. Image Processing) with classical representation
  methods such as JPEG. This comparison allows us to provide a synthesized approach
  using a probabilistic representation which would progressively construct the neural
  representation by using lateral cooperations. We propose an algorithm which dynamically
  diffuses information to correlated filters so as to yield a progressively disambiguated
  representation. This approach takes advantage of the computational properties of
  spiking neurons such as Integrate-and-Fire neurons and provides an efficient yet
  simple model for the representation of natural images. This representation is directly
  linked with the edge content of natural images and we show applications of this
  method to edge extraction, denoising and compression. We also show that this dynamical
  approach fits with neuro-physiological observations and may explain the non-linear
  interactions between neighboring neurons which may be observed in the cortex.
authors:
- Sylvain Fischer
- Rafael Redondo
- Laurent U Perrinet
- Gabriel Cristóbal
date: 2005-01-01
featured: false
projects:
- facets
publication: '*Perception*'
publication_types:
- inproceedings
tags: ["matching-pursuit", "vision"]
title: Efficient representation of natural images using local cooperation
categories: ["Computational Neuroscience"]
---
* relies on log-Gabor filters: {{< cite page="/publication/fischer-07-cv" view="4" >}}
{{< figure src="https://laurentperrinet.github.io/publication/fischer-07/figure2.png" width="80%" title="Schematic structure of the primary visual cortex implemented in the present study. Simple cortical cells are modeled through log-Gabor functions. They are organized in pairs in quadrature of phase (dark-gray circles). For each position the set of different orientations compose a pinwheel (large light-gray circles). The retinotopic organization induces that adjacent spatial positions are arranged in adjacent pinwheels. Inhibition interactions occur towards the closest adjacent positions which are in the direc-tions perpendicular to the cell preferred orientation and toward adjacent orientations (light-red connections). Facilitation occurs to-wards co-aligned cells up to a larger distance (dark-blue connections). " >}}
