---
authors:
- hilde-teigen
bio: During my PhD, I am focusing on Ultra-fast vision using Spiking Neural Networks.
title: Hilde Langengen-Teigen
role: Phd candidate in Neuroscience
social:
- icon: house-user
  icon_pack: fas
  link: https://centuri-livingsystems.org/h-l-teigen/
- icon: house-user
  icon_pack: fas
  link: https://www.hf.uio.no/ifikk/english/people/aca/philosophy/temporary/hildelt/
superuser: false
user_groups:
- Former Students
categories: ["Biological Neuroscience"]
tags: ["predictive-coding", "spiking-neural-networks"]
---

#  "Neuromodulatory mechanisms of predictive processing in the mouse visual cortex" (PhD position, 2023-10 / 2026-09)

* Thesis director: [Dr. Ede Rancz](https://laurentperrinet.github.io/author/ede-rancz/), Mediterranean Institute of Neurobiology, Marseille
* Thesis co-director: Dr. Laurent Perrinet, Institut de Neurosciences de la Timone (INT)
* This PhD position is made possible thanks to a 3-year contract from AIX-MARSEILLE University awarded by the [Turing Centre for Living Systems PhD call (CENTURI)](https://centuri-livingsystems.org/phd2023-14/).


The predictive processing framework is considered a universal principle in the operation of the brain[^1]. However, how it is implemented on the level of circuits and single neurons is an open question[^2]. For any such computation, external sensory information must be compared with internally generated predictions. We have previously uncovered the connectivity and synaptic integration foundations for such algorithms in the mouse visual cortex[^3]. In this project, we will study how neuromodulators, such as serotonin (implicated in depression and psychosis) and acetylcholine (implicated in attention and dementia), govern the integration of internal and external information.

## Keywords

Neuromodulation, visual cortex, predictive processing, spiking neuronal network models, computational neuroscience, optogenetics, patch-clamp

## Objectives

* The first objective is to explore pre- and postsynaptic neuromodulatory mechanisms using spiking neuronal network models developed by the Perrinet team[^4].
* The second objective is testing model predictions experimentally. This will be done in the Rancz team using optogenetics, pharmacology and whole-cell recordings in brain slices.

## Proposed approach (experimental / theoretical / computational)

We will build spiking neuronal network models approximating the mouse visual cortex using connectivity data from our lab[^3] and the literature. On top of recurrent local connections, we will incorporate often neglected long-range excitatory input and the associated feed-forward inhibition currently being studied by the Rancz team. Notably, various models of neuromodulation, both on the pre- and postsynaptic levels, will be included. In particular, the normative models will allow designing stimulations using a recently developed optimisation method[^5]. The relative contribution of neuromodulatory mechanisms in model instantiations will then be tested experimentally. We will record somatic and dendritic neuronal activity during the optogenetic stimulation of different input streams. Model predictions of the neuronal coding of prediction errors will be tested by pharmacologically blocking or activating specific neuromodulator receptors.

## Interdisciplinarity

We will combine computational and experimental neuroscience in the proposed project. Theoretical and computational neuroscience (TCN) is essential to propose computations and their algorithmic instantiations. Experimental neuroscience (EN) can uncover the biological mechanisms underlying these model-predicted computations. TCN can tackle experimentally intractable problems by narrowing the parameter space. EN, in return, can feed back architectural insights to help build better models, e.g. for artificial intelligence. Ultimately, understanding the biological underpinnings of the mind will lead us to alleviate the suffering caused by psychiatric diseases and the human condition in general.

[^1]: Bar, M (2009) *Predictions: a universal principle in the operation of the human brain* [doi:10.1098/rstb.2008.0321](https://royalsocietypublishing.org/doi/10.1098/rstb.2008.0321)

[^2]: Spratling, M (2017) *A review of predictive coding algorithms* [doi:10.1016/j.bandc.2015.11.003](https://www.sciencedirect.com/science/article/abs/pii/S027826261530035X)

[^3]: Galloni, A, Ye, Z. & Rancz, E. (2022) *Dendritic Domain-Specific Sampling of Long-Range Axons Shapes Feedforward and Feedback Connectivity of L5 Neurons* [doi:10.1523/JNEUROSCI.1620-21.2022](https://www.jneurosci.org/content/42/16/3394)

[^4]: Perrinet, L (2023) *Accurate Detection of Spiking Motifs by Learning Heterogeneous Delays of a Spiking Neural Network* https://laurentperrinet.github.io/publication/
perrinet-23-icann/

[^5]: Walker, Y *et al.* (2019) *Inception loops discover what excites neurons most using deep predictive models* [doi:10.1038/s41593-019-0517-x](https://www.nature.com/articles/s41593-019-0517-x)