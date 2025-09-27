---
date: 2016-04-27 00:00:00
image:
  caption: Snapshot of a Motion Cloud
  focal_point: Smart
summary: 'To enable the dissemination of the knowledge that is produced in our lab, we share all source code with open source licences.'
tags:
- research-interests
- log-gabor
- psychophysics
- motion-clouds
title: Open Science
---
To enable the dissemination of the knowledge that is produced in our lab, we share all source code with open source licences. This includes code to reproduce results obtained in papers (e.g. [(Perrinet, Adams and Friston, 2015)](https://github.com/laurentperrinet/PerrinetAdamsFriston14), [(Perrinet and Bednar, 2015)](https://github.com/laurentperrinet/PerrinetBednar15), [(Khoei et, 2017)](https://github.com/laurentperrinet/Khoei_2017_PLoSCB), [(Perrinet, 2019)](https://github.com/laurentperrinet/2019-05_illusions-visuelles), [(Pasturel et al, 2020)]({{< ref "/publication/pasturel-montagnini-perrinet-20/index.md" >}}), [(Dauce et al, 2020)]({{< ref "/publication/dauce-20/index.md" >}})) or courses and slides (e.g. [2019-04-03: vision and modelization](https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization), [2019-04-18_JNLF](https://github.com/laurentperrinet/2019-04-18_JNLF), ...) and also the development of the following libraries on [GitHub](https://github.com/laurentperrinet).


<!-- Place this tag where you want the button to render. -->
<a class="github-button" href="https://github.com/laurentperrinet" data-size="large" data-show-count="true" aria-label="Follow @laurentperrinet on GitHub">Follow @laurentperrinet</a>
<!-- Place this tag in your head or just before your close body tag. -->
<script async defer src="https://buttons.github.io/buttons.js"></script>

# HD natural images database for sparse coding

A dataset of natural images, acquired with a Canon EOS6D and Canon EOS650. It has been curated to facilitate research, namely in sparse coding at the moment, but can be used for future endeavors. Maintainer: [Hugo Ladret](https://laurentperrinet.github.io/author/hugo-ladret/).

* [get the dataset](https://figshare.com/articles/media/HD_natural_images_database_for_sparse_coding/24167265)
* See the preprint publication @ {{< cite page="/publication/ladret-23-iclr" view="card" >}}

# Bayesian Change Point

A python implementation of [Adams &amp; MacKay 2007 "Bayesian Online Changepoint Detection"](http://arxiv.org/abs/0710.3742) for binary inputs in {{< icon name="python" pack="fab" >}} Python.

* [Source code](https://github.com/laurentperrinet/bayesianchangepoint)
* See the final publication @ {{< cite page="/publication/pasturel-montagnini-perrinet-20" view="card" >}}

# ANEMO: Quantitative tools for the ANalysis of Eye MOvements

This implementation proposes a set of robust fitting methods for the extraction of eye movements  parameters.

* [Source code](https://github.com/invibe/ANEMO/)
* See a poster @ [Pasturel, Montagnini and Perrinet (2018)]({{< ref "/publication/pasturel-18-anemo/index.md" >}})
* This library was used in the following publication @ {{< cite page="/publication/pasturel-montagnini-perrinet-20" view="card" >}}

# LeCheapEyeTracker

Work-in-progress : an eye tracker based on webcams.

* [Source code](https://github.com/laurentperrinet/LeCheapEyeTracker)

# Biologically inspired computer vision ({{< icon name="python" pack="fab" >}} Python)

## SLIP: a Simple Library for Image Processing

This library collects different Image Processing tools for use with the [LogGabor](https://pythonhosted.org/LogGabor/) and [SparseEdges](https://pythonhosted.org/SparseEdges/) libraries.

* [Web-site](https://pythonhosted.org/SLIP/)
* [Source code](https://github.com/bicv/SLIP/)
* [![Research software impact](http://depsy.org/api/package/pypi/SLIP/badge.svg)](http://depsy.org/package/python/SLIP)

## LogGabor: a Simple Library for Image Processing

This library defines the set of [LogGabor](https://pythonhosted.org/LogGabor/) kernels. These are generic edge-like filters at different scales, phases and orientations. The library develops a simple method to construct a simple multi-scale linear transform.

* [Web-site](https://pythonhosted.org/LogGabor)
* [Source code](https://github.com/bicv/LogGabor/)
* This library is detailed in the following publication {{< cite page="/publication/fischer-07-cv" view="card" >}}
* LogGabor filters are used in numerous computer vision applications and reaches 177 citations on [Google Scholar](https://scholar.google.com/scholar?cluster=15692697050569088559&hl=fr&as_sdt=7,39) (last updated 22/10/2021).
* [![Research software impact](http://depsy.org/api/package/pypi/LogGabor/badge.svg)](http://depsy.org/package/python/LogGabor)


## SparseEdges: sparse coding of natural images

Our goal here is to build practical algorithms of sparse coding for computer vision.

This class exploits the [SLIP](https://pythonhosted.org/SLIP/) and [LogGabor](https://pythonhosted.org/LogGabor/) libraries to provide with a sparse representation of edges in images.


* [Web-site](https://pythonhosted.org/SparseEdges)
* [Source code](https://github.com/bicv/SparseEdges/)
* This algorithm was presented in the following paper, which is available as a reprint {{< cite page="/publication/perrinet-15-bicv" view="card" >}}
* It was notably used in the following paper {{< cite page="/publication/perrinet-bednar-15" view="card" >}}
* [![Research software impact](http://depsy.org/api/package/pypi/SparseEdges/badge.svg)](http://depsy.org/package/python/SparseEdges)

##  Sparse Hebbian Learning : unsupervised learning of natural images

This is a collection of python scripts to test learning strategies to efficiently code natural image patches. This is here restricted to the framework of the SparseNet algorithm from Bruno Olshausen (http://redwood.berkeley.edu/bruno/sparsenet/).

* [Source code](https://github.com/bicv/SparseHebbianLearning/)
* This algorithm was presented in the following paper {{< cite page="/publication/perrinet-10-shl" view="card" >}}
* 54 citations on [Google Scholar](https://scholar.google.com/scholar?cluster=3780829296605136744&hl=fr&as_sdt=7,39) (last updated 22/10/2021)
* Follow-up paper {{< cite page="/publication/perrinet-19-hulk" view="card" >}}

# MotionClouds

**MotionClouds** are random dynamic stimuli optimized to study motion perception.

* [Web-site](https://neuralensemble.github.io/MotionClouds/)
* [Source code](https://github.com/NeuralEnsemble/MotionClouds) using {{< icon name="python" pack="fab" >}} Python.
* This algorithm was presented in the following paper {{< cite page="/publication/sanz-12" view="card" >}}
* 3746 citations on [Google Scholar](https://scholar.google.com/scholar?cluster=3286688289699014452&hl=fr&as_sdt=7,39) (last updated 04/09/2025)
* examples of use: https://laurentperrinet.github.io/sciblog/categories/motionclouds.html
* Follow-up paper {{< cite page="/publication/vacher-16" view="card" >}} {{< cite page="/publication/vacher-16" view="card" >}}
* This library was notably used in the following papers: {{< cite page="/publication/simoncini-12" view="card" >}}  {{< cite page="/publication/ravello-19" view="card" >}}  {{< cite page="/publication/ladret-23" view="card" >}}
[![Research software impact](http://depsy.org/api/package/pypi/MotionClouds/badge.svg)](http://depsy.org/package/python/MotionClouds)

# PyNN

**PyNN** is a simulator-independent language for building neuronal network models using {{< icon name="python" pack="fab" >}} Python.

* [Web-site](https://neuralensemble.github.io/PyNN/)
* [Source code](https://github.com/NeuralEnsemble/PyNN)
* This algorithm was presented in the following paper {{< cite page="/publication/davison-08" view="card" >}}
* 619 citations on [Google Scholar](https://scholar.google.com/scholar?cluster=4324955271726120014&hl=fr&as_sdt=7,39) (last updated 22/10/2021)
