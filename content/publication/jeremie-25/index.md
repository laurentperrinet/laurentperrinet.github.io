---
authors:
- Jean-Nicolas Jérémie
- Emmanuel Daucé
- Laurent U Perrinet
date: 2026-02-23
doi: 10.3390/vision10020017
grants:
- anr-anr
links:
- name: URL
  url: https://www.mdpi.com/2411-5150/10/2/17
- name: arXiv
  url: https://arxiv.org/abs/2402.15480
publication: 'Vision'
publication_types:
- article-journal
publishDate: '2024-08-06T15:13:44.587984Z'
tags:
- Convolutional Neural Networks
- Foveated vision
- Transfer learning
- visual categorization
title: Foveated Retinotopy Improves Classification and Localization in CNNs
---



From falcons spotting prey to humans recognizing faces, the ability to rapidly process visual information depends on a foveated retinal organization that provides high-acuity central vision while preserving low-resolution peripheral vision. This organization is conserved along early visual pathways, yet remains under-explored in machine learning. Here, we examine the impact of embedding a foveated retinotopic transformation as a preprocessing layer on convolutional neural networks (CNNs) for image classification. By applying a log-polar mapping to off-the-shelf models and retraining them, we achieve comparable accuracy while improving robustness to scale and rotation. We demonstrate that this architecture is highly sensitive to shifts in the fixation point and that this sensitivity provides an effective proxy for defining saliency maps that facilitate object localization. Our results demonstrate that foveated retinotopy encodes prior geometric knowledge, providing a solution for visual searches and a meaningful classification robustness and localization trade-off. These findings provides a proof of concept in order to connect principles of biological vision with artificial networks, suggesting new, robust and efficient approaches for computer vision systems.


{{< figure src="grid.gif" title="*Foveated Retinotopy simulated by a log-polar map.* We represent Left an input image with some geometrical objects and how it is transformed by the log-polar representation that implements foveated retinotopy. This shows that a rotation amounts to a translation on the polar axis (bscissa) and a zoom to a translation on the ordinates. We show right a representative reconstructionshowing that it also acts as a cortoical zoom on the image around the point of fixation." >}}
