---
authors:
- jean-nicolas-jeremie
bio: During my PhD, I am focusing on ultra-fast processing in event-based neural networks.
education:
  courses:
  - course: Phd candidate in Computational Neuroscience
    institution: Aix-Marseille Université
    year: 2024
  - course: Master in Neuroscience
    institution: Aix-Marseille Université
    year: 2021
title: Jean-Nicolas Jérémie
role: Phd candidate in Computational Neuroscience
social:
- icon: github
  icon_pack: fab
  link: https://github.com/JNJER/
- icon: twitter
  icon_pack: fab
  link: https://twitter.com/JnJerem
- icon: linkedin
  icon_pack: fab
  link: https://www.linkedin.com/in/jeremie-jean-nicolas-91306a1a1/
superuser: false
user_groups:
- Current Students
---

# PhD Student (2021-10 / 2024-09): Bio-mimetic agile aerial robots flying in real-life conditions

 * this fellowship is part of the [AgileNeuRobot project](https://laurentperrinet.github.io/grant/anr-anr/)
 * Institut des Neurosciences de la Timone, Aix-Marseille Université / CNRS

* Thesis direction: [Laurent Perrinet](https://laurentperrinet.github.io/author/laurent-u-perrinet/) and co-direction: [Emmanuel Daucé](https://laurentperrinet.github.io/author/emmanuel-dauce/)

{{< figure src="/grant/anr-anr/event_driven_computations.png" title="A miniature, event-based ATIS sensor. Contrary to a classical frame-based camera for which a full dense image representation is given at discrete, regularly spaced timings, the event-based camera provides with events at the micro-second resolution. These are sparse as they represent luminance increments or decrements (ON and OFF events, respectively)." numbered="true" >}}


## Projet #1 : 'Fast & Curious': Modèles ultra-rapides de recherche visuelle
## Project #1 : *'Fast & Curious': Models for ultra-fast visual search*

###  Mots clés - Keywords

> recherche visuelle, vision active, apprentissage profond, neurosciences computationnelles, comportement, sacades
> *visual search, active vision, deep learning, computational neuroscience, behavior, sacades*

###  Description de la problématique de recherche - Project description

La détection d'informations visuelles pertinentes dans une image nécessite un traitement ultra-rapide couvrant l'ensemble du champ visuel. Ces tâches comprennent, par exemple, les décisions concernant la présence ou non d'un animal dans la scène, ou la présence de proies ou de prédateurs. Il a été démontré qu'un tel traitement ultra-rapide est effectivement à l'œuvre, notamment dans le système visuel des primates (Thorpe et al., 1996) avec des réponses motrices de l'ordre de 150 ms chez l'homme (Kirchner et Thorpe, 2006). Une application de ces principes neuroscientifiques peut être établie en ce qui concerne la vision par ordinateur et appliquée en particulier aux systèmes embarqués tels que les robots aériens. Un drone, par exemple, doit être capable de distinguer une cible d'un obstacle, une tâche qui est actuellement impossible avec une latence rapide (Gallego et al., 2019). Cependant, avec le changement de paradigme provoqué par la nouvelle révolution de l'intelligence artificielle, et en particulier l'apprentissage profond, nous avons accès à de nouveaux outils et méthodes. Il est relativement facile de localiser des objets d'une certaine catégorie dans une image et donc de sélectionner un endroit par rapport à un autre. On peut citer par exemple les modèles VGG sur les bases de données Imagenet et sur les techniques de localisation telles que YOLO ou SSD. Cependant, ces techniques nécessitent l'utilisation d'infrastructures lourdes de type GPU qui sont difficilement transposables aux calculs embarqués. De plus, ces techniques sont basées sur le traitement statique des images alors que la plupart des flux naturels sont dynamiques et peuvent changer rapidement. Le but de la thèse est de développer de nouveaux algorithmes bio-mimétiques de recherche visuelle ultra-rapide.

*Detecting relevant visual information in an image requires ultra-fast processing covering the entire visual field. These tasks include, for example, decisions about the presence or absence of an animal in the scene, or the presence of prey or predators. It has been shown that such ultra-fast processing is indeed at work, particularly in the visual system of primates (Thorpe et al., 1996) with motor responses of the order of 150 ms in humans (Kirchner and Thorpe, 2006). An application of these neuroscience principles can be established with respect to computer vision and applied in particular to embedded systems such as aerial robots. A drone, for example, must be able to distinguish a target from an obstacle, a task that is currently impossible with rapid latency (Gallego et al., 2019). However, with the paradigm shift brought about by the new artificial intelligence revolution, and in particular deep learning, we have access to new tools and methods. It is relatively easy to locate objects of a certain category in an image and thus to select one location relative to another. Examples are the VGG models on Imagenet databases and localization techniques such as YOLO or SSD. However, these techniques require the use of heavy GPU-type infrastructures that are difficult to transpose to on-board calculations. Moreover, these techniques are based on static image processing whereas most natural flows are dynamic and can change rapidly. The goal of the thesis is to develop new bio-mimetic algorithms for ultra-fast visual search.*

###  Thématique / Domaine / Contexte

Pour résoudre ce problème vision par ordinateur, les neurosciences offrent de nouvelles perspectives autour d'une approche générique de vision active. En effet le fonctionnement du système visuel des mammifères repose sur une rétine non homogène (fovéale) souligne l’importance du traitement central de l'information visuelle. L’identité des objets dans l’environnement semble en effet nécessiter un centrage précis, réalisé à l’aide de saccades oculaires vers des cibles visuelles. Ce centrage nécessite un double traitement qui, d’un côté, traite la totalité du champ visuel périphérique pour localiser les cibles visuelles potentielles (voie du Where), et de l’autre analyse de manière détaillée le contenu visuel situé au centre de la rétine (voie du What) - (Daucé & Perrinet, 2020). La localisation des cibles périphériques et l’identification du champ visuel central sont donc deux tâches distinctes, mais complémentaires, qui doivent être combinées pour analyser de manière efficace l’ensemble de la scène visuelle sous les contraintes de ressources fortes communes aux systèmes biologiques et aux robots.

Le domaine de la thèse croise donc vision par ordinateur, apprentissage machine (deep learning), apports de la psychophysique expérimentale et de la neurophysiolgie du système visuel.

Un aspect crucial de la thèse est le traitement central dû à l’organisation log-polaire du champ visuel primaire. Celle-ci est constituée d'une organisation radiale avec forte densité de capteurs visuels au centre et très faible densité à la périphérie, codage que l’on retrouve des aires primaires jusqu’aux aux aires oculomotrices. Il est montré qu’une telle disposition spatiale des champs récepteurs permet une meilleure invariance de la réponse aux changements d’échelle (zoom) et à la rotation subjective (tilt) des objets de l'environnement.

### Objectifs
Tous ces caractéristiques combinées du traitement visuel des mammifères se distinguent fortement des approches classiques de la vision artificielle, basées sur une analyse uniforme des pixels de la scène visuelle et de nombreuses couches de convolution. Le but est donc de montrer que dans le cas d’un traitement visuel à large champ, en environnement dynamique, et sous des contraintes matérielles et énergétiques fortes, un traitement visuel qui combine recherche de cibles et traitement central log-polaire optimise le traitement des données visuelles (via une invariance native à la translation, au zoom et au tilt), tout en atteignant des capacités de reconnaissance égales, voire supérieures à celles des algorithme de vision artificielle traditionnels. Méthode Nous allons développer un modèle de recherche visuelle ultra-rapide en étendant un modèle existant basé sur le deep learning et appliqué à un flux d'images naturelles. La première contrainte que nous allons inclure est la transformation de l'entrée visuelle en une entrée log-polaire afin que la réduction de volume de données permette à cet algorithmique neuro-mimétique de fonctionner sur une carte de calcul embarquée (de type Jetson JTX2). En étendant un algorithme précédent (Daucé & Perrinet, 2020 September) à une tâche écologique (détecter la présence d'un animal ou d'une classe arbitraire d'objet), nous allons créer un système capable de produire une séquence de saccades. À chaque saccade sera associée une détection en vision centrale ainsi que la précision assignée à cette détection.

### Objectifs de valorisation des travaux de recherche du doctorant : diffusion, publication et confidentialité, droit à la propriété intellectuelle,...

Nous anticipons donc des retombées de ce genre d'étude dans le domaine de la vision par ordinateur mais aussi en neurosciences.

Tout d'abord, cet algorithme sera capable d'analyser un flux d'images en temps réel et notamment des flux videos. On peut prévoir des applications en notamment pour anticiper des scènes prédéfinies (comme celles potentiellement dangereuses pour un jeune public) ou en robotique pour piloter un drone de façon autonome, par exemple pour intercepter une cible ou éviter des obstacles. Ce genre d'applications sera construit en coopération avec le consortium réunit autour de l'ANR AgileNeuRobot (2021/2024, <https://laurentperrinet.github.io/grant/anr-anr/>).

Les résultats attendus relatifs aux neurosciences sont nombreux. Tout d'abord nous attendons acquérir une meilleure compréhension des mécanismes pré attentifs, notamment la prédiction des scanpaths oculaire (chemin de recherche visuelle des yeux sur l'image) mais aussi inversement de pouvoir décoder la tache visuelle depuis ce même scanpath. Ces modèles permettront notamment la génération de stimuli optimisés par rapport aux taches afin de mieux quantifier la réponse comportementale (collaboration Valérie Goffaux, UC Louvain). Ces stimuli pourront être notamment être utilisés en neurophysiologie et nous développons actuellement un générateur de paréidolie basés sur l'inversion des réseaux de catégorisation. Classiquement, différentes taches visuelles cognitives sont associées à différents chemins anatomiques distincts (par exemple voie dorsale versus ventrale). Notre modélisation permettra de mettre en évidence les conditions nécessaire à l'émergence de différentes voies de traitement et ainsi une meilleure description du fonctionnement macroscopique du système visuel. Ces méthodes pourront avantageusement être reliées au traitement dans d'autres modalités (comme la vocalisation telle qu'elle est étudiée dans l'équipe Banco @ INT). Collaborations envisagées C Casanova (UdeM, Canada), N Priebe (Austin, USA). Ouverture Internationale: Le projet APROVIS3D fait intervenir une collaboration en Europe (Grèce, Suisse, Espagne).

### Références bibliographiques

 * Thorpe, S., Fize, D., & Marlot, C. (1996). Speed of processing in the human visual system. Nature, 381 (6582), 520-522.\
 * Kirchner, H., & Thorpe, S. J. (2006). Ultra-rapid object detection with saccadic eye movements: Visual processing speed revisited. Vision research, 46(11), 1762-1776.\
 * Daucé, E., Albiges, P., & Perrinet, L. U. (2020). A dual foveal-peripheral visual processing model implements efficient saccade selection. Journal of Vision, 20(8), 22-22. <https://hal.archives-ouvertes.fr/hal-02947410/>\
 * Daucé, E., & Perrinet, L. (2020, September). Visual Search as Active Inference. In International Workshop on Active Inference (pp. 165-178). Springer, Cham. <https://hal.archives-ouvertes.fr/hal-03084758/>\
 * Gallego, G., Delbruck, T., Orchard, G., Bartolozzi, C., Taba, B., Censi, A., ... & Scaramuzza, D. (2019). Event-based vision: A survey. arXiv preprint arXiv:1904.08405.
