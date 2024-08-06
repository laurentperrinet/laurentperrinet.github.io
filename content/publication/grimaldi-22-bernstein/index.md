---
title: Detection of precise spiking motifs using spike-time dependent weight and delay
  plasticity
authors:
- Antoine Grimaldi
- Camille Besnainou
- Hugo Ladret
- Laurent U Perrinet
date: '2022-09-11'
publishDate: '2024-08-06T07:35:48.661616Z'
publication_types:
- paper-conference
publication: '*Bernstein Conference 2022*'
abstract: The spiking response of a biological neuron depends on the precise timing
  of afferent spikes. This temporal aspect of the neuronal code is essential in understanding
  information processing in neurobiology. In this model, raster plot analysis showed
  repeated activation of specific spiking motifs, which exhibit a precise temporal
  sequence of neural activations. Our first contribution is to develop a model for
  the efficient detection of temporal spiking motifs based on a layer of neurons with
  hetero-synaptic delays. Indeed, the variety of synaptic delays on the dendritic
  tree allows synchronizing synaptic inputs as they reach the basal dendritic tree.
  Second, we propose a bio-plausible unsupervised learning rule on both weights and
  delays through the derivation of a loss function which depends on the membrane potential
  of the spiking neuron and a sparseness regularization. We demonstrate on synthetic
  data that such a layer of spiking neurons is able to learn different repeating spatio-temporal
  motifs embedded in the spike train. Then, we test the robustness of the detection
  accuracy of the model by adding Poisson noise and compare it to a layer of Leaky-Integrate
  and Fire neurons trained with STDP. Results show a large improvement in performances
  when adding temporal delays for computations and a great increase in robustness
  to noise. We show that using synaptic delays for neuronal computations highly increases
  the representational capacities of a single neuron and its resilience to noise.
  .
---
