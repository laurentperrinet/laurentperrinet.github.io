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


{{< /speaker_note >}}

</section>

---

<section>

## Sparse representations?

<!-- {{< figure src="https://www.vhv.rs/dpng/d/57-574294_old-man-shrugging-shoulders-meme-hd-png-download.png" width="90%" >}} -->
{{< figure src="https://i.imgflip.com/2lmff7.jpg" width="80%" >}}

{{< speaker_note >}}

you may have heard of it but do you know what it is ?


{{< /speaker_note >}}

---

## Sparse representations in computer vision

{{< video src="https://laurentperrinet.github.io/sciblog/files/2015-05-22-a-hitchhiker-guide-to-matching-pursuit/MPtutorial_rec.mp4" controls="yes" height="90%" >}}

Code @ [A hitchhiker guide to Matching Pursuit](https://laurentperrinet.github.io/sciblog/posts/2015-05-22-a-hitchhiker-guide-to-matching-pursuit.html)

{{< speaker_note >}}

the whole is the sum of a few parts

Sparse coding is a technique used in signal processing and machine learning to represent data in a more concise and efficient manner. It aims to find a sparse representation of the data, which means representing the data with only a small number of non-zero coefficients or activations. In sparse coding, a set of basis functions or atoms is typically defined, and the goal is to find a linear combination of these atoms that best represents the input data. The coefficients of this linear combination are often constrained to be sparse, meaning that only a few of them are allowed to be non-zero. 

{{< /speaker_note >}}

---

## Sparse representations in neuroscience

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/Brunel200Fig2.png" title="[[Brunel, 2001](https://books.google.fr/books?hl=fr&lr=&id=b8woDqWdTssC&oi=fnd&pg=PA307&ots=KNHQrJ-TsZ&sig=0WI2cq2RnMXC7fVTyjOEWZEdlCg&redir_esc=y#v=onepage&q&f=false)]" width="50%" >}}

{{< speaker_note >}}
Phase diagrams of sparsely connected networks of excitatory and inhibitory spiking neurons


healthy network = 1Hz = sparse activity (stronger in auditory, in insects, ...)

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


---

## Sparse representations in neuroscience

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/fncir-10-00037-g001.jpg" title="[[Kremkow *et al*, 2016](https://laurentperrinet.github.io/publication/kremkow-16/)]" width="90%" >}}

{{< speaker_note >}}
mainen et sejnowski
diesmann
vinje et gallant
{{< /speaker_note >}}

---

## Sparse representations?

<!-- {{< figure src="https://www.vhv.rs/dpng/d/57-574294_old-man-shrugging-shoulders-meme-hd-png-download.png" width="90%" >}} -->
{{< figure src="https://memecreator.org/static/images/memes/5646953.jpg" width="45%" >}}

{{< speaker_note >}}
in summary: Sparse representations resulting from these processes have been successfully applied in various domains such as image processing, computer vision, and audio signal processing. It has shown promise in tasks such as noise reduction, compression, feature extraction, and pattern recognition. By capturing the essential structure and characteristics of the data in a sparse representation, sparse coding can help reduce redundancy and noise, and extract meaningful features for further analysis or processing.
{{< /speaker_note >}}


</section>

---

<section>

## Sparse representations in a nutshell


{{< figure src="https://i.giphy.com/26xBtPbmDlugFxUiY.webp" width="90%" >}}

{{< speaker_note >}}
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

{{< figure src="https://laurentperrinet.github.io/publication/rentzeperis-23/featured.png" title="[[Rentzeperis *et al* (2023)](https://laurentperrinet.github.io/publication/rentzeperis-23/)]" height="80%" >}}

{{< speaker_note >}}


{{< /speaker_note >}}


---

## Sparse representations in a nutshell

{{< figure src="https://laurentperrinet.github.io/2019-04-03_a_course_on_vision_and_modelization/figures/Olshausen_5.png" title="[[Olshausen and Field (1997)](http://mplab.ucsd.edu/~marni/Igert/Olshaussen_1997.pdf)]" height="80%" >}}

{{< speaker_note >}}

Neural implementation = gradient descent

LASSO = least absolute shrinkage and selection operator

Orthogonal Matching Pursuit (OMP): OMP is an iterative algorithm used for sparse signal recovery. It starts with an initial sparse solution and iteratively selects the most correlated dictionary atoms with the residual signal. OMP aims to minimize the L2 norm of the residual while maintaining sparsity. It has a greedy nature and can provide a near-optimal sparse solution.

Basis Pursuit (BP): Basis Pursuit is an optimization problem that seeks the sparsest solution to an underdetermined linear system of equations. It involves minimizing the L1 norm of the coefficient vector subject to a linear constraint. BP can be solved using linear programming techniques or convex optimization algorithms.

Iterative Soft Thresholding Algorithm (ISTA): ISTA is an iterative optimization algorithm commonly used in sparse coding. It alternates between a gradient descent step and a soft thresholding step. The gradient descent step minimizes the data fidelity term, and the soft thresholding step enforces sparsity by setting small coefficients to zero. ISTA converges to a sparse solution and can be used for dictionary learning.

FISTA (Fast Iterative Shrinkage-Thresholding Algorithm): FISTA is an accelerated version of ISTA that improves convergence speed. It incorporates momentum into the optimization process and achieves faster convergence rates.

ADMM (Alternating Direction Method of Multipliers): ADMM is an optimization technique that decomposes the original problem into smaller subproblems and solves them iteratively. It is often used for convex optimization problems with L1 regularization. ADMM has been applied to solve sparse coding problems efficiently.

{{< /speaker_note >}}


</section>


---

<section>


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
