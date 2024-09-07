---
 slides:
 # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  transition: 'fade'

# Talk start and end times. 2023-05-13-master-m-4-nc
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2024-09-09'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2024-09-06T12:47:11+02:00"

title: 2024-09-09_agileneurobot_anr

summary: Robots aériens agiles bio-mimetiques pour le vol en conditions réelles: Enjeux pour l'IA embarqué

# printing = https://revealjs.com/pdf-export/
---
<section>

<a href="https://laurentperrinet.github.io/grant/anr-anr">
<img src="https://laurentperrinet.github.io/grant/anr-anr/header.png" alt="header" height="450">
</a>
<table>
<tr>
	<th>
		<i> Laurent Perrinet (<a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>)</i>
    <br>
		<a href="https://laurentperrinet.github.io/slides/2024-09-09_agileneurobot_anr/?transition=fade">
			<u>[2024-09-09] ➡️ Enjeux pour l'IA embarquée</u>
		</a>
	</th>
	<th>
  <img src="https://laurentperrinet.github.io/grant/anr-anr/featured.png" alt="ANR" height="80">
	</th>
</tr>
</table>

{{< speaker_note >}}
- outline = 
 - Bonjour. Je suis Laurent Perrinet, chercheur en neurosciences computationnelles à l'Institut de Neurosciences de la Timone. Je vous remercie pour l'invitation à participer à cette table ronde sur l'IA embarquée dans le domaine spatial. Je suis convaincu que nous sommes au tournant d'une nouvelle ère dans le développement des systèmes embarqués, où l'intelligence artificielle va permettre de créer des innovations disruptives mais pour lesquelles il est essentiel de mieux comprendre les enjeux et de s'inspirer des neurosciences biologiques. Je suis moi-même un passionné d'aéronautique et de spatial, ce qui m'a amené à suivre l'école d'aéronautique SUPAERO. Et c'est là, grâce à la rencontre avec mon professeur de mathématiques, que j'ai découvert les neurosciences computationnelles et les pouvoirs qu'ils vont avoir pour créer des systèmes embarqués.

 - C'est pourquoi je suis très heureux de vous présenter le projet ANR AgileNeuRobot qui est un projet de recherche interdisciplinaire qui vise à développer des robots aériens agiles bio-mimétiques pour le vol en conditions réelles. L'apprentissage automatique et les réseaux neuronaux peuvent être utilisés pour analyser des données sensorielles massives provenant d'instruments spatiaux, permettant ainsi une meilleure compréhension de l'univers en évolution constante.

 -  Afin de caractériser quelques enjeux de l'IA embarquée, notamment dans le domaine du spatial, je vais vous présenter deux leviers inspirés de la biologie qui illustreront comment les neuroscien ces peuvent faire avancer le domaine de façon radicale. L'intégration de systèmes biomimétiques dans les engins spatiaux peut améliorer leur résilience et leur adaptabilité face aux environnements hostiles, tout en maitrisant la consommation d'énergie. Je serais ravi d'engager ensuite une discussion avec vous sur ces sujets et échanger sur vos propres expériences et perspectives dans ce domaine passionnant.

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

Le projet ANR AgileNeuRobot est donc un projet interdisciplinaire financé par l'Agence Nationale de la Recherche (ANR) dans le cadre de l'appel à projets "Intelligence Artificielle" (ANR-20-CE23-0021). Il vise à développer des robots aériens agiles bio-mimétiques pour le vol en conditions réelles sur une période de 4 ans, du 1er octobre 2021 au 30 septembre 2025. Le projet bénéficie d'un budget total de 435 k€ et représente un exemple convaincant de l'impact potentiel des neurosciences computationnelles sur les systèmes embarqués dans le domaine de l'aéronautique et spatiale.

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

Le projet AgileNeuRobot est une collaboration entre plusieurs institutions, dont :

Inst Sciences Mouvement pour l'aspect robotique bio-inspirée
Inst de la Vision pour l'aspect nouveaux senseurs
L'Institut de Neurosciences de la Timone (Aix-Marseille Université) pour l'intégration de ces disciplines

Ensemble, nous travaillons à la fois sur les aspects techniques et scientifiques pour créer des robots aériens agiles bio-mimétiques qui seront capables d'effectuer des tâches complexes dans un environnement réel. Ce projet vise à contribuer non seulement au développement de nouvelles technologies, mais aussi à la compréhension et l'élaboration de nouveaux modèles théoriques pour expliquer les mécanismes naturels sous-jacents aux capacités d'adaptabilité et d'apprentissage des systèmes biologiques.

{{< /speaker_note >}}

---
## AgileNeuRobot: Agile = Performant et efficace

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/principe_agile.jpg" title="The system includes 3 units to process event-driven visual inputs communicating by feed-forward and feed-back paths." numbered="true" >}}

{{< speaker_note >}}

Le système en développement est un exemple de robotique bio-inspirée qui combine des capteurs événementiels avec des réseaux de neurones impulsionnels pour créer un système agile et performant. Le système est conçu pour être capable de traiter des données visuelles en temps réel et de réagir rapidement aux changements de l'environnement. Il est également capable d'apprendre de nouvelles tâches et de s'adapter à des situations imprévues, ce qui en fait un outil puissant pour la recherche en robotique et en intelligence artificielle.

- performance : HD tout en gardant une réponse rapide et immédiate

- énergie : 

{{< /speaker_note >}}

</section>

---

<section>

## Enjeux de l'IA embarquée : latence de réponse

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies [[Grimaldi *et al*, 2022]](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)" width="75%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

---
## Enjeux de l'IA embarquée : budget énergétique

{{< figure src="/grant/anr-anr/prototype.jpg" title="Prototype avec caméra événementielle et calculateur."  width="50%" >}}

{{< speaker_note >}}



Je vais proposer deux leviers inspirés de la biologie pour faire avancer le domaine de façon radicale (pas juster gagner 30%) mais passer à une autre échelle.

{{< /speaker_note >}}

</section>

---
<section>

## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/event_driven_computations.png" title="From frame-based to event-based cameras." numbered="true" >}}

{{< speaker_note >}}

- nouvelles caméras : avantages en SNR  / latence / énergie

- le représentation de l'information est différente

- comment traiter ces données?

{{< /speaker_note >}}


---
## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

| Sensor           | Range   | Framerate   | Resolution  | Power |
|------------------|---------|-------------|-------------|-------|
| Human eye        | 60 (?) dB | 300 (?) fps | 100 (?) Mpx | 10 mW |
| DSLR             | 44.6 dB | 120     fps | 2--20   Mpx | 30  W |
| Ultra-high speed | 64   dB | 10^4 fps    | 0.3--4  Mpx | 300 W |
| Event-based      | 120  dB | 10^6 fps    | 0.1--2  Mpx | 30 mW |

{{< speaker_note >}}

There are several properties of event-driven cameras that make them remarkable. First of all, the *temporal precision* of events is of the order of microseconds, enabling a theoretical frame rate of the order of a million images per second to be reached. This can be compared with a conventional camera, which is of the order of a hundred images per second, or with a high-speed camera, which can reach 10,000 images per second. It is difficult to estimate the sampling frequency of human perception, because while 25 frames per second is often sufficient for movie viewing, it has been shown that the human eye can distinguish temporal details up to 300 or even 1,000 frames per second. It's worth noting that the *spatial resolution* of these event cameras is often relatively modest, in the order of megapixels, but this is not a technical limitation, but rather due to the technological applications in which these cameras are commonly used. Compared with conventional cameras, which will consume several watts, event cameras consume very little electrical *energy*, in the order of 10 milliwatts, a consumption equivalent to that of the human eye.  Another important feature of these cameras is their ability to detect a very wide *range* of luminosity, far exceeding that of conventional cameras at 120 dB (a factor of a million, compared with the human eye's factor of 1 in a thousand between full moon and full sun),

https://en.wikipedia.org/wiki/Event_camera#Functional_description

{{< /speaker_note >}}


---


## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/HDSNN_conv.png" width="50%" >}}{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="The HD-SNN neural network [[Grimaldi *et al*, 2023]](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="50%" >}}

{{< speaker_note >}}

- notre solution: une architecture similaire au deep learning

- mais chaque neurone (brique élémentaire) est un modèle simplifié de neurone biologique qui se trouve sur des puces embarquées (comme es pixels de la caméra évanementielle)

- un avantage: always on computing

quels résultats ? peut-on les évaluer avant d'avoir ces puces? 
{{< /speaker_note >}}

---
## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/accuracy.png" title="The HD-SNN neural network [[Grimaldi *et al*, 2023]](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

Time-to-Contact maps [[Nunes *et al*, 2023]](https://laurentperrinet.github.io/publication/nunes-23-iccv)

{{< speaker_note >}}
**2 MINUTES**

- nos simualations montrent 

- frugal computing / implémentation maintenant dans un PEPR IA

- deuxieme levier : éviter de tout traiter pour ne traiter que ce qui est nécessaire

{{< /speaker_note >}}

</section>

---

<section>

## Levier #2: Vision active / *Active Vision*


{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24-ccn/featured.png" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-24)]" width="100%" >}}

{{< speaker_note >}}


{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24/featured.jpg" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-24/)]" width="75%" >}}

{{< speaker_note >}}


{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24/fig_attack_rotation_imagenet.png" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-24/)]" width="90%" >}}

{{< speaker_note >}}
**2 MINUTES**

- même réultats qu'un CNN - mais plus robustes aux rotations / zooms

- peut traiter des images arbitraires en taille


- perspective en cours adapter aux SNN - et maintenant ...

{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24/fig_areadne.png" title="[[Jérémie *et al*, 2024](https://laurentperrinet.github.io/publication/jeremie-24/)]" width="90%" >}}

{{< speaker_note >}}
**2 MINUTES**

- saccades

- PEPR IA : multiples saccades et attention

- comment intégrer ces deux leviers dans un système embarqué? 

{{< /speaker_note >}}

</section>

---

<section>

<a href="https://laurentperrinet.github.io/grant/anr-anr">
<img src="https://laurentperrinet.github.io/grant/anr-anr/header.png" alt="header" height="450">
</a>
<table>
<tr>
	<th>
		<i> Laurent Perrinet (<a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>)</i>
    <br>
		<a href="https://laurentperrinet.github.io/slides/2024-09-09_agileneurobot_anr/?transition=fade">
			<u>[2024-09-09] ➡️ Enjeux pour l'IA embarquée</u>
		</a>
	</th>
	<th>
  <img src="https://laurentperrinet.github.io/grant/anr-anr/featured.png" alt="ANR" height="80">
	</th>
</tr>
</table>

{{< speaker_note >}}

- résumé: l'IA embarqué implique des enjeux importants
- les neurosciences peuvent approter pour résoudre ces enjeux de l'IA embarquée
- un objectif : acquérir une indépendance scientifique = projet "Active Loop" pour lequel je cherche des partenaires

{{< /speaker_note >}}
</section>
