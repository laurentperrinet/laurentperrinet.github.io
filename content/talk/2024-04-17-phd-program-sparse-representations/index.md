---
abstract: Sparse coding is a technique used in signal processing and machine learning
  to represent data in a more concise and efficient manner. It aims to find a sparse
  representation of the data, which means representing the data with only a small
  number of non-zero coefficients or activations. In sparse coding, a set of basis
  functions or atoms is typically defined, and the goal is to find a linear combination
  of these atoms that best represents the input data. The coefficients of this linear
  combination are often constrained to be sparse, meaning that only a few of them
  are allowed to be non-zero. Sparse representations resulting from these processes
  have been successfully applied in various domains such as image processing, computer
  vision, and audio signal processing. It has shown promise in tasks such as noise
  reduction, compression, feature extraction, and pattern recognition. By capturing
  the essential structure and characteristics of the data in a sparse representation,
  sparse coding can help reduce redundancy and noise, and extract meaningful features
  for further analysis or processing.
authors:
- Laurent U Perrinet
categories: []
date: 2024-04-17 14:00:00
draft: false
event: NeuroSchool PhD Program in Neuroscience
featured: false
image:
  caption: ''
  focal_point: Center
  preview_only: false
links:
- name: Code
  url: https://github.com/laurentperrinet/2024-04_sparse-representations
- name: URL
  url: https://laurentperrinet.github.io/talk/2024-04-17-phd-program-sparse-representations
location: Marseille (France)
projects:
- courses
publication: '*NeuroSchool PhD Program in Neuroscience*'
publication_types:
- inproceedings
publishDate: '2024-04-15T07:47:11.286659Z'
slides: 2024-04-17-phd-program-sparse-representations
subtitle: ''
tags: []
title: Sparse representations
---

Timeline of the whole course:

* April 15th (morning+afternoon): basics on machine learning, practice with notebook using scikit learn (MG)
* April 16th (morning+afternoon): deep learning and automated differenciation, practice with notebook using pytorch (MG)
* April 17th morning: interpretable machine learning (ET)
* April 17th afternoon: sparse representations (LP)


If not done already, please install a (reasonably) recent version of python (easy option is anaconda, see details here: https://etulab.univ-amu.fr/gilson.m/compneuro_course). Importantly, part of the course will rely on pytorch, see instructions for installing a dedicated environment here: https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/autodiff (we can do together it the first morning for those who have trouble).
The first day (or morning depending on how we go), we will first review basics in supervised learning, to be on the same page (with a focus on recursive feature elimination): https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/sup_lrn

If some of you are interested in machine learning for time series, we can have a session on this (we'll decide together on Monday morning)

Following, we will focus on autodifferenciation, first from scratch and then using pytorch, see https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/autodiff (in progress of being updated)

And a few datasets are available there: https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/data ; in particular we will use the MNIST dataset as a benchmark for classification, etc.
