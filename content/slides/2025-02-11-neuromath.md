---
 slides:
 # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  transition: 'fade'

# Talk start and end times. 2023-05-13-master-m-4-nc
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2025-02-11'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2025-02-04T12:47:11+02:00"

title: 2025-02-11-neuromath

summary: "When Cortical Neurons Talk Sideways: Beyond Feedforward Visual Processing"

# printing = https://revealjs.com/pdf-export/
---
<section>
<h2><u>
	[2025-02-11] When Cortical Neurons Talk Sideways: Beyond Feedforward Visual Processing
</u></h2>
<table>
<tr>
	<a href="https://laurentperrinet.github.io/grant/anr-anr"> 
		  <img src="https://laurentperrinet.github.io/grant/polychronies/featured.png" alt="header" height="300"> 
	</a>
</tr>
<tr>
	<th>
		<a href="https://laurentperrinet.github.io/slides/2025-02-11-neuromath/?transition=fade"> <i> Laurent Perrinet </i> </a> - <a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>
	    <br>
	</th>
</tr>
</table>

{{< speaker_note >}}
- outline = 

 - Bonjour. Je suis Laurent Perrinet, directeur de recherche CNRS en neurosciences computationnelles à l'Institut de Neurosciences de la Timone à Marseille. Je vous remercie pour cette invitation à participer à ce séminaire de l'équipe "NeuroMathématique" à la croisée entre mathématiques et science du vivant.  

 - J'ai une formation de ingénieur, ce qui ne me conduisait plus à poursuivre une carrière chez Airbus plutot que de devenir scientifique. encore moins dans un domaine de la biologie, les neurosciences. Mais c'est grâce aux rencontres que j'ai pu faire par l'intermédiaire de mon professeur de mathématiques, Manuel Samuelides, que j'ai pu être sensibiliser avec le monde des réseaux de neurones à la fin de mes études d'ingénieur. 
 
 - C'est aussi grâce à lui que j'ai pu suivre une formation universitaire en sciences congitives (ce qui s'appelle maintenant le CogMaster en 1998), et je voudrais à ce titre rendre hommage à Jean Petitot car C'est pas de son cours de cette formation que j'ai découvert la possibilité de relier les statistiques que l'on trouve dans les images naturel, avec des principes que l'on peut retrouver dans le système nerveux central. Ce fut un vrai déclic, et je tiens aussi à le remercier pour la patience qu'il a eu pour me guider vers les différentes formations que je pouvais suivre pour continuer mon chemin… Ce séminaire constitue donc un réel retour aux sources car je vais pouvoir vous exposer l'avancée de mes recherches depuis mon DEA sur exactement ce sujet !
 

{{< /speaker_note >}}

</section>

---

<section>

# Anatomy of the Human Visual system

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- cut in different levels: Marr (+ Poggio)
- arbitrary, but useful division of labor= computational / algorithm / hardware

- here:
  - dynamics (computational)
  - CNNs (hardware)
  - spiking (algorithm)
  
First: What is the function of vision?
{{< /speaker_note >}}

---

## Anatomy of the Human Visual system

{{< figure src="https://www.readkong.com/static/06/b0/06b09f0235ae7fcf29438ce317c10e60/optogenetic-visual-cortical-prosthesis-9612386-7.jpg" width="61%" >}}

{{< speaker_note >}}
- let's start with the anatomy
{{< /speaker_note >}}

---

## Human Visual system : the HMAX model

{{< figure src="https://i.stack.imgur.com/ZlFnp.png" title="[[Serre and Poggio, 2007](https://biology.stackexchange.com/questions/10955/ventral-stream-pathway-and-architecture-proposed-by-poggios-group)]" width="65%" >}}

{{< speaker_note >}}
- and a model of it...
- CNN, the mother of all deep learning models
{{< /speaker_note >}}

---

## Primary visual cortex

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/scientists.jpg" title="[Hubel & Wiesel, 1962]" width="80%" >}}

{{< speaker_note >}}
- let's zoom in, the basic ingredient is the receptive field
{{< /speaker_note >}}

---

## Primary visual cortex

{{< video src="https://raw.githubusercontent.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/master/figures/ComplexDirSelCortCell250_title.mp4" controls="yes" width="100%" >}}

[Hubel & Wiesel, 1962]

{{< speaker_note >}}
- a single neuron is selective to some visual features...
{{< /speaker_note >}}

---

## Convolutional Neural Nets (CNN)

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- this can be integrated in a hierarchy...
- defining a Convolutional Neural Networks (CNN)
- one layer is a convolution
{{< /speaker_note >}}

---

{{< slide background-image="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg" >}}

<!-- <img src="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg"  width="80%"/> -->

{{< speaker_note >}}

Paysage catalan (Le Chasseur)

{{< /speaker_note >}}

---

## CNN: Topography

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]"width="70%" >}}

{{< speaker_note >}}
- topography?
{{< /speaker_note >}}

</section>

---

<section>

# Challenging the like-to-like hypothesis

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies [[Grimaldi *et al*, 2022]](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)" width="55%" >}}

{{< speaker_note >}}
Tout d’abord, les systèmes sensoriels biologiques sont composés de séquences de traitement qui possèdent des délais de traitement. Je décris ici la chaîne de traitement d’une image visuelle, ici pour un enfant jouant à un jeu video et devant cliquer sur le bon bouton, et qui illustre les différentes latences du traitement de l’information de la vision à l’action.

Si les délais dans un système embarqué sont plus rapides, il reste que les informations dans les différentes étapes de traitement peuvent être décalées et nécessitent un traitement adapté afin de répondre de la façon la plus immédiate possible. Je pense notamment à la détection d'objets en mouvement très rapide dans le cadre d'un robot en mouvement.


{{< /speaker_note >}}

---

## Association field

{{< figure src="content/publication/perrinet-bednar-15/featured.jpg" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="content/publication/perrinet-bednar-15/figure_results.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="content/publication/perrinet-bednar-15/figure_chevrons.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="content/publication/perrinet-bednar-15/figure_chevrons2.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="content/publication/perrinet-bednar-15/figure_results.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

</section>

---
<section>

# Models challenging the like-to-like hypothesis


## CNN: Topography

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]"width="70%" >}}

{{< speaker_note >}}
- topography?
{{< /speaker_note >}}

---

## CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- modifications= adding sparse coding + feedback
{{< /speaker_note >}}


---

## CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/BoutinFranciosiniChavaneRuffierPerrinet20face.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- result= interpretable features
{{< /speaker_note >}}

---

## Convolutional Neural Networks : Topography

{{< figure  src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]"width="70%" >}}

---

## Convolutional Neural Networks : Topography

{{< figure  src="https://github.com/laurentperrinet/2020-09-25_IRPHE/raw/master/figures/PCOMPBIOL-D-19-01811_R2_compressed_FigS4.png" title="[Bosking *et al*, 1997]"width="70%" >}}

---

## A diversity of association fields

{{< figure src="https://laurentperrinet.github.io/publication/franciosini-21/featured.jpg" title="[[Boutin *et al*, 2022](https://laurentperrinet.github.io/publication/franciosini-21/)]" width="90%" >}}

</section>

---

<section>

# Dynamics of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- another important missing feature: time
{{< /speaker_note >}}

---

## Dynamics of vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency_bg.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="75%" >}}

{{< speaker_note >}}
**1 MINUTE**

- In particular in our group, we are interested in dynamics of neural processing

- The visual system is very efficient in generating a decision from the retinal image to the different stages of the visual pathways, here for a macaque monkey, a reaction of finger muscles in about 300 milliseconds.

- the process of categorizing an object takes 10 layers

{{< /speaker_note >}}

---

## Dynamics of vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="75%" >}}

{{< speaker_note >}}
**1 MINUTE**

- the latencies are of similar in the human brain but merely scaled due to the brain size

- as a consequence, it is thought that this efficiency is achieved by spikes that is, brief all-or-none events which are passed in the very large network which forms the brain from assemblies of neurons to others.

{{< /speaker_note >}}

---


## Dynamics of vision

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/tsonga.jpg" title="Sensorimotor delays ([Perrinet & Friston 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))" width="75%" >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---


## Dynamics of vision

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/figure-tsonga.jpg" title="Sensorimotor delays ([Perrinet & Friston, 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))" width="75%" >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---


## Dynamics of vision

{{< video src="https://laurentperrinet.github.io/publication/perrinet-19-temps/flash_lag.mp4" autoplay="yes" >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---

## Dynamics of vision

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov.jpg" width="100%" title="Diagonal markov model ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---

## Dynamics of vision

<!-- {{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/PBP_spatial_readout.mp4"  autoplay="yes" >}}{{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/MBP_spatial_readout.mp4"  autoplay="yes" >}} -->
{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/positional-delay.mp4" autoplay="yes" >}}

Flash-lag effect: MBP ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---

# Dynamics of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

</section>
---
<section>
<h2><u>
	[2025-02-11] When Cortical Neurons Talk Sideways: Beyond Feedforward Visual Processing
</u></h2>
<table>
<tr>
	<a href="https://laurentperrinet.github.io/grant/anr-anr"> 
		  <img src="https://laurentperrinet.github.io/grant/polychronies/featured.png" alt="header" height="300"> 
	</a>
</tr>
<tr>
	<th>
		<a href="https://laurentperrinet.github.io/slides/2025-02-11-neuromath/?transition=fade"> <i> Laurent Perrinet </i> </a> - <a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>
	    <br>
	</th>
</tr>
</table>

{{< speaker_note >}}

- résumé : diversity
- les neurosciences peuvent répondre à ces questions par des modélisations - rôle des mathématiques
- un objectif : passer en dynamique

{{< /speaker_note >}}
</section>