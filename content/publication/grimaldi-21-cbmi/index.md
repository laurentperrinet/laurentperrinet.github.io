---
abstract: 'We propose a neuromimetic architecture able to perform pattern recognition.
  To achieve this, we extended the existing event-based algorithm from Lagorce et
  al (2017) which introduced novel spatio-temporal features: time surfaces. Built
  from asynchronous events acquired by a neuromorphic camera, these time surfaces
  allow to code the local dynamics of a visual scene and create an efficient hierarchical
  event-based pattern recognition architecture. Inspired by biological findings and
  the efficient coding hypothesis, our main contribution is to integrate homeostatic
  regulation into the Hebbian learning rule. Indeed, in order to be optimally informative,
  average neural activity within a layer should be equally balanced across neurons.
  We used that principle to regularize neurons within the same layer by setting a
  gain depending on their past activity and such that they emit spikes with balanced
  firing rates. The efficiency of this technique was first demonstrated through a
  robust improvement in spatio-temporal patterns which were learnt during the training
  phase. In order to compare with state-of-the-art methods, we replicated past results
  on the same dataset as Lagorce et al (2017) and extended results in this study to
  the widely used N-MNIST dataset.'
authors:
- Antoine Grimaldi
- Victor Boutin
- Sio-Hoi Ieng
- Laurent U Perrinet
- Ryad Benosman
categories: []
date: 2021-04-16
draft: false
featured: false
grants:
- aprovis3D
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2021-02-25 17:01:28+01:00
projects: []
publication: '*Content-Based Multimedia Indexing (CBMI) 2021*'
publication_types:
- '1'
subtitle: ''
tags:
- efficient coding
- event-based vision
- homeostasis
- neuromorphic hardware
- online classification
title: A robust bio-inspired approach to event-driven object recognition
url_pdf: https://laurentperrinet.github.io/publication/grimaldi-21-cbmi/
---

{{< tweet 1364962423120265218 >}}
{{< figure src="poster.png" width="100%" >}}
* see the poster online on the [Hopin platform](https://app.hopin.com/events/cosyne-2021/expo/377631)
* Antoine Grimaldi and Laurent Perrinet received funding from the European Union ERA-NET CHIST-ERA 2018 research and innovation program under grant agreement No ANR-19-CHR3-0008-03.
