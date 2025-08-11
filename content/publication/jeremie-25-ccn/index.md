---
title: Integrating the What and Where Visual Pathways to Improve CNN Categorisation
authors:
- Jean-Nicolas Jérémie
- Emmanuel Daucé
- Laurent U Perrinet
date: '2025-01-01'
publishDate: '2025-06-03T07:46:10.985387Z'
publication_types:
- paper-conference
publication: '*Computational Cognitive Neuroscience Society Meeting (CCN) 2025*'
abstract: "Convolutional Neural Networks (CNNs) have been widely used for categorisation
  tasks over the past decades. Many studies have attempted to improve their performance
  by increasing model complexity, adding parameters, or adopting alternative architectures
  such as transformers, which excel at large-scale benchmarks. However, these approaches
  often come at a high computational cost. We take a different approach, prioritizing
  ecological plausibility to achieve high accuracy with minimal computational cost.
  We focus on visual search --- a task requiring both localisation and categorisation
  of a target object in natural scenes. Our work is inspired by the organisation of
  the primate visual system, which processes visual information through two distinct
  pathways: the ventral ''What'' pathway, responsible for object recognition, and
  the dorsal ''Where'' pathway, specialized in spatial localisation. Using this principle,
  we aim to evaluate the validity of a ''what/where'' approach, capable of selectively
  processing only the relevant areas of the visual scene with respect to the classification
  task. This selection relies on the implementation of a visual sensor (''retina'') 
  that samples only part of the image, coupled with a map representing the regions
  of the image. This map, referred to as a ''likelihood map'' is based on the probability
  of correctly identifying the target label. Depending on the case, it can be guided
  (resp not guided) by the target label, similar to the Grad-CAM  (resp DFF). In both
  scenarios, we show improved classification performance when the eye shifts toward
  the region of interest, outperforming previously mentioned methods. Surprisingly,
  the gain in classification accuracy is offset by a reduction in the precision of
  object localisation within the scene. Beyond its computational benefits, this What-Where
  framework serves as an experimental tool to further investigate the neural mechanisms
  underlying visual processing."
tags:
- Neuromorphic
- Convolutional Neuronal Networks
- Deep learning
- Localisation
- Categorisation
- ImageNet
- Visual search
- NeuroAI
projects:
- anr-anr
links:
- name: URL
  url: https://laurentperrinet.github.io/publication/jeremie-25-ccn
- name: Abstract
  url: https://2025.ccneuro.org/abstract_pdf/Jeremie_2025_Unravelling_relationship_location_categorisation_improves_convolutional.pdf
---

* What: Poster A145
* When: Tuesday, August 12, 1:30 – 4:30 pm,
* WHere: CCN 2025 conference venue, de Brug & E‑Hall