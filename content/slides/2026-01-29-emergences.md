---
slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  reveal_options:
    transition: 'fade'

# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2026-01-29'
all_day: false

## Schedule page publish date (NOT talk date).
publishDate: "2026-01-25T12:47:11+02:00"

title: 2026-01-29-emergences

summary: Sparse representations in biological vision applied to the effciency of machine learning.

categories: ["Computational Neuroscience", "NeuroAI & Machine Learning", "Theoretical Neuroscience"]
tags: ["motion-perception", "neuromorphic-computing", "sparse-coding", "predictive-coding", "spiking-neural-networks"]
---
<section>

# [Neurosciences and sparsity](https://laurentperrinet.github.io/slides/2026-01-29-emergences/?transition=fade)
##	*[Laurent Perrinet](https://laurentperrinet.github.io/talk/2026-01-29-emergences/)*
###	<u>[*Séminaire à l'atelier "IA embarquée" du PEPR IA*](https://www.pepr-ia.fr)</u>
###	[2026-01-29]
![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)
Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

<!-- <img src="https://laurentperrinet.github.io/qrcode.png" alt="QR code" height="80" width="80"> -->


{{< speaker_note >}}
- outline = 
  - to summarize= sparse representations help understand neuroscience biological vision
  - they have practical applications in machine learning / warning not network sparsity
  - let's sparse!

 - in practice: sparse coding in a nutshell
 
 - perspective: convolutional sparse coding

 url_code = https://github.com/CONECT-INT/2025-03_PhDProgram-course-in-computational-neuroscience

- Not only the speaker can read these notes, Press `S` key to view
- more on [doc](https://raw.githubusercontent.com/wowchemy/starter-hugo-academic/master/exampleSite/content/slides/example/index.md)

-   url?print-pdf http://localhost:8000/?print-pdf

{{< /speaker_note >}}

</section>

---

<section>

## Sparse representations in computer vision

{{< video src="https://laurentperrinet.github.io/sciblog/files/2015-05-22-a-hitchhiker-guide-to-matching-pursuit/MPtutorial_rec.mp4" controls="yes" height="90%" >}}

Code @ [A hitchhiker guide to Matching Pursuit](https://laurentperrinet.github.io/sciblog/posts/2015-05-22-a-hitchhiker-guide-to-matching-pursuit.html)

{{< speaker_note >}}

the whole is the sum of a few parts

Sparse coding is a technique used in signal processing and machine learning to represent data in a more concise and efficient manner. It aims to find a sparse representation of the data, which means representing the data with only a small number of non-zero coefficients or activations. In sparse coding, a set of basis functions or atoms is typically defined, and the goal is to find a linear combination of these atoms that best represents the input data. The coefficients of this linear combination are often constrained to be sparse, meaning that only a few of them are allowed to be non-zero. 

{{< /speaker_note >}}

---

## Neurosciences and sparsity: a survey


<!-- <iframe allowfullscreen frameborder="0" height="100%" mozallowfullscreen style="min-width: 500px; min-height: 355px" src="https://app.wooclap.com/events/HLEQUP/questions/697a765837a5e7d1b8a8eefe" width="100%"></iframe>
 -->

* Go to wooclap.com
* Enter the code HLEQUP
* Or directly follow https://app.wooclap.com/HLEQUP?from=instruction-slide

{{< speaker_note >}}

Time for a wooclap

{{< /speaker_note >}}

---

## Neurosciences and sparsity: a survey

{{< figure src="https://laurentperrinet.github.io/talk/2026-01-29-emergences/wooclap_1.png" width="62%" >}}

---

## Neurosciences and sparsity: a survey

{{< figure src="https://laurentperrinet.github.io/talk/2026-01-29-emergences/wooclap_2.png" width="62%" >}}

---

## Neurosciences and sparsity: a survey

{{< figure src="https://laurentperrinet.github.io/talk/2026-01-29-emergences/wooclap_3.png" width="62%" >}}

---

## Neurosciences and sparsity: a survey

{{< figure src="https://laurentperrinet.github.io/talk/2026-01-29-emergences/wooclap_4.png" width="62%" >}}

---

## Neurosciences and sparsity: a survey

{{< figure src="https://laurentperrinet.github.io/talk/2026-01-29-emergences/wooclap_5.png" width="62%" >}}

---

## Neurosciences and sparsity

{{< figure src="https://media.neuromatch.social/media_attachments/files/114/427/857/683/632/363/original/a3b375df340a54aa.png" title="[[Lennie, 2003, The Cost of Cortical Computation](https://neuromatch.social/@laurentperrinet/114427859025152015)]" width="50%" >}}

{{< speaker_note >}}

Starting with the brain's known energy consumption (approximately 20% of the body's entire energy budget despite being only 2% of body weight), Lennie worked backward to determine how many action potentials this energy could reasonably support.

By synthesizing these factors and dividing the available energy budget by the number of neurons and the energy cost per spike, Lennie calculated that cortical neurons can only sustain an average firing rate of approximately 0.16 Hz while remaining within the brain's metabolic constraints.

{{< /speaker_note >}}

---

## Neurosciences and sparsity

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/Brunel200Fig2.png" title="[[Brunel, 2001](https://books.google.fr/books?hl=fr&lr=&id=b8woDqWdTssC&oi=fnd&pg=PA307&ots=KNHQrJ-TsZ&sig=0WI2cq2RnMXC7fVTyjOEWZEdlCg&redir_esc=y#v=onepage&q&f=false)]" width="50%" >}}

{{< speaker_note >}}
Phase diagrams of sparsely connected networks of excitatory and inhibitory spiking neurons


healthy network = 1Hz = sparse activity (stronger in auditory, in insects, ...)

{{< /speaker_note >}}

---

## Neurosciences and sparsity

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/main/figures/replicating_MainenSejnowski1995.png" title="[[Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb)]" width="99%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}

---

## Neurosciences and sparsity

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/fncir-10-00037-g001a.jpg" title="[[Kremkow *et al*, 2016](https://laurentperrinet.github.io/publication/kremkow-16/)]" width="90%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
{{< /speaker_note >}}


---

## Neurosciences and sparsity

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/fncir-10-00037-g001.jpg" title="[[Kremkow *et al*, 2016](https://laurentperrinet.github.io/publication/kremkow-16/)]" width="90%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
vinje et gallant
{{< /speaker_note >}}


</section>

---

<section>

## Sparse representations in a nutshell


{{< figure src="https://i.giphy.com/26xBtPbmDlugFxUiY.webp" width="90%" >}}

{{< speaker_note >}}
in summary: Sparse representations resulting from these processes have been successfully applied in various domains such as image processing, computer vision, and audio signal processing. It has shown promise in tasks such as noise reduction, compression, feature extraction, and pattern recognition. By capturing the essential structure and characteristics of the data in a sparse representation, sparse coding can help reduce redundancy and noise, and extract meaningful features for further analysis or processing.

- ...let's delve into a computational theory of sparse coding

review_bib = s.content_bib("LP", "2015", '"Sparse models" in <a href="https://laurentperrinet.github.io/publication/cristobal-perrinet-keil-15-bicv/">Biologically Inspired Computer Vision</a>')


{{< /speaker_note >}}


---

## Sparse representations in a nutshell

{{< figure src="https://laurentperrinet.github.io/publication/perrinet-04-tauc/featured.png" title="[[LP *et al*, 2004](https://laurentperrinet.github.io/publication/perrinet-04-tauc/)]" height="90%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

---

## Sparse representations in a nutshell

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/Olshausen_2.png" title="[[Olshausen and Field (1997)](http://mplab.ucsd.edu/~marni/Igert/Olshaussen_1997.pdf)]" height="90%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}


---

## Sparse representations in a nutshell

Generative model of image synthesis:

$I[x, y] =  $ 
{{< fragment >}} $\sum_{i=1}^{K} a[i] \cdot \phi[i, x, y]$ {{< /fragment >}}
{{< fragment >}} $ + \varepsilon[x, y]$ {{< /fragment >}}


{{< fragment >}}
Where $\phi$ is a dictionary of $K$ atoms, $a$ is a sparse vector of coefficients, and $\varepsilon$ is a noise term.
{{< /fragment >}}

[[LP (2015)](https://laurentperrinet.github.io/publication/perrinet-15-bicv/)]

{{< speaker_note >}}

generative model

\phi is over-complete (else it is triviallly solved by pseudo inverse)

{{< /speaker_note >}}

---

## Sparse representations in a nutshell

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/Olshausen_1.png" title="[[Olshausen and Field (1997)](http://mplab.ucsd.edu/~marni/Igert/Olshaussen_1997.pdf)]" width="90%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

---

## Sparse representations in a nutshell

Given an observation $I$,

$$
\begin{aligned}
  \mathcal{L}(a) &amp; =  - \log Pr( a | I ) \\\\
  \end{aligned} 
$$

---

## Sparse representations in a nutshell

Given an observation $I$,

$$
\begin{aligned}
  \mathcal{L}(a) &amp; =  - \log Pr( a | I ) \\\\
  &amp; = - \log Pr( I | a ) - \log Pr(a) \\\\
  \end{aligned} 
  $$

---

## Sparse representations in a nutshell

Given an observation $I$,

$$
\begin{aligned}
  \mathcal{L}(a) &amp; =  - \log Pr( a | I ) \\\\
  &amp; = - \log Pr( I | a ) - \log Pr(a) \\\\
  &amp; = \frac{1}{2\sigma_n^2} \sum_{x, y} ( I[x, y] - \sum_{i=1}^{K} a[i] \cdot \phi[i, x, y])^2 - \sum_{i=1}^{K} \log Pr( a[i] )
  \end{aligned} 
  $$


{{< speaker_note >}}

Probabilistic model

{{< /speaker_note >}}

---

## Sparse representations in a nutshell

The problem is formalized as an optimization problem $a^\ast = \arg \min_a \mathcal{L}(a)$ with:

$$
\mathcal{L} = \frac{1}{2} \sum_{x, y} ( I[x, y] - \sum_{i=1}^{K} a[i] \cdot \phi[i, x, y])^2 + \lambda \cdot \sum_i ( a[i] \neq 0)
$$

[[LP (2015)](https://laurentperrinet.github.io/publication/perrinet-15-bicv/)]

{{< speaker_note >}}

spiking prior => l0 pseudo norm
l0 problem is NP-complete

{{< /speaker_note >}}

---

## Sparse representations in a nutshell

The problem is formalized as an optimization problem $a^\ast = \arg \min_a \mathcal{L}(a)$ with:

$$
\mathcal{L}(a) = \frac{1}{2} \sum_{x, y} ( I[x, y] - \sum_{i=1}^{K} a[i] \cdot \phi[i, x, y])^2 + \lambda \cdot \sum_{i=1}^{K} | a[i] |
$$


{{< speaker_note >}}

exponential prior => L1 norm

{{< /speaker_note >}}

---

## Sparse representations in a nutshell

{{< figure src="https://laurentperrinet.github.io/publication/rentzeperis-23/featured.png" title="[[Rentzeperis *et al* (2023)](https://laurentperrinet.github.io/publication/rentzeperis-23/)]" height="60%" >}}

{{< speaker_note >}}


{{< /speaker_note >}}


</section>


---

<section>


## Sparse representations and learning

{{< video src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/ssc.mp4" title="[[LP (2010)](https://laurentperrinet.github.io/publication/perrinet-10-shl/)]" controls="yes" width="55%" >}}

{{< speaker_note >}}



{{< /speaker_note >}}

--- 

## Convolutional Sparse Coding

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure1_c.svg" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- novel challenges for CNNs
- 1/ backpropagation is not bioplausible 
{{< /speaker_note >}}

---

## Convolutional Sparse Coding

{{< figure src="https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/BoutinFranciosiniChavaneRuffierPerrinet20face.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- novel challenges for CNNs
- 1/ backpropagation is not bioplausible 
{{< /speaker_note >}}


---

### CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/SDPC_3.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="80%" >}}

{{< speaker_note >}}
- result on MNIST
{{< /speaker_note >}}

---

### CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure4a.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

{{< speaker_note >}}
- modifications= adding sparse coding + feedback
{{< /speaker_note >}}

---

### CNN: Predictive processing

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/boutin-franciosini-ruffier-perrinet-19_figure4b.png" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" width="90%" >}}

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

### CNN: Predictive processing

{{< video src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/training_video_ATT.mp4" title="[[Boutin *et al*, 2021](https://laurentperrinet.github.io/publication/boutin-franciosini-chavane-ruffier-perrinet-20/)]" controls="yes" width="90%" >}}

{{< speaker_note >}}
- result= interpretable features
{{< /speaker_note >}}


---

## SNN in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/HDSNN_conv.png" title="The HD-SNN neural network." width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

- For instance, we show how precise spike times may be used to detect the direction of motion from such a stream of events in an ultrafast fashion.
{{< /speaker_note >}}


---

## SNN in neuromorphic engineering

{{< video src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/FastMotionDetection_input.mp4" autoplay="yes" >}}

{{< speaker_note >}}
**2 MINUTE**

- A nice HSD neuron

For instance, we show how precise spike times may be used to detect the direction of motion from such a stream of events in an ultrafast fashion.
{{< /speaker_note >}}


---

## SNN in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/motion_kernels.png" title="The HD-SNN neural network." width="90%" >}}

{{< speaker_note >}}
**2 MINUTE**

- nice kernels

{{< /speaker_note >}}


---

## SNN in neuromorphic engineering

{{< figure src="https://laurentperrinet.github.io/publication/grimaldi-23-bc/accuracy.png" title="The HD-SNN neural network." width="60%" >}}

{{< speaker_note >}}
**2 MINUTE**

- frugal computing

{{< /speaker_note >}}


---

<section>

# [Neurosciences and sparsity](https://laurentperrinet.github.io/slides/2026-01-29-emergences/?transition=fade)
##	*[Laurent Perrinet](https://laurentperrinet.github.io/talk/2026-01-29-emergences/)*
###	<u>[*Séminaire à l'atelier "IA embarquée" du PEPR IA*](https://www.pepr-ia.fr)</u>
###	[2026-01-29]
![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)
Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

<!-- <img src="https://laurentperrinet.github.io/qrcode.png" alt="QR code" height="80" width="80"> -->

{{< speaker_note >}}
- to summarize= sparse representations help understand neuroscience biological vision
- they have practical applications in machine learning
- let's sparse!
{{< /speaker_note >}}

</section>
