---
abstract: One core advantage of sparse representations is the efficient coding of
  complex signals using compact codes. For instance, it allows for the representation
  of any image as a combination of few elements drawn from a large dictionary of basis
  functions. In the context of the efficient processing of natural images, we propose
  here that such codes can be optimized by designing proper homeostatic rules between
  the elements of the dictionary. Indeed, a common design for unsupervised learning
  rules relies on a gradient descent over a cost measuring representation quality
  with respect to sparseness. The sparseness constraint introduces a competition which
  can be optimized by ensuring that each item in the dictionary is selected as often
  as others. We implemented this rule by introducing a gain normalization similar
  to what is observed in a balanced neural network. We validated this theoretical
  insight by challenging different sparse coding algorithms with the same learning
  rule but with or without homeostasis. The different sparse coding algorithms were
  chosen for their efficiency and generality. They include least-angle regression,
  orthogonal matching pursuit and basis pursuit. Simulations show that for a given
  homeostasis rule, gradient descent performed similarly the learning of a dataset
  of image patches. While the coding algorithm did not matter much, including homeostasis
  changed qualitatively the learned features. In particular, homeostasis results in
  a more homogeneous set of orientation selective filters, which is closer to what
  is found in the visual cortex of mammals. To further validate these results, we
  applied this algorithm to the optimization of a visual system embedded in an aerial
  robot. As a consequence, this biologically-inspired learning rule demonstrates that
  principles observed in neural computations can help improve real-life machine learning
  algorithms.
authors:
- Victor Boutin
- Franck Ruffier
- Laurent U Perrinet
code: https://github.com/laurentperrinet/BoutinRuffierPerrinet17spars
date: 2017-01-01
featured: false
grants:
- doc-2-amu
projects: []
publication: '*NeuroFrance 2017, International Conference from the Société des Neurosciences,
  Bordeaux, France*'
publication_types:
- '1'
publishDate: '2019-09-17'
tags:
- sparse coding
title: Efficient learning of sparse image representations using homeostatic regulation
---













* This work is a followup of [Perrinet, 2010, Neural Computation]({{< ref "/publication/perrinet-10-shl" >}})
* the [poster (PDF)](https://github.com/laurentperrinet/BoutinRuffierPerrinet17spars/raw/master/docs/BoutinRuffierPerrinet17neurofrance.pdf) will be presented Thursday, May 18 @ [NeuroFrance, Bordeaux](http://www.professionalabstracts.com/sn2017/programme-sn2017.pdf).
* see a follow-up publication on [BoutinRuffierPerrinet17spars]({{< ref "/publication/boutin-ruffier-perrinet-17-spars" >}})
