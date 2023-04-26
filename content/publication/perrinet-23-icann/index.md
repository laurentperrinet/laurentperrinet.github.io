---
abstract: Recently, there has been growing interest in the hypothesis that information can be carried within neural activity by precise spiking motifs. As a result, there have been several recent proposals for algorithms to detect such motifs in the Spiking Unit Activity (SUA) of populations of neurons. In this study, we introduce a detection model as an inversion of a generative model of raster plot synthesis. From this model, an optimal detection procedure is derived. This takes the form of a logistic regression coupled with a temporal convolution. Since this model is differentiable, we derive a supervised learning method in the form of gradient descent on the loss function of an auto-encoder model. We evaluate the ability of this model to detect spiking motifs in synthetic data. This learning method is able to recover the synthetically generated spiking motifs, and we plan to extend this method to neurobiological data as well.
authors:
- Laurent U Perrinet
date: 2023-04-21
grants:
- polychronies
title: Accurate detection of spiking motifs in multi-unit raster plots
---

* Submitted to the [special session on Recent Advances in Spiking Neural Networks at this year's ICANN 2023 conference](https://e-nns.org/icann2023/wp-content/uploads/sites/7/2023/04/ICANN2023-ASNN-CfP.pdf). 