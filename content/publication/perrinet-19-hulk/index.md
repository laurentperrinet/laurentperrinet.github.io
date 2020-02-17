+++
title = "An adaptive homeostatic algorithm for the unsupervised learning of visual features"
date = 2019-01-01
authors = [ "Laurent U Perrinet",]
publication_types = [ "2",]
abstract = "The formation of structure in the visual system, that is, of the connections between cells within neural populations, is by large an unsupervised learning process: the emergence of this architecture is mostly self-organized. In the primary visual cortex of mammals, for example, one can observe during development the formation of cells selective to localized, oriented features which results in the development of a representation of contours in area V1. We modeled such a process using sparse Hebbian learning algorithms. These algorithms alternate a coding step to encode the information with a learning step to find the proper encoder. We identified here a major difficulty of classical solutions in their ability to deduce a good representation while knowing immature encoders, and to learn good encoders with a non-optimal representation. To solve this problem, we propose to introduce a new regulation process between learning and coding, called homeostasis. It is compatible with a neuromimetic architecture and allows for a more efficient emergence of localized filters sensitive to orientation. The key to this algorithm lies in a simple adaptation mechanism based on non-linear functions that reconciles the antagonistic processes that occur at the coding and learning time scales. We tested this unsupervised algorithm with this homeostasis rule for a series of learning algorithms coupled with different neural coding algorithms. In addition, we propose a simplification of this optimal homeostasis rule by implementing a simple heuristic on the probability of activation of neurons. Compared to the optimal homeostasis rule, we show that this heuristic allows to implement a faster unsupervised learning algorithm while retaining much of its effectiveness. These results demonstrate the potential application of such a strategy in computer vision and machine learning and we illustrate it with a result in a convolutional neural network."
featured = false
publication = "*Vision*"
tags = [ "area-v1", "gain control", "homeostasis", "matching pursuit", "sparse coding", "sparse hebbian learning", "unsupervised learning",]
projects = []
url_pdf = "https://spikeai.github.io/HULK/"
doi = "10.3390/vision3030047"
publishDate = "2019-09-17"
grants = [ "anr-horizontal-v1", "spikeai; mesocentre",]
url_code = "https://github.com/SpikeAI/HULK"
url_preprint = "https://laurentperrinet.github.io/publication/perrinet-19-hulk/"
+++

# "An adaptive algorithm for unsupervised learning"
<BR>
<center><a href="https://laurentperrinet.github.io/publication/perrinet-19"><video controls autoplay loop src="https://laurentperrinet.github.io/sciblog/files/2019-09-11_Perrinet19.mp4" width=61.8%/></a> </center>
<BR>
* supplementary info : https://spikeai.github.io/HULK/
* [Abstract](https://www.mdpi.com/2411-5150/3/3/47)
* [HTML](https://www.mdpi.com/2411-5150/3/3/47/htm)
* [PDF](https://www.mdpi.com/2411-5150/3/3/47/pdf)
* code for paper: https://github.com/SpikeAI/HULK
* code for framework: https://github.com/bicv/SparseHebbianLearning/
* code for figures https://github.com/SpikeAI/HULK/blob/master/Annex.ipynb (which is rendered @ https://spikeai.github.io/HULK/ )
* [video abstract](https://laurentperrinet.github.io/sciblog/files/2019-09-11_Perrinet19.mp4) (and the [code](https://laurentperrinet.github.io/sciblog/posts/2019-09-11_video-abstract-vision.html) for generating it)

<!-- 
{{< figure src="flash_lag.gif" title="*Flash-Lag Effect.* When a visual stimulus moves along a continuous trajectory, it may be seen ahead of its veridical position with respect to an unpredictable event such as a punctuate flash. This illusion tells us something important about the visual system: contrary to classical computers, neural activity travels at a relatively slow speed. It is largely accepted that the resulting delays cause this perceived spatial lag of the flash. Still, after several decades of debates, there is no consensus regarding the underlying mechanisms." >}} -->
