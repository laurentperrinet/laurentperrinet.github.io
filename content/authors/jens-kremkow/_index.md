---
authors:
- jens-kremkow
education:
  courses:
  - course: Phd in Computational Neuroscience
    institution: Aix-Marseille Université
    year: 2009
title: Jens Kremkow
role: PI @ Neuroscience Research Center, Charité, Berlin, Germany.
bio: During my PhD, I focused on the interplay of Excitation and Inhibition in Visual
  Cortical Circuits.
social:
- icon: google-scholar
  icon_pack: ai
  link: https://scholar.google.com/citations?user=YEdekcAAAAAJ
- icon: researchgate
  icon_pack: ai
  link: https://www.researchgate.net/profile/Jens-Kremkow
- icon: external-link-alt
  icon_pack: fas
  link: http://jens.kremkow.de
superuser: false
user_groups:
- Former Students
tags:
- neuromorphic-computing
- primary-visual-cortex
- pynn
- sparse-coding
- spiking-neural-networks
projects:
- ''
categories:
- Biological Neuroscience
- Computational Neuroscience
- Education
- Outreach & Public Engagement
- Visual Neuroscience
---





# Correlating Excitation and Inhibition in Visual Cortical Circuits: Functional Consequences and Biological Feasibility  (PhD, 2006-01 / 2009-05)

The goal of the FACETS (Fast Analog Computing with Emergent Transient States) project was to create a theoretical and experimental foundation for the realisation of novel computing paradigms which exploit the concepts experimentally observed in biological nervous systems. The continuous interaction and scientific exchange between biological experiments, computer modelling and hardware emulations within the project provides a unique research infrastructure that will in turn provide an improved insight into the computing principles of the brain. This insight may potentially contribute to an improved understanding of mental disorders in the human brain and help to develop remedies.


* Venue: Thèse de Doctorat de l’Université d’Aix-Marseille II, Ecole Doctorale des Sciences de la Vie et de la Santé Marseille, France en Cotutelle avec la Fakultät für Biologie Albert-Ludwigs-Universität Freiburg im Breisgau, Allemagne
* Thesis director: Guillaume MASSON and Dr. Laurent PERRINET


## Main publications:

* {{< cite page="/publication/kremkow-16" view="4" >}}
* {{< cite page="/publication/kremkow-10-jcns" view="4" >}}

##  Description of the PHD thesis project

The primary visual cortex (V1) is one of the most studied cortical area in neuroscience. Together with the retina and the lateral geniculate nucleus (LGN), it forms the early visual system, which has become a common model for studying computational principles in the sensory systems. Simple artificial stimuli (such as drifting gratings (DG)) have given precious insights into the neural basis of visual processing. However, recently more researchers have used more complex natural images (NI) visual stimuli, arguing that the low dimensional artificial stimuli are not sufficient for a complete understanding of the visual system. For example, whereas the responses of V1 neurons to DG are dense but with variable spike timings, the neurons are activated with only few and precise spikes to NI. Furthermore, if linear receptive field models provide a good fit to responses during simple stimuli, they often fail during NI.

To investigate the mechanisms behind the stimulus dependent responses of cortical neurons we have built a biophysical, yet simple and comprehensible, model of the early visual system. We show how the spatial and temporal stimulus properties interact with the model architecture to give rise to differential response behaviour. Our results show in particular that during NI, the LGN afferents show epochs of correlated activity. These temporal correlations are necessary to induce transient excitatory synaptic inputs, and result in precise spike timings in V1. Furthermore, the sparseness of the responses to NI can be explained by a hardwired, correlated and lagging inhibitory conductance, or conductance temporal window, which is induced by the interactions of the thalamocortical circuit with the spatiotemporal correlations in the stimulus.

We continue by investigating the origin of nonlinear responses during NI in the temporal window, by comparing models of different complexity. Our results suggest first that adaptive processes shape the responses, depending on the temporal properties of the stimuli. The different spatial properties can result in nonlinear inputs through the recurrent cortical network. We then study the functional consequences of correlated excitatory and inhibitory condutances in more details in general models. These results show that: (1) spiking of individual neurons becomes sparse and precise, (2) the selectivity of signal propagation increases and the detailed delay allows to gate the propagation through feed-forward structures (3) and recurrent cortical networks are more stable and more likely to elicit in vivo type activity states.
Lastly our work illustrates new advances in methods of constructing and exchanging models of neuronal systems by the means of a simulator independent description language (called PyNN). We use this new tool to investigate the feasibility of comparing software simulations with neuromorphic hardware emulations. The presented work give new perspectives on the way conductances can be used for computations and it opens the door for more elaborated models of visual system's mechanisms.
