---
date: 2020-12-07 00:00:00

summary: 'Robots aériens agiles bio-mimetiques pour le vol en conditions réelles'

authors:
- emmanuel-daucé
- stéphane-viollet
- ryad-benosman
- laurent-u-perrinet

tags:
- grant
- current-grant

title: ANR AgileNeuRobot (2021/2025)

slides: "2020-12-10_agileneurobot_anr"
---

<!-- youtube-dl https://www.youtube.com/watch\?v\=36CTDiJjQ8I -->

{{< figure src="agile_UAV.jpg" title="An Unmanned aerial vehicle (UAV) flying autonomously in a cluttered environment would require the agility to navigate rapidly by detecting as fast as possible potential obstacles, as represented here by the collision zone, given a cruising speed, associated to slow or fast latencies (respectively red and blue shaded areas). This project will provide with a novel neuromorphic architecture designed to meet these requirements thanks to an event-based, two-way processing." numbered="true" >}}

## Fiche d'identité

* Acronyme : AgileNeuRobot (ANR-20-CE23-0021)
* Titre : Robots aériens agiles bio-mimetiques pour le vol en conditions réelles
* *Title : Bio-mimetic agile aerial robots flying in real-life conditions*
* CES : CE23 - Intelligence Artificielle / Instrument de financement : Projet de recherche collaborative (PRC) / Catégorie R&D : Recherche fondamentale
* Coordinateur Scientifique : PERRINET Laurent (UMR7289)
* Durée: 4 ans, à partir du 1er mars 2021 - 1er décembre 2025
* Budget total: 435 k€
* Responsables Scientifiques : Stéphane Viollet (BioRobotique, Inst Sciences Mouvement), Ryad Benosman (Inst de la Vision ) | Laurent Perrinet (NeOpTo, Inst Neurosciences de la Timone, coordinateur)

{{< figure src="event_driven_computations.png" title="A miniature, event-based ATIS sensor. Contrary to a classical frame-based camera for which a full dense image representation is given at discrete, regularly spaced timings, the event-based camera provides with events at the micro-second resolution. These are sparse as they represent luminance increments or decrements (ON and OFF events, respectively)." numbered="true" >}}

## Résumé
Des robots aériens autonomes seraient des outils essentiels dans les opérations de recherche et de sauvetage. Toutefois, voler dans des environnements complexes exige un haut niveau d'agilité, ce qui implique par exemple la capacité de déclencher des manœuvres agressives pour esquiver les obstacles: Les caméras et algorithmes d'intelligence artificielle conventionnels n'ont pas ces capacités. Dans ce projet, nous proposerons une solution associant de manière bio-inspirée une dynamique rapide de détection visuelle et de stabilisation. Nous intégrerons ces différents aspects dans un système neuromorphique événementiel de bout en bout. La clé de cette approche est l'optimisation des délais du système par traitement prédictif. Ceci permettra de voler indépendamment, sans aucune intervention de l'utilisateur. Notre objectif à plus long terme est de satisfaire ces besoins avec un minimum d'énergie et de fournir des solutions novatrices aux défis des algorithmes traditionnels d'IA.

{{< figure src="principe_agile.jpg" title="Our system is divided into 3 units to process visual inputs (ATIS) until the rotors: the ***C***amera, ***P***rocessor and ***M***otor units. Each represents respectively multi-channel feature maps ($C_i$), an estimate of the depth-of-field ($P$) and a navigation map, for instance time-of-contacts on a polar map ($M$). Compared to a discrete-time pipeline, we will design an integrated, back-to-back event-driven system based on a fast, two-way processing between the ***C***, ***P*** and ***M*** units. Event-driven, feed-forward and feed-back communications are denoted respectively in yellow, black and red. Notice the attention module $A$ from $P$ to $C$ and the feed-back of navigation information from $M$ and the IMU to $P$." numbered="true" >}}

## Abstract
Autonomous aerial robots would be essential tools in search and rescue operations. But flying in complex environments requires a high level of agility, which implies the ability to initiate aggressive maneuvers to avoid obstacles: Conventional AI cameras and algorithms do not have these capabilities. In this project, we propose a solution that will integrate bio-inspired rapid visual detection and stabilization dynamics into an end-to-end event based neuromorphic system. The key to this approach will be the optimization of delays through predictive processing. This will allow these robots to fly independently, without any user intervention. Our longer-term goal is to meet the requirements with very little power and provide innovative solutions to the challenges of traditional AI algorithms.

## Acknowledgement

This work was supported by ANR project "AgileNeuRobot" N° ANR-20-CE23-0021.
