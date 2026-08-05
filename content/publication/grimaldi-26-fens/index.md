---
title: Optimal Transport Theory to extract Spiking Motifs
authors:
- Antoine Grimaldi
- Matthieu Gilson
- Laurent U Perrinet
- Andrea Alamia
- Boris Sotomayor-Gomez
- Martin Vinck
date: '2026-07-07'
publishDate: '2026-06-29T10:24:36.718992Z'
publication_types:
- paper-conference
publication: '*Proceedings of the FENS Forum 2026*'
abstract: Whether cortical neurons encode information through firing rates or precise
  spike timing remains a central question in neuroscience. Although spike timing can
  theoretically convey more information than firing rates, its utility is often challenged
  by neural variability or synaptic noise. For these reasons, precisely estimating
  spike timing can be a challenging task. Here, we investigate the use of the Earth
  Mover’s Distance (EMD), a metric from optimal transport theory, to extract spatiotemporal
  spiking patterns with a single-layer autoencoder (AE). We compare AEs trained with
  the EMD or the mean squared error (MSE) on synthetic spike trains and on large-scale
  neural recordings from the Allen Institute. Using synthetic data, we demonstrate
  that EMD-based training is markedly more robust to temporal jitter and time warping,
  whereas the MSE is less sensitive to additive noise and probabilistic participation
  of the neurons. When many samples are available, MSE-trained AEs better capture
  temporal sequences along with spike-timing precision. However, EMD-trained AEs reliably
  estimate the averaged spike timings with relatively few samples, which is often
  the case in real-world experimental conditions. Applied to mouse visual cortex recordings,
  the EMD enables the extraction of temporal sequences that discriminate visual stimuli
  more effectively than the MSE, and capture different information than what can be
  achieved using averaged firing rates alone. Altogether, these results demonstrate
  that optimal transport theory provides an efficient tool for uncovering spatiotemporal
  structure in spiking activity.
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/grimaldi-26-fens/
- name: FENS
  url: https://fens2026.abstractserver.com/program/#/details/presentations/3594
tags:
- optimal-transport
---





