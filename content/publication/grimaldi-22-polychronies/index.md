---
title: Precise spiking motifs in neurobiological and neuromorphic data
date: 2022-12-23
authors:
- Antoine Grimaldi
- Amélie Gruel
- Camille Besnainou
- Jean-Nicolas Jérémie
- Jean Martinet
- Laurent U Perrinet
abstract: Why do neurons communicate through spikes? By definition, spikes are all-or-none
  neural events which occur at continuous times. In other words, spikes are on one
  side binary, existing or not without further details, and on the other can occur
  at any asynchronous time, without the need for a centralized clock. This stands
  in stark contrast to the analog representation of values and the discretized timing
  classically used in digital processing and at the base of modern-day neural networks.
  As neural systems almost systematically use this so-called event-based representation
  in the living world, a better understanding of this phenomenon remains a fundamental
  challenge in neurobiology in order to better interpret the profusion of recorded
  data. With the growing need for intelligent embedded systems, it also emerges as
  a new computing paradigm to enable the efficient operation of a new class of sensors
  and event-based computers, called neuromorphic, which could enable significant gains
  in computation time and energy consumption, a major societal issue in the era of
  the digital economy and global warming. In this review paper, we provide evidence
  from biology, theory and engineering that the precise timing of spikes plays a crucial
  role in our understanding of the efficiency of neural networks.
featured: true
draft: false
categories:
- Computational Neuroscience
- NeuroAI & Machine Learning
tags:
- motion-perception
- neuromorphic-computing
- polychronization
- primary-visual-cortex
- spiking-motifs
- spiking-neural-networks
- temporal-coding
publication_types:
- article-journal
doi: 10.3390/brainsci13010068
links:
- name: Hal
  url: https://hal.science/hal-03918338
- name: Code
  url: https://github.com/SpikeAI/2022_polychronies-review
- name: URL
  url: https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/
- name: arXiv
  url: https://arxiv.org/abs/2404.07866
grants:
- anr-anr
- aprovis-3-d
- polychronies
---
{{< video src="2022-12-23_polychrony-review_video-abstract.mp4" controls="yes" >}}
 * read the paper [online](https://arxiv.org/html/2404.07866v1) or in [PDF](https://arxiv.org/pdf/2404.07866v1.pdf)
 * [Video Abstract](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/2022-12-23_polychrony-review_video-abstract.mp4)
 * join the [Zotero group](https://www.zotero.org/groups/4562620/polychronies) to add and discuss more items
 * *code* for paper (including revisions): https://github.com/SpikeAI/2022_polychronies-review 
 
{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="**Core mechanism of polychrony detection.** *(Left)* In this example, three presynaptic neurons denoted *b*, *c* and *d* are fully connected to two post-synaptic neurons *a* and *e*, with different delays of respectively 1, 5, and 9 ms for *a* and 8, 5, and 1 ms for *e*. *(Middle)* If three synchronous pulses are emitted from presynaptic neurons, this will generate post-synaptic potentials that will reach a and e asynchronously because of the heterogeneous delays, and they may not be sufficient to reach the membrane threshold in either of the post-synaptic neurons; therefore, no spike will be emitted, as this is not sufficient to reach the membrane threshold of the post synaptic neuron, so no output spike is emitted. *(Right)* If the pulses are emitted from presynaptic neurons such that, taking into account the delays, they reach the post-synaptic neuron *a* at the same time (here, at t = 10 ms), the post-synaptic potentials evoked by the three pre-synaptic neurons sum up, causing the voltage threshold to be crossed and thus to the emission of an output spike (red color), while none is emitted from post-synaptic neuron *e*.">}}
* more posts on [reddit](https://www.reddit.com/r/neuroscience/comments/104q30e/precise_spiking_motifs_in_neurobiological_and/), [RG](https://www.researchgate.net/publication/365497113_Precise_Spiking_Motifs_in_Neurobiological_and_Neuromorphic_Data), or [HAL](https://hal.science/hal-03918338)
 
* see follow-up paper: {{< cite page="/publication/perrinet-23-icann" view="4" >}}
