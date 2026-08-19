--- 
slides:
  theme: white
  transition: fade
date: '2024-11-18'
all_day: false
publishDate: '2024-11-03T12:47:11+02:00'
title: 2024-11-18-journee-biomometisme
summary: 'NeuroAI: interactions multiples entre Neurosciences et Intelligence artificielle'
tags:
- eye-movements
- neuromorphic-computing
- spiking-neural-networks
- visual-illusions
categories:
- Computational Neuroscience
- Education
- NeuroAI & Machine Learning
projects:
- tout-public
---
<section>
<h2><u>
	[2024-11-18] NeuroAI: interactions multiples entre Neurosciences et Intelligence artificielle
</u></h2>
<table>
<tr>
	<a href="https://laurentperrinet.github.io/grant/anr-anr"> 
		<img src="https://laurentperrinet.github.io/grant/anr-anr/header.png" alt="header" height="300"> 
	</a>
</tr>
<tr>
	<th>
		<a href="https://laurentperrinet.github.io/slides/2024-11-18-journee-biomometisme/?transition=fade"> <i> Laurent Perrinet </i> </a> - <a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>
	    <br>
	</th>
	<th>
		  <img src="https://laurentperrinet.github.io/grant/anr-anr/featured.png" alt="ANR" height="80" width="80">
	</th>
</tr>
</table>

{{< speaker_note >}}
- outline = 

 - Bonjour. Je suis Laurent Perrinet, directeur de recherche CNRS en neurosciences computationnelles à l'Institut de Neurosciences de la Timone à Marseille. Je vous remercie pour cette invitation à participer à cette Journée Scientifique "Biomimove 2024 : Action, Perception et Traitement" à la croisée entre robotique et science du vivant.  

- Les neurosciences computationnelles sont les sciences qui essaient d’extraire de nos connaissances en neurosciences biologiques des principes computationnels, comme le neurone formel et sa capacité d’apprentissage, qui est la brique de base des réseaux de neurones. Ces derniers ont conduit à la révolution de l’IA avec les réseaux profonds.

 - Je suis convaincu que nous sommes au tournant d'une nouvelle ère dans le développement des systèmes embarqués, où l'intelligence artificielle a le potentiel de créer des innovations disruptives à la hauteur des performances de l’intelligence naturelle et pour lesquelles il est essentiel de s'inspirer des neurosciences biologiques. 

 - C'est pourquoi je suis très heureux de vous présenter en premier lieu le projet ANR AgileNeuRobot, un projet de recherche interdisciplinaire visant à développer des robots aériens agiles bio-mimétiques pour le vol en conditions réelles.

 Dans cette optique, afin de caractériser certains enjeux de l'IA embarquée, notamment dans le domaine du spatial, je vais vous présenter deux leviers s'inspirant de la biologie et illustrant comment les neurosciences peuvent faire avancer le domaine de façon radicale. L'intégration de connaissances biomimétiques dans les engins embarqués peut améliorer leur résilience et leur adaptabilité face aux environnements hostiles, tout en réduisant la consommation d'énergie. Je serais ravi d'engager ensuite une discussion avec vous sur ces sujets et d'échanger sur vos propres expériences et perspectives.

{{< /speaker_note >}}

</section>

---

<section>

## AgileNeuRobot: Fiche d'identité

* Titre : Robots aériens agiles bio-mimetiques pour le vol en conditions réelles
* *Title : Bio-mimetic agile aerial robots flying in real-life conditions*
* CES : CE23 - Intelligence Artificielle (ANR-20-CE23-0021)
* Durée: 4 ans, du 1er Octobre 2021 au 30 Septembre 2025
* Budget total: 435 k€
{{< speaker_note >}}

Le projet ANR AgileNeuRobot est donc un projet interdisciplinaire financé par l'Agence Nationale de la Recherche (ANR) dans le cadre de l'appel à projets « Intelligence Artificielle » (ANR-20-CE23-0021). Il vise à développer des robots aériens agiles bio-mimétiques pour le vol en conditions réelles sur une période de 4 ans, du 1er octobre 2021 au 30 septembre 2025. Il est financé à hauteur de 435 k€ et représente un exemple convaincant de l'impact potentiel des neurosciences computationnelles sur les systèmes embarqués dans le domaine des robots aériens autonomes.
{{< /speaker_note >}}

---
## AgileNeuRobot: Consortium:
<img src="https://laurentperrinet.github.io/author/stéphane-viollet/avatar.jpg" alt="SV" height="150"> | <img src="https://laurentperrinet.github.io/author/ryad-benosman/avatar.jpg" alt="RB" height="150"> | <img src="https://laurentperrinet.github.io/author/laurent-u-perrinet/avatar.png" alt="LP" height="150">
------ | ------ | ------
Stéphane Viollet | Ryad Benosman | Laurent Perrinet
Julien Diperi | Sio-Hoï Ieng | Emmanuel Daucé
Post-doc 1 | Post-doc 2 | PhD ([JN Jérémie](https://laurentperrinet.github.io/author/jean-nicolas-j%C3%A9r%C3%A9mie/))
Inst Sciences Mouvement | Inst de la Vision | Inst Neurosci de la Timone

{{< speaker_note >}}

Le projet AgileNeuRobot est un projet que je coordonne en collaboration avec plusieurs institutions :

- l'Inst Sciences du Mouvement pour la partie robotique bio-inspirée,
- l'Institut de la Vision pour le développement de nouveaux capteurs.
- l'Institut de Neurosciences de la Timone (Aix-Marseille Université) pour l’aspect théorique et l'intégration de ces disciplines.

Ensemble, nous travaillons à la fois sur les aspects techniques et scientifiques pour créer ces robots aériens. Ce projet a pour but de contribuer non seulement au développement de nouvelles technologies, mais aussi à la compréhension et à l'élaboration de nouveaux modèles théoriques pour expliquer les mécanismes naturels sous-jacents aux capacités d'adaptabilité et d'apprentissage des systèmes biologiques.

{{< /speaker_note >}}

---
## AgileNeuRobot: Agile = Performant et efficace

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/principe_agile.jpg" title="The system includes 3 units to process event-driven visual inputs communicating by feed-forward and feed-back paths." numbered="true" >}}

{{< speaker_note >}}

Le système en développement est un exemple de robotique bio-inspirée. Il est conçu pour être capable de traiter des données visuelles en temps réel et de réagir rapidement aux changements de l'environnement, notamment pour éviter ou intercepter des objets en vol.

- performance : garder une bonne acuité tout en répondant rapidement et presque immédiatement.

- efficacité : des besoins réduits en énergie pour un fonctionnement autonome.

Pour cela, nous avons utilisé une architecture inspirée des insectes qui combine des capteurs événementiels avec des réseaux de neurones impulsionnels pour créer un système agile et performant, que je vais décrire dans la suite de l’exposé.

Mais d'abord, je voudrais souligner deux contraintes majeures de ce type de systèmes embarqués :

{{< /speaker_note >}}

</section>

---

<section>

## Enjeux de l'IA embarquée : latence de réponse

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies [[Grimaldi *et al*, 2022]](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)" width="55%" >}}

{{< speaker_note >}}
Tout d’abord, les systèmes sensoriels biologiques sont composés de séquences de traitement qui possèdent des délais de traitement. Je décris ici la chaîne de traitement d’une image visuelle, ici pour un enfant jouant à un jeu video et devant cliquer sur le bon bouton, et qui illustre les différentes latences du traitement de l’information de la vision à l’action.

Si les délais dans un système embarqué sont plus rapides, il reste que les informations dans les différentes étapes de traitement peuvent être décalées et nécessitent un traitement adapté afin de répondre de la façon la plus immédiate possible. Je pense notamment à la détection d'objets en mouvement très rapide dans le cadre d'un robot en mouvement.
{{< /speaker_note >}}

---
## Enjeux de l'IA embarquée : budget énergétique

{{< figure src="/grant/anr-anr/prototype.jpg" title="Prototype avec caméra événementielle et calculateur."  width="50%" >}}

{{< speaker_note >}}

Deuxième contrainte liée à la première : la consommation énergétique.

Je vous présente ici une photo de notre premier prototype qui inclut, en plus des équipements classiques d'un robot aérien (capteurs de hauteur, accéléromètres, calculateur de navigation), différentes caméras ainsi qu’un calculateur dédié.

Il faut comprendre que ces équipements additionnels consomment une énergie non négligeable. Cela implique de dimensionner correctement la batterie, ce qui a pour effet d'augmenter les besoins énergétiques pour le vol lui-même. 

Je vais proposer deux leviers, inspirés de la biologie, pour faire avancer le domaine de façon radicale (pas juste gagner 30 %), mais pour passer à une autre échelle.

{{< /speaker_note >}}

</section>

---
<section>

## Levier #1: Réseaux de neurones impulsionnels (SNNs)

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/event_driven_computations.png" title="From frame-based to event-based cameras." numbered="true" >}}

{{< speaker_note >}}

- Nouvelles caméras : basées sur la même technologie qu’un CMOS, mais au lieu de récolter à intervalles réguliers l’ensemble des valeurs de luminance sur tous les pixels, chaque pixel est indépendant.

- le mode de représentation de l'information est différent : le signal consiste à émettre un événement si et seulement si un changement a été observé par ce pixel, ce qui est représenté ici par ces flux d’événements. 
{{< /speaker_note >}}
---
## Levier #1: Réseaux de neurones impulsionnels (SNNs)

| Sensor           | Range   | Framerate   | Resolution  | Power |
|------------------|---------|-------------|-------------|-------|
| Human eye        | 60 (?) dB | 300 (?) fps | 100 (?) Mpx | 10 mW |
| DSLR             | 44.6 dB | 120     fps | 2--20   Mpx | 30  W |
| Ultra-high speed | 64   dB | 10^4 fps    | 0.3--4  Mpx | 300 W |
| Event-based      | 120  dB | 10^6 fps    | 0.1--2  Mpx | 30 mW |

{{< speaker_note >}}

Les caméras événementielles présentent plusieurs propriétés qui les rendent remarquables. Tout d'abord, la précision temporelle des événements est de l'ordre de la microseconde, ce qui permet d'atteindre une cadence théorique de l'ordre du million d'images par seconde. On peut la comparer à celle d'une caméra classique, qui est de l'ordre de la centaine d'images par seconde, ou à celle d'une caméra à grande vitesse, qui peut atteindre 10 000 images par seconde. Il est difficile d'estimer la fréquence d'échantillonnage de la perception humaine, car si 25 images par seconde sont souvent suffisantes pour visionner un film, il a été démontré que l'œil humain peut distinguer des détails temporels jusqu'à la milliseconde. 

Une autre caractéristique importante de ces caméras est leur capacité à détecter une très large gamme de luminosité, dépassant de loin celle des caméras conventionnelles à 120 dB (un facteur d'un million, comparé au facteur de un sur mille de l'œil humain entre la pleine lune et le soleil),

Il convient de noter que la résolution spatiale de ces caméras est souvent relativement modeste, de l'ordre du mégapixel. Cependant, il ne s'agit pas d'une limitation technique, mais plutôt d'une conséquence des applications technologiques dans lesquelles ces caméras sont couramment utilisées. 

Par rapport aux caméras classiques, qui consomment plusieurs watts, les caméras événementielles consomment très peu d'énergie électrique, de l'ordre de 10 milliwatts, soit une consommation équivalente à celle de l'œil humain. 
https://en.wikipedia.org/wiki/Event_camera#Functional_description

{{< /speaker_note >}}
---

## Levier #1: Réseaux de neurones impulsionnels (SNNs)

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/HDSNN_conv.png" width="50%" >}}{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="The HD-SNN neural network [[Grimaldi *et al*, 2023]](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="50%" >}}

{{< speaker_note >}}

- Ces caméras ne présentent que des avantages, mais alors, comment traiter cette nouvelle représentation des données ? En effet, les neurosciences montrent que les neurones ne manipulent pas des données continues (comme ceux du deep learning), mais communiquent exactement de la même manière en échangeant de brèves impulsions prototypiques, les potentiels d’action (spikes).

- Notre solution : une architecture similaire au deep learning, mais chaque neurone (brique élémentaire) est un modèle simplifié de neurone biologique impulsionnel. Cependant, nous nous retrouvons avec un problème par rapport à l’établissement que nous avons réussi à résoudre théoriquement. Un avantage supplémentaire est que ce genre de calcul est actuellement développé sur des puces embarquées (comme les pixels de la caméra évanementielle).

- notre architecture fonctionne ainsi directement sur cette même représentation. Un autre avantage : le « always on computing ».

Quels résultats ? Peut-on les évaluer avant d'avoir ces puces ? 
{{< /speaker_note >}}

---
## Levier #1: Réseaux de neurones impulsionnels (SNNs)

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/accuracy.png" title="The HD-SNN neural network [[Grimaldi *et al*, 2023]](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

Time-to-Contact maps [[Nunes *et al*, 2023]](https://laurentperrinet.github.io/publication/nunes-23-iccv)

{{< speaker_note >}}
**2 MINUTES**

- Nos simulations montrent ainsi une très grande efficacité (ici pour catégoriser un type de flux optique, ce qui peut guider la navigation).  

- un aspect innovant de notre technologie réside dans notre capacité à utiliser autant de neurones, mais moins de connexions. Nous avons par ailleurs montré que l’efficacité restait acceptable. Par rapport à une technologie classique (en orange) qui montre une baisse rapide, nos résultats montrent une bonne efficacité avec une demi-valeur critique donnée pour un gain de 700x (noter l’axe log). C’est ce qu’on appelle le « frugal computing » et nous œuvrons maintenant à son implémentation dans un PEPR IA.

- c’est une étape importante, mais on peut aller plus loin, et je vais vous présenter un deuxième levier : éviter de tout traiter pour ne traiter que ce qui est nécessaire.

{{< /speaker_note >}}

</section>

---

<section>

## Levier #2: Vision active / *Active Vision*
{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24-ccn/featured.png" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-25)]" width="100%" >}}

{{< speaker_note >}}
Pour cela, je vais d’abord l’illustrer par le travail du chercheur russe Yarbus au début du siècle dernier.  Lorsqu’on présente une scène visuelle à un observateur (comme dans le cas de cette peinture sur le panneau A) – celui-ci va effectuer une série de sauts dans cette image, qu’on appelle saccades. 

En effet, notre vision possède cette propriété d’être focalisée, de telle sorte qu’une majeure partie de notre vision est concentrée suivant notre axe de vision. Cette propriété a co-évolué avec la capacité à effectuer des mouvements rapides des yeux et confère un avantage évolutif aux prédateurs qui peuvent agir plus rapidement sur leur environnement pour attraper une proie.

{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/featured.jpg" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-25/)]" width="65%" >}}

{{< speaker_note >}}
Cette capacité d’agir sur l’entrée sensorielle, et notamment d’avoir une capacité attentionnelle de cette sorte, est largement absente des approches classiques de l’apprentissage machine et nous avons pu l’implanter grâce au projet ANR. 

Pour cela, nous avons utilisé une transformée de type log-polaire qui concentre l’information autour de l’axe de vision, comme on peut le voir à l’intérieur de la zone matérialisée par la zone grise. Notez également l’importance du point sur lequel se pose le regard, notamment s'il est éloigné ou proche de l’objet d’intérêt.
{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/fig_attack_rotation_imagenet.png" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-25/)]" width="90%" >}}

{{< speaker_note >}}
**2 MINUTES**

- de façon surprenante, malgré la perte de résolution en périphérie, nous obtenons des résultats comparables à l’état de l’art, mais plus robustes aux rotations et zooms.

- il est important de noter qu’il peut traiter des images arbitraires en taille, ce qui constitue une limite importante des CNNs actuels.

- Une perspective en cours est d’abord d’adapter cette capacité aux SNN, mais aussi...

{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/fig_areadne.png" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-25/)]" width="90%" >}}

{{< speaker_note >}}
**2 MINUTES**

- d’inclure des saccades, c’est-à-dire de compléter le système que je viens de présenter et qui permet d’identifier des objets dans une image, par un système qui permet d’anticiper ou de regarder dans une image. 
Cette division du travail est inspirée des voies pariétales et dorsales du système visuel chez l'être humain.

- PEPR IA : les multiples saccades et l'attention

- comment intégrer ces deux leviers dans un système embarqué ? 

{{< /speaker_note >}}

</section>

---

<section>

<h2><u>
	[2024-11-18] NeuroAI: interactions multiples entre Neurosciences et Intelligence artificielle
</u></h2>
<table>
<tr>
	<a href="https://laurentperrinet.github.io/grant/anr-anr"> 
		<img src="https://laurentperrinet.github.io/grant/anr-anr/header.png" alt="header" height="300"> 
	</a>
</tr>
<tr>
	<th>
		<a href="https://laurentperrinet.github.io/slides/2024-11-18-journee-biomometisme/?transition=fade"> <i> Laurent Perrinet </i> </a> - <a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>
	    <br>
	</th>
	<th>
		  <img src="https://laurentperrinet.github.io/grant/anr-anr/featured.png" alt="ANR" height="80" width="80">
	</th>
</tr>
</table>
{{< speaker_note >}}

- résumé : l'IA embarquée implique des enjeux importants.
- les neurosciences peuvent apporter une contribution majeure pour résoudre les enjeux de l'IA embarquée.
- un objectif : acquérir une indépendance scientifique = projet « Active Loop » pour lequel je cherche des partenaires.

{{< /speaker_note >}}
</section>