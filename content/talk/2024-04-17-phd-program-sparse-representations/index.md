---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Sparse representations
subtitle: ''
summary: ''
authors:
- Laurent U Perrinet
tags: []
categories: []
date: '2024-04-17'
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2024-04-15T07:47:11.286659Z'
publication_types:
- 'inproceedings'
abstract: "Sparse coding is a technique used in signal processing and machine learning to represent data in a more concise and efficient manner. It aims to find a sparse representation of the data, which means representing the data with only a small number of non-zero coefficients or activations. In sparse coding, a set of basis functions or atoms is typically defined, and the goal is to find a linear combination of these atoms that best represents the input data. The coefficients of this linear combination are often constrained to be sparse, meaning that only a few of them are allowed to be non-zero. Sparse representations resulting from these processes have been successfully applied in various domains such as image processing, computer vision, and audio signal processing. It has shown promise in tasks such as noise reduction, compression, feature extraction, and pattern recognition. By capturing the essential structure and characteristics of the data in a sparse representation, sparse coding can help reduce redundancy and noise, and extract meaningful features for further analysis or processing."
publication: '*NeuroSchool PhD Program in Neuroscience*'

slides: 2024-04-17-phd-program-sparse-representations

links:
- name: code
  url: https://github.com/laurentperrinet/2024-04_sparse-representations
- name: link
  url: https://laurentperrinet.github.io/talk/2024-04-17-phd-program-sparse-representations
---

the timeline of the whole course:

April 15th (morning+afternoon): basics on machine learning, practice with notebook using scikit learn (MG)
April 16th (morning+afternoon): deep learning and automated differenciation, practice with notebook using pytorch (MG)
April 17th morning: interpretable machine learning (ET)
April 17th afternoon: sparse representations (LP)

If not done already, please install a (reasonably) recent version of python (easy option is anaconda, see details here: https://etulab.univ-amu.fr/gilson.m/compneuro_course). Importantly, part of the course will rely on pytorch, see instructions for installing a dedicated environment here: https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/autodiff (we can do together it the first morning for those who have trouble).

The first day (or morning depending on how we go), we will first review basics in supervised learning, to be on the same page (with a focus on recursive feature elimination): https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/sup_lrn
If some of you are interested in machine learning for time series, we can have a session on this (we'll decide together on Monday morning)
Following, we will focus on autodifferenciation, first from scratch and then using pytorch, see https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/autodiff (in progress of being updated)
And a few datasets are available there: https://etulab.univ-amu.fr/gilson.m/compneuro_course/-/tree/main/data ; in particular we will use the MNIST dataset as a benchmark for classification, etc.
