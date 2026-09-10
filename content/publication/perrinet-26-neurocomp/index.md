---
title: Efficient Working Memory in a recurrent Spiking Neural Network
authors:
- Laurent U Perrinet
date: '2026-09-03'
publishDate: '2026-09-10T10:34:20.736649Z'
publication_types:
- paper-conference
publication: '*First Scientific Meeting of the Réseau Thématique en Neurosciences
  Computationnelles (RT NeuroComp).*'
abstract: 'Working memory --- the ability to store and recall precise temporal patterns
  --- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent
  SNN in which each synapse is equipped with heterogeneous delays parameterised as
  a weight tensor and trained end-to-end with surrogate-gradient backpropagation through
  time. Each stored pattern is represented as a sequential chain of overlapping Spiking
  Motifs: contiguous context windows of length that uniquely predict the activity
  at the next time step. A closed-form Hebbian initialisation, derived by deconvolving
  the LIF membrane response and targeting a sub-threshold membrane potential value
  superior to the threshold, achieves an accuracy as measured by the F1-score relative
  close to that expected when noise is present and before any gradient step on a benchmark
  of 16 patterns of a duration of one second. With learning, the network tolerates
  up to 25% bit-flip noise, and reaches $F_1$ scrores closer to the value expected
  from the noise level. These results demonstrate attractor-like retrieval dynamics
  consistent with hippocampal pattern completion or mesoscopic traveling waves in
  sensory areas. These results show that heterogeneous synaptic delays are an efficient
  and scalable substrate for working memory in SNNs, with direct implications for
  neuromorphic edge deployment.'
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/perrinet-26-neurocomp/
---
