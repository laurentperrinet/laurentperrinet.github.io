---
abstract: 'We propose a neuromimetic architecture able to perform always-on pattern
  recognition. To achieve this, we extended an existing event-based algorithm [1],
  which introduced novel spatio-temporal features as a Hierarchy Of Time-Surfaces
  (HOTS). Built from asynchronous events acquired by a neuromorphic camera, these
  time surfaces allow to code the local dynamics of a visual scene and to create an
  efficient event-based pattern recognition architecture. Inspired by neuroscience,
  we extended this method to increase its performance. Our first contribution was
  to add a homeostatic gain control on the activity of neurons to improve the learning
  of spatio-temporal patterns [2]. A second contribution is to draw an analogy between
  the HOTS algorithm and Spiking Neural Networks (SNN). Following that analogy, our
  last contribution is to modify the classification layer and remodel the offline
  pattern categorization method previously used into an online and event-driven one.
  This classifier uses the spiking output of the network to define novel time surfaces
  and we then perform online classification with a neuromimetic implementation of
  a multinomial logistic regression. Not only do these improvements increase consistently
  the performances of the network, they also make this event-driven pattern recognition
  algorithm online and bio-realistic. Results were validated on different datasets:
  DVS barrel [3], Poker-DVS [4] and N-MNIST [5]. We foresee to develop the SNN version
  of the method and to extend this fully event-driven approach to more naturalistic
  tasks, notably for always-on, ultra-fast object categorization. '
authors:
- Antoine Grimaldi
- Victor Boutin
- Sio-Hoi Ieng
- Ryad Benosman
- Laurent U Perrinet
date: 2024-10-01
doi: 10.1016/j.neunet.2024.106415
draft: false
featured: false
image:
  caption: ''
  focal_point: Smart
  preview_only: false
lastmod: 2022-01-13 15:27:10+01:00
links:
- name: Press
  url: https://neuromatch.social/@laurentperrinet/113119379508706565
- name: Hal
  url: https://hal.science/hal-04694717
- name: Code
  url: https://github.com/AntoineGrimaldi/hotsline
- name: URL
  url: https://laurentperrinet.github.io/publication/grimaldi-24/

publication: Neural Networks
publication_types:
- article-journal
subtitle: ''
title: A Robust Event-Driven Approach to Always-on Object Recognition
tags:
- event-based-vision
- homeostasis
- neuromorphic-computing
- spiking-neural-networks
categories:
- NeuroAI & Machine Learning
projects:
- aprovis3D
---

Main contributions:
- Builds an adaptive, back to  back event-based pattern recognition architecture, inspired by neuroscience and capable of always-on decision, that is, that the decision can be taken it can be needed,
{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-24/hots.png" title="The HOTS architecture." width="100%" >}}
- Extends the HOTS algorithm to increase its performance by adding a homeostatic gain control on the activity of neurons to improve the learning of spatio-temporal patterns, we prove an analogy with off-the-shelf LIF spiking neurons,
<img src="https://laurentperrinet.github.io/publication/grimaldi-24/DVSGesture_arm-roll.webp"  width="33%"/><img src="https://laurentperrinet.github.io/publication/grimaldi-24/DVSGesture_hand-clap.webp"  width="33%"/><img src="https://laurentperrinet.github.io/publication/grimaldi-24/DVSGesture_air-guitar.webp"  width="33%"/>
- Quantitative results assessing the role of homeostasis in the learning of spatio-temporal patterns and the performance of the network on different datasets: Poker-DVS, N-MNIST and DVS Gesture for different precisions of the temporal and spatial information.
{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-24/gesture_online.png" title="Performance of the algorithm on the DVSgesture dataset. For this gesture recognition task, the online HOTS accuracy remains close to the chance level for about 100 events. More evidence needs to be accumulated, and then the accuracy increases monotonically, outperforming the previous method after about 10.000 events (at an average of 9.3% of the number of events in the sample)." width="90%" >}}
