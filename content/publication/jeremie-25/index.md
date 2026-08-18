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
publication: '*Vision*'
publication_types:
- article-journal
publishDate: '2024-08-06T15:13:44.587984Z'
title: Foveated Retinotopy Improves Classification and Localization in CNNs
tags:
- bayesian-modelling
- eye-movements
- foveated-vision
- log-polar-mapping
- primary-visual-cortex
- retinotopy
categories:
- Behavioural Neuroscience
- Biological Neuroscience
- Computer Vision
- Education
- NeuroAI & Machine Learning
- Theoretical Neuroscience
- Visual Neuroscience
projects:
- ''
---

{{< figure src="graphical.png" title="*Foveated Retinotopy in CNNs.* We represent Left an input image and how it is transformed by foveated retinotopy. We show below a representative reconstruction showing that it also acts as a cortical zoom on the image around the point of fixation. The transformed image is then fed to the ResNet deep learning architecture." >}}

From falcons spotting prey to humans recognizing faces, the ability to rapidly process visual information depends on a foveated retinal organization that provides high-acuity central vision while preserving low-resolution peripheral vision. This organization is conserved along early visual pathways, yet remains under-explored in machine learning. Here, we examine the impact of embedding a foveated retinotopic transformation as a preprocessing layer on convolutional neural networks (CNNs) for image classification. By applying a log-polar mapping to off-the-shelf models and retraining them, we achieve comparable accuracy while improving robustness to scale and rotation. We demonstrate that this architecture is highly sensitive to shifts in the fixation point and that this sensitivity provides an effective proxy for defining saliency maps that facilitate object localization. Our results demonstrate that foveated retinotopy encodes prior geometric knowledge, providing a solution for visual searches and a meaningful classification robustness and localization trade-off. These findings provides a proof of concept in order to connect principles of biological vision with artificial networks, suggesting new, robust and efficient approaches for computer vision systems.

{{< figure src="grid.gif" title="*Foveated Retinotopy simulated by a log-polar map.* We represent Left an input image with some geometrical objects and how it is transformed by the log-polar representation that implements foveated retinotopy. This shows that a rotation amounts to a translation on the polar axis (abscissa) and a zoom to a translation on the ordinates. We show right a representative reconstructionshowing that it also acts as a cortical zoom on the image around the point of fixation." >}}

## links
* https://neuromatch.social/@laurentperrinet/116330144691046827
* https://bsky.app/profile/laurentperrinet.bsky.social/post/3migysn4bg22b
* [Linkedin](https://www.linkedin.com/feed/update/urn:li:ugcPost:7405576163546255360?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7405576163546255360%2C7445129580430147584%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287445129580430147584%2Curn%3Ali%3AugcPost%3A7405576163546255360%29)