+++
title = "The flash-lag effect as a motion-based predictive shift"
date = 2017-02-25
authors = [ "Mina A. Khoei", "Guillaume S Masson", "Laurent U Perrinet",]
publication_types = [ "2",]
abstract = "Due to its inherent neural delays, the visual system has an outdated access to sensory information about the current position of moving objects. In contrast, living organisms are remarkably able to track and intercept moving objects under a large range of challenging environmental conditions. Physiological, behavioral and psychophysical evidences strongly suggest that position coding is extrapolated using an explicit and reliable representation of object's motion but it is still unclear how these two representations interact. For instance, the so-called flash-lag effect supports the idea of a differential processing of position between moving and static objects. Although elucidating such mechanisms is crucial in our understanding of the dynamics of visual processing, a theory is still missing to explain the different facets of this visual illusion. Here, we reconsider several of the key aspects of the flash-lag effect in order to explore the role of motion upon neural coding of objects' position. First, we formalize the problem using a Bayesian modeling framework which includes a graded representation of the degree of belief about visual motion. We introduce a motion-based prediction model as a candidate explanation for the perception of coherent motion. By including the knowledge of a fixed delay, we can model the dynamics of sensory information integration by extrapolating the information acquired at previous instants in time. Next, we simulate the optimal estimation of object position with and without delay compensation and compared it with human perception under a broad range of different psychophysical conditions. Our computational study suggests that the explicit, probabilistic representation of velocity information is crucial in explaining position coding, and therefore the flash-lag effect. We discuss these theoretical results in light of the putative corrective mechanisms that can be used to cancel out the detrimental effects of neural delays and illuminate the more general question of the dynamical representation of spatial information at the present time in the visual pathways."
publication = "*PLoS Computational Biology*"
url_pdf = "http://dx.doi.org/10.1371/journal.pcbi.1005068"
doi = "10.1371/journal.pcbi.1005068"
url_code = "https://github.com/laurentperrinet/Khoei_2017_PLoSCB"
url_preprint = "http://dx.doi.org/10.1371/journal.pcbi.1005068"
featured = true
tags = [ "motion prediction", "Bayesian model",]
url_press = "http://www.cnrs.fr/insb/recherche/parutions/articles2017/l-perrinet.html"
projects = [ "facets-itn",]
+++





* [Press release](http://www.cnrs.fr/insb/recherche/parutions/articles2017/l-perrinet.html")


# Visual illusions: their origin lies in prediction

{{< figure src="flash_lag.gif" title="*Flash-Lag Effect.* When a visual stimulus moves along a continuous trajectory, it may be seen ahead of its veridical position with respect to an unpredictable event such as a punctuate flash. This illusion tells us something important about the visual system: contrary to classical computers, neural activity travels at a relatively slow speed. It is largely accepted that the resulting delays cause this perceived spatial lag of the flash. Still, after several decades of debates, there is no consensus regarding the underlying mechanisms." >}}

**Researchers from the Timone Institute of Neurosciences bring a new theoretical hypothesis on a visual illusion discovered at the beginning of the 20th century. This illusion remained misunderstood while it poses fundamental questions about how our brains represent events in space and time. This study published on January 26, 2017 in the journal PLOS Computational Biology, shows that the solution lies in the predictive mechanisms intrinsic to the neural processing of information.**

{{< tweet 829354100273745920 >}}

Visual illusions are still popular: in a quasi-magical way, they can make objects appear where they are not expected... They are also excellent opportunities to question the constraints of our perceptual system. Many illusions are based on motion, such as the flash-lag effect. Observe a luminous dot that moves along a rectilinear trajectory. If a second light dot is flashed very briefly just above the first, the moving point will always be perceived in front of the flash while they are vertically aligned.

Processing visual information takes time and even if these delays are remarkably short, they are not negligible and the nervous system must compensate them. For an object that moves predictably, the neural network can infer its most probable position taking into account this processing time. For the flash, however, this prediction can not be established because its appearance is unpredictable. Thus, while the two targets are aligned on the retina at the time of the flash, the position of the moving object is anticipated by the brain to compensate for the processing time: it is this differentiated treatment that causes the flash-lag effect.

The researchers show that this hypothesis also makes it possible to explain the cases where this illusion does not work: for example if the flash appears at the end of the moving dot's trajectory or if the target reverses its path in an unexpected way. In this work, the major innovation is to use the accuracy of information in the dynamics of the model. Thus, the corrected position of the moving target is calculated by combining the sensory flux with the internal representation of the trajectory, both of which exist in the form of probability distributions. To manipulate the trajectory is to change the precision and therefore the relative weight of these two information when they are optimally combined in order to know where an object is at the present time. The researchers propose to call parodiction (from the ancient Greek paron, the present) this new theory that joins Bayesian inference with taking into account neuronal delays.

Despite the simplicity of this solution, parodiction has elements that may seem counter-intuitive. Indeed, in this model, the physical world is considered "hidden", that is to say, it can only be guessed by our sensations and our experience. The role of visual perception is then to deliver to our central nervous system the most likely information despite the different sources of noise, ambiguity and time delays. According to the authors of this publication, the visual treatment would consist in a "simulation" of the visual world projected at the present time, even before the visual information can actually modulate, confirm or cancel this simulation. This hypothesis, which seems to belong to "science fiction", is being tested with more detailed and biologically plausible hierarchical neural network models that should allow us to better understand the mysteries underlying our perception. Visual illusions have still the power to amaze us!

{{< tweet 829474896023474176 >}}
