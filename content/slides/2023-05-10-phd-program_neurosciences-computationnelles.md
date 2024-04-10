---
 slides:
 # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  transition: 'fade'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2023-05-10'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2023-05-10T08:47:11+02:00"

title: 2023-05-10-phd-program_neurosciences-computationnelles.md

summary: Interactions between machine learning, artificial neural networks and our understanding of biological vision

---
<section>

# [Interactions between machine learning, artificial neural networks and our understanding of biological vision](https://laurentperrinet.github.io/slides/2023-05-10-phd-program_neurosciences-computationnelles/?transition=fade)
####	*[Laurent Perrinet](https://laurentperrinet.github.io)*
####	<u>[[2023-05-10]](https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles) [NeuroSchool PhD Program in Neuroscience](https://neuro-marseille.org/en/training/phd-program/): Computation Neuroscience</u>

<img src="https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.jpg" alt="logos" height="130"/>
<img src="https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles/qrcode.png" alt="qrcode" height="130"/>


Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

<!-- ![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.jpg) 
![QR code](https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles/qrcode.png) -->


{{< speaker_note >}}

- welcome to the course on COMPUTATIONAL NEUROSCIENCE 2023 entitled "Machine learning to analyze complex data"
- objective= understand models of biological vision which are the inspiration for modern deep learning
- outcome= interaction between artificial and natural NNs
- outline= principles / CNNs / challenges / solutions
{{< /speaker_note >}}


</section>

---

<section>

# Principles of Vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- break down problem in three different levels: Marr (+ Poggio)
- arbitrary, but useful division of labor
{{< /speaker_note >}}

---


## What is the function of vision?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_001.jpg" title="[An Unexpected Visitor (Ilya Repin, 1884)](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}


{{< speaker_note >}}
- seeing= interacting with the visual world
- social animals: looking at emotions
{{< /speaker_note >}}


---

## What is the function of vision?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_002.jpg" title="[An Unexpected Visitor (Yarbus, 1965)](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}

{{< speaker_note >}}
- active: the eye is always moving
- https://fr.wikipedia.org/wiki/Alfred_Iarbous
- "1) examine the painting freely"
- consistency of eye traces / interindividual differences
{{< /speaker_note >}}


---

## What is the function of vision?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_004.jpg" title="[An Unexpected Visitor - *Age?* (Yarbus, 1965)](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}


{{< speaker_note >}}
- active: depends on task:
- "3) assess the ages of the characters"
{{< /speaker_note >}}


---

## What is the function of vision?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_007.jpg" title="[An Unexpected Visitor - *How long?* (Yarbus, 1965)](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}


{{< speaker_note >}}
- "6) surmise how long the “unexpected visitor” had been away"
- adaptive and efficient system...
- yet, surprisingly....
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/42_rotsnakes_main.jpg" title="[Rotating Snakes *Akiyoshi KITAOKA*](http://www.ritsumei.ac.jp/~akitaoka/index-e.html)" width="70%" >}}

{{< speaker_note >}}
- the visual system experiences "hallucinations"
- ...
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/) : [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Face-on-mars.jpg" title="[Cydonia Mensae, 1976, *Viking Orbiter image*](https://en.wikipedia.org/wiki/Cydonia_(Mars))" width="50%" >}}

{{< speaker_note >}}
these hallucinations may appear to be
- real
- persistent
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/) : [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Viking_moc_face_20m_low.png" title="[Cydonia Mensae, 2007, *Mars Global Surveyor*](https://en.wikipedia.org/wiki/Cydonia_(Mars))" width="50%" >}}

{{< speaker_note >}}
in that specific case...
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/) : [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Viking_moc_face_20m_high.png" title="[Cydonia Mensae, 2007, *Mars Global Surveyor*](https://en.wikipedia.org/wiki/Cydonia_(Mars))" width="50%" >}}

{{< speaker_note >}}
- more date = less ambiguity
- beware: models may also hallucinate
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/): Context


{{< video src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Kitaoka.mp4" controls="yes" width="80%" >}}
[Ilusions of brightness or lightness *Akiyoshi KITAOKA*](http://www.ritsumei.ac.jp/~akitaoka/index-e.html)

{{< speaker_note >}}
- these may be of low level
- ...
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/): Context

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Hering_illusion_without.svg" title="[Hering illusion](https://en.wikipedia.org/wiki/Hering_illusion)" width="70%" >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/): Context

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Hering_illusion.svg" title="[Hering illusion](https://en.wikipedia.org/wiki/Hering_illusion)" width="70%" >}}

{{< speaker_note >}}
- of showing an effect of context -> 3D
{{< /speaker_note >}}


---


## Principles of vision?

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}




</section>

---

<section>

# Computational neuroscience of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}


---

## Computational neuroscience of vision

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Churchland92.png" title="[[Sejnowski, Koch & Churchland, 1998](http://www.hms.harvard.edu/bss/neuro/bornlab/nb204/papers/sejnowski-koch-churchland-science1988.pdf)]" width="50%" >}}


---

## Anatomy of the Human Visual system

{{< figure src="https://www.readkong.com/static/06/b0/06b09f0235ae7fcf29438ce317c10e60/optogenetic-visual-cortical-prosthesis-9612386-7.jpg" width="61%" >}}

---

## Human Visual system : the HMAX model

{{< figure src="https://i.stack.imgur.com/ZlFnp.png" title="[[Serre and Poggio, 2006]](https://biology.stackexchange.com/questions/10955/ventral-stream-pathway-and-architecture-proposed-by-poggios-group)" width="65%" >}}

---

## Convolutional Neural Networks : Hierarchy

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

---

## Convolutional Neural Networks (CNNs)

{{< figure src="https://www.mdpi.com/vision/vision-07-00029/article_deploy/html/images/vision-07-00029-g003.png" title="[[Jérémie & LP, 2023](https://laurentperrinet.github.io/publication/jeremie-23-ultra-fast-cat/)]" width="90%" >}}

{{< speaker_note >}}
- sota
{{< /speaker_note >}}

<!-- ---

## Anatomy of the Human Visual system

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Voies_visuelles3.svg" title="[[Wikipedia]](https://en.wikipedia.org/wiki/Visual_system)" width="45%" >}} -->

---

## Primary visual cortex: Hubel & Wiesel

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/scientists.jpg" title="[Hubel & Wiesel, 1962]" width="80%" >}}

---

## Primary visual cortex: Hubel & Wiesel

{{< video src="https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles/hubel_wiesel.webm" controls="yes" height=250 >}}

[Hubel & Wiesel, 1962] - from [@Neuroslicer](https://www.youtube.com/@Neuroslicer)


{{< speaker_note >}}
- https://www.youtube.com/watch?v=KE952yueVLA -
https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles/hubel_wiesel.webm
- simple cell 4:09
- excerpt https://raw.githubusercontent.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/master/figures/ComplexDirSelCortCell250_title.mp4
{{< /speaker_note >}}

---

## Convolutional Neural Networks : hierarchy

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- backpropagation is not bioplausible 
- modification
{{< /speaker_note >}}


---

## Convolutional Neural Networks : Mathematics

* One-dimensional [discrete convolution](https://en.wikipedia.org/wiki/Convolution#Discrete_convolution) (eg in time) with a kernel $g$ of radius $K$:
$$
(f \ast g)[n]=\sum_{m=-K}^{K} f[n-m] \cdot g[m]
$$

---

## Convolutional Neural Networks : Mathematics

* Convolution of an image (two-dimensional) with a kernel $g$ of radius $K\times K$:

$$
(f \ast g)[x, y] = \sum_{i=-K}^{K} \sum_{j=-K}^{K} f[x-i, y-j] \cdot g[i, j]
$$

---

## Convolutional Neural Networks : Mathematics

* **Cross-correlation** of an image (two-dimensional) with a kernel $g$ of radius $K\times K$:

$$
(f \ast \tilde{g})[x, y] = \sum_{i=-K}^{K} \sum_{j=-K}^{K} f[x+i, y+j] \cdot g[i, j]
$$

---

## Convolutional Neural Networks : Mathematics

{{< figure src="https://stanford.edu/~shervine/teaching/cs-230/illustrations/convolution-layer-a.png" title="[[Amidi & Amidi](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks)]" width="90%" >}}

---

## Convolutional Neural Networks : Mathematics

* Correlation of an image defined on several  channels (note [the order of the indices](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)):

$$
(f \ast \tilde{g})[x, y] = \sum_{c=1}^{C} \sum_{i,j} f[c, x+i, y+j] \cdot g[c, i, j]
$$


---

## Convolutional Neural Networks : Mathematics

* Correlation of a multi-channel image for multiple output channels (note [the order of the indices](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)):

$$
(f \ast \tilde{g})[k, x, y] = \sum_{c=1}^{C} \sum_{i,j} f[c, x+i, y+j] \cdot g[k, c, i, j]
$$

---

## Convolutional Neural Networks : Predictive coding

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- adding sparse coding + feedback
{{< /speaker_note >}}


---

## Convolutional Neural Networks : Predictive coding

{{< figure src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/BoutinFranciosiniChavaneRuffierPerrinet20face.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- interpretable features
{{< /speaker_note >}}

---

## Convolutional Neural Networks : Topography

{{< figure  src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]"width="70%" >}}

---

## Convolutional Neural Networks : Topography

{{< figure src="https://laurentperrinet.github.io/publication/franciosini-21/featured.jpg" title="[[Boutin *et al*, 2022](https://laurentperrinet.github.io/publication/franciosini-21/)]" width="90%" >}}

</section>

---

<section>

# Computational neuroscience of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

---


# Dynamics of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

<!--
---


## Dynamics of vision

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/scheme_thorpe.jpg" title="[[Thorpe, 2001]](https://laurentperrinet.github.io/2022-01-12_NeuroCercle/#/2/1)" width="70%" >}} -->


<!--
---


## Dynamics of vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency-estimate.jpg" title="Precise Spiking Motifs] ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="80%" >}} -->

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


---


## Dynamics of vision

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/figure-tsonga.jpg" title="Sensorimotor delays ([Perrinet & Friston, 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))" width="75%" >}}

---


## Dynamics of vision


{{< video src="https://laurentperrinet.github.io/publication/perrinet-19-temps/flash_lag.mp4" autoplay="yes" >}}


---

## Dynamics of vision

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov.jpg" width="100%" title="Diagonal markov model ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

---

## Dynamics of vision

<!-- {{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/PBP_spatial_readout.mp4"  autoplay="yes" >}}{{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/MBP_spatial_readout.mp4"  autoplay="yes" >}} -->
{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/positional-delay.mp4" autoplay="yes" >}}

Flash-lag effect: MBP ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))


---

## Dynamics of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}


</section>

---

<section>

# Spiking Neural Networks

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

---

## Spiking Neural Networks: Leaky Integrate-and-Fire Neuron

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/LIF.gif" title="[Grimaldi *et al*, 2023, [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)]" width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

- A standard LIF

{{< /speaker_note >}}

---

## Spiking Neural Networks in neurobiology

{{< figure src="http://i.stack.imgur.com/ixnrz.png" title="[[Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb)]" width="99%" >}}


{{< speaker_note >}}
**2 MINUTE**

- reproduucibility

{{< /speaker_note >}}

---


## Spiking Neural Networks in neurobiology

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/replicating_MainenSejnowski1995.png" title="[[Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb)]" width="99%" >}}


{{< speaker_note >}}
**2 MINUTE**

- reproduucibility

{{< /speaker_note >}}

---


## Spiking Neural Networks in neurobiology

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/Diesmann_et_al_1999.png" title="[[Diesmann et al. 1999](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_3_Diesmann_et_al_1999.py)]" width="99%" >}}

{{< speaker_note >}}
**2 MINUTE**

- "This hypothesis is reviewed with respect to our knowledge of the neurobiology, for instance in the hippocampus of rodents. We also review

{{< /speaker_note >}}

---


## Spiking Neural Networks in neurobiology

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/haimerl2019.jpg" title="[[Haimerl et al, 2019](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)]" width="99%" >}}

{{< speaker_note >}}
**2 MINUTE**

- Izhikevich polychronization

- yet the domain is vast, and there s lot to do in SNNs

{{< /speaker_note >}}

---

## Spiking Neural Networks: Spiking motifs

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="[Grimaldi *et al*, 2023, [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)]" width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

- This hypothesis is reviewed with respect to our knowledge of the neurobiology, for instance in the hippocampus of rodents. We also review

{{< /speaker_note >}}

---

## Spiking Neural Networks: Spiking motifs

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/LIF.gif" title="Review on [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)." width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

- A standard LIF

{{< /speaker_note >}}

---

## Spiking Neural Networks: Spiking motifs

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/HSD.gif" title="Review on [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)." width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

- A nice HSD neuron

{{< /speaker_note >}}


---

## Spiking Neural Networks in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/grant/anr-anr/event_driven_computations.png" title="From frame-based to event-based cameras." width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

- event-based cameras

{{< /speaker_note >}}


---

## Spiking Neural Networks in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/HDSNN_conv.png" title="The HD-SNN neural network." width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

- For instance, we show how precise spike times may be used to detect the direction of motion from such a stream of events in an ultrafast fashion.
{{< /speaker_note >}}


---

## Spiking Neural Networks in neuromorphic engineering

{{< video src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/FastMotionDetection_input.mp4" autoplay="yes" >}}

{{< speaker_note >}}
**2 MINUTE**

- A nice HSD neuron

For instance, we show how precise spike times may be used to detect the direction of motion from such a stream of events in an ultrafast fashion.
{{< /speaker_note >}}


---

## Spiking Neural Networks in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/motion_kernels.png" title="The HD-SNN neural network." width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

- nice kernels

{{< /speaker_note >}}


---

## Spiking Neural Networks in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/accuracy.png" title="The HD-SNN neural network." width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

- frugal computing

{{< /speaker_note >}}


</section>

---

<section>


## Artificial neural networks and machine learning applied to the understanding of biological vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- Only the speaker can read these notes
- Press `S` key to view
- more on [doc](https://raw.githubusercontent.com/wowchemy/starter-hugo-academic/master/exampleSite/content/slides/example/index.md)
{{< /speaker_note >}}

---

# [Interactions between machine learning, artificial neural networks and our understanding of biological vision](https://laurentperrinet.github.io/slides/2023-05-10-phd-program_neurosciences-computationnelles/?transition=fade)
####	*[Laurent Perrinet](https://laurentperrinet.github.io)*
####	<u>[[2023-05-10]](https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles) [NeuroSchool PhD Program in Neuroscience](https://neuro-marseille.org/en/training/phd-program/): Computation Neuroscience</u>

<img src="https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.jpg" alt="logos" height="130"/>
<img src="https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles/qrcode.png" alt="qrcode" height="130"/>


Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

<!-- ![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.jpg) 
![QR code](https://laurentperrinet.github.io/talk/2023-05-10-phd-program-neurosciences-computationnelles/qrcode.png) -->


{{< speaker_note >}}
- thanks for your attention
{{< /speaker_note >}}


</section>
