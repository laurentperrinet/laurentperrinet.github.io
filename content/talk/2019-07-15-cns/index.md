---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Learning where to look: a foveated visuomotor control model'
subtitle: ''
summary: ''
authors:
- Emmanuel Daucé
- Pierre Albigès
- Laurent U Perrinet
tags:
- '"Active Inference"'
- '"Deep Learning"'
- '"Object localization"'
- '"Visual search"'
- '"Visuomotor control"'
categories: []
date: '2019-01-01'
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
publishDate: '2021-10-12T10:44:44.229609Z'
publication_types:
- '1'
abstract: In computer vision, the visual search task consists in extracting a scarce
  and specific visual information (the target) from a large and crowded visual display.
  This task is usually implemented by scanning the different possible target identities
  at all possible spatial positions, hence with strong computational load. The human
  visual system employs a different strategy, combining a foveated sensor with the
  capacity to rapidly move the center of fixation using saccades. Saccade-based visual
  exploration can be idealized as an inference process, assuming that the target position
  and category are independently drawn from a common generative process. Knowing that
  process, visual processing is then separated in two specialized pathways, the where
  pathway mainly conveying information about target position in peripheral space,
  and the what pathway mainly conveying information about the category of the target.
  We consider here a dual neural network architecture learning independently where
  to look and then at what to see. This allows in particular to infer target position
  in retinotopic coordinates, independently to its category. This framework was tested
  on a simple task of finding digits in a large, cluttered image. Simulation results
  demonstrate the benefit of specifically learning where to look before actually knowing
  the target category. The approach is also energy-efficient as it includes the strong
  compression rate performed at the sensor level, by retina and V1 encoding, which
  is preserved up to the action selection level, highlighting the advantages of bio-mimetic
  strategies with regards to traditional computer vision when computing resources
  are at stake.
publication: '*CNS*2019 Barcelona, Spain*'
url_pdf: https://bmcneurosci.biomedcentral.com/articles/10.1186/s12868-019-0538-0#Sec73
---
