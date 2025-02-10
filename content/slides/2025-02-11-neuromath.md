---
 slides:
 # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  transition: 'fade'
  width: 1280
  height: 780
  margin: 0.01

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

Hi, thanks for the introduction! I am Laurent Perrinet, a researcher in computational neuroscience and currently a research director at CNRS at the Institute of Neurosciences of la Timone in Marseille. Thank you for inviting me to participate in this "NeuroMathematics" seminar at the intersection of mathematics and neuroscience.

As an engineer by training, I could have pursued a career in aeronautics rather than becoming a scientist in neuroscience. However, thanks to my mathematics professor Manuel Samuelides, I discovered neural networks at the end of my engineering studies. This developped a curiosity for me, and thanks to him, I was also able to study in a mastere of cognitive sciences (now called CogMaster) in 1998. I particularly want to acknowledge Jean Petitot - in his course I discovered how natural image statistics could link to principles in the central nervous system. This was a vivid revelation, and I'm grateful for his guidance in my academic path. Today's seminar represents a return to these roots, as I'll present my research progress since my mastere thesis on this very topic.


Today, I will address our current knowledge about horizontal connectivity rules in V1. Why is this important? As a matter of fact, one main function of sensory systems, such as the pivotal role of the primary visual cortex for vision, is to bind together the different visual features to help ultimately build a global perception.

{{< /speaker_note >}}

</section>

---

<section>


{{< slide background-image="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg" >}}

<!-- <img src="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg" height="420"/> -->
<!-- [Paysage catalan (Le Chasseur) [Joan Miró, 1924]](https://fr.wikipedia.org/wiki/Paysage_catalan_(Le_Chasseur)) -->
<table>
<tr >
	<th>
		<a href ="https://fr.wikipedia.org/wiki/Paysage_catalan_(Le_Chasseur)">Paysage catalan (Le Chasseur), <i>Joan Miró</i> (1924)</a>
	</th>	
</tr>
<tr style="height:600px;">
</tr>
</table>
{{< speaker_note >}}

 This is playfully illustrated in this painting from Joan Miró, which allows us to depict this Catalan landscape with the hunter. A few strokes are sufficient to signify the landscape or allow us to imagine the hunter.

This is so striking that the lines and contours may appear even when they do not exist, such as in this display created with the visual artist Etienne Rey.

{{< /speaker_note >}}

---

{{< slide background-image="https://laurentperrinet.github.io/post/2018-04-10_trames/featured.png" >}}

<table>
<tr >
	<th>
		  <a href ="https://laurentperrinet.github.io/post/2018-04-10_trames/">Trames (Etienne Rey)</a>
	</th>	
</tr>
<tr style="height:600px;">
</tr>
</table>


{{< speaker_note >}}

With only dots, we still see lines, such as a hexagonal grid, and even an illusion of depth. Notice how this illusion depends on the position of your eye and therefore of your retina. Can we make sense of these phenomena?

{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Field1993Fig3B.jpg" title="[Field *et al*, 1993]" height="420" >}}

{{< speaker_note >}}

This percept of continuity which was previously already framed in the Gestalt paradigm has developed into a quantitative framework. This seminal work by Field, Hayes and Hess in 1993 demonstrated that observers were better at detecting contours formed by aligned Gabor patches compared to randomly oriented ones. Like how a contour may preferentially emerge in a dense field of edges.
{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Field1993Fig3.jpg" title="[Field *et al*, 1993]" height="420" >}}


{{< speaker_note >}}

Their psychophysical experiments showed that detection performance was best when elements were co-aligned and degraded systematically as the relative orientation between elements increased. This highlighted significant edge parameters such a relative orientation, distance, but not phase. 
Consequently, they proposed that this perceptual grouping relies on an "association field" - a hypothetical linking mechanism that preferentially connects neurons tuned to similar orientations. 
This association field concept provided a compelling framework for understanding how the visual system may implement contour integration through neural connectivity patterns.

{{< /speaker_note >}}

---

## Natural Images : Edges are on a common circle


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Sigman2001Fig4.jpg" title="[Sigman *et al*, 2001]" height="420" >}}

{{< speaker_note >}}

A significant contribution to understanding edge co-occurrences in natural images came from Sigman et al. (2001). By analyzing edge orientations in natural images, they quantified the probability density function of edge co-occurrences based on their relative positions and orientations. The figure demonstrates this by showing the spatial distribution patterns for edges relative to a reference edge at different orientations. For iso-oriented edges (a), the co-occurrence pattern shows clear structure. As the relative orientation increases through 22.5° (b), 45° (c), 67.5° (d), to 90° (e), distinct spatial patterns emerge. 

A key finding was that for any given relative orientation between edges, the angle of maximal interaction occurs at the bisector between the orientations. This suggests that co-occurring edges tend to lie on a common circle - a property known as cocircularity. Panel (f) illustrates this geometrical principle: given two edges at angles w (red, 20°) and c (blue, 40°), the cocircularity solutions (green lines at 30° and 120°) represent the possible orientations of connecting circular arcs. This mathematical relationship provides insights into how the visual system might leverage statistical regularities in natural scenes for contour integration.

{{< /speaker_note >}}


---

## Anatomy of the Human Visual system

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Human Visual system ([Grimaldi *et al* 2022](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))" height="420" >}}

{{< speaker_note >}}
Let's begin with the anatomy of the visual system. The diagram shows the human visual pathways, where information flows from the retina through the optic nerve to reach the lateral geniculate nucleus  in the thalamus. From there, signals project to the primary visual cortex (V1) and then proceed through higher visual areas following two main streams - the ventral "what" pathway (which I show here) and the dorsal "where/how" pathway. This hierarchical organization allows for increasingly complex visual processing, ultimately enabling motor responses and behavior. The latencies shown in the figure indicate the sequential timing of neural activation across these processing stages.
{{< /speaker_note >}}

---

## Anatomy of the Primary Visual Cortex

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Kaschube2010Fig1.jpg" title="[Kaschube *et al* (2010)]" height="420" >}}

{{< speaker_note >}}

V1 is central to these pathways and shows distinctive anatomical and functional properties along with a complex topographical organization.

This figure from Kaschube et al. (2010) illustrates the organization of orientation preference maps in primary visual cortex (V1). 
Individual V1 neurons exhibit selective responses to oriented visual stimuli (as denoted by varying hues Colors code preferred ORs as indicated by the bars in (C)), with their spatial arrangement following highly structured patterns across the cortical surface. 
Panel B shows Synthetic orientation-maps of equal column spacing Λ but widely different pinwheel densities ρ. Left to right: solutions of different models: (13–16).. (C) High (blue frame) and low (orange frame) pinwheel density regions in tree shrew visual cortex. (D to F), Optically recorded orientation-maps in tree shrew (D), galago (E), and ferret (F) visual cortex. Regions shown in (C) are marked in (D). White arrows in (F) mark selected pinwheel centers. Framed regions in (C) and (F) are magnified.
In many mammals including cats, monkeys and ferrets, orientation preference is organized in a quasi-periodic manner, forming what are known as orientation preference maps. These maps show remarkable consistency in their geometric properties across species, particularly in the spatial organization of pinwheel centers where orientation preferences converge.

However, this organization shows important species-specific variations. Most notably, while primates and carnivores display orderly orientation maps with smooth transitions between preferred orientations, rodents lack such maps and instead show a "salt-and-pepper" arrangement where neighboring neurons have seemingly random orientation preferences. This organizational diversity raises interesting questions about the computational advantages of these different architectures and their relationship to visual processing requirements and behavioral needs across species.


{{< /speaker_note >}}

---

## Thalamic, short- & long-range lateral, interareal


<!-- {{< figure src="https://laurentperrinet.github.io/publication/perrinet-07-neurocomp/featured.png" height="200" >}}{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/cortical-columns_a_02_cl_vis_3e.jpg"  height="150" >}} -->
{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/cortical-columns.jpg" height="420" >}}

{{< speaker_note >}}

A key feature of primary visual cortex is its layered organization, which is shared across visual areas. The main thalamic input arrives in layer 4, which connects to a dense network of vertical connections across layers. These columns can then communicate via horizontal connections within layers.


Hubel and Wiesel also showed that every point in the visual field produces a response in a 2 mm x 2 mm area of the cortex. Such an area can contain two complete groups of ocular dominance columns, 16 blobs and interblobs that may contain more than two times all of the orientations possible across 180 degrees. This region of the cortex, which Hubel and Wiesel called a hypercolumn (or, more generally, a cortical module) seems both necessary and sufficient for analyzing the image of a point in visual space. Because the cortex is a continuous cellular layer and because it is very hard to establish the boundaries of these modules physically, their existence from a functional standpoint is still the subject of debate. 
https://thebrain.mcgill.ca/flash/a/a_02/a_02_cl/a_02_cl_vis/a_02_cl_vis.html

Figure 9.2. Hypercolumn Diagram. Ocular dominance columns are segregated into left and right eye inputs. Orientation columns are neurons that get excited at different orientations and a cluster of these is called a pinwheel. Blobs are color selective and for every pinwheel there is a blob. (Credit: McGill: The Brain from Top to Bottom, Figure of hypercolumns, Copyleft https://copyleft.org/, https://thebrain.mcgill.ca/flash/a/a_02/a_02_cl/a_02_cl_vis/a_02_cl_vis.html. No modifications.)

From: https://pressbooks.umn.edu/sensationandperception/chapter/columns-and-hypercolumns-in-v1/
{{< /speaker_note >}}

---

## Thalamic, short- & long-range lateral, interareal

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Markov2011Fig2_cercorbhq201f02_ht.jpg" title="[Markov *et al* 2011]" height="420" >}}

{{< speaker_note >}}

This figure from Markov et al. (2011) quantifies intrinsic connectivity patterns in macaque V1 through retrograde tracer injections. The data shows that 85% of connections are intra-areal, with connection density decreasing exponentially with distance (characteristic length ~0.23mm). Most connections (80%) remain within 1.5mm radius - notably close given the ~0.5mm spacing between orientation pinwheels. This provides strong evidence that the vast majority of inputs to V1 neurons come from within V1 itself rather than from other areas, suggesting local processing plays a dominant role in V1 computation.

{{< /speaker_note >}}

---

## Horizontal connectivity links different hypercolumns

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" height="420" >}}

{{< speaker_note >}}

This figure shows landmark results by Bosking et al. (1997) combining orientation preference maps with retrograde tracers. After injecting tracers (white arrow), they found labeled synapses (black dots) primarily connecting neurons of similar orientation preference, leading to the influential "like-to-like" connectivity hypothesis. However, later studies by Hunt, Goodhill and others revealed significant diversity in these connection patterns across cortical regions and species, suggesting more complex connectivity rules than initially proposed. This nuanced understanding has important implications for how we think about the functional organization of horizontal connections in V1.

{{< /speaker_note >}}

---

## The like-to-like hypothesis

{{< figure src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/bosking2Asso.png" title="[Field *et al*, 2013]" height="420" >}}


{{< speaker_note >}}

The like-to-like hypothesis has been influential in understanding horizontal connectivity patterns. Drawing from anatomical studies and natural image statistics, it suggests that neurons preferentially connect to others with similar orientation preferences. This appears to align with the statistical structure of natural scenes, where co-oriented edges tend to form smooth contours.

However, we should be cautious about overstating these relationships. While horizontal connections show some orientation specificity, recent evidence indicates the connectivity patterns are more complex and heterogeneous than initially proposed. The functional role of this diverse connectivity remains an active area of investigation.

During the remainder of this talk, I will try to shed light on our current knowledege on horizontal connectivities.

{{< /speaker_note >}}


---

## Supplementary: the HMAX model

{{< figure src="https://www.researchgate.net/profile/Thomas-Serre/publication/253467382/figure/fig1/AS:298143448092675@1448094345807/a-Organization-of-the-visual-cortex-The-diagram-is-modified-from-Gross-1998-Key.png" title="[Serre and Poggio, 2007]" height="420" >}}

{{< speaker_note >}}
- and a model of it...(https://biology.stackexchange.com/questions/10955/ventral-stream-pathway-and-architecture-proposed-by-poggios-group)
- CNN, the mother of all deep learning models
{{< /speaker_note >}}

---

## Supplementary:  Convolutional Neural Nets (CNN)

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}
- this can be integrated in a hierarchy...
- defining a Convolutional Neural Networks (CNN)
- one layer is a convolution
{{< /speaker_note >}} 

---

## Supplementary: Orientation selectivity in V1

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/scientists.jpg" title="[Hubel & Wiesel, 1962]" height="420" >}}

{{< speaker_note >}}
- let's zoom in, the basic ingredient is the receptive field
{{< /speaker_note >}}

---

## Supplementary: Orientation selectivity in V1

{{< video src="https://raw.githubusercontent.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/master/figures/ComplexDirSelCortCell250_title.mp4" controls="yes" height="420" >}}

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

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/header.png" title="[[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Together with my colleagues Frédéric Chavane (INT) and James Rankin (University of Exeter), we published a review paper in Brain Structure and Function that examines anatomical, functional, computational and theoretical evidence challenging the like-to-like hypothesis. The paper evaluates whether this influential hypothesis about V1 horizontal connectivity holds up against accumulated empirical evidence. The review systematically examines multiple lines of research to reassess our understanding of these important cortical circuits.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1A.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

This figure illustrates different hypothetical connectivity rules for horizontal connections in V1. The target neuron (large circle on left) has a specific orientation preference indicated by its color. Following the classical like-to-like hypothesis (shown in panel A), this neuron would preferentially connect to other neurons with matching orientation preference (similar colors) across multiple hypercolumns, as indicated by the vertical red arrows. The radial spread of connections spans approximately three hypercolumns, consistent with anatomical observations. Each hypercolumn contains a complete set of orientation preferences, represented by the different colored neurons.

This first schematic (noted A) represents one of the simplest proposed connectivity rules, where horizontal connections strictly follow orientation similarity. 

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1AB.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}
Panel B shows a more nuanced version of the like-to-like hypothesis that we call "modulated like-to-like bias". In this case, the target neuron still preferentially connects to neurons with similar orientation preferences, but the selectivity is less strict and extends over longer distances. The connections (shown by the gradients of red arrows) exhibit a smooth fall-off in specificity with distance, rather than the binary selectivity shown in panel A. This model better reflects the biological reality where connection specificity tends to be graded rather than absolute, and where horizontal connections can span multiple hypercolumns while maintaining some degree of orientation preference.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1AD.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Panel C shows evidence for a different type of connectivity pattern in inhibitory interneurons - a "like-to-unlike" bias where neurons preferentially connect to others with different orientation preferences. This highlights how different cell types may follow distinct connectivity rules.

Panel D illustrates a "like-to-all" connectivity pattern that has been observed in layers 4 and 6 of V1, where neurons form connections broadly across orientation preferences without strong selectivity. The arrows indicate connections to neurons of all orientations, suggesting these layers may serve different computational roles that do not require orientation-specific horizontal connectivity.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1AE.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Panel E presents an integrative model that combines aspects of the previous hypotheses. It shows a hybrid connectivity pattern where neurons exhibit a like-to-like bias at short distances (within adjacent hypercolumns), but this orientation specificity gradually diminishes with distance, transitioning to a like-to-all pattern in more distant hypercolumns. This model better reflects recent empirical findings suggesting that horizontal connectivity rules are more complex and distance-dependent than originally proposed. The gradual fade of red arrows illustrates how connection specificity weakens over larger cortical distances.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/voges-12/featured.jpg" title="[[Voges and LP, 2012]](https://laurentperrinet.github.io/publication/voges-12/)" height="420" >}}

{{< speaker_note >}}

To quantitatively understand how connectivity patterns shape network dynamics, we previously showed in simulated neural networks that transitioning from local unspecific to local specific and long-range patchy connectivities can fundamentally alter emergent activity patterns [Voges & LP, 2012]. This highlights how the detailed organization of horizontal connections plays a crucial role in shaping the dynamics of recurrent neural circuits. We will examine this computational aspect further in our review of the evidence challenging strict like-to-like connectivity rules.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< video src="https://laurentperrinet.github.io/publication/chavane-22/area17_lo_diff_circ_plot.mp4" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)"  autoplay="yes" repeat="yes" height="420" >}}


{{< speaker_note >}}

This video shows voltage-sensitive dye imaging (VSDI) data from cat primary visual cortex (area 17) in response to a local oriented grating stimulus. The visualization reveals two key aspects:

1. The broader activation pattern shown by overall fluorescence changes (gray)
2. The more restricted orientation-selective response pattern (colored regions)

Two contours are overlaid: a red line marking the boundary of significant activation, and a white line delineating regions with statistically significant orientation selectivity. The orientation selectivity is encoded by color hue.

The bottom plots quantify the spatiotemporal dynamics by showing:
- Left: The total activated cortical area over time
- Right: The extent of orientation-selective regions over time 

Together, these measurements demonstrate how orientation-selective signals propagate laterally beyond the classical feedforward input zone through horizontal connections, while maintaining some degree of feature selectivity.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig2A.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}
This figure shows spatial and temporal dynamics of orientation selectivity in cat V1 analyzed from voltage-sensitive dye imaging data. Panel A displays a cortical orientation map averaged over the final 145ms of the response, where hue indicates preferred orientation and brightness shows orientation tuning strength. The dotted red line delineates the expected retinotopic boundary of feedforward input based on Albus (2004).

The inset quantitatively compares the spatial extent of:
1. Total cortical activation (grey contour)
2. Orientation-selective activation (black contour) 
3. Theoretical feedforward input boundary (red contour)

This data demonstrates that orientation-selective responses propagate laterally beyond the classical feedforward input zone through horizontal connections, while maintaining some degree of feature selectivity. The systematic comparison between total activation and selective activation provides direct evidence for how horizontal connectivity shapes the spatiotemporal dynamics of orientation processing in V1.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig2AB.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Panel B presents a comprehensive population analysis spanning nine hemispheres (three from area 17 marked with 'o' and six from area 18 marked with '+') examining how orientation selectivity changes with horizontal distance. The top plot shows the iso-orientation bias as a function of lateral spread distance, beginning from the initial cortical activation point. An exponential decay function (shown in black) fits this relationship. The bottom plot quantifies how the condition-wise modulation depth diminishes as the lateral propagation distance increases. Together, these results demonstrate a systematic weakening of orientation selectivity with increasing horizontal distance from the activation site.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig2AC.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Panel C displays intracellular recordings of subthreshold responses visualized as a visuotopic orientation polar map. The color hue represents preferred orientation while brightness indicates the strength of orientation tuning in the membrane potential. White contours outline regions showing statistically significant responses based on both amplitude and orientation selectivity criteria. The middle plots show averaged subthreshold responses to four different oriented stimuli (color-coded) at specific recording locations (marked by circle, triangle and square symbols), with scale bars indicating 50 ms and 1 mV. On the right, normalized orientation tuning curves are shown, computed by integrating responses within a fixed temporal window (shaded region in middle panel). The black circle marks the spontaneous activity level for the depolarizing integral measurement.

These shows a direct functional evidence for a diversity of tuning profile in th horizontal connectivity.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig4ABC.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Figure 4 illustrates a neural field model that bridges anatomical structure with functional observations in V1, as developed by Rankin and Chavane (2017). 

Panel A depicts radial connectivity profiles with Gaussian-decaying inhibition and distance-dependent excitation that peaks periodically at multiples of distance L. The Ring Width (RW) parameter controls the spread of these excitatory peaks.

Panel B shows how local orientation preference maps influence lateral connectivity patterns under different orientation bias (BR) values in the recurrent connections. 

Panel C quantifies the orientation tuning that emerges from these connectivity patterns. While orientations are uniformly represented globally, the local excitatory component shows strong bias around -60°. As BR increases above 0.5, the lateral connection orientation bias strengthens, reaching values around k=1 (consistent with Buzás et al. 2006).

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig4ABCDE.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}


Panel D presents a simulation snapshot at 600ms demonstrating two key activity components: orientation-selective responses (within white contour) confined to the feedforward footprint (FFF, red), and broader non-orientation-specific activity (grey contour) extending beyond.

Panel E tracks the temporal evolution of both the non-orientation-specific and orientation-selective response areas.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig4.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

Panel F maps the normalized selective area (relative to the feedforward footprint) across Ring Width (RW) and orientation bias (BR) parameters. White contours delineate anatomically plausible ranges where k values fall between 0.7-1.2, consistent with experimental measurements. The green region indicates parameter combinations that additionally satisfy constraints on both orientation preference and the observed radial decay of selectivity.

The neural field model effectively connects anatomical connectivity patterns with functional observations of orientation selectivity propagation in V1. The resulting connectivity structure exhibits similarities with "association field" patterns, suggesting potential optimization for encoding natural image statistics. This framework provides a quantitative basis for investigating computational principles underlying horizontal connectivity in visual cortex.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig5A.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}
This figure illustrates the groundbreaking approach developed by Geisler et al. (2001) for analyzing edge statistics in natural images. The method involves:

This landmark work systematically analyzed the occurrence of edge pairs in natural images through:

1. Edge detection using orientation-selective filters (red segments)
2. Measuring geometric relationships between edge pairs:
	- Relative orientation difference (𝜃)
	- Relative position angle (𝜙)

The analysis revealed robust statistical regularities:
- A predominance of parallel edge arrangements
- A strong bias for co-circular edge configurations


{{< /speaker_note >}}


</section>

---

<section>

# Modelling the Association field

{{< figure src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/bosking2Asso.png" title="[Field *et al*, 2013]" height="420" >}}


{{< speaker_note >}}


Understanding how these image statistics relate to cortical connectivity patterns provides key insights into the computational principles underlying horizontal connections in V1.

{{< /speaker_note >}}

<!-- 
---

## Edge co-occurences in natural images

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/featured.jpg" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" height="420" >}}

{{< speaker_note >}}

Panel A shows a sample image overlaid with detected edges represented as red line segments. Each segment encodes position (center point), orientation, and scale (segment length). The edge detection was controlled to ensure the reconstruction error remained below 5% of the original image energy.

Panel B illustrates the geometric relationships between edge pairs. For any reference edge A and target edge B, these relationships are quantified by:
- Orientation difference (θ)
- Scale ratio (σ) 
- Center-to-center distance (d)
- Azimuth difference (φ)
- Co-circularity parameter ψ = φ - θ/2

Following Geisler et al. (2001), edges outside a central circular mask were excluded to prevent boundary artifacts in the statistical analysis.

{{< /speaker_note >}} -->

---

## Edge co-occurences in natural images

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig5A.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}
Panel A illustrates the groundbreaking approach developed by Geisler et al. (2001) for analyzing edge statistics in natural images. The method involves:

1. Detecting oriented edge elements in natural images (shown as red segments)
2. For each edge pair, measuring:
	- Their relative orientation difference (𝜃)
	- The relative position angle (𝜙)
	- Center-to-center distance (d)
	- Azimuth difference (φ)
	- Co-circularity parameter ψ = φ - θ/2

This quantitative analysis reveals two key distributions:
- A strong bias for parallel edge arrangements, evident in the orientation difference histogram
- A marked preference for co-circular alignments, shown in the relative position histogram

These statistics vary significantly across image databases. For example, images containing animals exhibit enhanced co-circularity compared to general natural scenes. This suggests that rather than implementing a single fixed association field, the visual system may need to handle diverse statistical regularities present in natural inputs.

The next section will examine how these statistical regularities inform computational models of the association field.

{{< /speaker_note >}}


<!-- 
---

## Sparse representations in computer vision

{{< figure src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/figures/figure_synthesis.svg" title="[[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" height="420" >}} 
{{< speaker_note >}}

chevrons

{{< /speaker_note >}} -->

---

## Edge co-occurences in natural images


<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/Geisler01Fig3A.png" height="275"><img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/Geisler01Fig3B.png" height="275"> <img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/Geisler01Fig3C.png" height="275"> 
[Geisler, 2001]

{{< speaker_note >}}

Our analysis reproduced the key findings from Geisler et al. (2001) regarding edge co-occurrence statistics in natural images. Importantly, we observed that these co-occurrence patterns remain invariant with respect to distance, as this parameter depends primarily on viewpoint rather than intrinsic scene structure. Similarly, the statistics show rotational invariance with respect to the reference edge orientation. By leveraging these symmetries and marginalizing over distance and orientation, we were able to reduce the full 4-dimensional co-occurrence distribution to an informationally equivalent 2-dimensional representation of relative orientation difference and Co-circularity parameter ψ = φ - θ/2 where φ Azimuth difference.

{{< /speaker_note >}}

---

## Edge co-occurences in natural images

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_chevrons.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" height="420" >}}

{{< speaker_note >}}

The probability distribution function p(ψ,θ) represents the distribution of the different geometrical arrangements of edges’ angles, which we call a “chevron map”. We show here the histogram for non-animal natural images, illustrating the preference for co-linear edge configurations. For each chevron configuration, deeper and deeper red circles indicate configurations that are more and more likely with respect to a uniform prior, with an average maximum of about 3 times more likely, and deeper and deeper blue circles indicate configurations less likely than a flat prior (with a minimum of about 0.8 times as likely). Conveniently, this “chevron map” shows in one graph that non-animal natural images have on average a preference for co-linear and parallel edges, (the horizontal middle axis) and orthogonal angles (the top and bottom rows), along with a slight preference for co-circular configurations (for ψ =0 and ψ = ± π/2, just above and below the central row).

{{< /speaker_note >}}

---


## Edge co-occurences in natural images

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_chevrons2.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" height="420" >}}

{{< speaker_note >}}

The chevron maps reveal distinct edge configuration biases across image categories. Animal images show relatively more circular continuations and converging angles compared to non-animal images (red regions in central vertical axis), while having fewer co-linear, parallel and orthogonal arrangements (blue regions along horizontal axis). In contrast, man-made images exhibit a strong bias for co-linear features (intense red at center). This suggests the visual system must adapt to diverse statistical regularities rather than implementing a fixed association field pattern, as different image categories contain systematically different geometric arrangements of edges.

{{< /speaker_note >}}

---

## Edge co-occurences in natural images

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_results.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" height="420" >}}

{{< speaker_note >}}

This figure shows classification performance across image categories using different statistical features. We used an SVM classifier with three feature sets: first-order orientation statistics (FO), the reduced 2D "chevron map" (CM), and full 4D second-order statistics (SO). The classification accuracy (F1 score) was tested for distinguishing between image categories. Results show strong performance in separating man-made from natural images, as expected. More notably, the classifier achieved ~80% accuracy in discriminating animal vs non-animal natural images, matching human performance levels reported by Serre et al. This suggests that relatively simple edge co-occurrence statistics contain sufficient information for basic image categorization tasks, without requiring higher-level semantic processing.

We also found that our model made the same errors as humans do: if an image without an animal contains more co-circular edges, it is more likely to be falsely categorized as containing an animal.

{{< /speaker_note >}}

---

## Edge co-occurences in natural images

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-bednar-15/figure_chevrons.png" title="Edge co-occurrences can account for rapid categorization of natural versus animal images [[LP and Bednar, 2015]](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)" height="420" >}}

{{< speaker_note >}}

While we have demonstrated how to derive association fields from natural image statistics, it is important to note that the resulting probability distribution function represents an average over many possible edge configurations. Though this statistical approach successfully discriminates between image categories (e.g., animal vs non-animal images), it likely oversimplifies the true diversity of edge arrangements present in natural scenes. Individual images may contain unique geometrical patterns that deviate significantly from the average statistics. Understanding this variability, rather than just mean tendencies, could provide deeper insights into how the visual system handles the rich complexity of natural scenes.

{{< /speaker_note >}}

</section>

---
<section>

## Predictive processing

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" height="420" >}}

{{< speaker_note >}}
The anatomical data reveals that V1 horizontal connectivity exhibits more complexity than suggested by the classical like-to-like hypothesis. While orientation-specific connections exist, they coexist with non-selective connections that link neurons irrespective of their tuning preferences. This diversity likely serves multiple computational functions:

1. Specific connections could support contour integration and feature binding
2. Non-selective connections may enable broad contextual modulation 
3. Mixed connectivity patterns could help maintain network stability while preserving functional specificity

This anatomical heterogeneity aligns with V1's role in both specialized feature detection and broader contextual processing. Understanding how these distinct connectivity patterns interact remains an active area of research in visual neuroscience.

{{< /speaker_note >}}

---

## Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}
- this can be integrated in a hierarchy...
- defining a Convolutional Neural Networks (CNN)
- one layer is a convolution
{{< /speaker_note >}} 

---

## Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}
- modifications= adding sparse coding + feedback
{{< /speaker_note >}}


---

## Predictive processing

{{< figure src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/BoutinFranciosiniChavaneRuffierPerrinet20face.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}
- result= interpretable features
{{< /speaker_note >}}

---

## Predictive processing

{{< figure  src="https://github.com/laurentperrinet/2020-09-25_IRPHE/raw/master/figures/PCOMPBIOL-D-19-01811_R2_compressed_FigS4.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Predictive processing

{{< figure  src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" height="420" >}}

{{< speaker_note >}}

{{< /speaker_note >}}

---

## Supplementary : Predictive processing with pooling

{{< figure src="https://laurentperrinet.github.io/publication/franciosini-21/featured.jpg" title="[[Boutin *et al*, 2022](https://laurentperrinet.github.io/publication/franciosini-21/)]" height="420" >}}

{{< speaker_note >}}

{{< /speaker_note >}}


</section>

---

<section>

# Dynamics of vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" height="420" >}}

{{< speaker_note >}}
- another important missing feature: time
{{< /speaker_note >}}

---

## Dynamics of vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency_bg.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." height="420" >}}

{{< speaker_note >}}
**1 MINUTE**

- In particular in our group, we are interested in dynamics of neural processing

- The visual system is very efficient in generating a decision from the retinal image to the different stages of the visual pathways, here for a macaque monkey, a reaction of finger muscles in about 300 milliseconds.

- the process of categorizing an object takes 10 layers

{{< /speaker_note >}}

---

## Dynamics of vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Visual latencies ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." height="420" >}}

{{< speaker_note >}}
**1 MINUTE**

- the latencies are of similar in the human brain but merely scaled due to the brain size

- as a consequence, it is thought that this efficiency is achieved by spikes that is, brief all-or-none events which are passed in the very large network which forms the brain from assemblies of neurons to others.

{{< /speaker_note >}}

---


## Dynamics of vision

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/tsonga.jpg" title="Sensorimotor delays ([Perrinet & Friston 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))" height="420" >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---


## Dynamics of vision

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/figure-tsonga.jpg" title="Sensorimotor delays ([Perrinet & Friston, 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))" height="420" >}}

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

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" height="420" >}}

{{< speaker_note >}}
- ...
{{< /speaker_note >}}

---

# Dynamics of vision: Neural modeling

{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/figure_series.png" height="420"> {{% /fragment %}}{{% fragment %}}<img src="https://github.com/laurentperrinet/PerrinetBednar15/raw/master/talk/figure_series_11.png" height="420"> {{% /fragment %}}

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