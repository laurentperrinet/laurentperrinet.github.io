---
abstract: Choosing an appropriate set of stimuli is essential to characterize the
  response of a sensory system to a particular functional dimension, such as the eye
  movement following the motion of a visual scene. Here, we describe a framework to
  generate random texture movies with controlled information content, i.e., Motion
  Clouds. These stimuli are defined using a generative model that is based on controlled
  experimental parametrization. We show that Motion Clouds correspond to dense mixing
  of localized moving gratings with random positions. Their global envelope is similar
  to natural-like stimulation with an approximate full-field translation corresponding
  to a retinal slip. We describe the construction of these stimuli mathematically
  and propose an open-source Python-based implementation. Examples of the use of this
  framework are shown. We also propose extensions to other modalities such as color
  vision, touch, and audition.
authors:
- Paula S Leon
- Ivo Vanzetta
- Guillaume S Masson
- Laurent U Perrinet
date: 2012-03-14
doi: 10.1152/jn.00737.2011
featured: false
projects:
- motion-clouds
links:
- name: HAL
  url: https://hal.science/hal-00726828
- name: URL
  url: https://doi.org/10.1152/jn.00737.2011
- name: arXiv
  url: https://arxiv.org/abs/1208.6467
- name: Supp
  url: https://neuralensemble.org/MotionClouds/ms/MotionClouds_Supplementary.pdf

publication: '*Journal of Neurophysiology*'
publication_types:
- article-journal
tags:
- log-gabor
- motion-clouds
title: 'Motion Clouds: Model-based stimulus synthesis of natural-like random textures
  for the study of motion perception'
categories: ["Computational Neuroscience"]
---
![header](sanz-12.png)
**MotionClouds** are random dynamic stimuli optimized to study motion perception.
* [Web-site](https://neuralensemble.github.io/MotionClouds/)
* [Source code](https://github.com/NeuralEnsemble/MotionClouds) using {{< icon name="python" pack="fab" >}} Python.
* 37 citations on [Google Scholar](https://scholar.google.com/scholar?cluster=3286688289699014452&hl=fr&as_sdt=7,39) (last updated 22/10/2021)
* [Supplementary information](https://neuralensemble.org/MotionClouds/ms/MotionClouds_Supplementary.pdf)
* Follow-up paper {{< cite page="/publication/vacher-16" view="4" >}} {{< cite page="/publication/vacher-15-nips" view="4" >}}
* This library was notably used in the following paper {{< cite page="/publication/simoncini-12" view="4" >}}

{{< figure src="featured.png" width="80%" title="**Figure 4** Broadband vs. narrowband stimuli. From A through B to C, the frequency bandwidth Bf increases, while all other parameters (such as f0) are kept constant. The MC with the broadest bandwidth is thought to best represent natural stimuli, since, as those, it contains many frequency components. A: Bf = 0:05 (Supplemental Movie S4). B: Bf = 0:15 (Supplemental Movie S5). C: Bf = 0:4 (Supplemental Movie S6)." >}}
