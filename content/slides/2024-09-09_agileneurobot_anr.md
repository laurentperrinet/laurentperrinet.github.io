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
	<th><a href="https://laurentperrinet.github.io/slides/2024-09-09_agileneurobot_anr">
		Robots aériens agiles bio-mimetiques pour le vol en conditions réelles - L. Perrinet
    <br>
		<u>[2024-09-09] Enjeux pour l'IA embarquée</u>
	</a>
	</th>
	<th>
  <img src="https://laurentperrinet.github.io/grant/anr-anr/featured.png" alt="ANR" height="80">
	</th>
</tr>
</table>

{{< speaker_note >}}
- outline = 
 - fact: paradoxically vision is a complex process for the simplest function
 - objective= understand biological vision
 - interaction between artificial and natural NNs...
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


{{< /speaker_note >}}

---
## AgileNeuRobot: le Principe Agile = Performant et efficace

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/principe_agile.jpg" title="Our system is divided into 3 units to process visual inputs communicating by event-driven, feed-forward and feed-back communications." numbered="true" >}}

{{< speaker_note >}}

- performance : HD tout en gardant une réponse rapide et immédiate

- énergie : 

{{< /speaker_note >}}

</section>

---

<section>

## Enjeux de l'IA embarquée : latence de réponse

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="75%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

---
## Enjeux de l'IA embarquée : budget énergétique

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="75%" >}}

{{< speaker_note >}}


Je vais proposer deux leviers inspirés de la biologie pour faire avancer le domaine de façon radicale (pas juster gagner 30%) mais passer à une autre échelle.

{{< /speaker_note >}}

---
## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/event_driven_computations.png" title="From frame-based to event-based cameras." numbered="true" >}}

{{< speaker_note >}}

- nouvelles caméras : avantages en SNR  / latence / énergie

- le représentation de l'information est différente

- comment traiter ces données?

{{< /speaker_note >}}

</section>

---

<section>

## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/HDSNN_conv.png" title="The HD-SNN neural network." width="60%" >}}
{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="Review on [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)." width="60%" >}}

{{< speaker_note >}}

- notre solution: une architecture similaire au deep learning

- mais chaque neurone (brique élémentaire) est un modèle simplifié de neurone biologique qui se trouve sur des puces embarquées (comme es pixels de la caméra évanementielle)

- un avantage: always on computing

quels résultats ? peut-on les évaluer avant d'avoir ces puces? 
{{< /speaker_note >}}

---
## Levier #1: Réseaux de neurones impulsionnels / *Spiking Neural Networks (SNNs)*

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/accuracy.png" title="The HD-SNN neural network." width="80%" >}}

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


{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24-ccn/featured.png" title="[[Jérémie *et al*, 2023](https://laurentperrinet.github.io/publication/jeremie-24)]" width="90%" >}}

{{< speaker_note >}}


{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24/featured.png" title="[[Jérémie *et al*, 2023](https://laurentperrinet.github.io/publication/jeremie-24/)]" width="90%" >}}

{{< speaker_note >}}


{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24/fig_attack_rotation_imagenet.png" title="[[Jérémie *et al*, 2023](https://laurentperrinet.github.io/publication/jeremie-24/)]" width="90%" >}}

{{< speaker_note >}}
**2 MINUTES**

- même réultats qu'un CNN - mais plus robustes aux rotations / zooms

- peut traiter des images arbitraires en taille


- perspective en cours adapter aux SNN - et maintenant ...

{{< /speaker_note >}}

---
## Levier #2: Vision active / *Active Vision*

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-24/fig_areadne.svg" title="[[Jérémie *et al*, 2023](https://laurentperrinet.github.io/publication/jeremie-24/)]" width="90%" >}}

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
	<th><a href="https://laurentperrinet.github.io/slides/2024-09-09_agileneurobot_anr">
		Robots aériens agiles bio-mimetiques pour le vol en conditions réelles - L. Perrinet
    <br>
		<u>[2024-09-09] Enjeux pour l'IA embarquée</u>
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
