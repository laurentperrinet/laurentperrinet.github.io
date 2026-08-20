---
title: 2024-03-27-emergences.md
date: '2024-03-27'
publishDate: '2024-03-12T07:59:44.385734Z'
categories:
- Computational Neuroscience
- NeuroAI & Machine Learning
- Theoretical Neuroscience
tags:
- motion-perception
- neuromorphic-computing
- primary-visual-cortex
- spiking-neural-networks
- visual-illusions
projects:
- tout-public
slides:
  theme: simple
  reveal_options:
    transition: fade
all_day: false
summary: 'Analyser de larges volumes de données neurobiologiques : modèles émergents
  bio-inspirés, a Seminar at *the Emergences workshop, Autrans, France*'
---
<section>

### [Analyser de larges volumes de données neurobiologiques](https://laurentperrinet.github.io/slides/2024-03-27-emergences/?transition=fade)
####	*[Laurent Perrinet](https://laurentperrinet.github.io)*
####	<u>[[2024-03-27]](https://laurentperrinet.github.io/talk/2024-03-27-emergences) [Emergences workshop, Autrans, France](https://laurentperrinet.github.io/grant/emergences/)</u>

<img src="https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg" alt="logos" height="130"/>

#### [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

{{< speaker_note >}}

*Hello*, can you hear me in the back? First of all, I'd like to *thank* the organizers for this opportunity and all of you for coming.

I'm Laurent Perrinet from the Institut des Neurosciences de la Timone, a joint AMU / CNRS unit, and I'm a computational neuroscientist interested in large-scale models of vision. 

Alors que ce projet vient juste de commencer, je voudrais déjà parler de quelques idées pour l'avenir. En effet, la question peut se poser quant  aux applications futures des puces neuromorphiques qui vont être développées dans le cadre du projet "Emergences". pour ce développement technologique, on va souvent penser à des applications technologiques, comme les voitures autonome ou la vision robotique. Mais il y a aussi des applications qui peuvent viser à la compréhension du fonctionnement du cerveau et de la cognition en général. Et ceci passe par une meilleure connaissance de la façon dont celle-ci est contenues dans l'activité neurale.

If you wish to go further, these slides along with a number of references and useful links are available on my website.

{{< /speaker_note >}}

</section>

---

<section>

## Techniques d'enregistrement de données neurobiologiques

{{< speaker_note >}}
Nous allons passer en revue différentes techniques d'enregistrement de données neurobiologiques et leur évolution au cours du temps. Ensuite, j'évoquerai quelques méthodes d'analyse en donnant des exemples concrets et le lien avec les systèmes neuro morphiques.
{{< /speaker_note >}}

---
### Enregistrement extracellulaire

{{< figure width="80%" src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/scientists.jpg" title="[Hubel & Wiesel, 1962]" >}}

{{< speaker_note >}}
Même si ce ne sont pas les premiers à avoir enregistré l'activité électrique de neurones (ce sont physiologistes allemands Emil du Bois-Reymond et Hermann von Helmholtz au milieu du 19e siècle), David Hubel et Torsten Wiesel ont marqué leur époque. En 1962, ils ont mené des expériences révolutionnaires qui ont permis de comprendre les mécanismes de base de la perception visuelle et ont jeté les bases de la compréhension de l'organisation fonctionnelle du cortex visuel. Leur travail a valu à Hubel et Wiesel le prix Nobel de physiologie ou médecine en 1981.

La technique principale utilisée par Hubel et Wiesel dans leurs expériences était la microélectrode d'enregistrement extracellulaire. Ils ont inséré de fines électrodes dans le cortex visuel primaire (aussi appelé cortex strié) de chats et de singes anesthésiés. Ces électrodes leur ont permis d'enregistrer l'activité électrique des neurones individuels lors de la présentation de stimuli visuels.
{{< /speaker_note >}}
---
### Aire visuelle primaire

{{< figure src="https://www.readkong.com/static/06/b0/06b09f0235ae7fcf29438ce317c10e60/optogenetic-visual-cortical-prosthesis-9612386-7.jpg" width="61%" >}}

{{< speaker_note >}}
L'aire visuelle primaire est une région du cerveau spécialisée dans le traitement des informations visuelles. Située à l'arrière du lobe occipital, elle joue un rôle clé dans la perception visuelle en analysant des caractéristiques telles que l'orientation, la couleur et la taille des stimuli. Son organisation topographique et l'activité électrique de ses neurones permettent la construction d'une représentation visuelle cohérente.
{{< /speaker_note >}}
---

### Enregistrement extracellulaire

{{< video width="100%" src="https://raw.githubusercontent.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/master/figures/ComplexDirSelCortCell250_title.mp4" controls="yes" >}}

[Hubel & Wiesel, 1962]

{{< speaker_note >}}
Hubel et Wiesel ont utilisé une variété de stimuli visuels, tels que des lignes, des barres, des points lumineux et des motifs en mouvement, qu'ils ont présentés à des animaux dans des conditions contrôlées. En enregistrant les réponses des neurones visuels, ils ont pu observer des motifs caractéristiques d'activité neuronale en fonction des propriétés visuelles des stimuli.

Leur travail a révélé l'existence de neurones spécifiques, appelés neurones simples et neurones complexes, qui répondent de manière sélective à des caractéristiques visuelles spécifiques, telles que l'orientation, la direction du mouvement et la taille des stimuli. Ils ont également découvert que ces neurones étaient organisés de manière hiérarchique, avec des neurones simples détectant des caractéristiques visuelles élémentaires et des neurones complexes intégrant ces informations pour former des représentations plus complexes.

mais aussi:  sharp electrodes, patch-clamp

{{< /speaker_note >}}

---
### Multi-électrodes

{{< figure src="https://medtech.citeline.com/-/media/editorial/medtech-insight/2021/12/mt2112_utah_array.jpg" title="[[Microelectrode array (MEAs)](https://en.wikipedia.org/wiki/Microelectrode_array)]" width="90%" >}}

{{< speaker_note >}}
population distribué

peignes, utah array = débit augment proportionnellement au nombre x freq d'echant... 4,8 mégabits par seconde (100 canaux × 30 000 échantillons/seconde × 16 bits).

exemple ladret chat = 100Go
exemple ladret macaque = quelques tera

une aire, à plusieures aires mesoscopique (parler taille cerveau)

{{< /speaker_note >}}

---
### Différentes échelles

{{< figure src="https://laurentperrinet.github.io/talk/2024-03-27-emergences/scales.png" title="[[Chemla *et al*, 2017](https://dx.doi.org/10.1117/1.NPh.4.3.031215)]" width="70%" >}}
{{< speaker_note >}}
imagerie: fMRI, EEG, MEG, MEEG, iEEG, ...

big initiatives: BRAIN, HBP, Human Connectome Project, Allen Institute, Blue Brain Project, OpenWorm, OpenAI, OpenPhilanthropy, OpenCog, OpenMind

{{< /speaker_note >}}

---
### Vers des données massives

{{< figure src="https://laurentperrinet.github.io/talk/2024-03-27-emergences/featured.png" title="[[Stevenson and Kording, 2011](https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC3410539&blobtype=pdf)]" width="90%" >}}
{{< speaker_note >}}

Ian H Stevenson & Konrad P Kording 

{{< /speaker_note >}}

---
### Vers des données massives

{{< figure src="https://www.ucl.ac.uk/neuropixels/sites/neuropixels/files/styles/medium_image/public/neuropixels_1_and_2.png" title="[[Steinmetz *et al*, 2017](https://www.ucl.ac.uk/neuropixels/)]" width="80%" >}}
{{< speaker_note >}}

neuropixel

Compared to Neuropixels 1.0, the 2.0 probe has a smaller, lighter weight package, and is available in single- or four-shank versions allowing even higher density chronic recording in small animal models.. 
The probe features 1280 low-impedance TiN recording sites densely tiled along one thin, 10 mm-long, straight shank, or 5120 electrodes divided over 4 shanks. The 384 parallel, configurable, low-noise recording channels integrated in the base enable simultaneous full band recording of hundreds of neurons.

Données Priebe: utilisation de GPUs... mais jusqu'à quand?

{{< /speaker_note >}}
</section>

---

<section>

## Techniques d'analyse des données neurobiologiques

{{< speaker_note >}}
...
{{< /speaker_note >}}

---
### Méthodes statistiques

{{< figure src="https://laurentperrinet.github.io/publication/ladret-23/featured.png" title="[[Ladret *et al*, 2023](https://laurentperrinet.github.io/publication/ladret-23/)]" width="90%" >}}

{{< speaker_note >}}

https://hugoladret.github.io/publications/ladret_et_al_variance_v1/
depuis les PAs: fréquence de tir (Adrian) donner l'exemple de Ladret
souvent pas suffisantes, c'est de la biologie
rhythmes, connectivité fonctionnelle
manifold churchland
{{< /speaker_note >}}

---
### Méthodes statistiques

{{< figure src="https://hugoladret.github.io/publications/imgs/ladret_et_al_variance_V1_2.png" title="[[Ladret *et al*, 2023](https://laurentperrinet.github.io/publication/ladret-23/)]" width="80%" >}}

{{< speaker_note >}}
Pour donner un peu plus de détails, nous avons conduit ce protocole, afin de comprendre comment des neurones visuel à différentes textures dans les images naturelles.
{{< /speaker_note >}}

---
### Méthodes statistiques

{{< figure src="https://hugoladret.github.io/publications/imgs/ladret_et_al_variance_V1_4.png" title="[[Ladret *et al*, 2023](https://laurentperrinet.github.io/publication/ladret-23/)]" width="80%" >}}

{{< speaker_note >}}
Cette première analyse statistique nous a permis de caractériser la réponse de différents types de neurones, et en particulier de proposer que certains codent pour différents niveaux de précision dans l'image, ce qui est une nouveauté par rapport à la littérature.
{{< /speaker_note >}}

---
### ... et au-delà!

{{< figure src="https://www.thetransmitter.org/wp-content/uploads/2023/11/teach-a-paper.png" title="[[Churchland & Cunningham et al. (2012)](https://www.thetransmitter.org/how-to-teach-this-paper/how-to-teach-this-paper-neural-population-dynamics-during-reaching-by-churchland-cunningham-et-al-2012-3/)]" width="90%" >}}

{{< speaker_note >}}
dans tous ces types d'enregistrement avec plusieurs neurones simultanés, on observe une réponse de population et on doit donc inventer de nouvelles techniques pour analyser ses données.
{{< /speaker_note >}}

---
### ... et au-delà: le décodage

{{< figure src="https://hugoladret.github.io/publications/imgs/ladret_et_al_variance_V1_6.png" title="[[Ladret *et al*, 2023](https://laurentperrinet.github.io/publication/ladret-23/)]" width="90%" >}}

{{< speaker_note >}}
Une autre méthode consiste à utiliser un procédé de décodage qui va appliquer un modèle d'apprentissage machine sur l'ensemble des données. Ici, nous avons utilisé une simple régression logistique. Première incursion dans le machine learning.
{{< /speaker_note >}}

---
### ... et au-delà: le décodage

{{< figure src="https://hugoladret.github.io/publications/imgs/ladret_et_al_variance_V1_7.png" title="[[Ladret *et al*, 2023](https://laurentperrinet.github.io/publication/ladret-23/)]" width="90%" >}}
{{< speaker_note >}}
The next question was: what exactly do these different neurons do? To figure this out, we used a method called neural decoding, which tries to guess what the neurons are “seeing” based on their responses.

{{< /speaker_note >}}

---
### ... et au-delà: le décodage

{{< figure src="https://hugoladret.github.io/publications/imgs/ladret_et_al_variance_V1_8.png" title="[[Ladret *et al*, 2023](https://laurentperrinet.github.io/publication/ladret-23/)]" width="90%" >}}

{{< speaker_note >}}

explicabilité des coefficients
ICA, SVM auto-encoder Gallant
{{< /speaker_note >}}

---
### Brain-Computer Interface (BCI)
{{< figure src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/InterfaceNeuronaleDirecte-fr.svg/2560px-InterfaceNeuronaleDirecte-fr.svg.png" title="[[Interface neuronale directe (BCI)](https://fr.wikipedia.org/wiki/Interface_neuronale_directe)]" width="75%" >}}

{{< speaker_note >}}
potentiels évoqués

motifs / récemment detec vagues 

causal par rapport à ce que fait l'activité (?)
{{< /speaker_note >}}

</section>

---

<section>

## Perspectives et opportunités du neuromorphique

{{< speaker_note >}}
...
{{< /speaker_note >}}

---
### Exploitation d'un timing précis

{{< figure src="https://i.sstatic.net/ixnrz.png" title="[[Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb)]" width="80%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

---
### Exploitation d'un timing précis

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/replicating_MainenSejnowski1995.png" title="[[Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb)]" width="99%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

---
### Exploitation d'un timing précis

{{< figure src="https://laurentperrinet.github.io/publication/kremkow-16/featured.png" title="[[Kremkow *et al*, 2016](https://laurentperrinet.github.io/publication/kremkow-16/)]" width="90%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

---
### Exploitation d'un timing précis

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/Diesmann_et_al_1999.png" title="[[Diesmann et al. 1999](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_3_Diesmann_et_al_1999.py)]" width="99%" >}}
{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

---
### Codage par latence

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/haimerl2019.jpg" title="[[Haimerl et al, 2019](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)]" width="99%" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Codage par latence

{{< figure width="70%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/scheme_thorpe.jpg" title="[[Thorpe (2001)]](https://laurentperrinet.github.io/2022-01-12_NeuroCercle/#/2/1)" >}}

{{< speaker_note >}}
- The visual system is very efficient in generating a decision from the retinal image to the different stages of the visual pathways, here for a macaque monkey, a reaction of finger muscles in about 300 milliseconds.

- the process of categorizing an object takes 10 layers
{{< /speaker_note >}}

---

### Latences et rapidité

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="75%" >}}

{{< speaker_note >}}
**1 MINUTE**

- the latencies are of similar in the human brain but merely scaled due to the brain size

- as a consequence, it is thought that this efficiency is achieved by spikes that is, brief all-or-none events which are passed in the very large network which forms the brain from assemblies of neurons to others.

{{< /speaker_note >}}
</section>

---

<section>

## Algorithmes neuromorphiques

{{< speaker_note >}}
...
{{< /speaker_note >}}

---
### Always-on classification using HOTS

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-24/hots.png" title="[[Grimaldi, Boutin, Sio-Ieng, Benosman & LP, 2023](https://laurentperrinet.github.io/publication/grimaldi-24/)]" width="80%" >}}

{{< speaker_note >}}
always-on
{{< /speaker_note >}}

---
### Always-on classification using HOTS

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-24/gesture_offline.png" title="[[Grimaldi, Boutin, Sio-Ieng, Benosman & LP, 2023](https://laurentperrinet.github.io/publication/grimaldi-24/)]" width="75%" >}}
{{< speaker_note >}}
always-on
{{< /speaker_note >}}

---
### Always-on classification using HOTS
{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-24/gesture_online.png" title="[[Grimaldi, Boutin, Sio-Ieng, Benosman & LP, 2023](https://laurentperrinet.github.io/publication/grimaldi-24/)]" width="75%" >}}
{{< speaker_note >}}
always-on
{{< /speaker_note >}}

---
### Spiking motifs in vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="[Grimaldi *et al*, 2023, [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)]" width="80%" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs in vision
{{< video src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/FastMotionDetection_input.mp4" autoplay="yes" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs in vision

{{< figure src="https://raw.githubusercontent.com/laurentperrinet/figures/7f382a8074552de1a6a0c5728c60d48788b5a9f8/animated_neurons/conv_HDSNN.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="100%" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs in vision

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/motion_kernels.png" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}
{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs in vision

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/quant_accuracy_raw.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs in vision

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/quant_accuracy_shortening.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs in vision
{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/quant_accuracy.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

{{< speaker_note >}}
thorpe
{{< /speaker_note >}}

---
### Spiking motifs pour la bio (HD-SNN)

<img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_toy-a_k.svg" width="42%">
{{% fragment %}} <img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_toy-b.svg" width="42%">     {{% /fragment %}}
{{% fragment %}} <img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_toy-c.svg" width="42%">     {{% /fragment %}}
{{% fragment %}} <img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_toy-a.svg" width="42%"> {{% /fragment %}}
{{< speaker_note >}}
spiking motifs
{{< /speaker_note >}}

---
### Spiking motifs pour la bio (HD-SNN)

{{% fragment %}} <img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_N_SMs.svg" width="31%">     {{% /fragment %}}
{{% fragment %}} <img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_N_pre.svg" width="31%">     {{% /fragment %}}
{{% fragment %}} <img src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/THC_N_SM_time.svg" width="31%"> {{% /fragment %}}

[LP (2023)](https://laurentperrinet.github.io/publication/perrinet-23-icann/)

{{< speaker_note >}}
This was a toy example and let's now quantify the performance of this method in real scale settings by measuring the accuracy of finding the right SM at the right time. For this we will compare our method to a classical approach using the correlation. 
First, by increasing the number of motifs, we show that the accuracy of our method (in blue) is very high and outperforms the cross-correlation method (red), in particular as the number of SMs increases. The same trend is shown also when the number of presynaptic inputs increases from a low to a high dimension. Finally, the number of possible delays is a crucial parameter and enough heterogenous delays are necessary to reach a good performance.
{{< /speaker_note >}}
</section>

---

<section>

## Future steps

{{% fragment %}} 
* unsupervised
 {{% /fragment %}}
{{% fragment %}}
* high-throughput
  {{% /fragment %}}
{{% fragment %}}
* real-time
 {{% /fragment %}}

{{< speaker_note >}}

{{< /speaker_note >}}
<!-- 
---
### unsupervised

{{< speaker_note >}}
unsupervised / contrastive learning
{{< /speaker_note >}}

---
### high-throughput

{{< speaker_note >}}
puces neuromorphiques, spike sorting on electrode
{{< /speaker_note >}}

---
### real-time using  neuromorphic hardware

{{< figure src="https://cdn.cnx-software.com/wp-content/uploads/2022/09/Intel-Loihi-2.jpg" title="Loihi 2" width="100%" >}}
{{< speaker_note >}}
énergie (heat) +
rapidité +
anticpation (PP)
{{< /speaker_note >}} -->

</section>

---

<section>

### [Analyser de larges volumes de données neurobiologiques](https://laurentperrinet.github.io/slides/2024-03-27-emergences/?transition=fade)
####	*[Laurent Perrinet](https://laurentperrinet.github.io)*
####	<u>[[2024-03-27]](https://laurentperrinet.github.io/talk/2024-03-27-emergences) [Emergences workshop, Autrans, France](https://laurentperrinet.github.io/grant/emergences/)</u>

<img src="https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg" alt="logos" height="130"/>

#### [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

<aside class="notes">

En conclusion, ...
... in coopearation with robotics
</aside>

</section>
