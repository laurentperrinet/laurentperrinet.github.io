---
 slides:
 # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  transition: 'fade'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2024-04-10'
all_day: false

## Schedule page publish date (NOT talk date).
publishDate: "2024-03-29T12:47:11+02:00"

title: 2024-04-17_phd-program-sparse-representations

summary: Sparse representations in machine learning applied to the understanding of biological vision

---
<section>

### [Sparse representations](https://laurentperrinet.github.io/slides/2024-04-17_phd-program-sparse-representations/?transition=fade)
####	*[Laurent Perrinet](https://laurentperrinet.github.io)*
####	<u>[[2024-04-17]](https://etulab.univ-amu.fr/gilson.m/compneuro_course) [NeuroSchool PhD Program in Neuroscience.](https://neuro-marseille.org/en/training/phd-program/)</u>

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.jpg)
Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)


{{< speaker_note >}}
- outline = 
  - to summarize= sparse representations help understand neuroscience biological vision
  - they have practical applications in machine learning
  - let's sparse!
 - in practice: sparse coding in a nutshell
 - perspective: convolutional sparse coding

 url_code = https://github.com/laurentperrinet/2024-04_sparse-representations

- Not only the speaker can read these notes, Press `S` key to view
- more on [doc](https://raw.githubusercontent.com/wowchemy/starter-hugo-academic/master/exampleSite/content/slides/example/index.md)


{{< /speaker_note >}}

</section>

---

<section>

## Sparse representations?

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
Sparse coding is a technique used in signal processing and machine learning to represent data in a more concise and efficient manner. It aims to find a sparse representation of the data, which means representing the data with only a small number of non-zero coefficients or activations. In sparse coding, a set of basis functions or atoms is typically defined, and the goal is to find a linear combination of these atoms that best represents the input data. The coefficients of this linear combination are often constrained to be sparse, meaning that only a few of them are allowed to be non-zero. Sparse representations resulting from these processes have been successfully applied in various domains such as image processing, computer vision, and audio signal processing. It has shown promise in tasks such as noise reduction, compression, feature extraction, and pattern recognition. By capturing the essential structure and characteristics of the data in a sparse representation, sparse coding can help reduce redundancy and noise, and extract meaningful features for further analysis or processing.
{{< /speaker_note >}}

---

{{< slide background-image="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg" >}}

<!-- <img src="https://3minutosdearte.com/wp-content/uploads/2016/11/Mir%C3%B3-Paisaje-catal%C3%A1n-el-cazador-1923-24-e1534625628322.jpg"  width="80%"/> -->

{{< speaker_note >}}

Paysage catalan (Le Chasseur)

{{< /speaker_note >}}

---

{{< slide background-image="https://www.christies.com/img/LotImages/2017/CKS/2017_CKS_13486_0110_000(rene_magritte_la_corde_sensible011104).jpg" >}}

<!-- <img src="https://www.christies.com/img/LotImages/2017/CKS/2017_CKS_13486_0110_000(rene_magritte_la_corde_sensible011104).jpg"  width="80%"/> -->

{{< speaker_note >}}

René Magritte La corde sensible (Heartstring)

Occam's razor: "Entities should not be multiplied without necessity."

{{< /speaker_note >}}

---

## Sparse representations in computer vision

<img src="https://laurentperrinet.github.io/publication/perrinet-04-tauc/featured.png"  width="80%"/>
{{< figure src="https://laurentperrinet.github.io/publication/perrinet-04-tauc/featured.png" title="[[LP *et al*, 2004](https://laurentperrinet.github.io/publication/perrinet-04-tauc/)]" width="90%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

---

## Sparse representations in computer vision

<img src="https://laurentperrinet.github.io/publication/perrinet-03-ieee/v1_tiger.gif"  width="80%"/>

{{< speaker_note >}}



{{< /speaker_note >}}

---

## Sparse representations in neuromorphic engineering


<img src="https://laurentperrinet.github.io/publication/grimaldi-23/DVSGesture_arm-roll.webp"  width="33%"/><img src="https://laurentperrinet.github.io/publication/grimaldi-23/DVSGesture_hand-clap.webp"  width="33%"/><img src="https://laurentperrinet.github.io/publication/grimaldi-23/DVSGesture_air-guitar.webp"  width="33%"/>


<!-- {{< figure src="https://lenzgregor.com/posts/event-cameras/post-rethinking/events.gif" title="[[Gregor Lenz, 2020](https://lenzgregor.com/posts/event-cameras/)]" width="100%" >}} -->

{{< speaker_note >}}

Ultimately, we get a list of events for each pixel that can be *merged* to represent the entire image. This list of events includes pixel addresses, times of occurrence, and polarities. Note that since events are generated over time, they are naturally sorted by their time of occurrence. These events are then transmitted in *real time* to the output bus, often via a USB3 connection. 
It's interesting to draw a parallel between this process and the optic nerve that connects our retina to the brain. In fact, the output of the retina consists of a million ganglion cells that emit action potentials, which are the only source of information transmitted by the *optic nerve*.

- https://www.researchgate.net/profile/Guido-Croon/publication/313221316/figure/fig2/AS:668997448134663@1536512829861/Picture-of-the-event-based-camera-employed-in-this-work-the-DVS_W640.jpg


{{< /speaker_note >}}

---

## Sparse representations in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/motion_kernels.png" title="The HD-SNN neural network." width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

- kernels learned for motion detection
- can we force a sparse connectivity (beware that's diferent from sparse activity)

{{< /speaker_note >}}


---

## Sparse representations in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/accuracy.png" title="The HD-SNN neural network." width="80%" >}}

{{< speaker_note >}}
**2 MINUTE**
- yes, the accuracy drops, but it's still good enough with a 500x sparsity
- frugal computing

{{< /speaker_note >}}

---

## Sparse representations in neuroscience

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/replicating_MainenSejnowski1995.png" title="[[Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb)]" width="99%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

---

## Sparse representations in neuroscience

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/fncir-10-00037-g001a.jpg" title="[[Kremkow *et al*, 2016](https://laurentperrinet.github.io/publication/kremkow-16/)]" width="90%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

--

## Sparse representations in neuroscience

https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/fncir-10-00037-g001a.jpg
{{< figure src="https://laurentperrinet.github.io/publication/kremkow-16/featured.png" title="[[Kremkow *et al*, 2016](https://laurentperrinet.github.io/publication/kremkow-16/)]" width="90%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}


</section>

---

<section>

## Sparse representations in a nutshell


{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- ...let's delve into a computational theory of vision
{{< /speaker_note >}}

</section>

---

<section>

## Convolutional Sparse Coding

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- this can be integrated in a hierarchy...
- defining a Convolutional Neural Networks (CNN)
- one layer is a convolution
{{< /speaker_note >}}

---

### Convolutional Neural Nets (CNN)

{{< figure src="https://www.mdpi.com/vision/vision-07-00029/article_deploy/html/images/vision-07-00029-g003.png" title="[[Jérémie & LP, 2023](https://laurentperrinet.github.io/publication/jeremie-23-ultra-fast-cat/)]" width="80%" >}}

{{< speaker_note >}}
- sota...
{{< /speaker_note >}}

---

## Convolutional Sparse Coding

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- this can be integrated in a hierarchy...
- defining a Convolutional Neural Networks (CNN)
- one layer is a convolution
{{< /speaker_note >}}

---

## Convolutional Sparse Coding


{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
- another important missing feature: time


https://journals.plos.org/ploscompbiol/article/figure/image?size=large&download=&id=10.1371/journal.pcbi.1008629.g002

https://journals.plos.org/ploscompbiol/article/figure/image?size=large&download=&id=10.1371/journal.pcbi.1008629.g014

{{< /speaker_note >}}

---

### CNN: Mathematics

* One-dimensional [discrete convolution](https://en.wikipedia.org/wiki/Convolution#Discrete_convolution) (eg in time) with a kernel $g$ of radius $K$:
$$
(f \ast g)[n]=\sum_{m=-K}^{K} f[n-m] \cdot g[m]
$$

{{< speaker_note >}}
- and be formalized as a convolution...
- but what is a convolution?
- let's start in 1D
{{< /speaker_note >}}

---

### CNN: Mathematics

* Convolution of an image (two-dimensional) with a kernel $g$ of radius $K\times K$:

$$
(f \ast g)[x, y] = \sum_{i=-K}^{K} \sum_{j=-K}^{K} f[x-i, y-j] \cdot g[i, j]
$$

{{< speaker_note >}}
- now in 2D
{{< /speaker_note >}}

---

### CNN: Mathematics

* **Cross-correlation** of an image (two-dimensional) with a kernel $g$ of radius $K\times K$:

$$
(f \ast \tilde{g})[x, y] = \sum_{i=-K}^{K} \sum_{j=-K}^{K} f[x+i, y+j] \cdot g[i, j]
$$

{{< speaker_note >}}
- note the difference between convolutions and cross-correlation
{{< /speaker_note >}}

---

### CNN: Mathematics

{{< figure src="https://stanford.edu/~shervine/teaching/cs-230/illustrations/convolution-layer-a.png" title="[[Amidi & Amidi](https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-convolutional-neural-networks)]" width="90%" >}}

{{< speaker_note >}}
-  it is a translation-invariant feature detector...
{{< /speaker_note >}}

---

### CNN: Mathematics

* Correlation of an image defined on several channels (note [the order of the indices](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)):

$$
(f \ast \tilde{g})[x, y] = \sum_{c=1}^{C} \sum_{c,i,j} f[c, x+i, y+j] \cdot g[c, i, j]
$$

{{< speaker_note >}}
- we can add different channels to the image (eg colors)...
{{< /speaker_note >}}

---

### CNN: Mathematics

* Correlation of a multi-channel image for multiple output channels (note [the order of the indices](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html)):

$$
(f \ast \tilde{g})[k, x, y] = \sum_{c,i,j} f[c, x+i, y+j] \cdot g[k, c, i, j]
$$

{{< speaker_note >}}
- now we get to the full CNN 
{{< /speaker_note >}}

---

### CNN: the HMAX model

{{< figure src="https://i.stack.imgur.com/ZlFnp.png" title="[[Serre and Poggio, 2006]](https://biology.stackexchange.com/questions/10955/ventral-stream-pathway-and-architecture-proposed-by-poggios-group)" width="65%" >}}

{{< speaker_note >}}
- sota
{{< /speaker_note >}}

---

### CNN: challenges

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_a.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- novel challenges for CNNs
- 1/ backpropagation is not bioplausible 
{{< /speaker_note >}}

---

### CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- modifications= adding sparse coding + feedback
{{< /speaker_note >}}
 
---

### CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/BoutinFranciosiniChavaneRuffierPerrinet20face.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- result= interpretable features
{{< /speaker_note >}}

---

### CNN: Topography

{{< figure src="https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization/raw/master/figures/Bosking97Fig4.jpg" title="[Bosking *et al*, 1997]"width="70%" >}}

{{< speaker_note >}}
- topography?
{{< /speaker_note >}}

---

### CNN: Topography

{{< figure src="https://laurentperrinet.github.io/publication/franciosini-21/featured.jpg" title="[[Boutin *et al*, 2022](https://laurentperrinet.github.io/publication/franciosini-21/)]" width="90%" >}}

{{< speaker_note >}}
- result= bio-mimetism
{{< /speaker_note >}}

</section>


---

<section>


## Artificial neural networks applied to the understanding of biological vision

{{< figure src="https://outde.xyz/img/Rawski/Marr/3Lvls.jpg" title="[[Marr, 1982](https://outde.xyz/2020-01-12/overappreciated-arguments-marrs-three-levels.html)]" width="90%" >}}

{{< speaker_note >}}
{{< /speaker_note >}}

---

### [Sparse representations](https://laurentperrinet.github.io/slides/2024-04-17_phd-program-sparse-representations/?transition=fade)
####	*[Laurent Perrinet](https://laurentperrinet.github.io)*
####	<u>[[2024-04-17]](https://etulab.univ-amu.fr/gilson.m/compneuro_course) [NeuroSchool PhD Program in Neuroscience.](https://neuro-marseille.org/en/training/phd-program/)</u>

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/troislogos.jpg)
Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)


{{< speaker_note >}}
- to summarize= sparse representations help understand neuroscience biological vision
- they have practical applications in machine learning
- let's sparse!
{{< /speaker_note >}}

</section>
