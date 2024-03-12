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
date: 2021-06-24
doi: 10.1109/CBMI50038.2021.9461901
draft: false
featured: false
grants:
- aprovis3D
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2021-04-20 17:01:28+01:00
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
title: A homeostatic gain control mechanism to improve event-driven object recognition
url_pdf: https://laurentperrinet.github.io/publication/grimaldi-21-cbmi/
url_preprint: https://hal.archives-ouvertes.fr/hal-03336554
url_video: https://www.youtube.com/watch?v=KxX4pZKexCo&t=3335s
---

* was presented at the [Bio-inspired circuits, systems and algorithms for multimedia](https://cbmi2021.univ-lille.fr/call-for-contributions#callforpapersspecialbioinspired) special session of the [Content-Based Multimedia Indexing (CBMI) 2021](https://cbmi2021.univ-lille.fr/) conference that you can [watch on Youtube](https://www.youtube.com/watch?v=KxX4pZKexCo&t=3335s).
* this proceedings paper follows up he poster presented in : {{< cite page="/publication/grimaldi-21-cosyne" view="4" >}}
* this proceedings paper was followed by the poster presented at CRS : {{< cite page="/publication/grimaldi-21-crs" view="4" >}}
* read the follow-up paper : {{< cite page="/publication/grimaldi-23" view="4" >}}
* Antoine Grimaldi and Laurent Perrinet received funding from the European Union ERA-NET CHIST-ERA 2018 research and innovation program under grant agreement No ANR-19-CHR3-0008-03.
