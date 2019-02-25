+++
title = "Speed-Selectivity in Retinal Ganglion Cells is Sharpened by Broad Spatial Frequency, Naturalistic Stimuli"
date = 2019-01-25
authors = [ "Cesar U Ravello", "Laurent U Perrinet", "Maria-José Escobar", "Adrián G Palacios",]
publication_types = [ "2",]
abstract = "Motion detection represents one of the critical tasks of the visual system and has motivated a large body of research. However, it remains unclear precisely why the response of retinal ganglion cells (RGCs) to simple artificial stimuli does not predict their response to complex, naturalistic stimuli. To explore this topic, we use Motion Clouds (MC), which are synthetic textures that preserve properties of natural images and are merely parameterized, in particular by modulating the spatiotemporal spectrum complexity of the stimulus by adjusting the frequency bandwidths. By stimulating the retina of the diurnal rodent, Octodon degus with MC we show that the RGCs respond to increasingly complex stimuli by narrowing their adjustment curves in response to movement. At the level of the population, complex stimuli produce a sparser code while preserving movement information; therefore, the stimuli are encoded more efficiently. Interestingly, these properties were observed throughout different populations of RGCs. Thus, our results reveal that the response at the level of RGCs is modulated by the naturalness of the stimulus - in particular for motion - which suggests that the tuning to the statistics of natural images already emerges at the level of the retina."
publication = "*Scientific Reports*"
tags = [ "Retina", "motion-clouds", "motion detection",]
projects = [ "motion-clouds",]
url_pdf = "https://doi.org/10.1038%2Fs41598-018-36861-8"
doi = "10.1038/s41598-018-36861-8"
url_preprint = "https://doi.org/10.1038%2Fs41598-018-36861-8"
featured = true
+++





* [Press release](http://www4.cnrs-dir.fr/insb/recherche/parutions/articles2019/l-perrinet.html)

# Dès la rétine, le système visuel préfère des images naturelles

*Dans la rétine, au premier étage du traitement de l'image visuelle, on peut obtenir des représentations extrêmement fines. Une collaboration entre des chercheurs français et chiliens a permis de mettre en évidence que, dans la rétine de rongeurs, une représentation de la vitesse de l'image visuelle est précisément codée. Dans cette collaboration pluridisciplinaire, l'utilisation d'un modèle du fonctionnement de la rétine a permis de générer un nouveau type de stimuli visuels qui a révélé des résultats expérimentaux surprenants.*

{{< tweet 1092139540788244480 >}}

La rétine est la première étape du traitement visuel, aux capacités étonnantes. À la différence d'un simple capteur comme ceux qu’on trouve dans les appareils photographiques numériques, ce mince tissu neuronal est un système complexe et encore largement méconnu. Une meilleure connaissance de cette structure est essentielle pour la construction de capteurs du futur efficaces et économes -par exemple ceux qui équiperont les futures voitures autonomes- mais aussi pour mieux comprendre des pathologies comme la Déficience Maculaire Liée à l'Age (DMLA). Une des facettes méconnues de la rétine est sa capacité à détecter des mouvements et cet article permet de mieux comprendre une partie des mécanismes en jeu.

{{< tweet 1092200890377879552 >}}
{{< tweet 1092211339311923201 >}}

Conciliant modélisation et neurophysiologie, cette étude a permis de faire des prédictions sur le traitement de l'information rétinienne et en particulier de générer des textures synthétiques qui sont optimales pour ces modèles (voir film). Les enregistrements effectués sur la rétine de rongeurs diurnes Octodon degus ont ensuite permis de mesurer la sélectivité à la vitesse mais aussi de valider une nouvelle fois ces modèles en reconstruisant l'image d'entrée à partir de l'activité neurale.

Le résultat le plus inattendu est la différence de sélectivité de certaines classes de neurones rétiniens par rapport à la complexité du stimulus présenté. En effet, la représentation de la vitesse est relativement peu précise si on utilise des réseaux de lignes ("Grating"), comme cela est d'habitude réalisé dans la plupart des expériences neurophysiologiques. Au contraire, elle devient plus précise si on utilise comme signaux visuels des textures artificielles ressemblant à des nuages en mouvement ("MC Narrow"). En particulier, plus cette texture est complexe, plus la représentation est précise ("MC Broad").

{{< tweet 1091392027848294401 >}}
{{< tweet 1090452532223045632 >}}

Ces textures complexes sont plus proches des images naturellement observées et ces résultats montrent donc que dès la rétine, le système visuel est particulièrement adapté à des stimulations naturelles. Ce résultat devrait pouvoir s'étendre à des textures encore plus complexes et encore plus proches d'images naturelles, mais aussi pouvoir se généraliser à d'autres aires visuelles plus complexes, comme le cortex visuel primaire, et à d'autres espèces.

 {{< figure src="featured.jpg" title="Pour une cellule représentative, on montre ici la réponse au cours du temps sous forme d'impulsions pour différentes présentations (Trial) ainsi que la moyenne de cette réponse (Firing rate). Les différentes colonnes représentent différentes vitesses des stimulations sur la rétine. Les différentes lignes sont différentes stimulations. En bleu, une stimulation classique sous forme de réseaux de lignes (« Grating »). En vert et Orange, la réponse à une texture progressivement plus complexe (de « Mc Narrow » à « MC Broad »). Si les réponses aux différents stimulations sont en moyenne similaires, elles sont variables d’essai en essai et une analyse statistique a permis de montrer que dans la majorité des cellules, les réponses sont d'autant plus précises que la stimulation est complexe. © Cesar Ravello " >}}

{{< video src="video_perrinet.mp4" controls="yes" >}}
Cette vidéo montre les trois classes de stimulations utilisées dans cette étude. En plus des réseaux sinusoïdaux (“Grating”) qui sont classiquement utilisés en neurosciences, cette étude a utilisé des textures aléatoires (Motion Clouds (MC)) qui sont inspirées de modèles du traitement visuel. Ils permettent en particulier de manipuler des paramètres visuels critiques comme la variété de fréquences spatiales qui sont superposées: soit unique (“Grating”), fine (“MC Narrow”), soit plus large (“MC Broad”). Ces vidéos ont été directement projetées sur des rétines posées sur des grilles d’électrodes qui permettent de mesurer l’activité neurale (voir figure). © Laurent Perrinet / Cesar Ravello
