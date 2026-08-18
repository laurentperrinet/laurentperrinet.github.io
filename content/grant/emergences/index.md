---
authors:
- laurent-u-perrinet
date: 2023-10-05 14:00:00
summary: Near-physics emerging models for embedded AI (PhD position, 2023 / 2027).
image:
  caption: Rufous Hummingbird "Super fast little hummer on a scarlet Kunzea plant,
    (thanks for the plant ID, Teddy) El Chorro regional park" photo [Anita Ritenour](https://www.flickr.com/photos/puliarfanita/13322040205)
    - Attribution 2.0 Generic (CC BY 2.0)
  focal_point: Smart
  placement: 2
  preview_only: false
links:
- name: URL
  url: https://emergences.lirmm.fr/
title: Emergences (2023 / 2027)
tags:
- bayesian-modelling
- neuromorphic-computing
- sparse-coding
- spiking-neural-networks
categories:
- Education
- Grants & Funding
- NeuroAI & Machine Learning
---

{{% callout note %}}
TL;DR: Conventional deep learning models consume too much energy. Inspired by biology, we will explore new models that are more energy efficient.
{{% /callout %}}

The [*Emergences* project](https://emergences.lirmm.fr/) aims at advancing the state-of-the art on near-physics emerging models by collaboratively exploring various computation models leveraging physical devices properties. This project will focus on Event-based models, Physics-inspired models and innovative near-physics Machine Learning solutions.
*Emergences* further intends to extend the collaborative research activities beyond the fence of the consortium by means of connecting with other projects of the PEPR IA and other research institutes.

* Pilote: Marina Reyboz, CEA, Research Director
* Co-Pilote: Gilles Sassatelli, CNRS, Research Director
## Latest news

- 2026-01-29 : talk at the PEPR AI meeting {{< cite page="/talk/2026-01-29-emergences" view="4" >}}

- 2025-03-18: PEPR IA Days du 18 au 20 mars à CentraleSupélec.

- 2024-09-26: 2nd workshop meeting in Paris.

- 2024-05-03 : we are hiring ! {{< cite page="/post/2024-05-03_phd-position_focus-of-attention" view="4" >}}

- 2024-03-27 : talk at the PEPR AI meeting {{< cite page="/talk/2024-03-27-emergences" view="4" >}}

- 2023-10-05: Kick-off meeting!

{{< figure src="2024-09-26_paris.png" numbered="false" >}}

## Description of the "*Emergences*" project

Contemporary machine learning (ML) has incurred profound changes in the scientific, societal and economic landscapes alike. After a decade of sustained progress AI as a discipline is still making regular breakthroughs on many fronts, at the expense of an ever-increasing amount of consumption of compute resources. Modern language models feature hundreds of billion parameters and training energy consumption alone likely falls in the GWh range, with a logical forecast worsening the already prohibitive carbon footprint of AI.

Besides the flourishing initiatives aimed at defining AI-friendly digital compute stack, the next logical breakthrough on the horizon is undoubtedly the emergence of disruptive AI compute technologies having improved energy efficiency. This development will likely involve the utilization of models that differ from those traditionally used in ML and exhibit properties that resemble the behavior of physical components, thereby facilitating implementation. 

The *Emergences* project aims at advancing the state-of-the art on near-physics emerging models by collaboratively exploring various computation models leveraging physical devices properties. Efforts will be put on 3 distinct fronts: Event-based models, Physics-inspired models (from physical systems dynamics) and innovative near-physics ML solutions (exploiting device properties). The investigations will be focused on embedded systems for Edge AI that call for increased energy efficiency for inference and learning, which could be incremental. They will apply to several application domains ranging for instance from the monitoring of the environment to health. Other important tasks such as common tools, performance metrics definition and model scalability analysis and will be conducted through as a collaborative transverse initiative.

*Emergences* further intends to extend the collaborative research activities beyond the fence of the consortium by means of connecting with other projects of the PEPR IA and other research institutes, some of which are listed in this proposal. Finally, because of the unavoidable societal and philosophical implications of AI as a whole, *Emergences* will concurrently to the research activities run a track aimed at analyzing and anticipating the impact of its upcoming contributions.

## Description of the PhD project (WP1): *Focus of attention: a sensory-motor task for energy reduction in unsupervised spiking neural networks*

* attention mechanisms based on our cognitive architecture using a dual pathway: {{< cite page="/publication/dauce-20" view="4" >}}

* implementation in a spiking neural network based: {{< cite page="/publication/grimaldi-23-bc" view="4" >}}
{{< figure src="carte_partenaire.jpg" title="Carte des partenaires du projet Emergences." numbered="false" >}}

{{% callout note %}}
L'intelligence artificielle induit des changements profonds dans les paysages scientifiques, économiques, politiques et sociétaux contemporains. Une décennie après sa « renaissance », l'apprentissage automatique continue à réaliser des avancées sur de nombreux fronts, au prix cependant d'une boulimie de ressources informatiques induisant une consommation électrique préoccupante. Les modèles de langage actuels comportent quelques centaines de milliards de paramètres et consomment pour leur entraînement seul plusieurs GWh, ce qui aujourd'hui motive la recherche d'approches (de rupture) plus sobres.
En plus des diverses initiatives visant à développer des composants et systèmes numériques pensés pour l'IA et dotés d'une meilleure efficacité énergétique, des approches disruptives en IA doivent être développées pour viser des gains énergétiques encore plus importants. Cette évolution passera par l'utilisation de modèles différents de ceux utilisés traditionnellement en apprentissage et présentant des propriétés proches des comportements de composants physiques, en facilitant par là-même l'implantation.
Le projet Emergences fait avancer l'état de l'art sur les modèles émergents proches de la physique en explorant de manière collaborative divers modèles de calcul en utilisant les propriétés de différents dispositifs physiques. Les efforts concentrés sur trois fronts distincts : i) les modèles événementiels bio-inspirés pour lesquels des avancées sont réalisées sur la compréhension du fonctionnement de ces modèles et leur optimisation notamment dans le cas d’implémentation sur semiconducteurs (FPGA et ASIC) mais aussi de lois d’apprentissage émergentes (Sparse Forward forward) ou encore sur la parcimonie des données ii) les modèles inspirés de la physique pour lesquelles des premières propositions concrètes de solutions permettant de réaliser des circuits émergent (création d’un testchip, modèles stochastiques, apprentissage continu bayésien, accélération matériel de couches MHA, entre autres) et enfin iii) les solutions d'apprentissage automatique innovantes proches de la physique, avec des propositions d’implémentation d’apprentissage on-chip pour des composants émergents (apprentissage forward-only sur réseaux memristifs, apprentissage multimodal et incrémental). 
Toutes ces investigations sont menées dans un cadre d’expérimentations basés sur des jeu de données et indicateurs de performances décidés communément, et un effort très significatif à l’endroit de la soutenabilité est réalisé avec une méthodologie d’évaluation de l’empreinte environnementale en cours de mise en place. Ainsi Emergences vise à proposer un cadre de travail pour qualifier ses propositions, face à l’état de l’art académique et industriel dans le domaine de l’IA à la périphérie (Edge AI) qui nous sert de référentiel d’analyse.
{{% /callout %}}
## Key figures

 * starting date: September 1, 2023 
 * Duration: 48 months (until August 31, 2027)
 * 14 partners
 * Nb of PhD: 19
 * Nb of Post doc: 13
 * TRL: basic research
 * Total grant requested: 6.8 M€ 

- This work is supported by a public grant overseen by the French National Research Agency (ANR) under the grant number ANR-23-PEIA-0002 EMERGENCES.

{{< figure src="logo_PEPR-IA.png" numbered="false" >}}

![Funded by...](ackno.jpg)