---
title: "PhD thesis 'Focus of attention: a sensory-motor task for energy reduction in spiking neural networks'"
subtitle: THE POSITION HAS BEEN FILLED. 
authors:
- laurent-u-perrinet
date: 2024-05-03 09:00:00
draft: false
image:
  caption: "Animal camouflage illustrates the importance of exploration in vision: looking straight ahead reveals only vegetation, while making the right saccade reveals a cheetah ready to hunt its prey."
  focal_point: Smart
  placement: 2
  preview_only: false
lastmod: 2024-05-03 09:00:00

tags: ["bayesian-modelling", "deep-learning", "eye-movements", "foveated-vision", "log-polar-mapping", "neuromorphic-computing", "predictive-coding", "primary-visual-cortex", "retinotopy", "spiking-neural-networks", "visual-illusions"]
categories: ["Behavioural Neuroscience", "Biological Neuroscience", "Computational Neuroscience", "Education", "NeuroAI & Machine Learning", "Outreach & Public Engagement", "Visual Neuroscience"]
projects: [""]
---

Dear colleagues,

Applications are welcome for a fully funded PhD position **Focus of attention: a sensory-motor task for energy reduction in spiking neural networks**. The position will be located at the [EDGE Team @ LEAT Laboratory](https://leat.univ-cotedazur.fr/) within [Université Côte d'Azur](https://www.univ-cotedazur.fr/) and/or at the [INT](http://www.int.univ-amu.fr/?lang=en) in [Marseille](https://en.wikipedia.org/wiki/Marseille), France. 

## Context

This project takes place in the context of the [EMERGENCES project (ANR
PEPR IA 2023-2027)](https://emergences.lirmm.fr/) which aims to advance the state of the art on machine
learning models using inspiration from biology. Indeed, inspiration from
brain features promises to show the emergence of unrivalled efficient
processing. Among the most promising features studied in the literature
of bio-inspired AI are temporal data encoding using spikes, multimodal
association, local learning or attention-based processing.

This PhD subject focuses on the association between attention and
spiking neural networks for defining new efficient AI models for
embedded systems such as drones, robots and more generally autonomous
systems.

The thesis will take place between the LEAT research lab in
Sophia-Antipolis and the INT institute in Marseille which both develop
complementary approaches on bio-inspired AI from neuroscience
observation to embedded systems design.

## Subject

The volume as well as the diversity of visual information that reaches
our eyes at every moment are huge and cannot be fully integrated by the
visual system. In other words, the biological system is confronted to
the same challenge as the one encountered by artificial systems
(especially at the edge) when dealing with the huge amounts of
information coming continuously from the real world. Interestingly, the
brain has found an original approach to deal with this issue by
*focusing* on a sub-part of the visual information at a time. Indeed,
the study of the visual cortex in neuroscience has made it possible to
highlight subregions that treat each or all of the multiple properties
of information coming from the visual pathways: shapes, colors,
movements, etc [\[1\]](#ref1), thus revealing the interaction of attentional
processes and the concept of "saliency" used in cognitive science.

Creating a fully autonomous system remains a significant challenge,
especially when operating in the dynamic real world. In recent times,
machine learning has assumed a prominent role in machine vision,
particularly through the implementation of deep learning algorithms.
These algorithms have yielded impressive outcomes in tasks such as
object detection, recognition, and tracking. However, these systems come
with a high computational cost, as they must process entire camera
images to generate these results. Additionally, they struggle to
dynamically adapt to changes in their environment.

Our focus lies on two integrated bio-inspired approaches that leverage
attentional mechanisms. The first approach, known as **bottom-up**,
draws inspiration from the work of the Gestalt theory, the Feature
Integration Theory (Triesman, Gelad) [\[3\]](#ref3), and the model of visual
attention from Itti & Koch [\[1\]](#ref1). This approach relies on the saliency
of low-level features in the visual field, processed in parallel,
including movement, color, and edges. It employs emergent mechanisms to
integrate features guided by their saliency in order to detect the
consistency of objects, encompassing their form, position, and speed. As
shown by the Gestalt theory, only the more salient data are needed in
this mechanism. Thus, we can dramatically reduce the amount of needed
data by extracting only the more salient regions of interest during
bottom-up phase.

The second approach, known as **top down**, considers that the visual
attention is guided by higher level cognitive stages. For instance, in
the Guided Search theory [\[4\]](#ref4), Wolfe emphasizes the role of prior
knowledges, expectations, and intentions. In this work, Wolfe proposes a
guided search mechanism that relies on a "Priority map that represents
the system's best guess as to where to deploy attention next.". This
Priority map is built on multiple sources of information such as the
visual system as well as higher-level information such as intention,
search history and the actual visual semantics. In this way,
higher-level information is used to guide the filtering of the botom-up
path, so that only the information required for a given task is selected
and processed. Similar systems are proposed by Schöner [\[5\]](#ref5) in which
saliency maps, working memories and "priority map", guided visual search
mechanisms are implemented through the Neural Field Theory (NFT). Here,
Dynamic Neural Fields are used to implement the saliency of feature
maps, as well as scene spatial selection mechanism, working memory, etc.

In a previous work from the LEAT [\[6\]](#ref6), we have proposed a brain
inspired attentional process implementing bottom-up and top-down paths
based on a dynamic neural fields properties embodied in a sensory-motor
loop. In a complementary work, the INT group has developed a dual
pathway model of the visual system in which saliency emerges as a
property of the perceptual system to perform saccades, that is, rapid
shifts of the fixation point [\[7\]](#ref7). This uses a recognition model which
takes as an input a retinotopically transformed input and shows the
emergence of saliency maps [\[8\]](#ref8) In the dual-pathway model, the
exploration of a visual scene is based on both the saliency of the color
feature (bottom-up) and the class of the last selected object recognized
by a convolutional neural network (top-down). Both paths are integrated
by a dynamic neural field to select the next visual information to be
explored or conserved by setting motor orders accordingly.

The main goal of the thesis is to propose a new vision of the
integration of attention into machine learning models. The proposed
model will draw on the dynamics at play in a sensory-motor approach to
perception and will thus reconsider the classical perception tasks in
order to better fit with the continuous flow of information coming from
the environment.

## Work plan

The PhD will be co-supervised between INT in Marseille and LEAT in Nice.
According to the preferences of the candidate, a main laboratory of
affiliation will be selected. Weekly meetings will be organized remotely
and visiting weeks will be planned to work in-person in the other lab
along the year.

### Year 1

-   Study the state of the art in both neuroscience and machine learning
    on the use of attentional properties to make AI models more
    effective in environmental perception tasks.

-   Write a synthesis report on this study.

-   Develop a first neural model integrating attention-based selection
    in a specific perception task such as visual search.

-   Define the specific metrics (KPI) dedicated to the evaluation of the
    performance and efficiency of such a bio-inspired AI model.

-   Submit a first publication on this preliminary study in an
    international conference.

### Year 2

-   Analyze of the performances of the preliminary attention-based model

-   Develop the approach in order to integrate step by step the features
    related to dual pathway perception, attention, foveation, DNF and
    make the model compatible with convolutional neural networks

-   Submit a second publication in a international journal

### Year 3

-   Study the adaptation of the model to spiking neural networks

-   Evaluation and comparison of the different approaches

-   Submit publications on the final results of the thesis

-   Write the thesis report and prepare the defense

## Required skills

-   Master thesis in one of the following domains: neuromorphic systems,
    spiking neural networks, neurocognition, machine learning.

-   Background and experience in machine-learning, artificial neural
    networks, and/or neurosciences.

-   Strong motivation, team working, fluent in English (spoken and
    written).

-   Programming skills in python, keras, pytorch or equivalent

Start: year 2024

Duration: 3 years

Location: Sophia-Antipolis and/or Marseille

## Contacts

* Benoît Miramond is Full Professor in Electrical Engineering at LEAT
laboratory from University Côte d'Azur (UCA). He holds the chair on
bio-inspired AI at 3IA Cote d'Azur Institute and leads the eBRAIN
research group which develops a interdisciplinary research activity on
embedded Bio-inspiRed AI and Neuromorphic architectures, especially
based on SNNs. LEAT is a mixt research unit (UMR 72 48) from UCA and
CNRS.

* Laurent Perrinet is a director of research at Institut des Neurosciences
de la Timone (CNRS - Aix-Marseille Université). He is studying the link
between brain microstructures and their macroscopic function by
implementing realistic models of the primary visual cortex using spiking
neural networks.

* Laurent Rodriguez is associate professor at LEAT laboratory in the
eBRAIN group. He is interested in dynamic neural networks and develop
neural models from biological inspiration.
* More details on the "Emergences" grant: {{< cite page="/grant/emergences" view="4" >}}

# Application

Apply by sending an email directly to the supervisors (<Benoit.miramond@univ-cotedazur.fr> <Laurent.perrinet@univ-amu.fr> <Laurent.rodriguez@univ-cotedazur.fr>). The application
will include:

• Letter of recommendation of the master supervisor.

• Curriculum vitæ.

• Motivation Letter.

## References

* <a name="ref1"> \[1\] L. Itti et C. Koch, « Computational modelling of visual attention ». *Nat Rev Neurosci*, vol. 2, 3, 3, mars 2001, doi:
[10.1038/35058500](https://doi.org/10.1038/35058500).

* <a name="ref2"> \[2\] Gerstner, W., Kistler, W. M., Naud, R., & Paninski, L. (2014). « Neuronal dynamics: From single neurons to networks and models of cognition ». Cambridge University Press

* <a name="ref3"> \[3\] A. M. Treisman et G. Gelade, « A feature-integration theory of attention ». *Cognitive Psychology*, vol. 12, 1, p. 97‑136, janv. 1980, doi:[10.1016/0010-0285(80)90005-5](https://doi.org/10.1016/0010-0285(80)90005-5).

* <a name="ref4"> \[4\]  Wolfe, J.M. «Guided Search 6.0: An updated model of visual search ». Psychon Bull Rev 28, 1060--1092 (2021).
<https://doi.org/10.3758/s13423-020-01859-9>

* <a name="ref5"> \[5\]  [Grieben, R.](https://dynamicfieldtheory.org/people/raul-grieben/), & [Schöner, G.](https://dynamicfieldtheory.org/people/gregor-schoner/). « A neural dynamic process model of combined bottom-up and top-down guidance in triple conjunction visual search». In T. Fitch, Lamm, C., Leder, H., & Teßmar-Raible, K. (Eds.), Proceedings of the 43rd Annual Conference of the Cognitive Science Society

* <a name="ref6"> \[6\]  M. Rasamuel, Lyes Khacef, Laurent Rodriguez, et Benoit Miramond, « Specialized visual sensor coupled to a dynamic neural field for embedded attentional process ». IEEE Conference Publication \| IEEE Xplore. <https://ieeexplore.ieee.org/abstract/document/8705979>

* <a name="ref7"> \[7\]  Emmanuel Daucé, Pierre Albigès, Laurent U Perrinet (2020). « [A dual foveal-peripheral visual processing model implements efficient saccade selection](https://laurentperrinet.github.io/publication/dauce-20/) ». *Journal of Vision*. doi:<https://doi.org/10.1167/jov.20.8.22>

* <a name="ref8"> \[8\] Jean-Nicolas Jérémie, Emmanuel Daucé, Laurent U Perrinet (2020). « Retinotopic Mapping Enhances the Robustness of Convolutional Neural Networks ». arXiv https://arxiv.org/abs/2402.15480

