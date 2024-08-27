---
authors:
- hugo-ladret
bio: My PhD subject focused on the role of precision in natural and artificial neural networks.

education:
  courses:
    - course:  Now a Postdoc in Georg Keller’s lab
      institution: FMI (Friedrich Miescher Institute for Biomedical Research), Basel, Switzerland
      year: 2024
    - course: Phd candidate in Computational Neuroscience
      institution: Aix-Marseille Université
      year: 2023
    - course: Master in Neuroscience
      institution: Aix-Marseille Université
      year: 2019
title: Hugo Ladret
role: Phd in Computational Neuroscience
social:
- icon: github
  icon_pack: fab
  link: https://github.com/hugoladret
- icon: linkedin
  icon_pack: fab
  link: https://www.linkedin.com/in/hugoladret/
- icon: twitter
  icon_pack: fab
  link: https://twitter.com/hugoladret
- icon: external-link-alt
  icon_pack: fas
  link: https://hugoladret.github.io
superuser: false
user_groups:
- Former Students
---

# PhD Student (2019-09 / 2024-02): A multiscale cortical model to account for orientation selectivity in natural-like stimulations

 * Aix-Marseille Université, Institut des Neurosciences de la Timone
 * Université de Montréal, Laboratoire des Neurosciences de la Vision

Hugo Ladret focuses on predictive coding, an influential brain theory that promises to account for the many seemingly disparate results neuroscientists have gathered over decades of experiments. Using neurobiology with a theory-driven approach, his experimental work deals about vision, and to find theoretical insights for neural network modelling.


## Relevant papers

{{< cite page="publication/ladret-23-iclr" view="4" >}}
{{< cite page="publication/ladret-23" view="4" >}}
{{< cite page="publication/ladret-24-joconde" view="4" >}}


# previous experience

## master 2B (undergrad, 2019-01-12 / 2019-05-24)

* Université de Montréal, Laboratoire des Neurosciences de la Vision


## master 2A (undergrad, 2018-09-10 / 2019-01-11) : Learning temporal integrations in a visual spiking neural network

Building upon our previous work, we are investigating how recurrent neural networks learn to integrate temporal information, a dimension which is absent in most deep learning networks but provides a wealth of information in biological neural networks.

To be able to generalize our findings, I created a model of the early visual pathway (retina and thalamus) that generates neural activity from any natural image, based on data gathered in biological systems for the past several decades.
The output from this early visual pathway is then processed by a recurrent spiking neural network whose dynamics match that of the primary visual cortex.

We showed that Spike Timing Dependant Plasticity (STDP) and recurrence are key components that allow spiking neural networks to extract patterns from noisy input and build strong internal representations. Such representations not only correctlt predict spatial informations (for example the organization of a visual scene) but also predict temporal structure underlying such informations.

 * source code : https://github.com/hugoladret/InternshipM2

# Neuroscience Specialist for Artistic Creation (2018-07 / 2018-09)

I developed computational neuroscience and computational physics models, in collaboration with well-known contemporary artist [Etienne Rey]({{< relref "/authors/etienne-rey" >}})
 at Friche la Belle de Mai (Marseille) and AI researcher Laurent Perrinet. The idea behind our project was to create works of art by distributing particles in a constrained, semi-stable space, thereby creating discrete illusory perceptions.

To dive into more technical details, my work included the implementation of a Boltzmann lattice for computational fluid dynamics (D2Q9 structure), as well as various electro-magnetic interaction models. On the neuroscience side, I used Deep Convoluted Generative Adverserial Networks (DCGAN), Kohonen maps and Canny edge detectors to generate triangulated graphs with a hidden underlying structure.
In order to facilitate collaboration between the three of us, I also developed a GUI and multi-threading support that allowed us to work efficiently and use at best each our respective skill set.

* source code : https://github.com/NaturalPatterns/

# master 1 (undergrad, 2018-04 / 2018-06): Orientation selectivity in a ring model of the primary visual cortex

I created a ring model that performs orientation discrimination tasks, using an hybrid model of convolutionnal and recurrent networks. This work was, to our knowledge, the first visual ring model based on deep learning techniques.

The recurrence in the network plays a role akin to that of lateral interactions within the primary visual cortex. We have shown in this work that these lateral interactions provide robustness to noisy inputs in the model, which we infer to also be the  the case in the brain.
To verify this assessment, I designed a 2-outcome discriminative psychophysics task (2AFC) and compared various metrics for human and model trials. The results showed that the lateral interactions allowed human-like performance, which is a strong qualitative argument in favor of the biological plausiblity of this model.

 * all material is available @ https://github.com/hugoladret/InternshipM1
