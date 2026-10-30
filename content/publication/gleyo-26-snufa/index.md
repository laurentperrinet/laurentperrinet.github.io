---
title: Bio-plausible statistical regularizer for spiking LeJEPA
authors:
- Alexis Gleyo
- Laurent U Perrinet
date: 2026-11-01
publishDate: '2026-10-19T09:35:54.426161Z'
publication_types:
- paper-conference
publication: '*Flash talk at SNUFA 2026 online workshop (5-6 Nov 2026)*'
abstract: Joint Embedding Predictive Architectures (JEPA) offer a promising path toward
  self-supervised learning, but their application to SNNs is hindered by significant
  challenges. Training heuristics like stop-gradient and Exponential Moving Averages
  (EMA) are often unstable and provide no mathematical guarantee against representation
  collapse. This problem is amplified by the training unstability of SNNs. Some JEPA
  models like VICReg and LeJEPA use statistical regularizers to prevent collapse and
  optimize the representation distribution for downstream tasks but those methods
  are designed for continuous representations and are not directly applicable to the
  discrete, event-based nature of SNNs. To address this, we introduce a novel framework
  for a bio-plausible spiking JEPA. We derive the theoretically optimal target distribution
  for latent representations up to the second-order moment, and enforce it using only
  locally available statistics. Using a binary latent space over a single timestep,
  our model achieves performance on-par with comparable continuous models on the ImageNette
  benchmark. Future work will focus on scaling up experiments to larger datasets and
  more complex architectures.
tags:
- neuromorphic-computing
- spiking-neural-networks
- temporal-coding
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/gleyo-26-snufa/
---
