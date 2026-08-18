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
date: 2023-10-06
doi: 10.1109/ICCV51070.2023.02162
draft: false
featured: false
grants:
- anr-anr
image:
  focal_point: Smart
  preview_only: false
lastmod: 2023-09-05 10:59:11+02:00
links:
- name: Venue
  url: https://openaccess.thecvf.com/content/ICCV2023/html/Nunes_Time-to-Contact_Map_by_Joint_Estimation_of_Up-to-Scale_Inverse_Depth_and_ICCV_2023_paper.html
- name: Pdf
  url: https://openaccess.thecvf.com/content/ICCV2023/supplemental/Nunes_Time-to-Contact_Map_by_ICCV_2023_supplemental.pdf
- name: Code
  url: https://github.com/neuromorphic-paris/ETTCM
- name: URL
  url: https://laurentperrinet.github.io/publication/nunes-23-iccv/
publication: '*International Conference on Computer Vision 2023 (ICCV2023)*'
publication_types:
- inproceedings
publishDate: '2023-09-05T08:59:11.517138Z'
title: Time-to-Contact Map by Joint Estimation of Up-to-Scale Inverse Depth and Global
  Motion using a Single Event Camera
tags:
- motion-perception
- neuromorphic-computing
- visual-illusions
categories:
- Computer Vision
- Education
- NeuroAI & Machine Learning
---

* the code is openly available on [GitHub](https://github.com/neuromorphic-paris/ETTCM) with the accompanying data [VL.zip](https://www.dropbox.com/scl/fi/lw9ztsopinnjfztt82oxt/VL.zip?rlkey=6uccvu486iulvityrvrom50e4&dl=0).
