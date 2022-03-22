---
slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2022-03-23T09:00:00Z"
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2012-03-21T06:00:00Z"


title: 2022-03-23_UE-neurosciences-computationnelles

summary: Réseaux de neurones artificiels et apprentissage machine appliqués à la compréhension de la vision

---
# [Réseaux de neurones artificiels et apprentissage machine appliqués à la compréhension de la vision](https://github.com/laurentperrinet/2022_UE-neurosciences-computationnelles)
####	*[Laurent Perrinet](https://laurentperrinet.github.io/talk/2022-03-23-ue-neurosciences-computationnelles/)*
####	<u>[[2022-03-23]](https://ametice.univ-amu.fr/pluginfile.php/5559779/mod_resource/content/1/Planning_Neurocomp_M1_2022.pdf) [Master 1 Neurosciences et Sciences Cognitives](https://ametice.univ-amu.fr/course/view.php?id=89069)</u>

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.png)

---

# Principes de la Vision

---
## À quoi sert la vision?

{{< figure width="45%" src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_001.jpg" title="[An Unexpected Visitor (Ilya Repin, 1884)](https://www.cabinetmagazine.org/issues/30/archibald.php)" >}}

---
## À quoi sert la vision?

{{< figure width="45%" src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_002.jpg" title="[An Unexpected Visitor (Yarbus, 1965)](https://www.cabinetmagazine.org/issues/30/archibald.php)" >}}

---
## À quoi sert la vision?

{{< figure width="45%" src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_003.jpg" title="[An Unexpected Visitor - *Age?* (Yarbus, 1965)](https://www.cabinetmagazine.org/issues/30/archibald.php)" >}}

---
## À quoi sert la vision?

{{< figure width="45%" src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_006.jpg" title="[An Unexpected Visitor - *How long?*  (Yarbus, 1965)](https://www.cabinetmagazine.org/issues/30/archibald.php)" >}}

---
## Les illusions visuelles

{{< figure width="90%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Hering_illusion_without.svg" title="[Hering illusion](https://en.wikipedia.org/wiki/Hering_illusion)" >}}

---
## Les illusions visuelles

{{< figure width="90%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Hering_illusion.svg" title="[Hering illusion](https://en.wikipedia.org/wiki/Hering_illusion)" >}}

---
## Les illusions visuelles

{{< figure width="90%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/42_rotsnakes_main.jpg" title="[Rotating Snakes *Akiyoshi KITAOKA*](http://www.ritsumei.ac.jp/~akitaoka/index-e.html)" >}}
    [path2('42_rotsnakes_main.jpg')],
---
## Les neurosciences computationnelles

{{< figure width="35%" src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Churchland92.png" title="[[Sejnowski,  Koch  & Churchland (1998)](http://www.hms.harvard.edu/bss/neuro/bornlab/nb204/papers/sejnowski-koch-churchland-science1988.pdf)]" >}}

---
# De V1 aux réseaux convolutionnels

---
## Le système visuel

{{< figure width="45%" src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Voies_visuelles3.svg" title="[Système visuel humain (Wikipedia)](https://fr.wikipedia.org/wiki/Syst%C3%A8me_visuel_humain)" >}}

---
## Le cortex visuel primaire


{{< figure width="90%" src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/scientists.jpg" title="[Hubel & Wiesel, 1962]" >}}

---
## Hubel & Wiesel

{{< video  src="https://raw.githubusercontent.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/master/figures/ComplexDirSelCortCell250_title.mp4" controls="yes" title="[Hubel & Wiesel, 1962]" >}}

[Hubel & Wiesel, 1962]


---
## Topographie dans V1

{{< figure width="90%" src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]" >}}

---
## Réseaux convolutionnels : hiérarchie

{{< figure width="90%" src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" >}}


---
## Réseaux convolutionnels : CNN

{{< figure width="90%" src="https://stanford.edu/~shervine/teaching/cs-230/illustrations/architecture-cnn-fr.jpeg" title="[[Amidi & Amidi](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks)]" >}}

---
## Réseaux convolutionnels : l'opération de convolution

{{< figure width="90%" src="https://stanford.edu/~shervine/teaching/cs-230/illustrations/convolution-layer-a.png?1c517e00cb8d709baf32fc3d39ebae67" title="[[Amidi & Amidi](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks)]" >}}


---
## Réseaux convolutionnels

{{< figure width="90%" src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" >}}


---
## Réseaux convolutionnels

{{< figure width="90%" src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" >}}
---

## Math

In-line math: $x + y = z$

Block math:

$$
f\left( x \right) = \;\frac{{2\left( {x + 4} \right)\left( {x - 4} \right)}}{{\left( {x + 4} \right)\left( {x + 1} \right)}}
$$


---

# Perspectives

---

## Spiking Neural Networks

{{< figure width="90%" src="https://laurentperrinet.github.io/grant/anr-anb/event_driven_computations.png" title="From frame-based to event-based cameras." >}}

---
## Recurrent processing

{{< figure width="90%" src="https://laurentperrinet.github.io/grant/anr-anb/principe_agile.jpg" title="Our system is divided into 3 units to process visual inputs communicating by event-driven, feed-forward and feed-back communications." >}}

---

# Questions?

Ask info @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

More info @ [web-site](https://laurentperrinet.github.io/grant/anr-anb)
