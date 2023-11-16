---
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
authors:
- Urbano Miguel Nunes
- Laurent U Perrinet
- Sio-Hoi Ieng
categories: []
date: 2023-10-06
draft: false
featured: false
grants:
- anr-anr
image:
  caption: ''
  focal_point: ''
  preview_only: false
lastmod: 2023-09-05 10:59:11+02:00
projects: []
publication: '*International Conference on Computer Vision 2023 (ICCV2023)*'
publication_types:
- '1'
publishDate: '2023-09-05T08:59:11.517138Z'
subtitle: ''
tags:
- event-based vision
- neuromorphic hardware
- time-to-contact
title: Time-to-Contact Map by Joint Estimation of Up-to-Scale Inverse Depth and Global
  Motion using a Single Event Camera
links:
- name: PDF
  url: https://openaccess.thecvf.com/content/ICCV2023/supplemental/Nunes_Time-to-Contact_Map_by_ICCV_2023_supplemental.pdf

- name: HAL
  url: https://hal.science/hal-04230502

- name: ICCV
  url: https://openaccess.thecvf.com/content/ICCV2023/html/Nunes_Time-to-Contact_Map_by_Joint_Estimation_of_Up-to-Scale_Inverse_Depth_and_ICCV_2023_paper.html  

- name: code
  url:  https://github.com/neuromorphic-paris/ETTCM
---


