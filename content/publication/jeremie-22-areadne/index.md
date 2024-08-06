---
abstract: Visual search, that is, the simultaneous localization and detection of a
  visual target of interest, is a vital task. Applied to the case of natural scenes,
  searching for example to an animal (either a prey, a predator or a partner) constitutes
  a challenging problem due to large variability over numerous visual dimensions such
  as shape, pose, size, texture or position. Yet, biological visual systems are able
  to perform such detection efficiently in  briefly flashed scenes and in a very short
  amount of time.Deep convolutional neuronal networks (CNNs) were shown to be well
  fitted to the image classification task, providing with human (or even super-human)
  performance. Previous models also managed to solve the visual search task, by roughly
  dividing the image into sub-areas. This is at the cost, however, of computer-intensive
  parallel processing on relatively low-resolution image samples. Taking inspiration
  from natural vision systems, we develop here a model that builds over the anatomical
  visual processing pathways observed in mammals, namely the What and the Where pathways.
  It operates in two steps, one by selecting regions of interest, before knowing their
  actual visual content, through an ultra-fast/low resolution analysis of the full
  visual field, and the second providing a detailed categorization over the detailed
  foveal selected region attained with a saccade.
authors:
- Jean-Nicolas Jérémie
- Emmanuel Daucé
- Laurent U Perrinet
categories: []
date: 2022-06-29
draft: false
featured: false
grants:
- aprovis3D
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2022-05-20 13:42:38+02:00
links:
- name: Venue
  url: https://areadne.org/
projects: []
publication: '*Proceedings of AREADNE*'
publication_types:
- inproceedings
publishDate: '2022-06-16T11:51:41.890310Z'
subtitle: ''
tags:
- efficient coding
- localization
- online classification
- ultra-fast categorization
- visual search
title: Ultra-rapid visual search in natural images using active deep learning
---

* This work extends to natural scenes a previous work on visual search on a simplified task formulated in  {{< cite page="/publication/dauce-20" view="4" >}}
* It is based on a first work on transfer learning and its application to a natural task : {{< cite page="/publication/jeremie-23-ultra-fast-cat" view="4" >}}
* in particular, we found retinotopic mapping to be adapted to that extension : {{< cite page="/talk/2022-06-19-neuro-vision-retinotopic" view="4" >}}
* for a follow-up, check out  {{< cite page="/publication/jeremie-22-fens" view="4" >}}
