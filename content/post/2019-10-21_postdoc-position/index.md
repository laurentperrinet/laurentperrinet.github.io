+++
title = "Postdoc position on Visual computations using Traveling Waves"
subtitle = "Post-doc in Marseille, France on Visual computations using Traveling Waves."

date = 2019-10-21T09:00:00
lastmod = 2019-10-21T09:00:00
draft = false

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["laurent-u-perrinet"]

tags = ["events"]
summary = "Post-doc in Marseille, France on Visual computations using Traveling Waves."

projects = []

# https://pixabay.com/photos/drops-of-water-water-liquid-fresh-578897/
[image]
  # Caption (optional)
  caption = "Photo by [Rony Michaud](https://pixabay.com/users/ronymichaud-647623/)"
  placement = 2
  focal_point = "Center"
  preview_only = false
+++

Dear colleagues,

Applications are welcome for a post-doctoral position at [INT](http://www.int.univ-amu.fr/?lang=en)-[Marseille](https://en.wikipedia.org/wiki/Marseille), France.

In collaboration with [Yves Fregnac](http://neuro-psi.cnrs.fr/spip.php?article934&lang=fr), [Lyle Muller](https://www.mullerlab.ca) and [Frédéric Chavane](http://www.int.univ-amu.fr/spip.php?page=equipe&equipe=NeOpTo&lang=en), we aim at exploring novel visual computations using traveling waves. We are seeking candidates with a strong background in machine learning, computer vision and computational neuroscience.

The project will be coordinated by Laurent Perrinet. For more information visit [https://laurentperrinet.github.io/post/2019-10-21_postdoc-position](https://laurentperrinet.github.io/post/2019-10-21_postdoc-position).

To obtain further information or send applications (including a full CV, a letter of motivation, 2 reference names), please contact: [Laurent.Perrinet@univ-amu.fr](mailto:Laurent.Perrinet@univ-amu.fr). The appointment is for 18 month. The starting date is set to January 6th, 2020 but can be flexibly extended. Applications are welcome immediately and until the end of year 2019.

Thanks for distributing this announcement to potential candidates!

# Detailed description: Visual computations using Traveling Waves

Biological vision is surprisingly efficient. To understand this
efficiency, Deep learning and convolutional neural networks (CNNs) have
recently produced great advances in computer. However, these algorithms
now face multiple challenges: learned architectures are often not
interpretable, disproportionally energy greedy, and often lack the
integration of contextual information. Such feats are fundamental
features of human visual behavior. It is clear today that nonlinear,
recurrent interactions are key to this efficiency ([Kietzmann el al, 2019](#Kietzmann19)). We
will use inspiration from neurophysiology to resolve this apparent gap
between traditional CNNs and biological visual systems.

In this post-doctoral project, we propose to address these major
limitations by incorporating a new dynamical feature of cortical
circuits: ** sensory-evoked traveling waves ** ([Muller el al, 2018](#muller2018cortical)). Indeed,
the architecture of primary visual cortex (V1) contains dense local
connectivity with sparse long-range connections ([Voges and Perrinet, 2012](#Voges12)). Such
connections add to the traditional convolutional kernel a novel
interaction kernel within a single layer (across positions and
channels). This introduces a recurrent network architecture which
integrates sensory input and current activity. Coupled with the
continuous time dynamics of cortical circuits, this architecture
provides the necessary conditions for generating traveling waves.
Inspired by recent work in neuroscience uncovering the ubiquity of these
waves during visual processing, we aim to design a self-supervised CNN
that will exploit these dynamics for new applications in computer
vision.

We first expect to extend results of self-supervised learning that we
have obtained on complex static
images ([Boutin el al, 2019](#BoutinFranciosiniChavaneRuffierPerrinet19)) and which
phenomenologically correspond to an "association field". Such
processes have a huge importance in the dynamics of visual processing.
In particular, we will disentangle the different forms of interactions
in form and motion ([Gerard-Mercier el al, 2016](#gerard2016synaptic); [Chavane el al, 2000](#Chavane2000))). Analyzing the
activity of the network using tools from
neurophysiology ([Muller el al, 2014](#muller2014stimulus); [Chemla el al, 2019](#Chemla2018)), we will analyze the
role of observed traveling waves in forming efficient representations
of the visual world. Lastly, we will analyze how those algorithms scale
to the learning of the processing of representations invariant to common
geometrical transforms as is believed to be implemented in biological
visual systems.

Expected profile of the candidate
---------------------------------

Candidates should have at least a PhD degree in the domain of
computational neuroscience, physics or engineering, and a solid training
in machine learning and computer vision.

Good command of programming tools (Python scripting) is required.
Multidisciplinary background would be strongly appreciated and in
particular an advanced knowledge in mathematics, for a deep
understanding of signal processing methods, along with strong
computational skills. The candidate needs to show a keen interest in
neuroscience. Moreover the candidate will have to be curious about
neuronal networks in general and neuro-mimetic approaches to robotics in
particular even if this specific knowledge is not mandatory.

The candidate has to fluently speak English to understand publications
and to attend international conferences and workshops. The candidate has
to show good skills in computer science (programming skills,
architecture understanding...), and in image processing methods. The
preferred candidate will have the ability to work autonomously, and
needs to be flexible to comply with the working method of the
supervisors.

Research context
----------------

This project is financed by the [ANR Horizontal
V1](https://laurentperrinet.github.io/grant/anr-horizontal-v1/) grant
which aims at understanding the emergence of sensory predictions linking
local shape attributes (orientation, contour) to global indices of
movement (direction, speed, trajectory) at the earliest stage of
cortical processing (primary visual cortex, i.e. V1). The cross-talk
between physiological and theoretical approaches will be fostered by the
close collaboration with the teams of Frédéric Chavane and Yves Fregnac.
The theoretical work will be performed in close collaboration with [Lyle
Muller](https://www.mullerlab.ca/) (Western U). The project is hosted at
the [Institut de Neurosciences de la
Timone](http://www.int.univ-amu.fr/?lang=en) in
[Marseille](https://en.wikipedia.org/wiki/Marseille), a lively town by
the Mediterranean sea in the south of France.

# References

<a name="BoutinFranciosiniChavaneRuffierPerrinet19">
Boutin, Victor, Angelo Franciosini, Frédéric Y Chavane, Franck Ruffier,
and Laurent U Perrinet. 2019. </a> "[Sparse Deep Predictive Coding captures contour integration capabilities of the early visual system.](https://arxiv.org/abs/1902.07651)"

<a name="Chavane2000">
Chavane, F., C. Monier, V. Bringuier, P. Baudot, L. Borg-Graham, J.
Lorenceau, and Y. Frégnac. 2000. </a> "[The Visual Cortical Association Field: A Gestalt Concept or a Psychophysiological Entity?](https://doi.org/10.1016/S0928-4257(00)01096-2)" *Journal of Physiology Paris* 94 (5-6): 333--42.


<a name="Chemla2018">
Chemla, Sandrine, Alexandre Reynaud, Matteo diVolo, Yann Zerlaut,
Laurent Perrinet, Alain Destexhe, and Frédéric Chavane. </a> 2018.
"[Suppressive Waves Disambiguate the Representation of Long-Range Apparent Motion in Awake Monkey V1](https://doi.org/10.1101/372763)"".


<a name="gerard2016synaptic">
Gerard-Mercier, Florian, Pedro V Carelli, Marc Pananceau, Xoana G
Troncoso, and Yves Frégnac. 2016. </a> "[Synaptic Correlates of Low-Level Perception in V1](https://www.jneurosci.org/content/36/14/3925)." *Journal of Neuroscience* 36 (14): 3925--42.


<a name="Kietzmann19">
Kietzmann, Tim C., Courtney J. Spoerer, Lynn K. A. Sörensen, Radoslaw M. Cichy, Olaf Hauk, and Nikolaus Kriegeskorte. </a> 2019. "[Recurrence Is Required to Capture the Representational Dynamics of the Human Visual System.](https://doi.org/10/gf9j2t)." *Proceedings of the National Academy of Sciences*,
October, 201905544.


<a name="muller2014stimulus">
Muller, Lyle, Alexandre Reynaud, Frédéric Chavane, and Alain Destexhe.
</a> 2014. "[The Stimulus-Evoked Population Response in Visual Cortex of Awake Monkey Is a Propagating Wave.](http://www.int.univ-amu.fr/IMG/pdf/Muller_Nature_Communications2014.pdf)" *Nature Communications* 5: 3675.


<a name="muller2018cortical">
Muller, Lyle, Frédéric Chavane, John Reynolds, and Terrence J Sejnowski.
</a> 2018. "[Cortical Travelling Waves: Mechanisms and Computational
Principles](https://papers.cnl.salk.edu/PDFs/Cortical%20travelling%20waves_%20mechanisms%20and%20computational%20principles.%202018-4515.pdf)." *Nature Reviews Neuroscience* 19 (5): 255.


<a name="Voges12">
Voges, Nicole, and Laurent U Perrinet.</a> 2012. "[Complex Dynamics in Recurrent Cortical Networks Based on Spatially Realistic Connectivities.](https://doi.org/10.3389/fncom.2012.00041)" *Frontiers in Computational Neuroscience* 6.
