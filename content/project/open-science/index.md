+++
# Project title.
title = "Open Science"

# Date this page was created.
date = 2016-04-27T00:00:00

# Project summary to display on homepage.
summary = ""

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["log-gabor", "psychophysics", "motion-clouds"]

# Optional external URL for project (replaces project detail page).

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder.
[image]
  # Caption (optional)
  caption = "Snapshot of a Motion Cloud"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Smart"
+++
To enable the dissemination of the knowledge that is produced in our lab, we share all source code with open source licences. This includes code to reproduce results obtained in papers (e.g. [(Perrinet, Adams and Friston, 2015)](https://github.com/laurentperrinet/PerrinetAdamsFriston14), [(Perrinet and Bednar, 2015)](https://github.com/laurentperrinet/PerrinetBednar15), [(Khoei et, 2017)](https://github.com/laurentperrinet/Khoei_2017_PLoSCB), [(Perrinet, 2019)](https://github.com/laurentperrinet/2019-05_illusions-visuelles) or courses and slides (e.g. [2019-04-03_a_course_on_vision_and_modelization](https://github.com/laurentperrinet/2019-04-03_a_course_on_vision_and_modelization), [2019-04-18_JNLF](https://github.com/laurentperrinet/2019-04-18_JNLF), ...).


# bayesianchangepoint

An implementation of [Adams &amp; MacKay 2007 "Bayesian Online Changepoint Detection"](http://arxiv.org/abs/0710.3742) in Python.

* [Source code](https://github.com/laurentperrinet/bayesianchangepoint)

# LeCheapEyeTracker

Work-in-progress : an eye tracker based on webcams.

* [Source code](https://github.com/laurentperrinet/LeCheapEyeTracker)

# Biologically inspired computer vision

## SLIP: a Simple Library for Image Processing

This library collects different Image Processing tools for use with the  [LogGabor](https://pythonhosted.org/LogGabor/) and  [SparseEdges](https://pythonhosted.org/SparseEdges/) libraries.

* [Web-site](https://pythonhosted.org/SLIP/)
* [Source code](https://github.com/bicv/SLIP/)

## LogGabor: a Simple Library for Image Processing

This library collects different Image Processing tools for use with the  [LogGabor](https://pythonhosted.org/LogGabor/) and  [SparseEdges](https://pythonhosted.org/SparseEdges/) libraries.

* [Web-site]((https://pythonhosted.org/LogGabor)
* [Source code](https://github.com/bicv/LogGabor/)

## SparseEdges: sparse coding of natural images

Our goal here is to build practical algorithms of sparse coding for computer vision.

This class exploits the [SLIP](https://pythonhosted.org/SLIP/) and [LogGabor](https://pythonhosted.org/LogGabor/) libraries to provide with a sparse representation of edges in images.

This algorithm was presented in the following paper, which is available as a reprint @ https://laurentperrinet.github.io/publication/perrinet-15-bicv/

* [Web-site](https://pythonhosted.org/SparseEdges)
* [Source code](https://github.com/bicv/SparseEdges/)

##  SparseHebbianLearning : unsupervised learning of natural images

This is a collection of python scripts to test learning strategies to efficiently code natural image patches. This is here restricted to the framework of the SparseNet algorithm from Bruno Olshausen (http://redwood.berkeley.edu/bruno/sparsenet/).

* [Source code](https://github.com/bicv/SparseHebbianLearning/)


# MotionClouds

**MotionClouds** are random dynamic stimuli optimized to study motion perception.

Motion Clouds are random, textured dynamical stimuli synthesized such as to challenge spatio-temporal integration properties of the early visual system. Unlike classical low-entropy stimuli such as gratings, these stimuli are less susceptible to create interference patterns when mixed together. This is essential to study integrative and discriminative properties of the low-level sensory systems. Moreover, this pseudo-random stimulation protocol allows to make a trial-by-trial analysis locked to the stimulation onset. This allows to study experimentally trial-by-trial variability and relative importance between measurement noise and contextual uncertainty.

This is a first step before extending synthesis to probabilistic synthesis models of the texture's geometric structure. The model will use geometrical multi-scale transformations extending the classical wavelet representation. For instance, these transformations synthesize the stimuli as randomized superposition of geometrical wavelets that match the spatio-temporal profile of association fields in V1. These will be implemented by computing evolutions of partial differential equations with randomized initial conditions. Finally, models are designed such that we explicitly tune the statistics of the generative model and thus control the structural complexity of the stimuli, such as different scales of smoothness in the spatio-temporal dynamics as displayed by natural scenes.

* [Web-site](http://www.motionclouds.invibe.net)
* [Source code](https://github.com/NeuralEnsemble/MotionClouds)
