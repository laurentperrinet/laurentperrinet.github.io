---
title: A New Look for Convolutional Deep Networks
authors:
- Laurent U Perrinet
date: 2026-11-03 10:30:00
publishDate: '2026-10-28T09:25:23.000000Z'
publication_types:
- paper-conference
publication: '*Seminar at Université Grenoble Alpes*'
abstract: 'By construction, deep convolutional networks treat all pixels equally.
  Result: they are energy-hungry, fragile to rotations or zooms, and poor at object
  localization. This contrasts sharply with biological vision, which demonstrates
  remarkable efficiency. Think of an eagle spotting prey from kilometers away or a
  human recognizing a face within an eye blink time. We propose that by using a mechanism
  concentrating processing at the center of gaze, biological vision is optimally suited
  for object localization. To test this hypothesis, we embed foveated retinotopy into
  CNN inputs. We observe that while standard ResNets drop from 80% accuracy to 46%
  under rotation attacks, our retrained networks achieve comparable accuracy (76%)
  while dropping only to 66%. Critically, without additional learning, this foveated
  CNN reveals high sensitivity to fixation point location: the maximum likelihood
  position points to ground truth bounding boxes with 85% accuracy, compared to 71%
  for classical CNNs. This suggests that this specific Nature''s million-year solution
  may offer deep learning visual networks a fundamentally new architectural look.'
categories:
- Behavioural Neuroscience
- Biological Neuroscience
- Computer Vision
- NeuroAI & Machine Learning
- Visual Neuroscience
links:
- name: Slides
  url: https://laurentperrinet.github.io/2025-12-13_Perrinet-talk-MAIN2025
tags:
- computer-vision
- deep-learning
- eye-movements
- foveated-vision
- log-polar-mapping
- primary-visual-cortex
- retinotopy
event: Seminar at Université Grenoble Alpes
---

* Invited seminar at Université Grenoble Alpes, 2026-11-03, 10:30

* Room A6, Bâtiment Michel Dubois (or MSH amphitheatre), Saint-Martin-d'Hères, Grenoble, France

* Same topic as the talk given at the [MAIN 2025 conference](/talk/2025-12-12-main/) (see also the [slides](https://laurentperrinet.github.io/2025-12-13_Perrinet-talk-MAIN2025))

* Paper: {{< cite page="publication/jeremie-25" view="4" >}}

{{< figure src="/talk/2025-12-12-main/where_5.jpg" width="95%" >}}
