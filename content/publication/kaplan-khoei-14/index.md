---
abstract: As it is confronted to inherent neural delays, how does the visual system
  create a coherent representation of a rapidly changing environment? In this paper,
  we investigate the role of motion-based prediction in estimating motion trajectories
  compensating for delayed information sampling. In particular, we investigate how
  anisotropic diffusion of information may explain the development of anticipatory
  response as recorded in a neural populations to an approaching stimulus. We validate
  this using an abstract probabilistic framework and a spiking neural network (SNN)
  model. Inspired by a mechanism proposed by Nijhawan [1], we first use a Bayesian
  particle filter framework and introduce a diagonal motion-based prediction model
  which extrapolates the estimated response to a delayed stimulus in the direction
  of the trajectory. In the SNN implementation, we have used this pattern of anisotropic,
  recurrent connections between excitatory cells as mechanism for motion-extrapolation.
  Consistent with recent experimental data collected in extracellular recordings of
  macaque primary visual cortex [2], we have simulated different trajectory lengths
  and have explored how anticipatory responses may be dependent on the information
  accumulated along the trajectory. We show that both our probabilistic framework
  and the SNN model can replicate the experimental data qualitatively. Most importantly,
  we highlight requirements for the development of a trajectory-dependent anticipatory
  response, and in particular the anisotropic nature of the connectivity pattern which
  leads to the motion extrapolation mechanism.
authors:
- Bernhard A Kaplan
- Mina A Khoei
- Anders Lansner
- Laurent U Perrinet
date: 2014-01-01
doi: 10.1109/IJCNN.2014.6889847
featured: false
grants:
- brain-scales
- facets-itn
projects: []
publication: '*IEEE International Joint Conference on Neural Networks (IJCNN) 2014
  Beijing, China*'
publication_types:
- PublicationType.ConferencePaper
publishDate: '2019-09-17'
tags:
- Bayesian model
- motion detection
- motion prediction
- pynn
title: Signature of an anticipatory response in area V1 as modeled by a probabilistic
  model and a spiking neural network
url_pdf: https://laurentperrinet.github.io/publication/kaplan-khoei-14
---



* Based on {{< cite page="/publication/perrinet-12-pred" view="4" >}}
* see  follow-up on motion extrapolation: {{< cite page="/publication/khoei-13-jpp" view="4" >}}
* see  follow-up on the flash-lag effect: {{< cite page="/publication/khoei-masson-perrinet-17" view="4" >}}

{{< figure src="https://www.frontiersin.org/files/Articles/53894/fncom-07-00112-r2/image_m/fncom-07-00112-g003.jpg" title="Figure 4: *Rasterplot of input and output spikes.* The raster plot from excitatory neurons is ordered according to their position. Each input spike is a blue dot and each output spike is a black dot. While input is scattered during blanking periods (Figure 1), the network output shows shows some tuned activity during the blank (compare with the activity before visual stimulation). To decode such patterns of activity we used a maximum-likelihood estimation technique based on the tuning curve of the neurons." >}}
