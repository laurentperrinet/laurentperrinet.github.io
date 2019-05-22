+++
# Display name
name = "Angelo Franciosini"

# Username (this should match the folder name)
authors = ["angelo-franciosini"]

# Is this the primary user of the site?
superuser = false

# Role/position
role = "Phd candidate in Computational Neuroscience"

# Short bio (displayed in user profile at end of posts)
bio = "During my PhD, I focused on predictive coding in a bio-inspired neural network."

# Organizational groups that you belong to (for People widget)
#   Set this to `[]` or comment out if you are not using People widget.
user_groups = ["Alumni"]

tags = ["phd-icn"]

# List qualifications (such as academic degrees)

[[education.courses]]
  course = "Phd in Computational Neuroscience"
  institution = "Aix-Marseille Université"
  year = 2014

[[social]]
  icon = "github"
  icon_pack = "fab"
  link = "https://github.com/AngeloFranciosini"

[[social]]
  icon = "researchgate"
  icon_pack = "ai"
  link = "https://www.researchgate.net/profile/Angelo_Franciosini"

[[social]]
  icon = "twitter"
  icon_pack = "fab"
  link = "https://twitter.com/RaguDellaNonna"

[[social]]
  icon = "linkedin"
  icon_pack = "fab"
  link = "https://www.linkedin.com/in/angelo-franciosini-325900132"

+++

# Trajectories in natural images and the sensory processing of contours (PhD position, 2017 / 2021)

* Venue: Aix-Marseille Université's [Neuroschool PhD program in Neuroscience](https://laurentperrinet.github.io/project/phd-icn/) (formerly known as "Ph.D. program in Integrative and Clinical Neuroscience")

* Keywords: Vision, Neural Networks, Bio-Inspired Computer Vision, contours, learning

* Thesis director: Dr. Laurent PERRINET, Director's research unit: Institut de Neurosciences de la Timone (INT)

##  Description of the PHD thesis project

Binding the different features of objects in images is at the core of visual perception. As such, the visual system needs to detect local edges and to bind them together to form contours at a higher, more global level. A state-of-the art theory is that of the “association field”: the confidence of an edge depends on the configuration of neighboring edges. For instance it is facilitated for co-linear or co-circular edges. This process takes advantage of the statistical regularities of edges that are present in natural images. In particular, we have developed a method to quantify the association field in different classes of natural images ([Perrinet & Bednar, 2015](https://laurentperrinet.github.io/publication/perrinet-bednar-15/)). Using an [existing library](https://github.com/bicv/SparseEdges), it is possible to compute histograms of edge co-occurrences from the sparse representation of static natural images. We have already shown that these different statistics were sufficient to categorize images, for instance to know if they contain an animal or not.  At the neural level, modeling the representation of the image, such as that formed in the primary visual cortex of primates (V1), this heuristics translates to a set of rules that adapts dynamically the activity of isolated neurons representing edges into the coherent population activity of contours. '''Yet, we miss an understanding of the link between these statistics and the probabilistic rules that binds features together and how this information is dynamically encoded in V1.'''

### Objectives
In this computational neuroscience project, we will exploit our current expertise in computer vision for the statistical integration of visual of objects to translate them in the form of probabilistic predictive models for biological vision. '''Our core hypothesis is that in natural scenes, contours follow coherent trajectories and that this knowledge is integrated (learned) by the visual system to optimally inform the representation of the image.'''

###  Methods

First, we will learn the different classes of edge co-occurrences that are relevant to natural images. Using an [existing  unsupervised learning algorithm](https://github.com/bicv/SparseHebbianLearning), we will learn these as an independent components analysis. Such an algorithm extends well to a deep-learning convolutional neural network, but importantly, it will be informed by our expertise of modeling neural networks in low-level visual areas by including horizontal connectivity. We expect that relevant features will be mainly the predictable arrangements, such as co-linear or co-circular pairs of edges, but also highly surprising ones, such as T-junctions or end-stopping features. Importantly, we will be able to compare this representation with that present in higher level areas and to refine our knowledge on the representation of natural-like images. Second, we have previously found that using synthetic textures could further advance our understanding of neural computations and perception. These random synthetic textures, coined “Motion Clouds” were initially targeted to quantify the integration properties of visual motion perception ([Leon et al, 2012](https://laurentperrinet.github.io/publication/sanz-12/), [Simoncini et al, 2012](https://laurentperrinet.github.io/publication/simoncini-12/)). Informed by the generative model of edge co-occurrences studied above, an extension to such stimuli would be to include dependencies between different elements. As such, we will be able to manipulate the level of dependency between different elements, whether in space, time or feature space (orientations). A potential outcome will be to use these in neurophysiological and psychophysical experiments within the team. In particular, the ability to select different classes of dependencies learned above will make it possible to evaluate the relative contribution of each component to the association field.

### Expected results

Finally, those two tasks converge to a long-term goal of '''understanding the impact of the spatio-temporal structure of natural images in the neural computations implementing visual processing in low-level visual areas and perception'''. Indeed, the regularities observed in static images can be extended to dynamical scenes by observing that a co-occurrence in time can be implemented by simple geometrical operations as they are operated during that period. For instance a co-circularity can be described as a smooth roto-translational transformation of an edge along a smooth trajectory. Importantly, such a distinction should allow us to determine the hierarchy of different features relevant to describe the full statistics of the feature space (that is, of spatio-temporal edge co-occurrences). We expect to see that the different independent features should decompose at various scales both in space and in time. This translates into a probabilistic hierarchical model that would combine dependencies from different cues. In particular, we expect to see the emergence of differential pathways for form and motion.

### Feasibility

 The project is based on existing expertise and libraries in computer vision and computational neuroscience. The extension of this expertise to the dynamical domain will be made possible thanks to an existing collaboration ([JM Morel at ENS-Cachan](http://www.cmla.ens-cachan.fr/version-francaise/haut-de-page/annuaire/morel-jean-michel-780.kjsp), [G Peyré at ENS-Ulm](http://www.gpeyre.com)). The groundbreaking nature of the work takes advantage of the interaction with  neurophysiological and psychophysical experiments thanks to the use of synthetic textures (collaboration with F Chavane, INT; Y Fregnac, UNIC) as planned in a the parallel (approved) grant [Horizontal-V1](https://laurentperrinet.github.io/project/anr-horizontal-v1/).

### References

 * [Simoncini C, Perrinet LU, Montagnini A, Mamassian P, Masson GS (2012)](https://laurentperrinet.github.io/publication/simoncini-12/) More is not always better: dissociation between perception and action explained by adaptive gain control. Nature Neuroscience, 15:1596–1603
 * [Friston KJ, Adams RA, Perrinet LU, Breakspear M (2012)](https://laurentperrinet.github.io/publication/friston-12/) Perceptions as Hypotheses: Saccades as Experiments. Frontiers in Psychology, 3
 * [Perrinet LU, Adams RA, Friston KJ. (2014)](https://laurentperrinet.github.io/publication/perrinet-adams-friston-12/) Active inference, eye movements and oculomotor delays. Biological Cybernetics, 108(6):777-801
 * [Perrinet LU, Bednar JA (2015)](https://laurentperrinet.github.io/publication/perrinet-bednar-15/) Edge co-occurrences can account for rapid categorization of natural versus animal images. Scientific Reports, 5:11400
 * [Khoei M, Masson GS, Perrinet LU (2017)](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/) The flash-lag effect as a motion-based predictive shift. PLoS Computational Biology, 13(1):e1005068
 * we keep a bibliography on the project @ https://www.mendeley.com/community/edgetracks/
