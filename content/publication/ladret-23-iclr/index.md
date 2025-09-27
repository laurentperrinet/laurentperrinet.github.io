---
abstract: Aleatoric uncertainty characterizes the variability of features found in
  natural images, and echoes the epistemic uncertainty ubiquitously found in computer
  vision models. We explore this ''uncertainty in, uncertainty out'' relationship
  by generating convolutional sparse coding dictionaries with parametric epistemic
  uncertainty. This improves sparseness, resilience and reconstruction of natural
  images by providing the model a way to explicitly represent the aleatoric uncertainty
  of its input. We demonstrate how hierarchical processing can make use of this scheme
  by training a deep convolutional neural network to classify a sparse-coded CIFAR10
  dataset, showing that encoding uncertainty in a sparse code is as efficient as using
  conventional images, with additional beneficial computational properties. Overall,
  this work empirically demonstrates the advantage of partitioning epistemic uncertainty
  in sparse coding algorithms.
authors:
- Hugo Ladret
- Laurent U Perrinet
categories: []
date: 2023-05-05
draft: false
featured: false
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2023-04-07 12:45:44+02:00
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/ladret-23-iclr/

publication: '*ICLR 2023 SNN Workshop*'
publication_types:
- inproceedings
publishDate: '2023-04-07T10:45:44.753196Z'
subtitle: ''
tags:
- coding
- convolutional
- images
- natural
- sparse
- uncertainty
title: Convolutional Sparse Coding is improved by heterogeneous uncertainty modeling
---

* Accepted paper (poster) at the [ICLR 2023 Workshop on
Sparsity in Neural Networks](https://www.sparseneural.net/accepted-papers):
 * the focus of the WS is on "On practical limitations and tradeoffs between sustainability and efficiency" in Kigali, Rwanda / May 5th 2023
 * reviews will be made public on https://openreview.net/forum?id=tgr8FEcl28M
 
* In a nutshell: We found that sparse coding of images (here extended in a convolutional framework) is improved when using kernels with heterogeneous precision in how they encode orientation information. This was confirmed by learning, but also by comparison with what is observed in the statistics of natural images and in our recordings from neurons in primary visual cortex.
{{< figure src="fig_dicos.png" title="Epistemic uncertainty in a CSC dictionary improves both sparseness and reconstruction performance. **(a)** Elements from dictionaries with fixed epistemic uncertainty before (green) and after dictionary learning (orange). **(b)** Elements from a dictionary with heterogeneous epistemic uncertainty before (blue) and after dictionary learning (purple). **(c)** Elements from a dictionary learned from scratch. **(d)** Distribution of the sparseness (top) and Peak Signal-to-Noise Ratio (PSNR, right) of the five dictionaries, shown as a scatter plot for each of the 600 images of the dataset (center). Median values are shown as dashed line on the histograms." numbered="true" >}}
* This theoretical work accompanies a similar study in neurophysiology: {{< cite page="/publication/ladret-23" view="card" >}}
* This work was extended in {{< cite page="/publication/ladret-24-sparse" view="card" >}}
