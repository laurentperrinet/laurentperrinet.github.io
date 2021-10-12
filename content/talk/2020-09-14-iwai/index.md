---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Visual search as active inference
subtitle: ''
summary: ''
authors:
- Emmanuel Daucé
- Laurent Perrinet
tags: []
categories: []
date: '2020-09-14'
lastmod: 2021-10-12T12:44:44+02:00
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
publishDate: '2021-10-12T10:44:44.695492Z'
publication_types:
- '1'
abstract: Visual search is an essential cognitive ability, offering a prototypical
  control problem to be addressed with Active Inference. Under a Naive Bayes assumption,
  the maximization of the information gain objective is consistent with the separation
  of the visual sensory flow in two independent pathways, namely the \"What\" and
  the \"Where\" pathways. On the \"What\" side, the processing of the central part
  of the visual field (the fovea) provides the current interpretation of the scene,
  here the category of the target. On the \"Where\" side, the processing of the full
  visual field (at lower resolution) is expected to provide hints about future central
  foveal processing given the potential realization of saccadic movements. A map of
  the classification accuracies, as obtained by such counterfactual saccades, defines
  a utility function on the motor space, whose maximal argument prescribes the next
  saccade. The comparison of the foveal and the peripheral predictions finally forms
  an estimate of the future information gain, providing a simple and resource-efficient
  way to implement information gain seeking policies in active vision. This dual-pathway
  information processing framework is found efficient on a synthetic visual search
  task and we show here quantitatively the role of the precision encoded within the
  accuracy map. More importantly, it is expected to draw connections toward a more
  general actor-critic principle in action selection, with the accuracy of the central
  processing taking the role of a value (or intrinsic reward) of the previous saccade.
publication: '*IWAI 2020*'
url_pdf: https://whova.com/embedded/subsession/ecmlp_202009/1215095/1215123/
doi: 10.1007/978-3-030-64919-7_17
---
