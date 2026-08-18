---
title: A saccade-inspired approach to image classification using vision transformer
  attention maps
authors:
- Matthis Dallain
- Laurent Rodriguez
- Laurent U Perrinet
- Benoît Miramond
date: '2026-01-01'
publishDate: '2026-01-31T14:12:18.239393Z'
publication_types:
- preprint
links:
- name: arXiv
  url: https://arxiv.org/abs/2603.09613
tags:
- eye-movements
categories:
- Computational Neuroscience
- Computer Vision
- Education
- NeuroAI & Machine Learning
projects:
- ''
---

{{< figure src="saccade_selection.jpg" title="Saccade selection method: (a.) The input image of dimensionH× Wis split intoH16×Wnsized patches and embeddedinto token vectors. (b.) The tokens are passed through the DINO transformer, and attention flow from patch tokens to [CLS]token (white arrows) are extracted and reshaped into one attention map per attention-head. (c.) The multiple attention maps arefused into one by taking the maximum value across heads. (d.) The highest-attention locations define square regions(“saccades”) whose tokens are retained. (e.) Selected regions are revealed sequentially, and the image variants are classified by a pre-trained linear head." numbered="false" >}}
