---
title: A saccade-inspired approach to image classification using vision transformer
  attention maps
date: 2026-01-01
publishDate: '2026-01-31T14:12:18.239393Z'
authors:
- Matthis Dallain
- Laurent Rodriguez
- Laurent U Perrinet
- Benoît Miramond
categories:
- Computational Neuroscience
- Computer Vision
- NeuroAI & Machine Learning
tags:
- eye-movements
publication_types:
- preprint
doi: 10.48550/arXiv.2603.09613
links:
- name: arXiv
  url: https://arxiv.org/abs/2603.09613
- name: URL
  url: http://arxiv.org/abs/2603.09613
abstract: Human vision achieves remarkable perceptual performance while operating
  under strict metabolic constraints. A key ingredient is the selective attention
  mechanism, driven by rapid saccadic eye movements that constantly reposition the
  high-resolution fovea onto task-relevant locations, unlike conventional AI systems
  that process entire images with equal emphasis. Our work aims to draw inspiration
  from the human visual system to create smarter, more efficient image processing
  models. Using DINO, a self-supervised Vision Transformer that produces attention
  maps strikingly similar to human gaze patterns, we explore a saccade inspired method
  to focus the processing of information on key regions in visual space. To do so,
  we use the ImageNet dataset in a standard classification task and measure how each
  successive saccade affects the model's class scores. This selective-processing strategy
  preserves most of the full-image classification performance and can even outperform
  it in certain cases. By benchmarking against established saliency models built for
  human gaze prediction, we demonstrate that DINO provides superior fixation guidance
  for selecting informative regions. These findings highlight Vision Transformer attention
  as a promising basis for biologically inspired active vision and open new directions
  for efficient, neuromorphic visual processing.
---
{{< figure src="saccade_selection.jpg" title="Saccade selection method: (a.) The input image of dimensionH× Wis split intoH16×Wnsized patches and embeddedinto token vectors. (b.) The tokens are passed through the DINO transformer, and attention flow from patch tokens to [CLS]token (white arrows) are extracted and reshaped into one attention map per attention-head. (c.) The multiple attention maps arefused into one by taking the maximum value across heads. (d.) The highest-attention locations define square regions(“saccades”) whose tokens are retained. (e.) Selected regions are revealed sequentially, and the image variants are classified by a pre-trained linear head." alt="Saccade selection method using vision transformer attention maps." numbered="false" >}}
