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
		  <!-- <img src="https://laurentperrinet.github.io/grant/polychronies/featured.png" alt="header" height="300">  -->
		  <img src="https://laurentperrinet.github.io/post/2019-06-22_ardemone/featured.png" alt="header" height="300"> 
	</a>
</tr>
<tr>
	<th>
		<a href="https://laurentperrinet.github.io/slides/2025-02-11-neuromath/?transition=fade"> <i> Laurent Perrinet </i> </a> - <a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>
	    <br>
		Séminaire Neuromathématiques, <b>Collège de France</b>
	</th>
	<th>
		  <img src="https://laurentperrinet.github.io/qrcode.png" alt="QR code" height="80" width="80">
	</th>	
</tr>
</table>

{{< speaker_note >}}

- Hello. I am Laurent Perrinet, a researcher in computational neuroscience and currently a research director at CNRS at the Institute of Neurosciences of Timone in Marseille. Thank you for inviting me to participate in this seminar of the "NeuroMathematics" team at the intersection of mathematics and life sciences.

- I have an engineering background, which could have led me to pursue a career at Airbus rather than becoming a scientist, especially in a field of biology like neuroscience. But it is thanks to the encounters I had through my mathematics professor, Manuel Samuelides, that I became interested in the world of neural networks at the end of my engineering studies.

- It is also thanks to him that I was able to follow a university education in cognitive sciences (now called the CogMaster in 1998), and I would like to pay tribute to Jean Petitot in this regard. It was in his course during this training that I discovered the possibility of linking the statistics found in natural images with principles that can be found in the central nervous system. It was a real revelation, and I also want to thank him for his patience in guiding me towards the various training programs I could follow to continue my path... This seminar is therefore a real return to the roots as I will be able to present the progress of my research since my DEA on exactly this subject!

{{< /speaker_note >}}

</section>

---

<section>


{{< slide background-image="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg" >}}

<!-- <img src="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg"  width="80%"/> -->

[Paysage catalan (Le Chasseur) [Joan Miró, 1924]](https://fr.wikipedia.org/wiki/Paysage_catalan_(Le_Chasseur))

{{< speaker_note >}}


Today, I will address our current knowledge about horizontal connectivity rules in V1. Why is this important? As a matter of fact, one main function of sensory systems, such as the pivotal role of the primary visual cortex for vision, is to bind together the different visual features to help ultimately build a global perception. This is playfully illustrated in this painting from Joan Miró, which allows us to depict this Catalan landscape with the hunter. A few strokes are sufficient to signify the landscape or allow us to imagine the hunter.

{{< /speaker_note >}}

---

{{< slide background-image="https://laurentperrinet.github.io/post/2018-04-10_trames/featured.png" >}}

Trames (Etienne Rey)

{{< speaker_note >}}

This is so striking that the lines and contours may appear even when they do not exist, such as in this display created with the visual artist Etienne Rey. With only dots, we still see lines, such as a hexagonal grid, and even an illusion of depth. Notice how this illusion depends on the position of your eye and therefore of your retina. Can we make sense of these phenomena?

{{< /speaker_note >}}

---

## Anatomy of the Human Visual system

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies ([Grimaldi *et al* 2022](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))" width="75%" >}}

{{< speaker_note >}}
Let's begin with the anatomy of the visual system. The diagram shows the human visual pathway, where information flows from the retina through the optic nerve to reach the lateral geniculate nucleus (LGN) in the thalamus. From there, signals project to the primary visual cortex (V1) and then proceed through higher visual areas following two main streams - the ventral "what" pathway and the dorsal "where/how" pathway. This hierarchical organization allows for increasingly complex visual processing, ultimately enabling motor responses and behavior. The latencies shown in the figure indicate the sequential timing of neural activation across these processing stages.
{{< /speaker_note >}}

---

## Anatomy of the Primary Visual Cortex

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Kaschube2010Fig1.jpg" width="75%" >}}

{{< speaker_note >}}

Let's examine the primary visual cortex (V1). A key characteristic found in many mammalian species is that V1 neurons exhibit selective responses to oriented visual stimuli, with their spatial arrangement following structured patterns across the cortical surface. In particular, orientation preference is organized in a quasi-periodic manner, forming what is known as an orientation map. However, this organization shows species-specific variations - notably, rodents lack such orderly maps and instead display a "salt-and-pepper" arrangement where neighboring neurons have random orientation preferences. This organizational diversity raises interesting questions about the functional role of these different architectures.

{{< /speaker_note >}}

---

## Thalamic, short- & long-range lateral, interareal


{{< figure src="https://laurentperrinet.github.io/publication/perrinet-07-neurocomp/featured.png" width="25%" >}}
{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/cortical-columns_a_02_cl_vis_3e.jpg" width="25%" >}}

{{< speaker_note >}}

A key feature of primary visual cortex is its layered organization, which is shared across visual areas. The main thalamic input arrives in layer 4, which connects to a dense network of vertical connections across layers. These columns can then communicate via horizontal connections within layers.


Hubel and Wiesel also showed that every point in the visual field produces a response in a 2 mm x 2 mm area of the cortex. Such an area can contain two complete groups of ocular dominance columns, 16 blobs and interblobs that may contain more than two times all of the orientations possible across 180 degrees. This region of the cortex, which Hubel and Wiesel called a hypercolumn (or, more generally, a cortical module) seems both necessary and sufficient for analyzing the image of a point in visual space. Because the cortex is a continuous cellular layer and because it is very hard to establish the boundaries of these modules physically, their existence from a functional standpoint is still the subject of debate. 
https://thebrain.mcgill.ca/flash/a/a_02/a_02_cl/a_02_cl_vis/a_02_cl_vis.html

Figure 9.2. Hypercolumn Diagram. Ocular dominance columns are segregated into left and right eye inputs. Orientation columns are neurons that get excited at different orientations and a cluster of these is called a pinwheel. Blobs are color selective and for every pinwheel there is a blob. (Credit: McGill: The Brain from Top to Bottom, Figure of hypercolumns, Copyleft https://copyleft.org/, https://thebrain.mcgill.ca/flash/a/a_02/a_02_cl/a_02_cl_vis/a_02_cl_vis.html. No modifications.)

From: https://pressbooks.umn.edu/sensationandperception/chapter/columns-and-hypercolumns-in-v1/
{{< /speaker_note >}}

---

## Thalamic, short- & long-range lateral, interareal

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Markov2011Fig2_cercorbhq201f02_ht.jpg" title="[Markov *et al* 2011]" height="60%" >}}

{{< speaker_note >}}
 Markov and colleagues quantified these connections through retrograde tracer injections in macaque V1. Their results showed that the vast majority (85%) of connections are intra-areal. The connection density decreases exponentially with distance, with a characteristic length of ~.23mm. Approximately 80% of connections are confined within 1.5mm, which is notable given that the typical distance between orientation pinwheels is ~0.5mm. As a consequence A vast majority of presynaptic contacts in cortex originate from neurons located in the same area as the postsynaptic target.

{{< /speaker_note >}}

---

## Horizontal connectivity links different hypercolumns

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]"width="70%" >}}

{{< speaker_note >}}

An important observation about horizontal connectivity is its apparent organization. The seminal work of Bosking and colleagues demonstrated this by combining orientation preference mapping with retrograde tracers. Their results showed that the injection site (marked by a white arrow) led to labeled synapses (black dots) predominantly connecting neurons with similar orientation preferences - supporting what became known as the "like-to-like" connectivity hypothesis. However, subsequent studies, particularly by Hunt and Goodhill, revealed that this pattern exhibits considerable diversity in the specificity and strength of these connections across cortical regions and species.

Note that while this hypothesis was influential, recent evidence suggests the connectivity rules may be more complex than initially thought. The observed variability in connection patterns likely serves important functional roles that are still being investigated.

{{< /speaker_note >}}
---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Field1993Fig3B.jpg" title="[Field *et al*, 1993]" height="80%" >}}

{{< speaker_note >}}

This seminal work by Field, Hayes and Hess in 1993 demonstrated that observers were better at detecting contours formed by aligned Gabor patches compared to randomly oriented ones. They proposed that this perceptual grouping relies on an "association field" - a hypothetical linking mechanism that preferentially connects neurons tuned to similar orientations. Their psychophysical experiments showed that detection performance was best when elements were co-aligned and degraded systematically as the relative orientation between elements increased. This association field concept provided a compelling framework for understanding how the visual system may implement contour integration through neural connectivity patterns.

{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Field1993Fig3.jpg" title="[Field *et al*, 1993]" height="80%" >}}


{{< speaker_note >}}

This figure elaborates on Field's original paradigm, demonstrating psychophysical evidence for contour perception. The plots show performance in detecting contours embedded in noise fields at different angles of curvature. The data reveals that observers are most sensitive to co-aligned elements, with detection performance declining systematically as contour curvature increases. This supports the existence of an "association field" mechanism that preferentially links oriented elements according to their geometric relationships, with a bias toward smooth contours commonly found in natural scenes.

{{< /speaker_note >}}

---

## Natural Images : Edges are on a common circle


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Sigman2001Fig4.jpg" title="[Sigman *et al*, 2001]" height="80%" >}}

{{< speaker_note >}}

A significant contribution to understanding edge co-occurrences in natural images came from Sigman et al. (2001). By analyzing edge orientations in natural images, they quantified the probability density function of edge co-occurrences based on their relative positions and orientations. The figure demonstrates this by showing the spatial distribution patterns for edges relative to a reference edge at different orientations. For iso-oriented edges (a), the co-occurrence pattern shows clear structure. As the relative orientation increases through 22.5° (b), 45° (c), 67.5° (d), to 90° (e), distinct spatial patterns emerge. 

A key finding was that for any given relative orientation between edges, the angle of maximal interaction occurs at the bisector between the orientations. This suggests that co-occurring edges tend to lie on a common circle - a property known as cocircularity. Panel (f) illustrates this geometrical principle: given two edges at angles w (red, 20°) and c (blue, 40°), the cocircularity solutions (green lines at 30° and 120°) represent the possible orientations of connecting circular arcs. This mathematical relationship provides insights into how the visual system might leverage statistical regularities in natural scenes for contour integration.

{{< /speaker_note >}}


---

## The like-to-like hypothesis

{{< figure src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/bosking2Asso.png" title="[Field *et al*, 2013]" height="400" >}}


{{< speaker_note >}}

The like-to-like hypothesis has been influential in understanding horizontal connectivity patterns. Drawing from anatomical studies and natural image statistics, it suggests that neurons preferentially connect to others with similar orientation preferences. This appears to align with the statistical structure of natural scenes, where co-oriented edges tend to form smooth contours.

However, we should be cautious about overstating these relationships. While horizontal connections show some orientation specificity, recent evidence indicates the connectivity patterns are more complex and heterogeneous than initially proposed. The functional role of this diverse connectivity remains an active area of investigation.

During the remainder of this talk, I will try to shed light on our current knowledege on horizontal connectivities.

{{< /speaker_note >}}


---

## Supplementary: modelling the Human Visual system : the HMAX model

{{< figure src="https://www.researchgate.net/profile/Thomas-Serre/publication/253467382/figure/fig1/AS:298143448092675@1448094345807/a-Organization-of-the-visual-cortex-The-diagram-is-modified-from-Gross-1998-Key.png" title="[Serre and Poggio, 2007]" width="65%" >}}

{{< speaker_note >}}
- and a model of it...(https://biology.stackexchange.com/questions/10955/ventral-stream-pathway-and-architecture-proposed-by-poggios-group)
- CNN, the mother of all deep learning models
{{< /speaker_note >}}

---

## Supplementary:  Convolutional Neural Nets (CNN)

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- this can be integrated in a hierarchy...
- defining a Convolutional Neural Networks (CNN)
- one layer is a convolution
{{< /speaker_note >}} 

---



## Supplementary: Orientation selectivity in the Primary visual cortex

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/scientists.jpg" title="[Hubel & Wiesel, 1962]" width="80%" >}}

{{< speaker_note >}}
- let's zoom in, the basic ingredient is the receptive field
{{< /speaker_note >}}

---

## Supplementary: Orientation selectivity in the Primary visual cortex

{{< video src="https://raw.githubusercontent.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/master/figures/ComplexDirSelCortCell250_title.mp4" controls="yes" width="100%" >}}

[Hubel & Wiesel, 1962]

{{< speaker_note >}}
- a single neuron is selective to some visual features...
{{< /speaker_note >}}

---

## Supplementary: Marr's three levels of analysis

<img src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" height="350"> {{% fragment %}} <img src="https://outde.xyz/img/Rawski/Marr/7lvls.jpg" height="350"> {{% /fragment %}}

[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)

{{< speaker_note >}}
- cut in different levels: Marr (+ Poggio)
- arbitrary, but useful division of labor= computational / algorithm / hardware

- here:
  - anatomy
  - algorithm / model
  - function
  
First: What is the anatomy of horizontal connections?

	<!-- {{< figure src="https://outde.xyz/img/Rawski/Marr/7lvls.jpg" title="[[Marr, 1982]](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="45%" >}}  -->
	<!-- {{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="Marr, 1982" width="45%" >}}   -->

{{< /speaker_note >}}

<!-- voges https://laurentperrinet.github.io/publication/voges-12/featured.jpg -->

</section>

---

<section>

# Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/header.png" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" width="80%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1AE.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/voges-12/featured.jpg" title="[[Voges and LP, 2012]](https://laurentperrinet.github.io/publication/voges-12/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig2AC.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig4.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig5A.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}


---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Markov2011Fig2_cercorbhq201f02_ht.jpg" title="[Markov *et al* 2011]" width="55%" >}}

[Markov *et al.* 2011]

{{< speaker_note >}}
Figure 2 of Markov et al. 2011

Intrinsic and extrinsic connectivity. (A) Intrinsic FLNt values of 9 areas. V1 and V4 are averages for repeated injections. (B) Exponential decay of density of intrinsic neurons with distance following injection in area V1. (C) Distances within which the 3 thresholds (75%, 80%, and 95%) of intrinsic FLNt are attained in 7 injected areas. Dashed lines indicate mean distance at which each threshold is reached. Error bars are SD.
{{< /speaker_note >}}

</section>

---

<section>



# Modelling the Association field

## Geisler


{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/Geisler01Fig3A.png" height="275"> {{% /fragment %}}{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/Geisler01Fig3B.png" height="275"> {{% /fragment %}}{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/Geisler01Fig3C.png" height="275"> {{% /fragment %}}

[Geisler, 2001]

{{< speaker_note >}}
- topography?
{{< /speaker_note >}}

---

## Association field

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/featured.jpg" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Sparse representations in computer vision

{{< figure src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/figures/figure_synthesis.svg" title="[[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="70%" >}}

{{< speaker_note >}}
- extracting edges is useful
{{< /speaker_note >}}

---

## Association field

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_results.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_chevrons.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_chevrons2.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Association field

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_results.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" width="55%" >}}

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

## A diversity of association fields

{{< figure  src="https://github.com/laurentperrinet/2020-09-25_IRPHE/raw/master/figures/PCOMPBIOL-D-19-01811_R2_compressed_FigS4.png" title="[Bosking *et al*, 1997]"width="70%" >}}

---

##  Convolutional Neural Networks : Topography

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

---

## CNN: Topography - plus bas car dynmique et hétérogene

{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/figure_series.png" height="275"> {{% /fragment %}}{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/figure_series_11.png" height="275"> {{% /fragment %}}

{{< speaker_note >}}
- topography?
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
		  <!-- <img src="https://laurentperrinet.github.io/post/2019-06-22_ardemone/featured.png" alt="header" height="300">  -->
	</a>
</tr>
<tr>
	<th>
		<a href="https://laurentperrinet.github.io/slides/2025-02-11-neuromath/?transition=fade"> <i> Laurent Perrinet </i> </a> - <a href="https://laurentperrinet.github.io">https://laurentperrinet.github.io</a>
	    <br>
		Séminaire Neuromathématiques, <b>Collège de France</b>
	</th>
	<th>
		  <img src="https://laurentperrinet.github.io/qrcode.png" alt="QR code" height="80" width="80">
	</th>	
</tr>
</table>

{{< speaker_note >}}

- résumé : diversity
- les neurosciences peuvent répondre à ces questions par des modélisations - rôle des mathématiques
- un objectif : passer en dynamique

{{< /speaker_note >}}
</section>