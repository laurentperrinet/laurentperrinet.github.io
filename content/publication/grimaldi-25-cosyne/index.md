--- 
title: Robust Unsupervised Learning of Spike Patterns with Optimal Transport Theory
authors:
- Antoine Grimaldi
- Matthieu Gilson
- Laurent U Perrinet
- Andrea Alamia
- Boris Sotomayor-Gomez
- Martin Vinck
date: '2025-03-28'
publishDate: '2025-03-27T16:16:39.715951Z'
publication_types:
- paper-conference
publication: '*Computational and Systems Neuroscience (Cosyne)  2025*'
abstract: Temporal sequences are an important feature of neural information processing
  in biology. Neurons can fire a spike with millisecond precision, and, at the network
  level, repetitions of spatiotemporal spike patterns are observed in neurobiological
  data. However, methods for detecting precise temporal patterns in neural activity
  suffer from high computational complexity and poor robustness to noise, and quantitative
  detection of these repetitive patterns remains an open problem. Here, we propose
  a new method to extract spike patterns embedded in raster plots using a 1D convolutional
  autoencoder with the Earth Mover’s Distance (EMD) as a loss function. Importantly,
  the properties of the EMD make the method suitable for spike-based distributions,
  easy to compute, and robust to noise. Through gradient descent, the autoencoder
  is trained to minimize the EMD between the input and its reconstruction. We then
  expect the weight matrices to learn the repeating spike patterns present in the
  data. We validate our method on synthetically generated raster plots and compare
  its performance with an autoencoder trained using the Mean Squared Error (MSE) as
  a loss function. We show that the method using the EMD performs better at detecting
  the occurrence of the spike patterns, while the method using the MSE is better at
  capturing the underlying distributions used to generate the spikes. Finally, we
  propose to train the autoencoder iteratively by sequentially combining the EMD and
  the MSE losses. This sequential approach outperforms the widely used seqNMF method
  in terms of robustness to various types of noise, speed and stability. Overall,
  our method provides a novel approach to reliably extract repetitive temporal spike
  sequences, and can be readily generalized to other sequence detection applications.
links:
- name: URL
  url: https://www.world-wide.org/cosyne-25/robust-unsupervised-learning-spike-fa46f105/
categories:
- Computational Neuroscience
- Education
- NeuroAI & Machine Learning
---

