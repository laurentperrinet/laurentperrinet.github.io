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

bibliography = "wave.bib"

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

In collaboration with [Lyle Muller](https://www.mullerlab.ca), Yves Fregnac and Frédéric Chavane, we aim at exploring novel visual computations using traveling waves. We are seeking candidates with a strong background in machine learning, computer vision and computational neuroscience.

The project will be coordinated by Laurent Perrinet. For more information visit [https://laurentperrinet.github.io/post/2019-10-21_postdoc-position](https://laurentperrinet.github.io/post/2019-10-21_postdoc-position).

To obtain further information or send applications (including a full CV, a letter of motivation, 2 reference names), please contact: [Laurent.Perrinet@univ-amu.fr](mailto:Laurent.Perrinet@univ-amu.fr) . The appointment is for 18 month. The starting date is set to January 6th, 2020 but can be flexibly extended. Applications are welcome immediately and until the end of year 2019.

Thanks for distributing this announcement to potential candidates!

# detailed description

Biological vision is surprisingly efficient. To understand this
efficiency, Deep learning and convolutional neural networks (CNNs) have
recently produced great advances in computer. However, these algorithms
now face multiple challenges: learned architectures are often not
interpretable, disproportionally energy greedy, and often lack the
integration of contextual information. Such feats are fundamental
features of human visual behavior. Is is clear today that nonlinear,
recurrent interactions are key to this efficiency [@Kietzmann19]. We
will use inspiration from neurophysiology to resolve this apparent gap
between traditional CNNs and biological visual systems.

In this post-doctoral project, we propose to address these major
limitations by incorporating a new dynamical feature of cortical
circuits: sensory-evoked traveling waves [@muller2018cortical]. Indeed,
the architecture of primary visual cortex (V1) contains dense local
connectivity with sparse long-range connections [@Voges12]. Such
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
images [@BoutinFranciosiniChavaneRuffierPerrinet19] and which
phenomenologically correspond to an "association field". Such
processes have a huge importance in the dynamics of visual processing.
In particular, we will disentangle the different forms of interactions
in form and motion [@gerard2016synaptic; @Chavane2000]. Analyzing the
activity of the network using tools from
neurophysiology [@muller2014stimulus; @Chemla2018], we will analyze the
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

[@muller2018cortical]: http://dx.doi.org/10.1371/journal.pmed.0020124 "Ioannidis JPA. Why Most Published Research Findings Are False. PLoS Medicine. Public Library of Science; 2005;2(8):e124. Available from: http://dx.doi.org/10.1371/journal.pmed.0020124"

- id: muller2014stimulus
  type: article-journal
  author:
  - family: Muller
    given: Lyle
  - family: Reynaud
    given: Alexandre
  - family: Chavane
    given: Frédéric
  - family: Destexhe
    given: Alain
  issued:
  - year: 2014
  title: The stimulus-evoked population response in visual cortex of awake monkey
    is a propagating wave
  container-title: Nature Communications
  publisher: Nature Publishing Group
  page: '3675'
  volume: '5'

- id: BoutinFranciosiniRuffierPerrinet19
  type: article-journal
  author:
  - family: Boutin
    given: Victor
  - family: Franciosini
    given: Angelo
  - family: Ruffier
    given: Franck
  - family: Perrinet
    given: Laurent U
  issued:
  - year: 2019
    month: 2
    day: 20
  title: Meaningful representations emerge from sparse deep predictive coding
  container-title: arXiv
  abstract: The formation of connections between neural cells is essentially emerging
    from an unsupervised learning process. During the development of primary visual
    cortex (V1) of mammals, for example, one may observe the emergence of cells selective
    to localized and oriented features. This leads to the development of a rough contour-based
    representation of the retinal image in area V1. We modeled the formation of this
    representation along the thalamo-cortical pathway using a sparse unsupervised
    learning algorithm in a hierarchical network. This algorithm alternates (i) a
    coding phase to encode the information and (ii) a learning phase to find the proper
    encoder (also called dictionary). We replicated and adapted the Multi-Layer Convolutional
    Sparse Coding (ML-CSC) model from Michael Elad’s group i̧teSulam2017. As an application,
    we have trained our implementation on a database containing images from faces.
    The extracted features show similarities with some of the neuron’s receptive field
    found in V1 and beyond. Furthermore, our results demonstrate the potential application
    of such a strategy to the fast classification of images, for example in hierarchical
    and dynamical architectures.
  keyword: sparse coding
  URL: https://arxiv.org/abs/1902.07651
