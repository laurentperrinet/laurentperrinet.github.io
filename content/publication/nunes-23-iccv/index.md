---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Time-to-Contact Map by Joint Estimation of Up-to-Scale Inverse Depth and Global
  Motion using a Single Event Camera
subtitle: ''
summary: ''
authors:
- Urbano Miguel Nunes
- Laurent U Perrinet
- Sio-Hoi Ieng
tags:
- time-to-contact
- event-based vision
- neuromorphic hardware
categories: []
date: '2023-10-06'
lastmod: 2023-09-05T10:59:11+02:00
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
publishDate: '2023-09-05T08:59:11.517138Z'
publication_types:
- '1'
abstract: Event cameras asynchronously report brightness changes with a temporal resolution
  in the order of microseconds, which makes them inherently suitable to address problems
  that involve rapid motion perception, such as ventral landing and fast obstacle
  avoidance. These problems are typically addressed by estimating a single global
  time-to-contact (TTC) measure, which explicitly assumes that the surface/obstacle
  is planar and fronto-parallel. We relax this assumption by proposing an incremental
  event-based method to estimate the TTC that jointly estimates the (up-to scale)
  inverse depth and global motion using a single event camera. The proposed method
  is reliable and fast while asynchronously maintaining a TTC map (TTCM), which provides
  per-pixel TTC estimates. As a side product, the proposed method can also estimate
  per-event optical flow. We achieve state-of-the-art performances on TTC estimation
  in terms of accuracy and runtime per event while achieving competitive performance
  on optical flow estimation.
publication: '*International Conference on Computer Vision 2023 (ICCV2023)*'
links:
- name: URL
  url: https://www.techrxiv.org/articles/preprint/A_robust_event-driven_approach_to_always-on_object_recognition/18003077
---
