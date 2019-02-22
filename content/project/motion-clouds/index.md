+++
# Project title.
title = "Motion Clouds"

# Date this page was created.
date = 2016-04-27T00:00:00

# Project summary to display on homepage.
summary = "**MotionClouds** are random dynamic stimuli optimized to study motion perception."

# Tags: can be used for filtering projects.
# Example: `tags = ["machine-learning", "deep-learning"]`
tags = ["psychophysics", "motion-clouds"]

# Optional external URL for project (replaces project detail page).
external_link = "http://motionclouds.invibe.net/"

# Featured image
# To use, add an image named `featured.jpg/png` to your project's folder.
[image]
  # Caption (optional)
  caption = "Snapshot of a Motion Cloud"

  # Focal point (optional)
  # Options: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight
  focal_point = "Smart"
+++

Motion Clouds are random, textured dynamical stimuli synthesized such as to challenge spatio-temporal integration properties of the early visual system. Unlike classical low-entropy stimuli such as gratings, these stimuli are less susceptible to create interference patterns when mixed together. This is essential to study integrative and discriminative properties of the low-level sensory systems. Moreover, this pseudo-random stimulation protocol allows to make a trial-by-trial analysis locked to the stimulation onset. This allows to study experimentally trial-by-trial variability and relative importance between measurement noise and contextual uncertainty.

This is a first step before extending synthesis to probabilistic synthesis models of the texture's geometric structure. The model will use geometrical multi-scale transformations extending the classical wavelet representation. For instance, these transformations synthesize the stimuli as randomized superposition of geometrical wavelets that match the spatio-temporal profile of association fields in V1. These will be implemented by computing evolutions of partial differential equations with randomized initial conditions. Finally, models are designed such that we explicitly tune the statistics of the generative model and thus control the structural complexity of the stimuli, such as different scales of smoothness in the spatio-temporal dynamics as displayed by natural scenes.

* [Web-site](http://www.motionclouds.invibe.net)
* [Source code](https://github.com/NeuralEnsemble/MotionClouds)
