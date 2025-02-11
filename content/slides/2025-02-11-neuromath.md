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
	<!-- <a href="https://laurentperrinet.github.io/grant/anr-anr">  -->
		  <img src="https://laurentperrinet.github.io/grant/polychronies/featured.png" alt="header" height="300"> 
		  <!-- <img src="https://laurentperrinet.github.io/post/2019-06-22_ardemone/featured.png" alt="header" height="300">  
	</a>-->
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

Hi, thanks for the introduction! I am Laurent Perrinet, a researcher in computational neuroscience and currently a research director at CNRS at the Institute of Neuroscience of la Timone in Marseille. **Thank you** for inviting me to participate in this "NeuroMathematics" seminar at the intersection of mathematics and neuroscience.

As an engineer by training, I could have pursued a career in aeronautics rather than becoming a neuroscientist. It is thanks to my mathematics professor **Manuel Samuelides** that I discovered the beauty of neural networks at the end of my engineering studies. This developped a curiosity, and thanks to him, I was also able to study in a mastere of cognitive sciences (now called CogMaster) in 1998. This is where I particularly want to acknowledge **Jean Petitot** - for his course I discovered how natural image statistics could link to principles in the central nervous system. This was a vivid revelation, and I'm grateful for his guidance in my academic path. Today's seminar represents a return to these roots, as I'll present my research progress since my mastere thesis on this very topic.

Today, I will address our current knowledge about **horizontal connectivity rules in V1**. Why is this important? As a matter of fact, one main function of sensory systems, such as the pivotal role of the primary visual cortex for vision, is to bind together the different visual features to help ultimately build a global perception.

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

to rephrase the expression ["The Unreasonable Effectiveness of Mathematics"](https://en.wikipedia.org/wiki/The_Unreasonable_Effectiveness_of_Mathematics_in_the_Natural_Sciences) by Wigner, the "Unreasonable efficiency of vision" is playfully illustrated in this painting from Joan Miró, which allows us to depict this Catalan landscape with the a few strokes where our imagination will fill the gaps and signify the landscape, allowing us to imagine the hunter, the sardine or the plane. 

This is so striking that lines or contours may appear even when they do not exist, such as in this display created with the visual artist Etienne Rey (beware! it will likely tickle your eyes).

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

With only dots arranged in two hewxagonal grids simply shifted by an anagle of 9°, we still see lines, such as a lower-frequency hexagonal grid, and even an illusion of depth. Notice how this illusion depends on the position of your eye and therefore of your retina. Can we make sense of these phenomena?

{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Field1993Fig3B.jpg" title="[Field *et al*, 1993]" height="420" >}}

{{< speaker_note >}}

This percept of continuity was previously already framed in the **Gestalt** paradigm and was further developed into a quantitative framework. This seminal work by Field, Hayes and Hess in 1993 demonstrated that observers were better at detecting contours formed by aligned Gabor patches compared to randomly oriented ones. Like how a contour may preferentially emerge in a dense field of edges.
{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Field1993Fig3.jpg" title="[Field *et al*, 1993]" height="420" >}}


{{< speaker_note >}}

Their psychophysical experiments showed that detection performance was best when elements were co-aligned and degraded systematically as the relative orientation between elements increased. This highlighted significant edge parameters such a relative orientation, distance, but not phase. 

{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/AssoFieldNoBosking.png" title="[Field *et al*, 1993]" height="420" >}}


{{< speaker_note >}}

Consequently, they proposed that this perceptual grouping relies on an "association field" - a hypothetical linking mechanism that preferentially connects neurons tuned to similar orientations. 
But where does this association field comes from ?

{{< /speaker_note >}}

---

## Natural Images : Edges are on a common circle


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Sigman2001Fig4.jpg" title="[Sigman *et al*, 2001]" height="420" >}}

{{< speaker_note >}}

A significant contribution to understanding the association field came from studying **edge co-occurrences in natural images** by Sigman et al. (2001). They quantified the probability density function of edge co-occurrences based on their relative positions and orientations. The figure demonstrates this by showing the spatial distribution patterns for edges relative to a reference edge at different orientations. For iso-oriented edges (a), the co-occurrence pattern shows clear structure. As the relative orientation increases through 22.5° (b), 45° (c), 67.5° (d), to 90° (e), distinct spatial patterns emerge. 

A key finding was that for any given relative orientation between edges, the angle of maximal interaction occurs at the bisector between the orientations. This suggests that **co-occurring edges tend to lie on a common circle** - a property known as cocircularity. Panel (f) illustrates this geometrical principle: given two edges at angles w (red, 20°) and c (blue, 40°), the cocircularity solutions (green lines at 30° and 120°) represent the possible orientations of connecting circular arcs. This mathematical relationship provides insights into how the visual system might leverage statistical regularities in natural scenes for contour integration. We will go back into the details of this a bit further in the talk.

This association field concept provided a compelling framework for understanding how the visual system may implement contour integration through neural connectivity patterns. but before going there we should go back to the **basic anatomy of the visual cortex**.

{{< /speaker_note >}}

---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/AssoFieldNoBosking.png" title="[Field *et al*, 1993]" height="420" >}}


{{< speaker_note >}}


{{< /speaker_note >}}

---

## Dynamics of vision

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency_bg.jpg" title="Human Visual system ([Grimaldi *et al* 2022](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))" height="420" >}}

{{< speaker_note >}}
**<1 MINUTE**

- Let's begin with the **anatomy** of the visual system. 

{{< /speaker_note >}}

---

## Anatomy of the Human Visual system

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/visual-latency.jpg" title="Human Visual system ([Grimaldi *et al* 2022](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))" height="420" >}}

{{< speaker_note >}}
The diagram shows the human visual pathways, where information flows from the **retina** through the optic nerve to reach the lateral geniculate nucleus  in the thalamus. From there, signals project to the **primary visual cortex** (V1) where neurons are selective to local oriented edges. Information then proceed through higher visual areas following two main streams - the ventral "what" pathway (which I show here) and the dorsal "where/how" pathway. This hierarchical organization allows for increasingly complex visual processing, ultimately enabling motor responses and behavior. The **latencies** shown in the figure indicate the sequential timing of neural activation across these processing stages.
{{< /speaker_note >}}

---

## Thalamic, short- & long-range lateral, interareal


<!-- {{< figure src="https://laurentperrinet.github.io/publication/perrinet-07-neurocomp/featured.png" height="200" >}}{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/cortical-columns_a_02_cl_vis_3e.jpg"  height="150" >}} -->
{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/cortical-columns.jpg" height="420" >}}

{{< speaker_note >}}

A key feature of primary visual cortex is its **layered organization**, which is shared across cortical areas. The main thalamic input arrives in layer 4, which connects to a dense network of vertical connections across layers. These columns can then communicate via horizontal connections within layers.


Hubel and Wiesel also proposed the **ice-cube model** that every point in the visual field produces a response in a 2 mm x 2 mm area of the cortex. Such an area can contain two complete groups of ocular dominance columns, 16 blobs and interblobs that may contain more than two times all of the orientations possible across 180 degrees. This region of the cortex, which Hubel and Wiesel called a hypercolumn (or, more generally, a cortical module) seems both necessary and sufficient for analyzing the image of a point in visual space. Because the cortex is a continuous cellular layer and because it is very hard to establish the boundaries of these modules physically, their existence from a functional standpoint is still the subject of debate. 
https://thebrain.mcgill.ca/flash/a/a_02/a_02_cl/a_02_cl_vis/a_02_cl_vis.html

Figure 9.2. Hypercolumn Diagram. Ocular dominance columns are segregated into left and right eye inputs. Orientation columns are neurons that get excited at different orientations and a cluster of these is called a pinwheel. Blobs are color selective and for every pinwheel there is a blob. (Credit: McGill: The Brain from Top to Bottom, Figure of hypercolumns, Copyleft https://copyleft.org/, https://thebrain.mcgill.ca/flash/a/a_02/a_02_cl/a_02_cl_vis/a_02_cl_vis.html. No modifications.)

From: https://pressbooks.umn.edu/sensationandperception/chapter/columns-and-hypercolumns-in-v1/
{{< /speaker_note >}}

---

## Thalamic, short- & long-range lateral, interareal

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Markov2011Fig2_cercorbhq201f02_ht.jpg" title="[Markov *et al* 2011]" height="380" >}}

{{< speaker_note >}}

This figure from Markov et al. (2011) quantifies intrinsic connectivity patterns in macaque V1 through retrograde tracer injections. The data shows that 85% of connections are intra-areal, with connection density decreasing exponentially with distance (characteristic length ~0.23mm). Most connections (80%) remain within 1.5mm radius - notably close given the ~0.5mm spacing between orientation pinwheels. This provides strong evidence that the vast majority of inputs to V1 neurons come from within V1 itself rather than from other areas, suggesting local processing plays a dominant role in V1 computation.

{{< /speaker_note >}}

---

## Anatomy of the Primary Visual Cortex

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Kaschube2010Fig1.jpg" title="[Kaschube *et al* (2010)]" height="420" >}}

{{< speaker_note >}}

V1 is central to these pathways and shows distinctive anatomical and functional properties along with a complex topographical organization.

This figure from Kaschube et al. (2010) illustrates the **organization of orientation preference maps** in primary visual cortex (V1). 
Individual V1 neurons exhibit selective responses to oriented visual stimuli (as denoted by varying hues Colors code preferred ORs as indicated by the bars in (C)), with their spatial arrangement following highly structured patterns across the cortical surface. 
Panel B shows Synthetic orientation-maps of equal column spacing Λ but widely different pinwheel densities ρ. Left to right: solutions of different models: (13–16).. (C) High (blue frame) and low (orange frame) pinwheel density regions in tree shrew visual cortex. (D to F), Optically recorded orientation-maps in tree shrew (D), galago (E), and ferret (F) visual cortex. Regions shown in (C) are marked in (D). White arrows in (F) mark selected pinwheel centers. Framed regions in (C) and (F) are magnified.
In many mammals including cats, monkeys and ferrets, orientation preference is organized in a quasi-periodic manner, forming what are known as orientation preference maps. These maps show remarkable consistency in their geometric properties across species, particularly in the spatial organization of pinwheel centers where orientation preferences converge.

However, this organization shows important **species-specific variations**. Most notably, while primates and carnivores display orderly orientation maps with smooth transitions between preferred orientations, rodents lack such maps and instead show a "salt-and-pepper" arrangement where neighboring neurons have seemingly random orientation preferences. This organizational diversity raises interesting questions about the computational advantages of these different architectures and their relationship to visual processing requirements and behavioral needs across species.


{{< /speaker_note >}}

---

## Horizontal connectivity links different hypercolumns

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" height="420" >}}

{{< speaker_note >}}

This figure shows landmark results by Bosking et al. (1997) combining orientation preference maps with retrograde tracers. After injecting tracers (white arrow), they found labeled synapses (black dots) primarily connecting neurons of similar orientation preference, leading to the influential "like-to-like" connectivity hypothesis. However, later studies by Hunt, Goodhill and others revealed significant diversity in these connection patterns across cortical regions and species, suggesting more complex connectivity rules than initially proposed. This nuanced understanding has important implications for how we think about the functional organization of horizontal connections in V1.

{{< /speaker_note >}}


---

## Contour detection and the Association Field


{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/AssoFieldNoBosking.png" title="[Field *et al*, 1993]" height="420" >}}


{{< speaker_note >}}


{{< /speaker_note >}}

---

## The like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/AssoFieldBosking.png" title="[Field *et al*, 1993]" height="420" >}}


{{< speaker_note >}}

The resemblance between what was shown by Bosking and the structure of the association field that we saw above is such that it is tempting to align both and state that the function of horizontal connections is to bind neurons with a selectivity to *similar orientations** over long distances. This **like-to-like hypothesis** has been influential in understanding horizontal connectivity patterns. 

However, we should be cautious about overstating these relationships. While horizontal connections show some orientation specificity, recent evidence indicates the connectivity patterns are **more complex and heterogeneous** than initially proposed. The functional role of this diverse connectivity remains an active area of investigation.

During the **remainder of this talk**, I will try to shed light on our current knowledege on horizontal connectivities.

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

</section>

---

<section>

# Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/header.png" title="[[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="380" >}}

{{< speaker_note >}}

Together with my colleagues Frédéric Chavane (INT) and James Rankin (University of Exeter), we published this paper in **Brain Structure and Function** that reviews anatomical, functional, computational and theoretical evidence **challenging the like-to-like hypothesis.** The paper evaluates whether this influential hypothesis about V1 horizontal connectivity holds up against accumulated empirical evidence. The review systematically examines multiple lines of research to reassess our understanding of these important cortical circuits.

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1A.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

This figure illustrates different hypothetical connectivity rules for horizontal connections in V1. The target neuron (large circle on left) has a specific orientation preference indicated by its color. Following the classical like-to-like hypothesis (shown in panel A), this neuron would preferentially connect to other neurons with matching orientation preference (similar colors) across multiple hypercolumns, as indicated by the vertical red arrows. The radial spread of connections spans approximately three hypercolumns, consistent with anatomical observations. Each hypercolumn contains a complete set of orientation preferences, represented by the different colored neurons.

This first schematic (noted A) represents one of the like-to-like connectivity rules, where horizontal connections strictly follow orientation similarity. 

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

{{< video src="https://laurentperrinet.github.io/publication/chavane-22/area17_lo_diff_circ_plot.mp4" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)"  autoplay="yes" repeat="yes" height="420" >}}


{{< speaker_note >}}

Let's first shows some functional evidence. 

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

{{< figure src="https://laurentperrinet.github.io/publication/voges-12/featured.jpg" title="[[Voges and LP, 2012]](https://laurentperrinet.github.io/publication/voges-12/)" height="420" >}}

{{< speaker_note >}}

To quantitatively understand how connectivity patterns shape network dynamics, we previously showed in simulated neural networks that transitioning from local unspecific to local specific and long-range patchy connectivities can fundamentally alter emergent activity patterns [Voges & LP, 2012]. This highlights how the detailed organization of horizontal connections plays a crucial role in shaping the dynamics of recurrent neural circuits. We will examine this computational aspect further in our review of the evidence challenging strict like-to-like connectivity rules.

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

While we demonstrated how association fields emerge from edge statistics, the resulting probability distribution represents an average across many possible configurations. Though this statistical approach successfully discriminates between image categories like animal vs non-animal images, it likely oversimplifies the true diversity of edge arrangements in natural scenes.

Individual images contain unique geometrical patterns that can deviate significantly from these average statistics - for example:
- Smooth contours 
- Edge occlusions
- Complex textures
- Fractal-like patterns

Understanding this variability, rather than just mean tendencies, could provide deeper insights into how horizontal connectivity patterns may adapt to handle the rich complexity of natural scenes.

{{< /speaker_note >}}

</section>

---
<section>

## Can we explain the diversity ?

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" height="420" >}}

{{< speaker_note >}}

Indeed, this diversity is revealed in the anatomical data: V1 horizontal connectivity exhibits more complexity than suggested by the classical like-to-like hypothesis. While orientation-specific connections exist, they coexist with non-selective connections that link neurons irrespective of their tuning preferences. This diversity likely serves multiple computational functions:

1. Specific connections could support contour integration and feature binding
2. Non-selective connections may enable broad contextual modulation 
3. Mixed connectivity patterns could help maintain network stability while preserving functional specificity

This anatomical heterogeneity aligns with V1's role in both specialized feature detection and broader contextual processing. Understanding how these distinct connectivity patterns interact remains an active area of research in visual neuroscience.

{{< /speaker_note >}}

---

## Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}
To understand the diversity in horizontal connectivity patterns, we developed a biologically plausible hierarchical model based on **Convolutional Neural Networks (CNNs) backbone**. The model processes natural images through multiple convolutional layers organized in a hierarchical structure:. 

1. Natural image as input
2. Local receptive fields via convolution operations  
3. Hierarchical processing through multiple layers

{{< /speaker_note >}}


---

## Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}

To bridge the gap between anatomical observations and functional requirements of visual processing, We added two key ingredients in the  sparse deep predictive coding (SDPC) model :


1. **Sparse** connectivity patterns:
	- Enforcing regularization of the activity map using L1 penalty
	- Activity computed via recurrent local connectivity
	- Similar to biological observations

2. **Feedback** from efferent layers:
	- Predicts activity of afferent layer
	- Only residual prediction error is processed 
	- Defines long-range inter-areal connectivity
	- Specific influence demonstrated in Neural Computation paper

By defining a **cost on minimizing the prediction error** in each layer,  everything stays derivable, such that we can use a classical gradient descent. These additions should allow us to better understand how feedback shapes visual processing in biological neural networks.


{{< /speaker_note >}}


---

## Predictive processing

{{< figure src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/BoutinFranciosiniChavaneRuffierPerrinet20face.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}

Our key findings reveal highly interpretable receptive fields:

1. First layer filters exhibit classical orientation-selective filters
2. When trained on face datasets, specialized feature detectors emerge içn the second layer for:
	* Eyes
	* Ears
	* Mouths
	* Smooth contours

These results suggest that predictive processing frameworks may offer better **interpretability** compared to classical deep learning architectures.

{{< /speaker_note >}}

---

## Predictive processing

{{< figure  src="https://github.com/laurentperrinet/2020-09-25_IRPHE/raw/master/figures/PCOMPBIOL-D-19-01811_R2_compressed_FigS4.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}

More specifically in the context of our focus today, we can look at the co-occurence 

llustration of the procedure to generate interaction map. In this
illustrative example we consider a V1 representation with only 4 feature maps
(represented in the upper-left box). Step 1 is to extract a neighborhood (of size 3x3 in
the illustration only) around the most strongly activated neuron (represented with a red
square in the illustration) for a given central preferred orientation (denoted ✓ c ). Step 2
is to normalize the neural activity in the extracted neighborhood using the marginal
activity (see Eq.8). Step 3 is to compute the resulting orientation and activity at every
position of the neighborhood using a circular mean (see Eq. 11 and Eq. 12 respectively).
To keep a concise figure we have illustrated the computation of the central edge of the
interaction map only. For simplification, the illustration shows only 1 neighborhood
extraction whereas the interaction maps shown in the paper are computed by averaging
neighborhoods centered on the 10 most strongly activated neurons

{{< /speaker_note >}}

---

## Predictive processing

{{< figure  src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/boutin-franciosini-chavane-ruffier-perrinet-20Fig3.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}

What is more relevant is to study the interaction patterns between neurons from the first layer. 

{{< /speaker_note >}}

---

## Predictive processing

{{< figure  src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/boutin-franciosini-chavane-ruffier-perrinet-20Fig4.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" height="420" >}}

{{< speaker_note >}}

We can further analyze the relative role fo feedback: Relative co-linearity and co-circularity of the V1 interaction map w.r.t. to feedback . (A) In the end-zone. (B) In the side-zone. For each plot, the left and right block of bars represents the relative co-linearity and co-circularity their respective value without feedback (see Eq. 23 and Eq. 24). Bars’ heights represent the median over all the orientations, and error bars are computed as the median absolute deviation. 

{{< /speaker_note >}}

---

## Predictive processing with pooling

{{< figure src="https://laurentperrinet.github.io/publication/franciosini-21/featured.jpg" title="[[Boutin *et al*, 2022](https://laurentperrinet.github.io/publication/franciosini-21/)]" height="420" >}}

{{< speaker_note >}}

It is worth noting that extending the model with additional architectural features, such as long-range horizontal connectivity across neighboring hypercolumns, enables the emergence of more complex properties including topographic maps and complex cell-like responses. However, examining these extensions falls beyond the scope of today's presentation.

{{< /speaker_note >}}


</section>

---

<section>


## Challenging the like-to-like hypothesis

{{< figure  src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" height="420" >}}

{{< speaker_note >}}

As a result, predictive processing may be an efficient model to better understand the richness of horizontal connectivity patterns. 

{{< /speaker_note >}}

---

## Challenging the like-to-like hypothesis

{{< figure src="https://laurentperrinet.github.io/publication/chavane-22/Chavane2022fig1AE.jpg" title="Revisiting Horizontal Connectivity Rules in V1: From like-to-like towards like-to-All [[Chavane, LP and Rankin, 2022]](https://laurentperrinet.github.io/publication/chavane-22/)" height="420" >}}

{{< speaker_note >}}

To conclude, our review of horizontal connectivity in V1 reveals patterns more complex than initially theorized. The classical like-to-like hypothesis, while valuable, doesn't fully capture the **diversity** of observed connectivity patterns.

**Mathematical modeling** has proven essential in bridging theory and biology. Our predictive processing framework shows how simple computational principles can explain the emergence of these complex connectivity patterns. The model demonstrates how feedback influences lateral interactions and reproduces key experimental observations.

However, **important questions remain unanswered**. We need to better understand how precise timing information is encoded in these circuits, how temporal dynamics shape processing, and whether similar principles apply across other cortical areas.

These fundamental questions will guide future experimental and theoretical work as we continue to unravel the computational principles of cortical processing.

{{< /speaker_note >}}

---
<h2><u>
	[2025-02-11] When Cortical Neurons Talk Sideways: Beyond Feedforward Visual Processing
</u></h2>
<table>
<tr>
	<!-- <a href="https://laurentperrinet.github.io/grant/anr-anr">  -->
		  <img src="https://laurentperrinet.github.io/grant/polychronies/featured.png" alt="header" height="300"> 
		  <!-- <img src="https://laurentperrinet.github.io/post/2019-06-22_ardemone/featured.png" alt="header" height="300">  
	</a>-->
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

Thanks for your attention, I would be happy to take your questions.

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

# Spiking Neural Networks: Spiking motifs

{{< speaker_note >}}
**2 MINUTE**

These observations have led us to *review* neurobiological evidence around the existence of a neural representation that would use the relative time of spikes as a means of representing information. In particular, it is possible to use the conduction *delays* that exist in the transmission of spikes from one neuron to another. It may seem paradoxical, but these delays are not simply a constraint, but can help to improve our ability to represent information by way of *spiking motifs*.

{{< /speaker_note >}}

---

## Spiking Neural Networks: Spiking motifs

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/izhikevich.png" title="[Grimaldi *et al*, 2023, [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)]" width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

 If we consider, for example, this ultra-simplified network consisting of three presynaptic neurons and two output neurons connected by *heterogeneous* delays, then we can see that a *synchronous* input will generate membrane activity in the two output neurons at different times, so the threshold will never be reached, and these neurons will not produce an output impulse. On the other hand, if these delays are such that the action potentials converge on the neuron at the same instant, then these contributions will be able to sum up at the *same instant* and produce an output spike, as denoted here by the red bar.
{{< /speaker_note >}}

---

## Spiking Neural Networks: Spiking motifs

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/LIF.gif" title="Review on [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)." width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

To better understand this mechanism, let's return to our animation of a spiking neuron. Action potentials arrive at the neuron and are *immediately* transmitted to the neuron's cell body to be integrated and potentially generate a spike. 

{{< /speaker_note >}}

---

## Spiking Neural Networks: Spiking motifs

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/HSD.gif" title="Review on [Precise Spiking Motifs](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/)." width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

When using *heterogeneous* delays, the situation is different, as the information will take a differential time to arrive or not at the neuron's cell body. Note that if we include a particular *spiking motif*, which we have here highlighted by green action potentials, then these converge at the same instant thanks to the delay. We will therefore have a detection in the neuron in the form of a new impulse.

{{< /speaker_note >}}

---

## Spiking Neural Networks: HD-SNN

{{< video src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/FastMotionDetection_input.mp4" autoplay="yes" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" >}}

{{< speaker_note >}}
**2 MINUTE**
We used this theoretical principle in an algorithm for detecting movement in an image. To do this, we first generated event data using natural images that are set in motion along trajectories that resemble those produced by free exploration of the visual scene. You'll notice several features of the event-driven output, such as the fact that faster motion generates more spikes, or that edges oriented parallel to one direction produce few changes, and therefore little spike output - the so-called aperture problem.

{{< /speaker_note >}}

---

## Spiking Neural Networks: HD-SNN

{{< figure src="https://raw.githubusercontent.com/laurentperrinet/figures/7f382a8074552de1a6a0c5728c60d48788b5a9f8/animated_neurons/conv_HDSNN.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="100%" >}}

{{< speaker_note >}}
**2 MINUTE**

We then used a neural network with a classical architecture, which we enhanced by using an impulse representation that takes into account different possible synaptic delays. In this figure, we have represented the input in the left grid, which represents the occurrence of spikes of positive or negative polarity. Then we have represented different processing channels denoted by the colors green and orange, which are applied to this input to produce membrane activity. As illustrated above, this activity will produce output pulses, notably in synaptic connection nuclei, with heterogeneous delays corresponding to the detection of precise spatio-temporal patterns.
{{< /speaker_note >}}


---

## Spiking Neural Networks: HD-SNN

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/motion_kernels.png" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

One advantage of this network is that it is differentiable, enabling us to apply classical machine learning methods, notably supervised learning. We then see the emergence of different convolution kernels, and here I represent a subset of its kernels for different directions, as denoted by the red arrows on the left of the graph. It shows the kernels obtained on the spatial representation according to the different columns, and each row represents the different delays from a delay of one on the right to a delay of 12 time steps on the left. Detectors that follow the motion emerge. For example, for the top line from top to bottom. These kernels integrate both positive neurons in red and negative polarity inputs in blue.
Such spatio-temporal filtering is observed in neurobiology, but to my knowledge had never been observed in a model of spiking neurons trained under natural conditions.

{{< /speaker_note >}}


---

## Spiking Neural Networks: HD-SNN

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/quant_accuracy_raw.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

We will now study the performance of this network in detecting motion in the flow of events entering the network. When we use all the weights of the convolution kernel, we get a very good performance of the order of 99%, represented by the black dot in the top right-hand corner. Note that in the kernels we've seen emerge, most of the synaptic weights are close to zero, so we might consider removing some of these weights, as this can be shown to reduce the number of event calculations required.

{{< /speaker_note >}}

---

## Spiking Neural Networks: HD-SNN

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/quant_accuracy_shortening.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**
This is what we've done, by first removing the parts of the core corresponding to the longest delays. This "shortens" the kernel. We quickly observed a degradation in performance, which reached half-saturation when we reduced the number of weights by around 50%. This demonstrates the importance of integrating information that is quite distant and structured over time.


{{< /speaker_note >}}

---

## Spiking Neural Networks: HD-SNN

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/quant_accuracy.svg" title="[Grimaldi & LP (2023) Biol Cybernetics](https://laurentperrinet.github.io/publication/grimaldi-23-bc/)" width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**

In a second step, we performed a pruning operation, which consists in progressively removing the weights that are the weakest. This time, performance remains optimal over a wide compression range, and we reach half-saturation when we have removed around 99.8% of the weights. This means that the network is able to maintain very good performance, even when only one weight out of 600 has been kept, and therefore, with a computation time increased by a factor of 600. This property, which we didn't expect, seems promising for creating machine learning algorithms that are less energy-hungry.

{{< /speaker_note >}}


</section>
