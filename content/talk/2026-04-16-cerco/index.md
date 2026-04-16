---
title: Working Memory in Recurrent Spiking Neural Networks Using Heterogeneous Synaptic
  Delays
authors:
- Laurent U Perrinet
date: '2026-04-16'
publishDate: '2026-04-09T06:52:10.397771Z'
publication_types:
- paper-conference
publication: '*Seminar at CerCo*'
abstract: 'Working memory --- the ability to store and retrieve precise temporal patterns of neural activity —-- remains a fundamental challenge for spiking neural networks (SNNs). We introduce a recurrent SNN in which each synapse is modeled as a three-dimensional weight tensor with learnable heterogeneous delays. The network learns to predict future spikes by representing each target pattern as a sequential chain of overlapping Spiking Motifs: contiguous windows of length DDD that encode the unique temporal signature of neural activity within a fixed delay range. By integrating spikes over these windows, the network autonomously recalls and extends the sequence beyond the clamped initial context, generating future spikes without further input. On a synthetic benchmark of M=8 patterns (N=512 neurons, T=1000 steps), training with surrogate-gradient backpropagation achieves a mean F1 score of 0.966, with recall emerging near the clamped window and propagating forward in time. Our results demonstrate that heterogeneous synaptic delays provide an efficient, biologically plausible substrate for working memory in SNNs, enabling energy-efficient neuromorphic implementations on edge devices.'

slides: 2026-04-16-cerco

links:
- name: URL
  url: https://laurentperrinet.github.io/talk/2026-04-16-cerco/
- name: Preprint
  url: http://arxiv.org/abs/2604.14096

---
