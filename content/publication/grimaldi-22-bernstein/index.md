---
abstract: The spiking response of a biological neuron depends on the precise timing
  of afferent spikes. This temporal aspect of the neuronal code is essential in understanding
  information processing in neurobiology. In this model, raster plot analysis showed
  repeated activation of specific spiking motifs, which exhibit a precise temporal
  sequence of neural activations. Our first contribution is to develop a model for
  the efficient detection of temporal spiking motifs based on a layer of neurons with
  hetero-synaptic delays. Indeed, the variety of synaptic delays on the dendritic
  tree allows synchronizing synaptic inputs as they reach the basal dendritic tree.
  Second, we propose a bio-plausible unsupervised learning rule on both weights and
  delays through the derivation of a loss function which depends on the membrane potential
  of the spiking neuron and a sparseness regularization. We demonstrate on synthetic
  data that such a layer of spiking neurons is able to learn different repeating spatio-temporal
  motifs embedded in the spike train. Then, we test the robustness of the detection
  accuracy of the model by adding Poisson noise and compare it to a layer of Leaky-Integrate
  and Fire neurons trained with STDP. Results show a large improvement in performances
  when adding temporal delays for computations and a great increase in robustness
  to noise. We show that using synaptic delays for neuronal computations highly increases
  the representational capacities of a single neuron and its resilience to noise.
  .
authors:
- Antoine Grimaldi
- Camille Besnainou
- Hugo Ladret
- Laurent U Perrinet
categories: []
date: 2022-09-11
draft: false
featured: false
grants:
- aprovis3D
- anr-anr
- polychronies
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2023-07-21 13:12:04+02:00
projects: []
publication: '*Bernstein Conference 2022*'
publication_types:
- inproceedings
publishDate: '2023-07-21T11:11:54.651024Z'
subtitle: ''
tags: []
title: Detection of precise spiking motifs using spike-time dependent weight and delay
  plasticity
---
