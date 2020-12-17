---
authors:
- alberto-vergani
bio: During my Post-Doc, I am focusing on traveling waves in a bio-inspired neural network.
title: Alberto Arturo Vergani
role: Post-Doc in Computational Neuroscience (04/2020 - 09/2021)
social:
- icon: github
  icon_pack: fab
  link: https://github.com/albertoarturovergani
- icon: researchgate
  icon_pack: ai
  link: https://www.researchgate.net/profile/Alberto_Vergani
- icon: linkedin
  icon_pack: fab
  link: https://www.linkedin.com/in/alberto-arturo-vergani-75288330
  link: https://www.researchgate.net/profile/Alberto_Vergani
- icon: youtube
  icon_pack: fab
  link: https://www.youtube.com/channel/UCzxesD7KEVc55s5aQaZug4Q
superuser: false

education:
  courses:
  - course: Research Fellow in Neuromorphic Computing.
    institution: Middlesex University, Department of Computer Science, London, UK
    year: 2019
  - course: PhD in Computer Science and Mathematics
    institution: University of Insubria, Varese, Italy
    year: 2018

tags:
- phd-icn
user_groups:
- Current Students
---

# Project description: Visual computations using Spatio-temporal Diffusion Kernels and Traveling Waves

Biological vision is surprisingly efficient. To take advantage of this efficiency, Deep learning and convolutional neural networks (CNNs) have recently produced great advances in artificial computer vision. However, these algorithms now face multiple challenges: learned architectures are often not interpretable, disproportionally energy greedy, and often lack the integration of contextual information that seems optimized in biological vision and human perception. It is clear from recent advances in system and computational neuroscience that nonlinear, recurrent interactions in visual cortical networks are key to this efficiency ([Tang et al., 2018](#Tang18); [Kietzmann et al., 2019](#Kietzmann19)). We will use inspiration from neurophysiology and brain imaging to resolve this apparent gap between traditional CNNs and biological visual systems.

**In this post-doctoral project, I will address these major limitations by focusing on specific dynamical features of cortical circuits: _lateral diffusion of sensory-evoked traveling waves_ ([Chavane et al., 2011](#Chavane2000); [Muller et al., 2018](#muller2018cortical)) and _dynamic neuronal association fields_ ([Frégnac et al., 2012](#Frégnac2012); [Frégnac et al., 2016](#Frégnac2016); [Gerard-Mercier et al., 2016](#gerard2016synaptic))**. Indeed, the architecture of primary visual cortex (V1), the direct target of the feedforward visual flow, contains dense local recurrent connectivity with sparse long-range connections ([Voges and Perrinet, 2012](#Voges12)). Such connections add to the traditional convolutional kernels representing feedforward and local recurrent amplification a novel lateral interaction kernel within a single layer (across positions and channels). Less studied, but probably decisive in active vision, recurrent cortico-cortical loops add a level of distributed top-down complexity which participates to the lateral integration of sensory input and perceptual context ([Keller et al., 2019](#Keller2019)). Coupled with the continuous time dynamics of cortical circuits, this elaborate multiplexed architecture provides the conditions possible for generating information diffusion through traveling waves. Inspired by recent work in neuroscience uncovering the ubiquity of these waves during visual processing, we aim to design a self-supervised CNN that will exploit these dynamics for new applications in computer vision.

The proposed work will be organized as a collaboration between two labs (INT, Marseille and UNIC, Gif) along three tasks to be integrated in a unified model:

1. The starting point will be to extend results of self-supervised learning that we have obtained on static, natural images ([Boutin et al., 2019](#BoutinFranciosiniChavaneRuffierPerrinet20)) showing in a recurrent cortical-like artificial CNN architecture the emergence of interactions which phenomenologically correspond to the "association field" described at the psychophysical ([Field et al., 1993](#Field1993)), spiking ([Li and Gilbert, 2002](#Li2002)) and synaptic ([Gerard-Mercier et al., 2016](#gerard2016synaptic)) levels.

2. The central aim will be to develop a dynamical version of this feedback/lateral kernel in the context of the [ANR Horizontal-V1](https://laurentperrinet.github.io/grant/anr-horizontal-v1/) project, linking the two labs and confronted to their recent electrophysiological data pointing to different classes of spatio-temporal diffusion and different degree of anisotropies during apparent and continuous motion.

3. The implementation of this kernel inspired by CNN theory will be compared with a biologically realistic models of the early visual system ([Antolik et al., 2019](#Antolik2019)), and simulations of the lateral diffusion kernel will be developed in collaboration with [Jan Antolik](https://antolik.net/), external collaborator to the ANR grant.  In parallel, using tools linking neural activity to VSD imaging ([Muller et al., 2014](#muller2014stimulus); [Chemla et al., 2019](#Chemla2018)), we will analyze at a more mesocopic level the role of observed traveling waves in forming efficient representations of the visual world.


## Research context

This project is funded by the French National Research Agency (ANR) under the [ANR Horizontal V1](https://laurentperrinet.github.io/grant/anr-horizontal-v1/) grant (coordinator Y. Frégnac) which aims at understanding the emergence of sensory predictions linking local shape attributes (orientation, contour) to global indices of movement (direction, speed, trajectory) at the earliest stage of cortical processing (primary visual cortex, i.e. V1). The cross-talk between physiological and theoretical approaches is fostered by the close collaboration with the teams of Frédéric Chavane at INT and Yves Frégnac at UNIC. The theoretical work is performed in close collaboration with [Lyle Muller](https://www.mullerlab.ca/) (Western U) and Jan Antolik (Prague). This project is primarily hosted at the [Institut de Neurosciences de la Timone](http://www.int.univ-amu.fr/?lang=en).


# References

* <a name="Antolik2019"> Antolik, J, C Monier, Y Frégnac, AP Davison. (2019). </a> "[A comprehensive data-driven model of cat primary visual cortex.](https://www.biorxiv.org/content/10.1101/416156v1)" *BioRxiv*, 416156.

* <a name="BoutinFranciosiniChavaneRuffierPerrinet20"> Boutin, Victor, Angelo Franciosini, Frédéric Chavane, Franck Ruffier, and Laurent U Perrinet. (2019). </a> "[Sparse Deep Predictive Coding captures contour integration capabilities of the early visual system.](https://arxiv.org/abs/1902.07651)" *arXiv*

* <a name="Chavane2000"> Chavane, F., C. Monier, V. Bringuier, P. Baudot, L. Borg-Graham, J. Lorenceau, and Y. Frégnac. 2000. </a> "The Visual Cortical Association Field: A Gestalt Concept or a Psychophysiological Entity?" *Frontiers in System Neuroscience* 4(5): 1-26.

* <a name="Chavane2011"> Chavane, F., Sharon, D., Jancke, D., Marre, O., Frégnac, Y. and Grinvald, A.  (2011). </a> "[Lateral spread of orientation selectivity in V1 is controlled by intracortical cooperativity.](https://doi.org/10.1016/S0928-4257(00)01096-2)" *Journal of Physiology Paris* 94 (5-6): 333--42.

* <a name="Chemla2018"> Chemla, Sandrine, Alexandre Reynaud, Matteo diVolo, Yann Zerlaut, Laurent Perrinet, Alain Destexhe, and Frédéric Chavane. </a> (2018). "[Suppressive Waves Disambiguate the Representation of Long-Range Apparent Motion in Awake Monkey V1.](https://doi.org/10.1523/JNEUROSCI.2792-18.2019)" *Journal of Neuroscience* 39 (22) 4282-4298.

* <a name="Field1993"> Field, D.J., Hayes, A. and Hess, R.F. (1993). </a> "[Contour integration by the human visual system: Evidence for a local “association field”.](https://doi.org/10.1016/0042-6989(93)90156-Q)" *Vision Research* 33 (2), pp. 173-193.

* <a name="Frégnac2012"> Frégnac, Y. (2012)  </a> "[Reading out the synaptic echoes of low-level perception in V1.](https://hal.archives-ouvertes.fr/hal-01685152/)" *European Conference in Computer Vision* 486-495. Springer, Berlin, Heidelberg.

* <a name="Frégnac2016"> Frégnac, Y., Fournier, J., Gerard-Mercier, F., Monier, C., Carelli, P., , M., Troncoso, X. (2016).  </a> "[The Visual Brain: Computing Through Multiscale Complexity.](https://link-springer-com.insb.bib.cnrs.fr/content/pdf/10.1007%2F978-3-319-28802-4_4.pdf)" In *Micro-, Meso- and Macro-Dynamics of the Brain* pp 43-57.

* <a name="gerard2016synaptic"> Gerard-Mercier, Florian, Pedro V Carelli, Marc Pananceau, Xoana G Troncoso, and Yves Frégnac. (2016). </a> "[Synaptic Correlates of Low-Level Perception in V1.](https://www.jneurosci.org/content/36/14/3925)" *Journal of Neuroscience* 36 (14): 3925--42.

* <a name="Keller2019">Keller, A., Roth, M.M. and Scanziani, M. (2019).  </a> 2019. "[The feedback receptive field of neurons in the mammalian primary visual cortex.](https://www.abstractsonline.com/pp8/#!/7883/presentation/65856)" *American Society for Neuroscience Abstracts*,  403.13. Chicago.

* <a name="Kietzmann19">Kietzmann, Tim C., Courtney J. Spoerer, Lynn K. A. Sörensen, Radoslaw M. Cichy, Olaf Hauk, and Nikolaus Kriegeskorte. </a> (2019). "[Recurrence Is Required to Capture the Representational Dynamics of the Human Visual System.](https://doi.org/10/gf9j2t)" *Proceedings of the National Academy of Sciences*, October, 201905544.

* <a name="Li2002">Li W, Piëch V, Gilbert CD</a>  (2006). "[Contour saliency in primary visual cortex.](http://www.paper.edu.cn/scholar/showpdf/MUz2UN2INTA0eQxeQh)" *Neuron*, 50(6):951–962.

* <a name="muller2014stimulus">Muller, Lyle, Alexandre Reynaud, Frédéric Chavane, and Alain Destexhe. </a> (2014). "[The Stimulus-Evoked Population Response in Visual Cortex of Awake Monkey Is a Propagating Wave.](http://www.int.univ-amu.fr/IMG/pdf/Muller_Nature_Communications2014.pdf)" *Nature Communications* 5: 3675.

* <a name="muller2018cortical"> Muller, Lyle, Frédéric Chavane, John Reynolds, and Terrence J Sejnowski. </a> (2018). "[Cortical Travelling Waves: Mechanisms and Computational Principles.](https://papers.cnl.salk.edu/PDFs/Cortical%20travelling%20waves_%20mechanisms%20and%20computational%20principles.%202018-4515.pdf)" *Nature Reviews Neuroscience* 19 (5): 255.

* <a name="Tang18">Tang, Hanlin, Martin Schrimpf, William Lotter, Charlotte Moerman, Ana Paredes, Josue Ortega Caro, Walter Hardesty, David Cox, and Gabriel Kreiman. </a> (2018). "[Recurrent computations for visual pattern completion.](https://doi.org/10.1073/pnas.1719397115)" *Proceedings of the National Academy of Sciences* 115 (35) 8835-8840.

* <a name="Voges12"> Voges, Nicole, and Laurent U Perrinet.</a> (2012). "[Complex Dynamics in Recurrent Cortical Networks Based on Spatially Realistic Connectivities.](https://doi.org/10.3389/fncom.2012.00041)" *Frontiers in Computational Neuroscience* 6.
