---
abstract: 'Both biological and artificial neural networks inherently balance their
  performance with their operational cost, which balances their computational abilities.
  Typically, an efficient neuromorphic neural network is one that learns representations
  that reduce the redundancies and dimensionality of its input. This is for instance
  achieved in sparse coding, and sparse representations derived from natural images
  yield representations that are heterogeneous, both in their sampling of input features
  and in the variance of those features. Here, we investigated the connection between
  natural images'' structure, particularly oriented features, and their corresponding
  sparse codes. We showed that representations of input features scattered across
  multiple levels of variance substantially improve the sparseness and resilience
  of sparse codes, at the cost of reconstruction performance. This echoes the structure
  of the model''s input, allowing to account for the heterogeneously aleatoric structures
  of natural images. We demonstrate that learning kernel from natural images produces
  heterogeneity by balancing between approximate and dense representations, which
  improves all reconstruction metrics. Using a parametrized control of the kernels''
  heterogeneity used by a convolutional sparse coding algorithm, we show that heterogeneity
  emphasizes sparseness, while homogeneity improves representation granularity. In
  a broader context, these encoding strategy can serve as inputs to deep convolutional
  neural networks. We prove that such variance-encoded sparse image datasets enhance
  computational efficiency, emphasizing the benefits of kernel heterogeneity to leverage
  naturalistic and variant input structures and possible applications to improve the
  throughput of neuromorphic hardware. '
author_notes: []
authors:
- Hugo Ladret
- Christian Casanova
- Laurent U Perrinet
date: 2024-08-20
doi: 10.1088/2634-4386/ad5d0f
featured: false
image:
  caption: ''
  focal_point: Smart
  preview_only: false
links:
- name: URL
  url: https://iopscience.iop.org/article/10.1088/2634-4386/ad5d0f
- name: HAL
  url: https://hal.science/hal-04842588

publication: Neuromorphic Computing and Engineering
publication_short: ''
publication_types:
- article-journal
publishDate: '2024-01-09T10:17:44.040592Z'
title: Kernel Heterogeneity Improves Sparseness of Natural Images Representations
url_code: ''
url_dataset: https://figshare.com/articles/media/HD_natural_images_database_for_sparse_coding/24167265?file=42404574
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''
tags:
- neuromorphic-computing
- primary-visual-cortex
- sparse-coding
categories:
- Biological Neuroscience
- Computational Neuroscience
- Education
- NeuroAI & Machine Learning
- Outreach & Public Engagement
- Theoretical Neuroscience
- Visual Neuroscience
projects:
- ''
---


![Artboard](2024_ladret.gif)
* 5 minutes summary: https://hugoladret.github.io/publications/ladret_et_al_sparsecoding/
![](@laurentperrinet_1826586440773275942_tweetcapture.png)
* In a nutshell: We found that sparse coding of images (here extended in a convolutional framework) is improved when using kernels with heterogeneous precision in how they encode orientation information. This was confirmed by learning, but also by comparison with what is observed in the statistics of natural images and in our recordings from neurons in primary visual cortex.
{{< figure src="https://laurentperrinet.github.io/publication/ladret-23-iclr/fig_dicos.png" title="Epistemic uncertainty in a CSC dictionary improves both sparseness and reconstruction performance. **(a)** Elements from dictionaries with fixed epistemic uncertainty before (green) and after dictionary learning (orange). **(b)** Elements from a dictionary with heterogeneous epistemic uncertainty before (blue) and after dictionary learning (purple). **(c)** Elements from a dictionary learned from scratch. **(d)** Distribution of the sparseness (top) and Peak Signal-to-Noise Ratio (PSNR, right) of the five dictionaries, shown as a scatter plot for each of the 600 images of the dataset (center). Median values are shown as dashed line on the histograms." numbered="true" >}}
* open access: https://iopscience.iop.org/article/10.1088/2634-4386/ad5d0f
* This work is a followup of {{< cite page="/publication/ladret-23-iclr" view="4" >}}
* This theoretical work accompanies a similar study in neurophysiology: {{< cite page="/publication/ladret-23" view="4" >}}
