---
abstract: 'We propose a neuromimetic  architecture able to perform online pattern
  recognition. To achieve this, we extended the existing event-based algorithm from
  Lagorce et al (2017) which introduced novel spatio-temporal features: time-surfaces.
  Built from asynchronous events acquired by a neuromorphic camera, these time surfaces
  allow to code the local dynamics of a visual scene and to create an efficient hierarchical
  event-based pattern recognition architecture. Inspired by biological findings and
  the efficient coding hypothesis, our main contribution is to integrate homeostatic
  regulation to the Hebbian learning rule. Indeed, in order to be optimally informative,
  average neural activity within a layer should be equally balanced across neurons.
  We used that principle to regularize neurons within the same layer by setting a
  gain depending on their past activity and such that they emit spikes with balanced
  firing rates. The efficiency of this technique was first demonstrated through a
  robust improvement in spatio-temporal patterns which were learned during the training
  phase. We validated classification performance with the widely used N-MNIST dataset
  reaching 87.3% accuracy with homeostasis compared to 72.5% accuracy without homeostasis.
  Finally, by studying the impact of input jitter on classification highlights resilience
  of this method. We expect to extend this fully event-driven approach to more naturalistic
  tasks, notably for ultra-fast object categorization.'
authors:
- Antoine Grimaldi
- Victor Boutin
- Sio-Hoi Ieng
- Laurent U Perrinet
- Ryad Benosman
date: 2021-02-26
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
publication: '*Computational and Systems Neuroscience (CoSyNe) 2021*'
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
url_pdf: https://laurentperrinet.github.io/publication/grimaldi-21-cosyne/
---

{{< tweet 1364962423120265218 >}}
{{< figure src="poster.png" width="100%" >}}
* see the poster online on the [Hopin platform](https://app.hopin.com/events/cosyne-2021/expo/377631)
* see a follow-up in: {{< cite page="/publication/grimaldi-21-cbmi" view="4" >}}
* Antoine Grimaldi and Laurent Perrinet received funding from the European Union ERA-NET CHIST-ERA 2018 research and innovation program under grant agreement No ANR-19-CHR3-0008-03.
