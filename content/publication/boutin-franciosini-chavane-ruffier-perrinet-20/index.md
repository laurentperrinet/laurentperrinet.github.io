---
abstract: Both neurophysiological and psychophysical experiments have pointed out
  the crucial role of recurrent and feedback connections to process context-dependent
  information in the early visual cortex. While numerous models have accounted for
  feedback effects at either neural or representational level, none of them were able
  to bind those two levels of analysis. Is it possible to describe feedback effects
  at both levels using the same model? We answer this question by combining Predictive
  Coding (PC) and Sparse Coding (SC) into a hierarchical and convolutional framework.
  In this Sparse Deep Predictive Coding (SDPC) model, the SC component models the
  internal recurrent processing within each layer, and the PC component describes
  the interactions between layers using feedforward and feedback connections. Here,
  we train a 2-layered SDPC on two different databases of images, and we interpret
  it as a model of the early visual system (V1~&~V2). We first demonstrate that once
  the training has converged, SDPC exhibits oriented and localized receptive fields
  in V1 and more complex features in V2. Second, we analyze the effects of feedback
  on the neural organization beyond the classical receptive field of V1 neurons using
  interaction maps. These maps are similar to association fields and reflect the Gestalt
  principle of good continuation. We demonstrate that feedback signals reorganize
  interaction maps and modulate neural activity to promote contour integration. Third,
  we demonstrate at the representational level that the SDPC feedback connections
  are able to overcome noise in input images. Therefore, the SDPC captures the association
  field principle at the neural level which results in better disambiguation of blurred
  images at the representational level.
authors:
- Victor Boutin
- Angelo Franciosini
- Frédéric Y Chavane
- Franck Ruffier
- Laurent U Perrinet
date: 2020-05-12
featured: false
grants:
- doc-2-amu
- phd-icn
- mesocentre
projects: []
publication: '*PLoS Computational Biology*'
publication_types:
- '2'
tags:
- sparse coding
title: Sparse Deep Predictive Coding captures contour integration capabilities of
  the early visual system
url_pdf: https://arxiv.org/abs/1902.07651
url_preprint: https://arxiv.org/abs/1902.07651
---

One often compares biological vision to a camera-like system where an image would be processed according to a sequence of successive transformations. In particular, this “feedforward” view is prevalent in models of visual processing such as deep learning. However, neuroscientists have long stressed that more complex information flow is necessary to reach natural vision efficiency. In particular, recurrent and feedback connections in the visual cortex allow to integrate contextual information in our representation of visual stimuli. These modulations have been observed both at the low-level of neural activity and at the higher level of perception. In this study, we present an architecture that describes biological vision at both levels of analysis. It suggests that the brain uses feedforward and feedback connections to compare the sensory stimulus with its own internal representation. In contrast to classical deep learning approaches, we show that our model learns interpretable features. Moreover, we demonstrate that feedback signals modulate neural activity to promote good continuity of contours. Finally, the same model can disambiguate images corrupted by noise. To the best of our knowledge, this is the first time that the same model describes the effect of recurrent and feedback modulations at both neural and representational levels.

* more about the role of top-down connections: {{< cite page="/publication/boutin-franciosini-ruffier-perrinet-20-feedback" view="4" >}}
* presented during this [talk]({{< ref "/talk/2019-03-25-hdr-robin-baures/index.md" >}})
