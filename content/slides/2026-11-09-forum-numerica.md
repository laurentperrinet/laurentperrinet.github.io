---
title: 2026-11-09-forum-numerica
date: '2026-11-09T14:00:00Z'
publishDate: '2026-10-28T09:28:26Z'
authors:
- Laurent U Perrinet
categories:
- Computational Neuroscience
- NeuroAI & Machine Learning
tags:
- spiking-neural-networks
- neuromorphic-computing
projects:
- open-science
slides:
  theme: white
  reveal_options:
    transition: fade
    controls: true
    progress: true
    slide_number: true
    hash: true
  branding:
    logo:
      show: true
      filename: favicon.svg
      position: top-right
      width: 50px
    title:
      show: true
      position: bottom-left
    footer:
      show: true
      text: © 2026 Laurent U Perrinet
      position: bottom-center
summary: Modelling memory to understand the brain
type: slides
---

<section>

<!-- no-branding -->

# [Modelling memory to understand the brain](https://laurentperrinet.github.io/slides/2026-11-09-forum-numerica/?transition=fade)
## *[Laurent U Perrinet](https://laurentperrinet.github.io/talk/2026-11-09-forum-numerica/)*
### <u>Forum Numerica seminar, Université Côte d'Azur</u>
### [2026-11-09]

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)

Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

{{< speaker_note >}}
**≈ 45 s**

- thank the Forum Numerica organisers (Academy of Excellence "Networks, Information and Digital society", DS4H); who I am (INT, Marseille; CNRS / Aix-Marseille Université)
- topic: neural networks that store patterns for seconds
- the problem: spiking neurons forget in tens of ms
- my answer: working memory in SNNs with polychronous chains and heterogeneous delays
- slides + references on my web-site; first, why model memory?


*Hello*, and thanks to the Forum Numerica organisers for the invitation. I'm Laurent Perrinet from the Institut de Neurosciences de la Timone in Marseille. Today I will speak about modelling memory: neural networks that store patterns for seconds. This is hard, because spiking neurons forget very fast, within tens of milliseconds. So how can we stretch this memory by two orders of magnitude? I will present a method to build *working memory in spiking neural networks, using chains of polychronous groups with heterogeneous delays*. The slides are on my web-site, with the references. But first, why is memory so important? Let's start with a philosophical insight.


- time scale: the membrane time constant of cortical neurons is typically 10-20 ms, whereas working memory operates over seconds (Baddeley, 2003; Goldman-Rakic, 1995)
- polychronization: Izhikevich (2006), *Polychronization: computation with spikes*, Neural Computation 18(2):245-282
{{< /speaker_note >}}

</section>

---

<section>

## Why Modelling Memory?

{{% fragment %}}{{< figure src="https://laurentperrinet.github.io/talk/2026-11-09-forum-numerica/featured.png" width="60%" >}}{{% /fragment %}}

{{< speaker_note >}}
**≈ 2 min 30 s** (without digressions; the story is the longest part of the intro)

- living systems are amazing, they keep their order from birth to death, without collapsing
- Shannon: order/disorder is measurable in bits (entropy, mutual information)
- 2nd law: random collisions -> entropy grows (gas in a box with a hole)
- Maxwell's demon: a sorter that uses information to undo it = needs a memory
- the baby piling up blocks is a demon (and he pays the bill: he eats)
- Crick: the mind is the behaviour of nerve cells -> let's model them


Living systems are amazing: from birth to death, they do not collapse into disorder, they maintain their structure and function over time. Yet quantifying this order is surprisingly simple: thanks to Claude Shannon, a system can be described by the information it holds, in bits, through its entropy or the mutual information between its parts, which are immensely useful in neuroscience. Now, the second law of thermodynamics says that the entropy of an isolated system never decreases, because its parts interact randomly, and this gives time its arrow. Imagine a box with two compartments, one full of gas, one empty. Open a small hole between them: by random collisions the gas spreads into both compartments, and entropy increases. Can we go back? Maxwell imagined a little demon sitting at the hole, who lets a molecule through only when it is heading to the left. Order emerges again, and the entropy of the gas decreases! The trick is that the demon uses information: it must observe each molecule and remember what it saw. Knowing dependencies across space and time is what lets a system locally resist disorder, and holding such information over time is what we call memory. Here is a picture of such a Maxwell demon: this baby is piling up blocks. He knows, and that is why he is happy, that if he does not act, the second law will win and the tower will collapse. And unlike Maxwell's demon, he pays his thermodynamic bill: he eats. As Francis Crick put it, we are "no more than the behavior of a vast assembly of nerve cells and their associated molecules". So let's model them, and see how memory is modelled today.


- the second law concerns isolated systems; living systems are open and export entropy (heat) to their environment (Schrödinger, 1944, *What is Life?*): they do not violate it
- the demon does not violate it either: Szilard (1929) and Brillouin (1951) showed that measuring costs entropy; Landauer (1961) and Bennett (1982) showed that the cost is paid when the demon's memory is erased, at least k T ln 2 per bit. The demon's memory is the key
- Maxwell (1867, letter to Tait); the original demon sorts fast from slow molecules, the one-way door is the Szilard-style simplification
- Shannon (1948), *A Mathematical Theory of Communication*, Bell System Technical Journal 27:379-423
- experimental demon: Toyabe et al. (2010), Nature Physics 6:988-992
- Crick (1994), *The Astonishing Hypothesis*: "You, your joys and your sorrows, your memories and your ambition, your sense of personal identity and free will, are in fact no more than the behavior of a vast assembly of nerve cells and their associated molecules." The previous wording was a paraphrase, not a verbatim quote
{{< /speaker_note >}}

---

## Modelling Memory: State-of-The-Art

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/7/7d/NN_LSTM-Cell_v2.svg" title="Long short-term memory ([Wikipedia](https://en.wikipedia.org/wiki/Long_short-term_memory))" width="80%" >}}

{{< speaker_note >}}
**≈ 45 s**

- first family: recurrent networks, state fed back at the next step
- problem: vanishing/exploding gradient when learning through time
- LSTM: memory cell + gates (input, forget, output)
- works for speech, handwriting; but analog state, far from neurons


How is memory modelled in machine learning? A first family is that of recurrent neural networks, where the state of the network at one time step is fed back at the next one. The problem is that, when learning, the gradient is multiplied at each time step, so it quickly vanishes or explodes as it travels back in time, and long-range dependencies cannot be learned. The LSTM solves this with a memory cell that works like a conveyor belt, and *gates*, input, forget and output, that decide what is written, kept or read. This made recurrent networks work for speech or handwriting, but the memory is a continuous, analog state, far from what neurons do.


- Hochreiter & Schmidhuber (1997), *Long short-term memory*, Neural Computation 9(8):1735-1780
- vanishing gradient: Hochreiter (1991, diploma thesis); Bengio, Simard & Frasconi (1994), IEEE Trans. Neural Networks 5(2):157-166
- forget gate added later: Gers, Schmidhuber & Cummins (2000), Neural Computation 12(10):2451-2471
- intuition for the vanishing gradient: going back T steps multiplies the gradient by about T factors; if each is 0.9, then 0.9^100 is about 3e-5 (vanishes); if each is 1.1, then 1.1^100 is about 14,000 (explodes). No signal survives a long delay
- intuition for the LSTM: the cell state is a "constant error carousel", a conveyor belt whose self-connection is exactly 1, so the factor is 1 and the gradient neither shrinks nor grows. The gates are the only places where something is put on the belt, removed from it or read from it, like a notebook where you write or erase on purpose
{{< /speaker_note >}}

---

## Modelling Memory: State-of-The-Art

{{< figure src="https://jalammar.github.io/images/t/transformer_resideual_layer_norm_2.png" title="The (Illustrated) Transformer ([Jay Alammar](https://jalammar.github.io/illustrated-transformer/))" width="60%" >}}

{{< speaker_note >}}
**≈ 40 s**

- breakthrough in NLP: the Transformer (the T in ChatGPT)
- no recurrence: attention compares the current token with the whole context
- long-range relationships used to predict the next token
- cost: memory = entire context window; massive, energy-hungry, not biological


A second route gave the real breakthrough, in natural language processing: the Transformer architecture, the T in ChatGPT. There is no recurrence any more: *attention* compares the current token with all the tokens of the context window. It thus memorises long-range relationships and uses them on the current sequence, here to predict the next token. But the memory is the whole context window, read again at every step. This requires massive models, is energy-intensive, and is not biologically plausible. So neither of these two routes is what the brain does.


- Vaswani et al. (2017), *Attention is all you need*, NeurIPS
- cost of self-attention grows quadratically with the context length n (n x n comparisons)
- Alammar's illustrated version: https://jalammar.github.io/illustrated-transformer/
- contrast for the talk: the brain keeps information in the *dynamics* of its network, not by re-reading a buffer
{{< /speaker_note >}}

---

## Modelling Memory: Outline

<ol class="outline">
  <li class="fragment"><strong>Including memory in spiking neurons</strong><span>Exploiting the temporal precision of the temporal code</span></li>
  <li class="fragment"><strong>MNESIS: polychronous chains</strong><span>Heterogeneous delays to hold patterns for seconds</span></li>
  <li class="fragment"><strong>Applications to neuroscience</strong><span>Travelling waves, chaotic dynamics, text</span></li>
</ol>

{{< speaker_note >}}
**≈ 30 s**

- part 1: memory in spiking neurons, using the precise timing of spikes (toy example)
- part 2: MNESIS at scale, performance on synthetic data
- part 3: applications to neuroscience


So what about spiking neurons? The *outline* of the talk is as follows. First, I'll show how to include memory in spiking neurons by exploiting the temporal precision of spikes, with a toy model example. Then, I'll present MNESIS, our polychronous chains with heterogeneous delays, at real scale, and quantify its performance on synthetic data. Finally, I will sketch some applications for neuroscience.


- the three parts match the three fragments on the slide
- MNESIS = the model of working memory with chains of polychronous groups
- total for the introduction (5 slides): about 5 min 10 s at a fast pace (about 170 words per minute)
{{< /speaker_note >}}

</section>

---

<section>

## Spiking Neural Networks

{{< speaker_note >}}
**≈ 30 s**

- these models work, but are power hungry
- the brain computes with spikes: all-or-none, sparse in time, cheap in energy
- so let's explore spiking neural networks (SNNs)


These models work, but at a high price in energy: training a large model takes megawatt-hours, whereas the brain runs on about twenty watts. The brain computes with spikes: all-or-none events, sparse in time, so energy is spent only when something happens. This is why I want to explore spiking neural networks, or SNNs.


- brain power: about 20 W (commonly quoted figure); cortical neurons fire a few Hz on average, so activity is very sparse
- training cost: Patterson et al. (2021) estimate about 1,300 MWh for GPT-3 (check before quoting)
- Roy, Jaiswal & Panda (2019), *Towards spike-based machine intelligence with neuromorphic computing*, Nature 575:607-617
- hardware exploiting sparse spikes: Loihi (Intel), SpiNNaker, TrueNorth (IBM)
- TODO: pick one concrete energy comparison for this audience
{{< /speaker_note >}}

---

## Spiking Neural Networks: Leaky Integrate-and-Fire

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/c509f781ac0d6d874c92e54080d6f96a520c32a7/figures/LIF.gif" title="Review on Precise Spiking Motifs ([Grimaldi *et al*, 2023](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))" width="80%" >}}

{{< speaker_note >}}
**≈ 45 s**

- a standard Leaky Integrate-and-Fire (LIF) neuron: the membrane potential integrates the input and leaks back to rest
- threshold crossed -> spike, then reset
- the leak = the memory of a single neuron: 10-20 ms
- so how can a network of such neurons hold a pattern for seconds?


The simplest spiking neuron is the leaky integrate-and-fire neuron. Its membrane potential integrates the input current, and leaks back to rest. When it crosses a threshold, the neuron emits a spike and is reset. Notice that the leak sets the memory of a single neuron: its membrane time constant, of the order of 10 to 20 milliseconds. So how can a network of such neurons hold a pattern for seconds?


- Lapicque (1907) introduced the integrate-and-fire neuron; textbook: Gerstner, Kistler, Naud & Paninski (2014), *Neuronal Dynamics*
- discrete time: $\beta = \exp(-\Delta t / \tau)$, so with $\Delta t = 1$ ms and $\tau = 10$-$20$ ms, $\beta \approx 0.90$-$0.95$
- a hint of the answer (paper, hyper-parameter search): the best networks have a *short* leak (best 10% of trials have $\beta \le 0.63$): the memory is in the delays, not in the leak
- animation from Grimaldi et al. (2023), *Precise Spiking Motifs in Neurobiological and Neuromorphic Data*, Brain Sciences
{{< /speaker_note >}}

---

## Spiking Neural Networks: neurobiology

{{< figure src="https://i.sstatic.net/ixnrz.png" title="([Mainen & Sejnowski, 1995](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_2_MainenSejnowski1995.ipynb))" width="80%" >}}

{{< speaker_note >}}
**≈ 45 s**

- is spike timing meaningful or noise?
- same cortical neuron stimulated repeatedly in vitro
- constant current (left): spike times drift from trial to trial
- fluctuating current (right): reproducible to within a millisecond -> neurons *can* be precise in time


Is the timing of spikes meaningful, or is it just noise? Mainen and Sejnowski stimulated the same cortical neuron repeatedly, in a slice. With a constant current, on the left, the spike times drift from trial to trial. With a fluctuating current, on the right, the spikes are reproducible to within a millisecond. So neurons can be precise in time: spike timing may carry information.


- Mainen & Sejnowski (1995), *Reliability of spike timing in neocortical neurons*, Science 268(5216):1503-1506
- neocortical slices from rat; the same "frozen" noisy current is injected in each trial
- the figure is regenerated from the notebook linked in the caption (review repository)
- an in vivo counterpart: Bair & Koch (1996), area MT of the awake monkey, Neural Computation 8:1185-1202 (check)
{{< /speaker_note >}}

---

## Spiking Neural Networks: neurobiology

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/c509f781ac0d6d874c92e54080d6f96a520c32a7/figures/Diesmann_et_al_1999.png" title="([Diesmann et al. 1999](https://github.com/SpikeAI/2022_polychronies-review/blob/main/src/Figure_3_Diesmann_et_al_1999.py))" width="99%" >}}

{{< speaker_note >}}
**≈ 45 s**

- if spikes can be precise, can the precision be kept across a network?
- synfire chain: a synchronous volley goes from one pool of neurons to the next
- large and synchronous enough: stable, even sharpens; otherwise dies out
- precise timing preserved across many synaptic stages


If spikes can be precise, can this precision be preserved across a network? This is the idea of synfire chains: a volley of synchronous spikes propagates from one pool of neurons to the next. Diesmann and colleagues showed that if the volley is large and synchronous enough, it is stable and even sharpens along the chain; otherwise it dies out. Precise timing can therefore be preserved across many synaptic stages.


- Abeles (1982, 1991), *Corticonics*: the synfire chain
- Diesmann, Gewaltig & Aertsen (1999), *Stable propagation of synchronous spiking in cortical neural networks*, Nature 402:529-533
- limit to mention: a synfire chain is synchronous, one time step per link and no diversity of delays; the next slides relax this
- leftover sentence from the previous version, to keep or drop: "This hypothesis is reviewed with respect to our knowledge of the neurobiology, for instance in the hippocampus of rodents."
{{< /speaker_note >}}

---

## Spiking Neural Networks: neurobiology

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/c509f781ac0d6d874c92e54080d6f96a520c32a7/figures/haimerl2019.jpg" title="Internal representation of hippocampal neuronal population spans a time-distance continuum. ([Haimerl et al, 2019](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))" width="99%" >}}

{{< speaker_note >}}
**≈ 1 min**

- is there such precise temporal structure at the scale of seconds? an example in the hippocampus
- CA1 neurons, calcium imaging in mice running on a track: sequences repeat across sessions
- a time-distance continuum, with a time scale of seconds
- the domain is vast, a lot to do in SNNs: next, Izhikevich's polychronization


Do we see such precise motifs in the brain, at the scale of seconds? Here is an example from the hippocampus. Haimerl and colleagues imaged the calcium activity of CA1 neurons in mice running on a track. Cells are ordered by their activity in the first imaging session: the same sequences of activity repeat in the following sessions, with a time scale of the order of seconds, a continuum of time and distance. So the brain does hold precise temporal motifs over seconds. The domain is vast and there is a lot to do in spiking networks; I now come to a model of such motifs, Izhikevich's polychronization.


- Haimerl et al. (2019), *Internal representation of hippocampal neuronal population spans a time-distance continuum*, PNAS (check volume and pages)
- caption of panel (A): calcium fluorescence (heatmap) of CA1 neurons participating in run sequences in consecutive imaging sessions; cells selected and ordered with respect to their activity in the first session (top); the black line is the speed of the mouse
- to fix: the link in the slide caption points to the Grimaldi review, not to the Haimerl paper
- raster analysis showing repeated precise motifs: Grimaldi et al. (2023) review
{{< /speaker_note >}}

---

## Spiking Neural Networks: Polychronization

{{< figure src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/izhikevich_left.svg" width="100%" >}}

{{< speaker_note >}}
**≈ 30 s**

- core idea: polychronous groups (Izhikevich, 2006)
- 3 presynaptic neurons -> 2 postsynaptic neurons
- each connection: a weight and a delay (travel time of the spike)


The core idea of the method follows the polychronous groups defined by Izhikevich in 2006. Suppose three presynaptic neurons are connected to two postsynaptic neurons, with certain weights and certain delays. A delay is the time it takes for a spike to travel from one neuron to the next.


- Izhikevich (2006), *Polychronization: computation with spikes*, Neural Computation 18(2):245-282
- axonal conduction delays in the cortex range from about 1 to several tens of ms
- Izhikevich's claim: the number of coexisting polychronous groups can far exceed the number of neurons, hence a large potential memory capacity
{{< /speaker_note >}}

---

## Spiking Neural Networks: Polychronization

{{< figure src="https://github.com/SpikeAI/2022_polychronies-review/raw/c509f781ac0d6d874c92e54080d6f96a520c32a7/figures/HSD.gif" title="Review on Precise Spiking Motifs ([Grimaldi *et al*, 2023](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="80%" >}}

{{< speaker_note >}}
**≈ 40 s**

- a neuron with heterogeneous synaptic delays (HSD): each input reaches the soma after its own delay
- delays shift the incoming spikes: a given temporal pattern arrives *synchronously*
- the neuron detects a precise spiking motif, not only a firing rate


Here is a neuron with heterogeneous synaptic delays: each input reaches the soma after its own delay. These delays shift the incoming spikes in time, so that a given temporal pattern arrives synchronously at the soma. The neuron then acts as a detector of a precise spiking motif, not just of a firing rate.


- animation from Grimaldi et al. (2023); same family of ideas as coincidence detection (Jeffress model for sound localisation)
- a rate code would ignore the order of the spikes; here the order is what matters
{{< /speaker_note >}}

---

## Spiking Neural Networks: Polychronization

{{< figure src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/izhikevich_middle.svg" title="Polychronization: Computation with Spikes ([Izhikevich, 2006](https://www.izhikevich.org/publications/spnet.pdf))" width="100%" >}}

{{< speaker_note >}}
**≈ 25 s**

- different delays + synchronous presynaptic spikes: the currents do not match in time
- the membrane potential does not reach the threshold


If the delays are different and the presynaptic neurons are activated synchronously, the postsynaptic currents do not match in time. The membrane potential then does not reach the threshold, and the neuron stays silent.


- this is the control case: a synchronous input is *not* what the neuron is tuned to
- figure: Izhikevich (2006), redrawn for the ICANN 2023 talk
{{< /speaker_note >}}

---

## Spiking Neural Networks: Polychronization

{{< figure src="https://github.com/laurentperrinet/2023-07-20_HDSNN-ICANN/raw/master/figures/izhikevich.svg" title="Polychronization: Computation with Spikes ([Izhikevich, 2006](https://www.izhikevich.org/publications/spnet.pdf))" width="100%" >}}

{{< speaker_note >}}
**≈ 30 s**

- if the presynaptic spikes form a *spiking motif* that compensates the delays
- they reach the soma of neuron $b_1$ at the same time
- this neuron is selectively activated


However, if the timing of the presynaptic spikes forms a *spiking motif*, such that the spikes reach the soma of neuron $b_1$ at the same time, then this neuron is selectively activated. The delays have turned a temporal pattern into a coincidence. Now, what happens if we chain such groups?


- the group of presynaptic neurons + the pattern of delays is a polychronous group
- the same neurons, with another timing, activate another neuron (e.g. $b_2$): neurons are shared across groups
{{< /speaker_note >}}

---

## Heterogeneous delays: detecting a spiking motif

<iframe src="https://spikeai.github.io/MNESIS/HD-SNN.html" width="100%" height="550" frameborder="0" allowfullscreen></iframe>

{{< speaker_note >}}
**≈ 2 min**

1. show the raster: 128 input neurons on top, 5 output neurons (membrane potential) in the frame below; slow it down (`k`) so that individual spikes become visible
2. pause with `space`: the animation stops on the next output spike; press `c` for the motif mode
3. press `d` three times: (1) the output spike and the 41 ms before it, (2) the input spikes of its motif, in its colour, (3) the delays, animated from the past to the present
4. press `d` a fourth time (or `n`) to go to the next output spike; `b` then `d` replays the animation
5. press `space` again to make it dynamic again

Here the 128 inputs fire as background noise, and each of the 5 output neurons listens to them through synapses with a weight and a delay between 0 and 40 ms. I pause on an output spike and switch on the motif mode: the 12 input spikes of its motif are coloured. Then the delays: each input spike slides along its connection, the one with the longest delay leaving first, and they all arrive together on the output neuron. Their potentials add up, the threshold is crossed and the neuron fires: the motif is detected. A partial motif, with only 3 of the 12 spikes, raises the potential without reaching the threshold. With heterogeneous delays, the position of a spike in the past matters, not only its neuron. This is the building block of the chains shown just before.

- demo: https://spikeai.github.io/MNESIS/HD-SNN.html (code in the MNESIS repository)
- keys: `space` pause/play, `c` motif, `d` delays (3 presses, a 4th goes to the next output spike), `n` next / `b` back, `k` / `l` slower / faster
- reference: Perrinet (2023), Accurate detection of spiking motifs by learning heterogeneous delays of a spiking neural network, ICANN 2023, arXiv 2307.11555
- backup if the iframe does not load: open the link in a new tab, or use a screenshot
{{< /speaker_note >}}


---

## Chaining polychronous groups

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/4bdeec0834c2bee1edf2ede1aaa8ab6829ca3457/figures/izhikevich_rec.svg" title="Working Memory in a Recurrent Spiking Neural Networks ([LP, 2026](https://arxiv.org/abs/2604.14096))" width="100%" >}}

{{< speaker_note >}}
**≈ 45 s**

- from the feedforward toy example to a *recurrent* network: synapses act on the same population
- a motif = a context window (green area) that predicts the spikes at the next time step
- the prediction creates a new context -> chain the motifs
- next slide: a live demo of this chain


We have just seen that delays turn a temporal pattern into a coincidence. Now let us close the loop: in a recurrent network, the synapses act on the same population. Deviating from Izhikevich, we define motifs such that, given one context window, the green shaded area, the network predicts the spikes at the next time step. This creates a new context, and a new prediction: the motifs chain, and the pattern is sustained much longer than the membrane time constant. Let me show how this looks in a simulation.


- the context window has the length of the longest delay: $D = 41$ time steps of 1 ms
- the chain is "overlapping": each context window shares $D-1$ steps with the previous one
- difference with an RNN/LSTM: the state is a window of spikes, and the memory is in the delays
- figure: LP (2026), arXiv:2604.14096
{{< /speaker_note >}}

---

## Chaining polychronous groups

<iframe src="https://spikeai.github.io/MNESIS/izhikevich.html" width="100%" height="550" frameborder="0" allowfullscreen></iframe>

{{< speaker_note >}}
**≈ 2 min**

1. show the raw raster of the 100 neurons, then slow it down so the individual spikes become visible
2. pause with `space`, then press `c` to show a chain and `d` to show its delays
3. press `n` several times to step through to the next spikes
4. press `space` again to make it dynamic again


This is the recurrent network of the previous slide, as a toy of 100 neurons. At first it looks like noise: a raster of random spikes. Let me slow it down: now we see individual spikes. I pause, and show a chain: a group of neurons firing in a precise order, and the delays that make their spikes converge on the next neuron at the same time. Each group is the context window that predicts the next one. Let me step to the next spikes: this group triggers the next one, and so on. If I let it run again, the pattern keeps itself going for much longer than the 10 to 20 milliseconds of a single neuron. So the question becomes: how do we build, and learn, such chains in a large network?


- demo: https://spikeai.github.io/MNESIS/izhikevich.html (code in the MNESIS repository)
- keys: `space` pause/play, `c` chain, `d` delays, `n` next spikes
- backup if the iframe does not load: open the link in a new tab, or use a screenshot
- TODO: say how many groups are in the chain and how long the chain lasts
{{< /speaker_note >}}

</section>

---

<section>

## Methods

{{< speaker_note >}}
**≈ 15 s**

- the demo showed that the chain works in a toy network of 100 neurons
- now: how to build, and learn, such chains in a full network?


We have seen in the demo that chained polychronous groups sustain a pattern. Let me now detail how we build them, and learn them, in a full network.


- the paper: Perrinet (2026), *Working Memory in a Recurrent Spiking Neural Network*, arXiv:2604.14096
- code: https://github.com/SpikeAI/MNESIS
{{< /speaker_note >}}

---

## Methods: chaining Polychronization

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/4bdeec0834c2bee1edf2ede1aaa8ab6829ca3457/figures/izhikevich_rec.svg" title="Working Memory in a Recurrent Spiking Neural Networks ([LP, 2026](https://arxiv.org/abs/2604.14096))" width="100%" >}}

{{< speaker_note >}}
**≈ 30 s**

- recap of the principle, now as a model: context window of $D = 41$ delays -> spikes at the next time step
- the weights form a tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$: one weight per pair of neurons and per delay
- a motif = a chain of such overlapping windows, which the weights have to encode


As you saw in the demo, a context window predicts the next spikes, which creates a new context. Formally, the synaptic weights form a tensor with one weight per pair of neurons and per delay, and a stored motif is a chain of overlapping windows. The question is how to find these weights.


- the context window has the length of the longest delay: $D = 41$ time steps of 1 ms
- the chain is "overlapping": each context window shares $D-1$ steps with the previous one
- difference with an RNN/LSTM: the state is a window of spikes, and the memory is in the delays
- figure: LP (2026), arXiv:2604.14096
{{< /speaker_note >}}

---

## Methods: BPTT (snnTorch)

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/4bdeec0834c2bee1edf2ede1aaa8ab6829ca3457/figures/unrolled.svg" title="Training SNNs Using Lessons From Deep Learning ([Eshraghian, 2023](https://ieeexplore.ieee.org/document/10242251))" width="80%" >}}

{{< speaker_note >}}
**≈ 1 min**

- implementation in snnTorch: delays add one more level in the unrolled graph (delay line, bottom)
- network: 1024 neurons, 41 delays, 16 patterns
- task: repeat *exactly* all the spikes of a random target (0.16 spikes/s/neuron)
- loss: F1-score; fast-sigmoid surrogate gradient; about 25 min (256 epochs)


We implement the network with snnTorch. The delays add just another level of propagation in the unrolled computational graph, here represented by the delay line at the bottom. The network has 1024 neurons, 41 delays, and has to learn 16 different patterns. The task is to repeat exactly all the spikes of a randomly drawn target, with a mean firing rate of 0.16 spikes per second per neuron. The loss is the F1-score, the harmonic mean of recall and precision. With a fast-sigmoid surrogate gradient, the network learns the targets in about 25 minutes, 256 epochs.


- Eshraghian et al. (2023), *Training spiking neural networks using lessons from deep learning*, Proceedings of the IEEE 111(9):1016-1054 (snnTorch)
- $p_A = 1.6 \cdot 10^{-4}$ per 1 ms time step, i.e. 0.16 Hz: a pattern of 1 s has about 160 spikes in total
- the spike is a non-differentiable step: the surrogate gradient replaces its derivative with a smooth one in the backward pass (Neftci, Mostafa & Zenke, 2019, IEEE Signal Processing Magazine)
- TODO: reconcile "25 min of training" with the paper's statement that the analytical initialisation alone reaches F1 about 0.8 and training changes the readout by 0.17% (check which is the best story)
{{< /speaker_note >}}

---

## Methods: leaky integrate-and-fire network

{{% fragment %}}
$$ I_j(t) = \sum_{i=1}^{N} \bigl ( \sum_{d=1}^{D} \mathbf{W}_{j, i, d} \cdot s_i(t-d) \bigr ) $$
$$ u_j(t) = \beta \cdot u_j(t-1) \cdot (1 - s_j(t-1)) + I_j(t) $$
$$ s_j(t) = \mathbf{H}[u_j(t) \geq \vartheta] $$
{{% /fragment %}}
{{% fragment %}}
<small>$N$: number of neurons, $D$: number of delays (time steps of 1 ms), $\mathbf{W}_{j, i, d}$: weight from neuron $i$ to neuron $j$ with delay $d$, $s_i(t)$: spike (0 or 1) of neuron $i$, $I_j$: input current, $u_j$: membrane potential, $\beta$: membrane decay constant, $\vartheta$: firing threshold, $\mathbf{H}$: Heaviside step function.</small>
{{% /fragment %}}

{{< speaker_note >}}
**≈ 1 min 15 s**

- each neuron integrates the spikes of *all* neurons over *all* the $D$ previous steps: delays add one dimension to the weights
- the potential decays by $\beta$ at each step and is reset after a spike (the LIF neuron seen earlier)
- a spike is emitted when the potential reaches the threshold $\vartheta$


Here is the model. The input current to neuron $j$ is the sum, over all neurons $i$ and all delays $d$, of the weight $W_{j,i,d}$ times the spike of neuron $i$, $d$ time steps ago. So the delays simply add one dimension to the weights. The membrane potential decays by $\beta$ at each step, and is reset after a spike: this is the discrete-time LIF neuron seen earlier. A spike is emitted when the potential reaches the threshold.


- $N = 1024$, $D = 41$: the tensor $\mathbf{W}$ has $1024 \times 1024 \times 41 \approx 43$ million weights
- hyper-parameter search (Optuna, 197 trials): the threshold matters most (importance 0.52); all trials with $\vartheta > 1$ failed; the best 10% have $\vartheta \in [0.59, 0.78]$
- $\beta$: best with short leaks; surrogate sharpness has negligible importance
- the fragments reveal the equations first, then the legend
{{< /speaker_note >}}

---

## Methods: weight initialisation

{{% fragment %}}
- $$ \mathbf{W} \mathbf{C} \approx \mathbf{S} $$
{{% /fragment %}}
{{% fragment %}}
$$ w_{j, i, d} = \frac{1}{N \cdot D \cdot p_A} \sum_{\mu=1}^{M} \sum_{t=D+1}^{T} s_i^{\mu}(t-d) \cdot \bigl( s_{j}^{\mu}(t) - \beta \cdot s_{j}^{\mu}(t-1) \bigr) $$
{{% /fragment %}}
{{% fragment %}}
<small>$\mathbf{S}$: target spikes, $\mathbf{C}$: context (spikes of the $D$ preceding time steps), $M$: number of target motifs (index $\mu$), $T$: duration of a motif (time steps), $p_A$: average spike probability per neuron and per time step, $\beta$: membrane decay constant.</small>
{{% /fragment %}}

{{< speaker_note >}}
**≈ 1 min 15 s**

- BPTT converges slowly: some weights lead to dead or epileptic regimes
- initialisation: each prediction is linear, $\mathbf{W}\mathbf{C} \approx \mathbf{S}$
- concatenate all the equations and invert with a Moore-Penrose pseudo-inverse
- per weight: a Hebbian-like rule (delayed presynaptic spikes x deconvolved postsynaptic target)


However, convergence is quite slow, in particular because some regions of the weight space correspond to non-linear regimes, dead or epileptic. So we use a weight initialisation. Each prediction can be seen as a linear prediction of the next time step: the weights times the context should approximately give the target spikes. We concatenate all these equations together, and invert them with a Moore-Penrose pseudo-inverse to get the weights. Written for each weight, this solution is a Hebbian-like rule: a correlation between the delayed presynaptic spikes and the deconvolved postsynaptic target. That is why Hebbian-like learning may incidentally work for training this type of network.


- Penrose (1955), a generalized inverse for matrices
- paper, hyper-parameter search: median loss about 0.22 with the pseudo-inverse initialisation versus about 1 with the Hebbian rule (check that the closed form on the slide is the one called "pseudo-inverse" in the paper)
- paper: starting from the analytical initialisation, the mean F1 is already about 0.80; training changes the readout by only 0.17% in relative norm
- here $\mathbf{S}$ = target spikes, $\mathbf{C}$ = context (spikes of the $D$ preceding steps), $M$ motifs, $T$ steps per motif
{{< /speaker_note >}}

</section>

---

<section>

## Results

{{< speaker_note >}}
**≈ 15 s**

- does it work?
- test the recall of the stored patterns, and how robust it is


Does it work? We now test the network on its ability to recall the stored patterns, and on how robust this recall is.


- plan: recall of one target -> retrieval among 16 -> robustness (noise, shorter trigger, fewer neurons) -> periodic replay -> analysis of the network
{{< /speaker_note >}}

---

## Results: recall of target

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/main/figures/pattern_full.svg" width="100%" >}}

{{< speaker_note >}}
**≈ 40 s**

- one target pattern: raster of random spikes, neurons (y) vs time (x)
- the network is triggered with the first time steps, then runs on its own


Here is one of the target patterns: a raster plot of randomly drawn spikes, with neurons on the vertical axis and time on the horizontal axis, over one second. The network is triggered with the first time steps of the pattern, the first context window, and then it runs on its own.


- $N = 1024$ neurons, $T = 1000$ steps (1 s), about 160 spikes in total at 0.16 Hz per neuron
- the pattern is random: no structure to exploit, a hard test for a memory
- TODO: describe the trigger window on the figure
{{< /speaker_note >}}

---

## Results: recall of target

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/main/figures/target.svg" width="100%" >}}

{{< speaker_note >}}
**≈ 45 s**

- comparison between the target and the activity produced by the network
- the spikes of the motif are reproduced well beyond the trigger, over 1 s, much longer than the membrane time constant
- mean F1 about 0.8; 9 of 16 motifs replayed exactly (F1 = 1)


Here is the comparison between the target and the activity produced by the network. The network reproduces the spikes of the motif well beyond the trigger, over one second, much longer than the membrane time constant. Over the 16 motifs, the mean F1-score is about 0.8, and nine motifs are replayed exactly.


- paper §3.1 (check): 9 of 16 motifs have F1 = 1 under a noisy trigger ($p_\mathrm{flip} = 0.01$)
- 4 motifs (4th, 10th, 12th, 13th) stop at a gap of $D$ silent steps (recall 0.18-0.56): with no spike in the context window, nothing triggers the next step
- 3 motifs (1st, 5th, 11th) have recall 1 but precision 0.55-0.65: over-activation; 425 false positives in total
- across realisations the mean F1 ranges 0.79-0.84, or 0.96 excluding the gap motifs: gaps set a deterministic ceiling
{{< /speaker_note >}}

---

## Results: memory retrieval

{{< video src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/retrieval.mp4" controls="yes" width="80%" >}}

{{< speaker_note >}}
**≈ 1 min**

- the same network stores 16 patterns; the beginning of one recalls that one and not the others
- content-addressable memory (as in Hopfield networks), for spatio-temporal patterns
- 12 of 16 retrieved cleanly (mean F1 0.96); the 4 gap motifs collapse after 200-600 steps


Now the same network stores 16 different patterns. Triggering it with the beginning of one of them recalls that pattern, and not the others. This is a content-addressable memory, as in Hopfield networks, but for spatio-temporal patterns. Twelve of the sixteen are retrieved cleanly, with a mean F1 of 0.96, and the four motifs with a gap collapse after a few hundred milliseconds.


- Hopfield (1982), PNAS 79:2554-2558
- paper §3.2 (check): clean retrieval for 12 of 16 motifs, F1 range 0.83-1.00; the cascade model predicts recall of 0.175, 0.221, 0.294 and 0.564 for the four failing motifs, matching the measures to three decimals
- errors propagate because each context window depends on the previous output

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/retrieval.svg" width="80%" >}}
{{< /speaker_note >}}

---

## Results: recall of target with noise

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/p_flip_target.svg" width="100%" >}}
 
{{< speaker_note >}}
**≈ 45 s**

- robustness to noise: a fraction of the trigger spikes is flipped (removed or added)
- graceful degradation: 25% flips still give F1 about 0.53
- below 0.1 only beyond 60% noise


How robust is the recall? We flip a fraction of the spikes of the trigger, removing or adding spikes. The recall degrades gracefully: with a quarter of the spikes flipped, the F1-score is still about 0.5, and it falls below 0.1 only beyond 60% of noise.


- paper §3.4 (check): at $p_\mathrm{flip} = 0.25$, F1 about 0.531 (precision 0.731, recall 0.419)
- the cascade model fits the curve (RMS error about 0.04)
- TODO: say what $p_\mathrm{flip}$ means in terms of the number of wrong spikes in the trigger
{{< /speaker_note >}}

---

## Results: recall of target with less trigger time

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/trigger_time.svg" width="100%" >}}

{{< speaker_note >}}
**≈ 45 s**

- shorter trigger: the network sees fewer steps before running on its own
- how short? compared with the $D = 41$ steps of the context window


Here we shorten the trigger: the network sees fewer time steps of the pattern before it runs on its own. With 31 of the 41 steps, that is three quarters of the context window, the score is still 0.79, and it reaches 80% of its maximum from 29 steps. So the network needs almost a whole context window to start.


- paper §3.4 (check): L = 31 of 41 steps: F1 about 0.788; 80% of the full-trigger value from L = 29
- cascade model fit: RMS error about 0.05
- control in the paper: in open loop, activity vanishes after $D$ steps, so the replay is sustained by the recurrent feedback, not by the trigger
{{< /speaker_note >}}

---

## Results: recall of target with less trigger neurons

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/fraction_target.svg" width="100%" >}}

{{< speaker_note >}}
**≈ 45 s**

- only a fraction of the neurons receive the trigger
- pattern completion: the network fills in the missing neurons from a partial cue
- how many neurons are needed?


Here only a fraction of the neurons receive the trigger. This is pattern completion: the network fills in the missing neurons from a partial cue. The score degrades smoothly with the fraction of missing neurons, and the recall remains good for a substantial fraction.


- paper §3.4 (check): with 128 of 1024 neurons silenced (N/8), F1 about 0.76; F1 levels off near 0.2 beyond N/2 silenced; cascade model RMS error about 0.06
- TODO: check that the figure shows the same manipulation as the paper's lesion experiment, and state the minimal fraction
{{< /speaker_note >}}

---

## Results: robustness of target recall

<div class="r-hstack" style="gap: 0.1rem;">
  <div style="flex: 1; margin: 0; text-align: center; display: grid;">
    <div class="fragment fade-out" data-fragment-index="0" style="grid-area: 1 / 1;">{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/p_flip_score_raw.svg" height="550" >}}</div>
    <div class="fragment" data-fragment-index="0" style="grid-area: 1 / 1;">{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/p_flip_score.svg" height="550" >}}</div>
  </div>
  <div style="flex: 1; margin: 0; text-align: center;">
    <div class="fragment" data-fragment-index="1">{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/trigger_time_score.svg" height="550" >}}</div>
  </div>
  <div style="flex: 1; margin: 0; text-align: center;">
    <div class="fragment" data-fragment-index="2">{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/fraction_target_score.svg" height="550" >}}</div>
  </div>
</div>

{{< speaker_note >}}
**≈ 1 min**

- the same three manipulations summarised by the recall score
- left: noise in the trigger; middle: duration of the trigger; right: fraction of neurons in the trigger
- smooth degradation, no sharp cliff


These three curves summarise the same manipulations with the recall score. On the left, the noise in the trigger; in the middle, the duration of the trigger; on the right, the fraction of neurons in the trigger. In all cases the score degrades smoothly, without a sharp cliff, and a simple cascade model of the chain reproduces the curves.


- cascade model: each spike is a test for igniting the next ones; RMS errors 0.042 (spike noise), 0.052-0.055 (truncated trigger), 0.061 (lesion)
- the fragments reveal the three panels one after the other
- TODO: confirm the shape of the curves on the figure (smooth or threshold-like?)
{{< /speaker_note >}}

---

## Results: free replay of periodic motifs

<div class="r-stack">
{{< figure src="https://github.com/SpikeAI/MNESIS/raw/ /figures/periodic_scores_0.svg" width="80%" >}}
{{% fragment %}}{{< figure src="https://github.com/SpikeAI/MNESIS/raw/7cc3e79bd13230c5415d0371566a5620bb947e04/figures/periodic_scores_1.svg" width="80%" >}}{{% /fragment %}}
{{% fragment %}}{{< figure src="https://github.com/SpikeAI/MNESIS/raw/7cc3e79bd13230c5415d0371566a5620bb947e04/figures/periodic_scores.svg" width="80%" >}}{{% /fragment %}}
</div>

{{< speaker_note >}}
**≈ 1 min 30 s**

- axes only: F1 of each period against time, one period lasts about 1 s (959 ms); one noisy trigger, then 100 periods of free replay (96 s)
- click 1, p_drop = 0 (data and theory): the score settles on a limit cycle after the first period -> a stable working memory
- click 2, the other levels (10^-4 to 10^-2): replay decays as predicted by the cascade model (dashed), each spike being a new ignition test

What happens if the chain closes on itself? For a periodic motif, the trigger window is copied onto the last $D$ steps, so that the period is 959 milliseconds, about one second. We give one noisy trigger, and let the network run freely for 100 periods, that is 96 seconds. Without failures, the score settles on a limit cycle after the first period: this is a stable working memory. To test its limits, each emitted spike is dropped with a probability from $10^{-4}$ to $10^{-2}$. The replay then decays, as predicted by the cascade model: each spike is a new ignition test. The mean lifetime goes from about 280 periods down to 2 periods.


- details: $T - D = 959$ ms; $p_\mathrm{flip} = 0.01$; thin lines = 5 seeds, thick = mean; each period scored ($F_1$) against the frozen motif; survival $\exp(-ht)$ (dashed)
- mean lifetimes of about 280, 60, 12 and 2 periods for the four non-zero levels
- paper §3.5 (check): noise-free trigger gives $F_1$ about 0.88 at the first period then a stable 0.83; 12 of 16 motifs sustained indefinitely, 4 fade within the first period
- score at period 100: 0.657 at $p_\mathrm{drop} = 10^{-4}$, 0.274 at $4.6 \cdot 10^{-4}$
{{< /speaker_note >}}

---

## Results: Analysing the network

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/histogram_log.svg" width="80%" >}}

{{< speaker_note >}}
**≈ 30 s**

- histogram of the weights (log scale) after learning
- TODO: what does the distribution tell us?


Let us look inside the network. This is the histogram of the weights after learning, on a logarithmic scale.


- TODO: describe the distribution (heavy tails? sparsity? balance of excitation and inhibition?), not found in the text of the paper I could access
- idea: a few strong weights carry the chain, most are close to zero
{{< /speaker_note >}}

---

## Results: role of parameters

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.1rem;">
  <div style="margin: 0;">
    {{% fragment %}}{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/scan_N_time.svg" width="100%" >}}{{% /fragment %}}
  </div>
  <div style="margin: 0;">
    {{% fragment %}}{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/scan_N_pattern.svg" width="100%" >}}{{% /fragment %}}
  </div>
  <div style="margin: 0;">
    {{% fragment %}}{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/scan_N_neuron.svg" width="100%" >}}{{% /fragment %}}
  </div>
  <div style="margin: 0;">
    {{% fragment %}}{{< figure src="https://github.com/SpikeAI/MNESIS/raw/827a6d88fd31196347cce007832f3311a065df18/figures/scan_num_delay.svg" width="100%" >}}{{% /fragment %}}
  </div>
</div>

{{< speaker_note >}}
**≈ 1 min**

- parameters varied one at a time: duration of patterns, number of neurons, number of delays
- the number of delays $D$ and of neurons $N$ matter most: the recall needs enough spikes per context window
- the number of stored patterns hardly matters (up to 26 tested)

Finally, the role of the parameters, varied one at a time. The score grows with the number of neurons and with the number of delays, and decreases only slowly with the duration of the patterns. What matters is the number of spikes in a context window, which is the number of neurons times the number of delays times the spike probability. Increasing the delays is the most economical way to raise it.


- paper §3.6 (check), 10 seeds per condition:
  - $D$: F1 near 0 for $D \le 15$, 0.86 at $D = 40$, above 0.95 from $D = 50$
  - $N$: near 0 up to $N \approx 430$, 0.7 at 795, 0.93 at 1081, 0.97 from about 1500
  - $T$: 0.97 at $T = 100$, 0.88 at 945, 0.78 at 1558
  - $M$: F1 between 0.84 and 0.94 for 3 to 26 motifs, no trend (load about 0.59 at $M = 26$)
- $\lambda_0 = p_A N D$: the mean number of spikes per context window; $D$ and $N$ act through it
- TODO: map each of the four panels (scan_N_time, scan_N_pattern, scan_N_neuron, scan_num_delay) to the numbers above
{{< /speaker_note >}}

</section>

---

<section>

## Applications to neuroscience

{{< speaker_note >}}
**≈ 20 s**

- beyond random patterns: activity resembling what we record in the brain, or what the brain must produce


So far the patterns were random. Can such a network store activity that resembles what we record in the brain, or what the brain has to produce? Here are a few applications.


- three cases: travelling waves, a chaotic trajectory (Lorenz attractor), and text
{{< /speaker_note >}}


<!-- 
---

## Applications to neuroscience: travelling waves

{{< video src="https://github.com/SpikeAI/MNESIS/raw/06c5537e11dbddb7508ae607a9490890739c4cfc/figures/TW.mp4" autoplay="yes" width="80%" loop="yes" >}}

{{< speaker_note >}}
**≈ 45 s**

- travelling waves are observed in sensory areas, e.g. visual cortex
- the target is a wave of activity sweeping the population
- the network learns to reproduce it


Travelling waves are observed in sensory areas, for instance in the visual cortex. Here the target is a wave of activity that sweeps across the population, and the network learns to reproduce it.


- Muller, Chavane, Reynolds & Sejnowski (2018), *Cortical travelling waves: mechanisms and computational principles*, Nature Reviews Neuroscience 19:255-268
- TODO: speed and direction of the wave, number of neurons involved, F1 reached
{{< /speaker_note >}}

---

## Applications to neuroscience: travelling waves

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/ad569d0f974e78c3f7da4a5122499c260ed7fd66/figures/TW_target_transitions.svg" width="60%" >}}

{{< speaker_note >}}
**≈ 45 s**

- transitions between waves
- TODO: describe the figure


This figure shows the transitions between waves: [TODO: describe, e.g. the network switching from one wave to another depending on the trigger].


- TODO: say what is on the axes and what the transition probabilities mean
- link with the retrieval slide: the same network holds several motifs
{{< /speaker_note >}} 
-->

---

## Applications to neuroscience: Lorenz attractor

{{< video src="https://github.com/SpikeAI/MNESIS/raw/4f5ad04d9f4c8403004b322aca5d41a98bcb7b1d/figures/lorenz_chaotic_code_decoding.svg" autoplay="yes" loop="yes" >}}

{{< speaker_note >}}
**≈ 45 s**

- a harder target: a chaotic trajectory (Lorenz attractor) encoded as spikes
- in a chaotic system, small errors grow exponentially: a demanding test for a memory


A harder target is a chaotic trajectory: the Lorenz attractor, encoded as spikes. In a chaotic system small errors grow exponentially, so it is a demanding test for a memory.


- Lorenz (1963), *Deterministic nonperiodic flow*, Journal of the Atmospheric Sciences 20:130-141
- TODO: how the three coordinates are encoded as spikes, and for how long the network replays the trajectory
{{< /speaker_note >}}

---

## Applications to neuroscience: Lorenz attractor

{{< video src="https://github.com/SpikeAI/MNESIS/raw/4f5ad04d9f4c8403004b322aca5d41a98bcb7b1d/figures/lorenz_chaotic_decoding.mp4" autoplay="yes" loop="yes" >}}

{{< speaker_note >}}
**≈ 20 s**

- decoded trajectory in 3D
- the network replays the butterfly-shaped attractor


In three dimensions, the decoded trajectory shows that the network replays the butterfly-shaped attractor.


- the replay stays on the attractor even when the exact trajectory is lost (to check)
{{< /speaker_note >}}

---

## Applications to neuroscience: Lorenz attractor

{{< figure src="https://github.com/SpikeAI/MNESIS/raw/4f5ad04d9f4c8403004b322aca5d41a98bcb7b1do/figures/lorenz_chaotic_decoding.svg" width="60%" >}}

{{< speaker_note >}}
**≈ 30 s**

- decoding of X, Y, Z from the spikes of the network
- compared with the original trajectory


To check, we decode the X, Y and Z coordinates from the spikes produced by the network, and compare them with the original trajectory.


- TODO: say how well they match, and after how long they diverge
{{< /speaker_note >}}

---

## Applications to neuroscience: encoding text

<ul style="width: 100%; margin: 0 auto; padding: 0; text-align: center; list-style-position: inside;">
  <li class="fragment"><span style="color: blue;"><i>Trigger:</i></span> severely. “What are you thinking of?”\n“I beg your pardon,” said Alice very humbly: “you had got to the fifth bend, I think?”\n“I had _not!_” cried the Mouse, sharply and very angrily.\n“A knot!” said Alice, always ready to make</li>
  <li class="fragment"><span style="color: green;"><i>Real:</i></span> herself useful, and looking anxiously about her. “Oh, do let me help to undo it!”\n“I shall do nothing of the sort,” said the Mouse, getting up and walking away. “You insult me by talking such nonsense!”\n“I didn’t mean it!” pleaded poor Alice.</li>
  <li class="fragment"><span style="color: red;"><i>Prediction:</i></span> herself useful, and looking anxiously about her. “Oh, do let me help to States it!”\n“I shall do nothing of the sort,” said the Mouse, getting up and walking away. “You insult me by talking such nonsense!”\n“I didn’t mean it!” pleaded poor Alice.</li>
</ul>

{{< speaker_note >}}
**≈ 45 s**

- storing text: characters of *Alice in Wonderland* encoded as spikes
- trigger (blue) -> continuation by the network (red) vs real text (green)
- almost perfect: a single wrong word ("States" instead of "undo")


Now text. The characters of *Alice in Wonderland* are encoded as spikes. The network is triggered with a passage, in blue, and then continues on its own, in red, to be compared with the real text, in green. Here the continuation is almost perfect: a single word is wrong, "States" instead of "undo".


- Carroll (1865), *Alice's Adventures in Wonderland* (public domain)
- each line appears as a fragment: trigger, real, prediction
- TODO: how characters are encoded (one-hot over neurons?) and how many characters are stored
{{< /speaker_note >}}

---

## Applications to neuroscience: encoding text

<ul style="width: 100%; margin: 0 auto; padding: 0; text-align: center; list-style-position: inside;">
  <li class="fragment"><span style="color: blue;"><i>Trigger:</i></span> —make—anything—prettier.”\n“Well, then,” the Gryphon went on, “if you don’t know what to uglify is, you _are_ a simpleton.”\nAlice did not feel encouraged to ask any more questions about it, so she turned to the Mock Turtle</li>
  <li class="fragment"><span style="color: green;"><i>Real:</i></span> and said “What else had you to learn?”\n“Well, there was Mystery,” the Mock Turtle replied, counting off the subjects on his flappers,</li>
  <li class="fragment"><span style="color: red;"><i>Prediction:</i></span> ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"</li>
</ul>

{{< speaker_note >}}
**≈ 30 s**

- a failure case: the network gets stuck repeating the same character
- the chain falls into a loop: a single polychronous group re-activating itself


This is a failure case: the network gets stuck repeating the same character. The chain falls into a loop, a single polychronous group re-activating itself.


- a loop is an attractor of the chain; it plays the role of the gap failures seen on random patterns
- TODO: how often this happens
{{< /speaker_note >}}

---

## Applications to neuroscience: encoding text

<ul style="width: 100%; margin: 0 auto; padding: 0; text-align: center; list-style-position: inside;">
  <li class="fragment"><span style="color: blue;"><i>Trigger:</i></span> one from this side of the ground.” So she tucked it away under her arm, that it might not escape again, and went back for a little more conversation with her friend.\nWhen she got back to the Cheshire Cat, she was surprised to find quite a large crowd collected round it: there was</li>
  <li class="fragment"><span style="color: green;"><i>Real:</i></span> a dispute going on between the executioner, the King, and the Queen, who were all talking at once, while all the rest were quite silent, and looked very uncomfortable.\nThe moment Alice appeared, she was appea</li>
  <li class="fragment"><span style="color: red;"><i>Prediction:</i></span> aI going on between, execution do, the King, and the Queen, who were all talking at once, while all the rest were quite silent, and looked very uncomfortable.\nThe moment Alice appeared, she was appea</li>
</ul>

{{< speaker_note >}}
**≈ 30 s**

- intermediate case: a few errors at the start, then the network recovers and continues exactly
- the chain is robust: after a perturbation, it falls back onto the stored trajectory


An intermediate case: a few errors at the start, then the network recovers and continues the text exactly. The chain is robust: after a perturbation, it falls back onto the stored trajectory.


- links with the robustness to noise seen before
- TODO: how many characters were wrong before recovery
{{< /speaker_note >}}

</section>

---

<section>

<!-- no-branding -->

## Modelling memory to understand the brain 

<ol class="outline">
  <li class="fragment"><strong>Efficient initialisation and learning</strong><span>Next:</span><ul><li>local</li><li>event-based learning</li></ul></li>
  <li class="fragment"><strong>Reservoir of memories</strong><span>Next:</span><ul><li>hierarchical</li><li>modular</li><li>multi-scale</li></ul></li>
  <li class="fragment"><strong>Applications to neuroscience</strong><span>Next:</span><ul><li>neural data</li><li>behaviour</li><li>closed loop</li></ul></li>
</ol>

{{< speaker_note >}}
**≈ 1 min 30 s**

- learning: BPTT is not realistic and compute heavy -> local, event-based learning, optimise the encoding
- reservoir of memories: could be more realistic -> hierarchical, modular, multi-scale
- applications to neuroscience: could be more advanced -> neural data, behavioural data, closed-loop experiments


To conclude: we built a working memory lasting seconds with spiking neurons that forget in milliseconds, by putting the memory in the delays, with chains of polychronous groups. There are three directions. First, learning: backpropagation through time is not realistic and is compute heavy, so we aim at local, event-based learning, and at optimising the encoding. Second, a reservoir of memories: it can be more realistic, hierarchical, modular and multi-scale. Third, applications to neuroscience, with neural data, behavioural data and closed-loop experiments.


- the key message: the memory is in the delays, not in the leak
- take-home for the discussion: capacity, biological plausibility of 41 delays per synapse, link with hippocampal sequences (Haimerl et al., 2019)
- paper: arXiv:2604.14096, code: github.com/SpikeAI/MNESIS
{{< /speaker_note >}}

---

# [Modelling memory to understand the brain](https://laurentperrinet.github.io/slides/2026-11-09-forum-numerica/?transition=fade)
## *[Laurent U Perrinet](https://laurentperrinet.github.io/talk/2026-11-09-forum-numerica/)*
### <u>Forum Numerica seminar, Université Côte d'Azur</u>
### [2026-11-09]

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)

Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

Code: [SpikeAI/MNESIS](https://github.com/SpikeAI/MNESIS) · Paper: [arXiv:2604.14096](https://arxiv.org/abs/2604.14096)

{{< speaker_note >}}
**≈ 15 s, then questions**

- thank the audience and the Forum Numerica organisers (room 007 at i3S, and the Zoom audience)
- code and paper links on the slide


Thanks for your attention! The code and the paper are linked on the slide, and I am happy to take your questions.


- have ready: capacity (M = 26 tested), failures due to gaps, link with synfire chains, hardware implementation
{{< /speaker_note >}}

</section>
