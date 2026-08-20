---
title: From event-based computations to a bio-plausible Spiking Neural Network
date: 2021-10-14
lastmod: 2021-10-12 12:44:34+02:00
authors:
- Antoine Grimaldi
- Victor Boutin
- Sio-Hoi Ieng
- Ryad Benosman
- Laurent U Perrinet
abstract: 'We propose a neuromimetic online classifier for always-on digit recognition.
  To achieve this, we extend an existing event-based algorithm which introduced novel
  spatio-temporal features: time surfaces. Built from asynchronous events acquired
  by a neuromorphic camera, these time surfaces allow to code the local dynamics of
  a visual scene and create an efficient hierarchical event-based pattern recognition
  architecture. Its formalism was previously adapted in the computational neuroscience
  domain by showing it may be implemented using a Spiking Neural Network (SNN) of
  leaky integrate-and-fire models and Hebbian learning. Here, we add an online classification
  layer using a multinomial logistic regression which is compatible with a neural
  implementation. A decision can be taken at any arbitrary time by taking the argmax
  of the probability values associated to each class. We extend the parallel with
  computational neuroscience by demonstrating that this classification layer is also
  equivalent to a layer of spiking neurons with a Hebbian-like learning mechanism.
  Our method obtains state-of-the-art performances on the N-MNIST dataset and we show
  that it is robust to both spatial and temporal jitter. As a summary, we were able
  to develop a neuromimetic SNN model for online digit classification. We aim at pursuing
  the study of this architecture for natural scenes and hope to offer insights on
  the efficiency of neural computations, and in particular how mechanisms of decision-making
  may be formed.'
featured: false
draft: false
categories:
- Computational Neuroscience
- Education
- NeuroAI & Machine Learning
tags:
- neuromorphic-computing
- spiking-neural-networks
publication: '*Champalimaud Research Symposium (CRS21)*'
publication_types:
- inproceedings
url_video: https://www.youtube.com/watch?v=aIt5OAleMR8
image:
  focal_point: Smart
  preview_only: false
links:
- name: Venue
  url: https://symposium.fchampalimaud.science
grants:
- anr-anr
- aprovis-3-d
---
{{< youtube aIt5OAleMR8 >}}
* this proceedings paper follows up the poster presented at CBMI : {{< cite page="/publication/grimaldi-21-cbmi" view="4" >}}
* read the follow-up paper : {{< cite page="/publication/grimaldi-24" view="4" >}}
