+++
title = "Learning where to look: a foveated visuomotor control model"
date = 2019-07-15T12:20:00
authors = [ "Emmanuel Daucé", "Pierre Albigès", "Laurent U Perrinet",]
publication_types = [ "1",]
featured = false
publication = "*CNS*2019 Barcelona, Spain*"
tags = [ "Active Inference", "Deep Learning", "Object localization", "Visual search", "Visuomotor control",]
projects = []
event = "CNS*2019 Barcelona, Spain"
publishDate = "2019-01-01"
url_slides = "https://SpikeAI.github.io/2019-07-15_CNS"
url_code = "https://github.com/SpikeAI/2019-07-15_CNS/"
url_pdf = "https://bmcneurosci.biomedcentral.com/articles/10.1186/s12868-019-0538-0#Sec73"
abstract = "In computer vision, the visual search task consists in extracting a scarce and specific visual information (the target) from a large and crowded visual display. This task is usually implemented by scanning the different possible target identities at all possible spatial positions, hence with strong computational load. The human visual system employs a different strategy, combining a foveated sensor with the capacity to rapidly move the center of fixation using saccades. Saccade-based visual exploration can be idealized as an inference process, assuming that the target position and category are independently drawn from a common generative process. Knowing that process, visual processing is then separated in two specialized pathways, the where pathway mainly conveying information about target position in peripheral space, and the what pathway mainly conveying information about the category of the target. We consider here a dual neural network architecture learning independently where to look and then at what to see. This allows in particular to infer target position in retinotopic coordinates, independently to its category. This framework was tested on a simple task of finding digits in a large, cluttered image. Simulation results demonstrate the benefit of specifically learning where to look before actually knowing the target category. The approach is also energy-efficient as it includes the strong compression rate performed at the sensor level, by retina and V1 encoding, which is preserved up to the action selection level, highlighting the advantages of bio-mimetic strategies with regards to traditional computer vision when computing resources are at stake."
grants = [ "spikeai",]
+++

 - download a [preliminary PDF](https://laurentperrinet.github.io/talk/2019-07-15-cns/2019-07-15-cns.pdf)
 {{< tweet 1150713758643380226 >}}
{{< figure src="https://raw.githubusercontent.com/SpikeAI/2019-07-15_CNS/master/figures/fig_intro.jpg" title="Problem setting: In generic, ecological settings, the visual system faces a tricky problem when searching for one target (from a class of targets) in a cluttered environment. **A)** It is synthesized in the following experiment: After a fixation period of 200 ms, an observer is presented with a luminous display  showing a single target from a known class (here digits) and at a random position. The display is presented for a short period of 500 ms (light shaded area in B), that is enough to perform at most one saccade (here, successful) on the potential target. Finally, the observer has to identify the digit by a keypress. **B)** Prototypical trace of a saccadic eye movement to the target position. In particular, we show the fixation window and the temporal window during which a saccade is possible (green shaded area). **C)** Simulated reconstruction of the visual information from the (interoceptive) retinotopic map at the onset of the display and after a saccade, the dashed red box indicating the visual area of the ``what'' pathway. In contrast to an exteroceptive representation (see A), this demonstrates that the position of the target has to be inferred from a degraded (sampled) image. In particular, the configuration of the display is such that by adding clutter and reducing the size of the digit, it may become necessary to perform a saccade to be able to identify the digit. The computational pathway mediating the action has to infer the location of the target \emph{before seeing it}, that is, before being able to actually identify the target's category from a central fixation. " >}}
{{< figure src="https://spikeai.github.io/2019-07-15_CNS/figures/CNS-saccade-20.png" title="Results: success" >}}
{{< figure src="https://spikeai.github.io/2019-07-15_CNS/figures/CNS-saccade-32.png" title="Results: failure to classify" >}}
{{< figure src="https://spikeai.github.io/2019-07-15_CNS/figures/CNS-saccade-47.png" title="Results: failure to locate" >}}
