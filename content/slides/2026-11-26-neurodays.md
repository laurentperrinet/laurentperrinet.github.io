---
title: 2026-11-26-neurodays
date: '2026-11-26T09:45:00Z'
publishDate: '2026-11-17T15:19:35Z'
authors:
- Laurent U Perrinet
categories:
- Behavioural Neuroscience
- Visual Neuroscience
tags:
- visual-illusions
projects:
- art-science
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
summary: 'Seeing, Surprising, Understanding: When Art Becomes Neuroscience'
type: slides
---

<section>

# [Seeing, Surprising, Understanding: When Art Becomes Neuroscience](https://laurentperrinet.github.io/slides/2026-11-26-neurodays/?transition=fade)
## *[Laurent U Perrinet](https://laurentperrinet.github.io/talk/2026-11-26-neurodays/)*
### <u>[NeuroDays 2026: The Art of Neuroscience](https://neurodays2026.sciencesconf.org/resource/page/id/6)</u>
### [2026-11-26]
![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)
[Art-Sciences](https://laurentperrinet.github.io/project/art-science/) / 
Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)
<!-- TODO: decide whether to add the NeuroDays logo next to the institutional logos -->

{{< speaker_note >}}
**≈ 1 min 30 s**

- welcome to Marseille; I am the local chair: thank the organising committee (PhD students of Aix-Marseille Université) for the theme "The Art of Neuroscience"
- who I am: computational neuroscience, Institut de Neurosciences de la Timone (CNRS / Aix-Marseille Université); I model vision
- session "Introduction to Art & Science": my job is to open these two days
- thesis: artistic work is a form of research
- slides + references on my web-site
- if the organisers have already welcomed everyone: skip the welcome and start at "I am Laurent Perrinet, a researcher at the Institut de Neurosciences de la Timone…"


*Good morning*, and welcome to Marseille and to the Saint-Charles campus. As the local chair, let me first thank the organising committee, PhD students of Aix-Marseille Université, for putting together these NeuroDays, and for choosing such a bold theme: "The Art of Neuroscience". I am Laurent Perrinet, a researcher at the Institut de Neurosciences de la Timone, where I build computational models of vision. My task this morning is to open the session "Introduction to Art & Science", and I will do it by defending a simple hypothesis: artistic work is a form of research. A quest for knowledge, and for surprise, that shares many features with the scientific approach, in particular when it explores our perception and our cognition. The slides and all the references are on my web-site.


- NeuroDays 2026: 2026-11-26 and 2026-11-27, Saint-Charles campus; description by the GIS Arts & Éducation: https://gisartseduc.hypotheses.org/1632
- themes of the edition: neurobiological bases of creativity, mechanisms of aesthetic perception, artistic approaches in research and science communication
{{< /speaker_note >}}

---

## Vision: Seeing, surprising, understanding


<ol class="outline">
  <li class="fragment"><strong>**Seeing**</strong><span>Vision is an active, creative process</span></li>
  <li class="fragment"><strong>**Surprising**</strong><span>Art and science both look for what defies our expectations</span></li>
  <li class="fragment"><strong>**Understanding**</strong><span>Surprises may reveal hidden mechanisms of perception</span></li>
</ol>


{{< speaker_note >}}
**≈ 1 min 30 s**

defending a simple hypothesis: artistic work is a form of research. - three words of the title = three steps

- first: classic, widely discussed works, seen from a specific angle
- second: a long-standing collaboration with Étienne Rey (Friche la Belle de Mai) focused on action and perception
- third: how this dialogue feeds back into models of vision by modelling the retinotopy of the retina and the visual cortex, and the dynamics of visual processing


The title of this talk gives its plan. Seeing: vision is not a camera, it is an active and creative process. Surprising: artists, like scientists, look for what defies our expectations. And understanding: precisely because they surprise us, these works reveal the hidden mechanisms of perception. I will first revisit a few classic, widely discussed works, and look at them from this specific angle: what do they tell us about how we see? Then I will present a long-standing collaboration with the artist Étienne Rey, at the Friche la Belle de Mai, to show in concrete terms how artistic creation and neuroscience can enter into a dialogue. And finally, I will show how this dialogue comes back to the lab, into our models of vision.


- surprise as a driving force of perception and learning: predictive coding (Rao & Ballard, 1999, Nature Neuroscience 2:79-87, doi:10.1038/4580); free energy (Friston, 2010, Nature Reviews Neuroscience 11:127-138, doi:10.1038/nrn2787)
{{< /speaker_note >}}

</section>

---

<section>

## "The unreasonable effectiveness of vision"

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/9/95/Nage_de_la_raie%2C_Marey%2C_1894.gif" title="Swimming ray, 1894 [[Étienne-Jules Marey]](https://en.wikipedia.org/wiki/%C3%89tienne-Jules_Marey)" width="100%" >}}

{{< speaker_note >}}
**≈ 1 min 30 s**

- Marey: chronophotography, a "photographic gun" to decompose movement
- scientific goal: understand movement (the ISM in Marseille bears his name)
- artistic consequence: cinema; a few poor still frames give a vivid motion
- "unreasonable effectiveness": borrowing Wigner's words about mathematics


Let me start with this swimming ray, captured in 1894 by Étienne-Jules Marey. Marey invented chronophotography: he used a device shaped like a rifle, with a photographic plate as a magazine, to "shoot" a movement that the eye cannot decompose. His goal was scientific, understanding movement, and here in Marseille the Institut des Sciences du Mouvement bears his name. But look at what happens in your head: a handful of still images, of poor quality, give you the vivid impression of a fluid motion. This is the principle of cinema. I like to call it, after Wigner's famous phrase about mathematics, the unreasonable effectiveness of vision: how can we get such a rich perception of the world from so little information? And this ability is not new.


- Marey's chronophotographic gun: 1882; the swimming ray is part of his studies of animal locomotion in water (1890s)
- Wigner (1960), *The unreasonable effectiveness of mathematics in the natural sciences*, Communications on Pure and Applied Mathematics 13:1-14, doi:10.1002/cpa.3160130102
- Institut des Sciences du Mouvement Étienne-Jules Marey (ISM), CNRS / Aix-Marseille Université
{{< /speaker_note >}}

---

{{< slide background-image="https://upload.wikimedia.org/wikipedia/commons/5/5b/18_PanneauDesLions%28PartieDroite%29BisonsPoursuivisParDesLions.jpg" >}}

{{< speaker_note >}}
**≈ 45 s**

- Chauvet: a pride of lions hunting bison
- several lions, or one lion at several instants? a "cinematographic" effect
- complicity with artists so distant in time, so close in sensitivity


Here is the Panel of the Lions in the Chauvet cave. Do we see a pride of lions hunting, or one single lion, unfolded at different instants, as in Marey's plates? Some prehistorians have argued for such cinematographic effects in cave art. In any case, what strikes me is the complicity we still share today with artists so distant in time, and yet so close in their sensitivity to motion.


- "animation" in Palaeolithic art: Azéma & Rivère (2012), *Animation in Palaeolithic art: a pre-echo of cinema*, Antiquity 86(332):316-324, doi:10.1017/s0003598x00062785
{{< /speaker_note >}}

---

## "The unreasonable effectiveness of vision"


{{< figure src="https://upload.wikimedia.org/wikipedia/commons/5/5b/18_PanneauDesLions%28PartieDroite%29BisonsPoursuivisParDesLions.jpg" title="Panel of the Lions [[Chauvet Cave, ~36 ka]](https://en.wikipedia.org/wiki/Chauvet_Cave)" width="90%" >}}

{{< speaker_note >}}
**≈ 30 s**

- tens of thousands of years old; replica (Chauvet 2) in the Ardèche
- transition: but what is this sense, vision?


These paintings are tens of thousands of years old; if you have the chance, visit the replica in the Ardèche, near Pont-de-l'Arc. But what exactly is this sense, vision?


- Chauvet cave: discovered in 1994, UNESCO World Heritage since 2014; replica "Grotte Chauvet 2" opened in 2015
{{< /speaker_note >}}

---

## "The unreasonable effectiveness of vision"

{{< figure src="https://images.theconversation.com/files/568221/original/file-20240108-17-78s0cj.png" title="How vision evolved... [[LP, 2024, The Conversation]](https://theconversation.com/chats-mouches-humains-comment-la-vision-a-evolue-en-de-multiples-facettes-220083)" width="100%" >}}

{{< speaker_note >}}
**≈ 1 min**

- eyes evolved in many forms across species
- first miracle: phototransduction, light -> electrochemical signal
- no details today: let us look at what vision does, through its "failures"


The organ of vision is the eye, and evolution has produced a striking diversity of eyes, as I described in this article for The Conversation. Everything starts with a first miracle: in the retina, light energy is transformed into an electrochemical signal, and the magic can begin. I will not go into the details, it would take hours. Instead, let us explore vision through what looks like its failures.


- Perrinet (2024), *Chats, mouches, humains : comment la vision a évolué en de multiples facettes*, The Conversation
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/)

{{< video src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Kitaoka.mp4" controls="yes" width="80%" >}}
[Illusions of brightness or lightness *Akiyoshi KITAOKA*](http://www.ritsumei.ac.jp/~akitaoka/index-e.html)

{{< speaker_note >}}
**≈ 1 min 15 s**

- Kitaoka: between science and minimal art
- not a bug but a feature: lightness is estimated relative to the context
- vision adapts to a huge range of illuminations, from moonlight to sunlight


Visual illusions. Here is a simple demonstration by Akiyoshi Kitaoka, a vision scientist whose work sits between science and minimal art. The same grey looks lighter or darker depending on its surroundings. This is not a bug, it is a feature: the brain does not measure light, it estimates the lightness of surfaces relative to their context. And this is essential, because the illumination of our world varies by many orders of magnitude, from moonlight to bright sunlight, while the objects themselves stay the same.


- illuminance: about 0.1 lux (full moon) to about 100,000 lux (direct sunlight), that is six orders of magnitude
- Adelson (2000), *Lightness perception and lightness illusions*, in The New Cognitive Neurosciences, MIT Press
- Perrinet (2019), *Illusions et hallucinations visuelles : une porte sur la perception*, The Conversation
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Hering_illusion_without.svg" title="[Hering illusion](https://en.wikipedia.org/wiki/Hering_illusion)" width="70%" >}}

{{< speaker_note >}}
**≈ 20 s**

- two parallel, straight lines


Vision can also play with geometry. Take these two lines: they are parallel and perfectly straight.
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Hering_illusion.svg" title="[Hering illusion](https://en.wikipedia.org/wiki/Hering_illusion)" width="70%" >}}

{{< speaker_note >}}
**≈ 1 min**

- in front of radiating lines, they look bent
- interpretation: the brain assumes a 3D scene (perspective, or motion towards the vanishing point)
- the illusion reveals a prior: vision creates its own interpretation


Now place them in front of this fan of radiating lines: they look bent outwards. One explanation is that the brain interprets the fan as a 3D scene, a perspective, or even a motion towards the vanishing point, and the distortions it expects in such a scene make curved lines more plausible. The illusion reveals a prior: vision does not passively record the image, it creates its most plausible interpretation.


- Hering (1861)
- perceptual compensation for neural delays: Changizi et al. (2008), *Perceiving the present and a systematization of illusions*, Cognitive Science 32(3):459-503, doi:10.1080/03640210802035191
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/): [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Face-on-mars.jpg" title="[Cydonia Mensae (1976) *Viking Orbiter image*](https://en.wikipedia.org/wiki/Cydonia_(Mars))" width="50%" >}}

{{< speaker_note >}}
**≈ 1 min**

- 1976: Viking orbiter photographs Mars
- context: since the late 19th century, "canals" and the myth of Martians
- a face, seemingly carved in the rock


This image is famous. In 1976, the Viking orbiter photographed the surface of Mars, until then only known through blurry telescope images. Since the end of the nineteenth century, some astronomers had seen "canals" on Mars, and with them the possibility of intelligent life, the "Martians". And then this image came out: a face, seemingly carved in the rock of the Cydonia region.


- Viking 1 orbiter, frame 35A72, 1976-07-25
- Schiaparelli's "canali" (1877), popularised by Percival Lowell
{{< /speaker_note >}}

<!-- 


---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/): [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Viking_moc_face_20m_low.png" title="[Cydonia Mensae (2007) *Mars Global Surveyor*](https://en.wikipedia.org/wiki/Cydonia_(Mars))" width="50%" >}}

{{< speaker_note >}}
**≈ 20 s**

- decades later, a new probe images the same terrain at higher resolution


Decades later, a new probe photographed the same terrain with a much higher resolution, revealing...
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/): [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Viking_moc_face_20m_high.png" title="[Cydonia Mensae (2007) *Mars Global Surveyor*](https://en.wikipedia.org/wiki/Cydonia_(Mars))" width="50%" >}}

{{< speaker_note >}}
**≈ 45 s**

- ... just a rock
- the brain is a machine to find meaning, even where there is none
- first lesson: surprise is the signature of the hidden assumptions of perception


... just a rock! Our brain is a machine to find meaning, and faces above all, even where there is none. More information was enough to dissolve the illusion. This is my first lesson: a surprise is the signature of a hidden assumption of our perception. And artists have played with these assumptions long before neuroscientists.


- face pareidolia activates face-selective cortex: Taubert et al. (2017), *Face pareidolia in the rhesus monkey*, Current Biology 27(16):2505-2509, doi:10.1016/j.cub.2017.06.075
{{< /speaker_note >}} 

-->


---

## What is vision for?

{{% fragment %}} 
{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_001.jpg" title="[Ilya Repin (1884) An Unexpected Visitor](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}
{{% /fragment %}}

{{< speaker_note >}}
**≈ 45 s**

- we know a little of the "how"; now the "why": what is vision for?
- Repin: a political exile returns home; the surprise in the title


We have seen that vision tries to make sense, even when there is none, by putting parts together. We know a little of the "how", but we can also ask "why": what is vision for? Here is a classic, and widely discussed, painting by Ilya Repin: a political exile returns home unannounced, and the tension in the room comes from the surprise evoked by the title.


- Repin, *They Did Not Expect Him* (1884-1888), Tretyakov Gallery, Moscow
{{< /speaker_note >}}

---

## What is vision for?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_002.jpg" title="[Yarbus (1965) An Unexpected Visitor](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}

{{< speaker_note >}}
**≈ 45 s**

- Yarbus records the eye movements of observers in front of the painting
- the eye moves, it is active; depends on species and on individuals
- structured scan paths, even in free viewing: faces attract fixations


In the 1960s, Alfred Yarbus recorded the eye movements of observers looking at this painting. First observation: the eye moves all the time, it is active. Second: even in free viewing, the scan paths are not random, they are structured, and faces attract most of the fixations.


- Yarbus (1965, Russian edition; English translation 1967), *Eye Movements and Vision*, Plenum Press
{{< /speaker_note >}}

---

## What is vision for?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_006.jpg" title="[Yarbus (1965) An Unexpected Visitor *How long?*](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}

{{< speaker_note >}}
**≈ 40 s**

- give a task: "how long has the visitor been away?"
- the scan paths change


And this structure depends on the task. If we ask the observer "How long has the visitor been away from his family?", the eye movements change: the gaze goes back and forth between the faces and the clothes.
{{< /speaker_note >}}

---

## What is vision for?

{{< figure src="https://www.cabinetmagazine.org/issues/30/cabinet_030_archibald_sasha_003.jpg" title="[Yarbus (1965) An Unexpected Visitor - *Age?*](https://www.cabinetmagazine.org/issues/30/archibald.php)" width="45%" >}}

{{< speaker_note >}}
**≈ 1 min**

- task: "give the ages of the people": the structure changes again
- we are social animals: vision finds our fellows and reads their emotions
- the painting becomes an instrument: stimulus = painting, task = question, measure = eye movements


If we ask for the ages of the people, the structure changes again, and the gaze concentrates on the faces. This shows that we are social animals: one of the main functions of vision is to find our fellow humans and to read their emotions. And notice what happened here: a classic work of art became a scientific instrument. The painting is the stimulus, the question is the task, and the eye movements are the measure.


- replication with modern eye tracking: DeAngelus & Pelz (2009), *Top-down control of eye movements: Yarbus revisited*, Visual Cognition 17(6-7):790-811, doi:10.1080/13506280902793843
- task decoding from eye movements is debated: Greene, Liu & Wolfe (2012), Vision Research 62:1-8
{{< /speaker_note >}}

---

## Art & science reveal vision in action

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/9/92/Cruz-Diez_2013_Grand_Palais_Paris_France.jpg" title="[Carlos Cruz-Diez (2013) Chromosaturation](https://en.wikipedia.org/wiki/Carlos_Cruz-Diez)" width="90%" >}}

{{< speaker_note >}}
**≈ 45 s** (optional)

- Cruz-Diez: rooms of saturated colour
- the visual system renormalises colour: adaptation made visible


Active vision is a recurring theme of kinetic art. Carlos Cruz-Diez immersed visitors in rooms saturated with a single colour. After a few minutes, the colour seems to fade, and when you move to the next room, you see its complement: the visual system constantly renormalises colour, and the artwork makes this adaptation visible.


- Cruz-Diez (1923-2019), *Chromosaturation* (first version 1965); shown at the Grand Palais in the exhibition *Dynamo* (2013)
{{< /speaker_note >}}

---

{{< slide background-video="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/Varini.mp4" background-video-loop="true" background-video-muted="true" title="Felice Varini: anamorphosis painted on architecture" >}}
<!-- TODO: this background video has no caption; add the title and year of the Varini work, and a credit -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- Varini: anamorphosis painted on architecture
- coherent from a single viewpoint only: perception depends on where we stand


Felice Varini paints on architecture shapes that only become coherent from a single viewpoint. Take one step aside, and the circle breaks into scattered fragments. Perception depends on where we stand, and this will be the thread of what follows.


- Varini (born 1952), Swiss artist working with anamorphosis in situ
{{< /speaker_note >}}

</section>

---

<section>

## When art becomes neuroscience

{{% fragment %}} 
{{< figure src="https://laurentperrinet.github.io/author/etienne-rey/avatar.jpg" title="[Étienne Rey](https://laurentperrinet.github.io/author/etienne-rey/)" width="35%" >}}
{{% /fragment %}}

{{% fragment %}}
**Hypothesis: artistic work is a form of research**
{{% /fragment %}}

<!-- TODO: insist on defending a simple hypothesis: artistic work is a form of research.  -->
<!-- DONE: the hypothesis now appears as a fragment on the slide and is restated in the note -->

{{< speaker_note >}}
**≈ 45 s**

- remind the hypothesis: artistic work is a form of research; this collaboration is the evidence
- Étienne Rey, visual artist, Friche la Belle de Mai, Marseille
- explores space and light; works in public space, galleries, festivals (Ososphère)
- we work together since the early 2010s


Remember my hypothesis: artistic work is a form of research, and this collaboration is my evidence. Let me now introduce my partner in this exploration. Étienne Rey is a visual artist based at the Friche la Belle de Mai, here in Marseille. His work explores the very notion of space: light is his main material, and his installations aim at producing shifts in perception. His works are shown in public space, in galleries, and in festivals such as the Ososphère in Strasbourg. We have been working together for more than fifteen years.


- Étienne Rey's work: http://ondesparalleles.org/ and Documents d'artistes PACA
- profile on this site: /author/etienne-rey/
{{< /speaker_note >}}

---

## When art becomes neuroscience

{{< figure src="https://ondesparalleles.org/wp-content/uploads/2014/02/cloche_fiche_a.jpg" title="[Étienne Rey (2010) Spectre audiographique](https://ondesparalleles.org/projets/cloche-spectre-audiographique-diffraction/)" width="100%" >}}
<!-- TODO: first meeting is the talk of 2010-04-14 (talk/2010-04-14-ondes-paralleles) while the site says "since 2011"; harmonise the start date -->
<!-- DONE: the note now says that it started in 2010 with this talk and that the regular collaboration dates from 2011, as on the site -->

{{< speaker_note >}}
**≈ 1 min 15 s**

- 2010: invited to talk at the opening of this work; regular collaboration since 2011
- the audio spectrum of a bell, in dichroic plates
- you move around it: vision is not passive but active


It all started in 2010, when Étienne invited me to give a talk at the opening of this work; we have worked together regularly since 2011. It is a spatio-temporal visualisation of the audio spectrum of the sound of a bell. It is made of many semi-transparent, dichroic plates, which show different colours depending on the viewing angle. As you walk around it, the sculpture changes, and its depth appears furtively. Here again, the work exists only through the movement of the viewer: vision is not a passive process, it is an active one.


- talk *Diffraction monochromatique, spectre audiographique*, 2010-04-14 (see /talk/2010-04-14-ondes-paralleles/)
{{< /speaker_note >}}

---

## Vision in action: Tropique

{{< figure src="https://ondesparalleles.org/wp-content/uploads/2014/02/tropique_fiche_b.jpg" title="[Étienne Rey, Tropique](https://ondesparalleles.org/projets/tropique-7/)" width="100%" >}}
<!-- TODO: check the technical figures in the note (six video projectors, twelve Kinects, six Raspberry Pis); the site only gives the room size (20 m x 15 m) and the team -->
<!-- DONE: the note no longer gives those figures (it says "video projectors, depth sensors, small computers"); the room size and the team match /post/2013-10-10_tropique/ -->

{{< speaker_note >}}
**≈ 1 min 15 s**

- first large project: Marseille-Provence 2013, European Capital of Culture
- a closed room filled with mist, sculpted by light and sound
- team: Étienne Rey, Wilfried Wendling (sound), engineers; residency at IMéRA
- question: how do we perceive space through vision, hearing and movement?


Our first large project was Tropique, for Marseille-Provence 2013, European Capital of Culture. Imagine a closed room, twenty metres by fifteen, filled with a mist of microscopic droplets, in which light and sound sculpt the space. The project was developed with the composer Wilfried Wendling and engineers, during a research residency at IMéRA. The scientific question was: how do we perceive space, through vision, hearing, and our own movement? Technically, it was an epic: video projectors, depth sensors, small computers, and a lot of code.


- Tropique (2013), installation in situ (France, Canada); coproduction Marseille-Provence 2013, IMéRA, GMEM, Ososphère / Quatre 4.0, Centre des arts d'Enghien-les-Bains, CNRS / INT; see /post/2013-10-10_tropique/
- code: https://github.com/NaturalPatterns/Tropique
- the site lists *Space Odyssey* (2015-2024) with Tropique: Festival Via (Maubeuge) and Exit (Créteil) in 2015, Lille 3000 (2015-2016), Korea (2016); see /post/2013-10-10_tropique/
{{< /speaker_note >}}


---

## Vision in action: Tropique

<iframe src="https://player.vimeo.com/video/66161665" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

{{< speaker_note >}}
**≈ 1 min**

- the light becomes material: blades of light in the mist
- (apologise for the video quality)


Please excuse the quality of the video. What you see are blades of light that become almost material in the mist: visitors try to touch them, to walk through them. Light, which is normally what lets us see things, becomes the thing we see.
{{< /speaker_note >}}

---

## Vision in action: Tropique

<iframe src="https://player.vimeo.com/video/56198653" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

{{< speaker_note >}}
**≈ 1 min**

- why sensors? interaction: the light responds to the visitors
- each visitor is surrounded by a luminous aura
- from an exteroceptive to an introspective experience


Why the sensors? For interaction. The light responds to the movements of the visitors: each person is surrounded by a luminous aura that follows them. The experience shifts from exteroceptive, looking at the world, to introspective, looking at the effect of one's own presence. Many visitors described it as a hallucinatory experience.
{{< /speaker_note >}}
<!-- TODO: Space Odyssey (2015-2024), listed with Tropique on the site, has no image on the site; add a slide if you have one -->
<!-- DONE: Space Odyssey is mentioned in the reference block of the Tropique note; no slide, since the site has no image of it -->

---

## Reflection: Cristal N°2

{{< figure src="https://laurentperrinet.github.io/post/2022-09-30_cristal-no2/cristal-n2-detail.jpg" title="[Étienne Rey (2014) Cristal n°2 - Arbre théorique, detail](https://laurentperrinet.github.io/post/2022-09-30_cristal-no2/)" width="70%" >}}
<!-- TODO: slide added from the works shown on the site; remove it if superfluous -->
<!-- DONE: kept (decision 2026-11-25); the note is marked "optional", so it can be skipped live -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- a fractal tree of mirrors, generated by an algorithm (rules of symmetry and proportion)
- the reflections make the tree seem infinite: does this infinite tree exist?
- a gift of the artist to the INT: you can see it in our institute


Cristal N°2, or "theoretical tree", is a fractal tree made of mirrors. An algorithm generates its branches according to rules of symmetry and proportion, and the mirrors multiply them, so that the tree seems to extend to infinity. As you move around it, you discover new reflections, and the question it asks is simple: does this infinite tree really exist? Étienne gave this work to our institute, so you can see it at the Institut de Neurosciences de la Timone.


- 2014, mirrors and wood, 134 × 91 × 21 cm; collection INT / CNRS (gift of the artist); see /post/2022-09-30_cristal-no2/
{{< /speaker_note >}}

---

{{< figure src="https://laurentperrinet.github.io/post/2016-06-02_elasticite/TRAME_Elasticité.jpg" title="[Étienne Rey, TRAME ÉLASTICITÉ](https://ondesparalleles.org/projets/trame-elasticite-vasarely/)" width="100%" >}}

{{< speaker_note >}}
**≈ 1 min 15 s**

- Trame Élasticité, 2016, Fondation Vasarely, homage to Vasarely
- 25 rotating mirror monoliths, 3 m high
- a real-time program drives the choreography: from crystalline calm to chaos


Another large collaboration: Trame Élasticité, shown in 2016 at the Fondation Vasarely, in homage to Vasarely. Twenty-five mirror monoliths, three metres high, rotate independently around their vertical axis, driven by a real-time program that we wrote together. The installation reflects the room and the visitors, multiplies the viewpoints, and its choreography moves from moments of crystalline calm to moments of chaos.


- 25 monoliths, 3 m high, 40 cm wide, on a 5 m base; Fondation Vasarely, 2016-06-02 to 2016-10-02 (exhibition *Multiplicité*); first shown at the Biennale Némo, CENTQUATRE, Paris, 2015-2016; see /post/2016-06-02_elasticite/
- code: https://github.com/NaturalPatterns/elasticite
{{< /speaker_note >}}

---

## Vision in action: TRAME ÉLASTICITÉ

<iframe src="https://player.vimeo.com/video/198189587" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

{{< speaker_note >}}
**≈ 1 min**

- an Instagram trap!
- from coherence to incoherence: the mirrors create a new material for perception


An Instagram trap, as you can imagine! But scientifically, what interests us is the transition from coherence to incoherence: when the mirrors align, the space becomes readable; when they diverge, it breaks into fragments, and the brain struggles to rebuild a coherent scene.
{{< /speaker_note >}}

---

## Perception as an emergent process

{{< figure src="https://laurentperrinet.github.io/post/2018-04-10_trames/featured.png" title="[Étienne Rey, Trames](https://laurentperrinet.github.io/post/2018-04-10_trames/)" width="72%" >}}

{{< speaker_note >}}
**≈ 1 min 15 s**

- in the lineage of Morellet: superimposed hexagonal grids
- virtual patterns emerge from the relation between the grids and our physiology
- forms found in nature (zebra coat, soap bubbles); they change with your eye movements


In the lineage of François Morellet, we experimented with superimposed grids. Elementary motifs are placed on a dense hexagonal grid, and a second grid is superimposed. What jumps to the eye is not the real motif, but virtual patterns that emerge from the relation between the physical grids and our perceptual physiology: hexagons, like in the Alhambra, three-dimensional spaces, or forms found in nature, like the coat of a zebra or a foam of soap bubbles. And notice that these forms change as you move your eyes.


- *Trame instabilité*; see /post/2018-04-10_trames/ and the essay *Formes & perception* (https://laurentperrinet.github.io/2023-01-31_formes-et-perception/)
{{< /speaker_note >}}

---

## Perception as an emergent process: Instabilité

{{< figure src="https://laurentperrinet.github.io/post/2018-09-09_artorama/instabilite-1-618.jpg" title="[Étienne Rey (2018) *Instabilité 1,618* , 100 × 100 cm](https://laurentperrinet.github.io/post/2018-09-09_artorama/)" width="50%" >}}

{{< speaker_note >}}
**≈ 45 s** (optional)

- Instabilité series: a graphical algorithm designed to make visual figures appear
- a regular field of dots; the brain builds patterns that are not printed
- forms found in nature, or in Turing's models of morphogenesis


The series Instabilité pushes this principle further. We designed together a graphical algorithm whose only goal is to make visual figures appear. What is printed is a simple field of dots, but the dimensions and the arrangement of this optical surface lead your visual system to build patterns that are not on the paper: forms that we find in nature, or in Turing's mathematical models of morphogenesis. The title of this one, 1.618, is the golden ratio.


- series shown at Art-O-Rama, Marseille, 2018 (guest artist of Mécènes du Sud); screen prints, 100 × 100 cm; see /post/2018-09-09_artorama/
- Turing (1952), *The chemical basis of morphogenesis*, Phil. Trans. R. Soc. B 237:37-72, doi:10.1098/rstb.1952.0012
{{< /speaker_note >}}

---

## Caustics: Turbulences

{{< figure src="https://laurentperrinet.github.io/post/2018-01-20_turbulences/featured.jpg" title="[Étienne Rey (2018) Turbulences](https://laurentperrinet.github.io/post/2018-01-20_turbulences/)" width="80%" >}}
<!-- TODO: slide added from the works shown on the site; remove it if superfluous (it overlaps with the Caustiques slide of the next section) -->
<!-- DONE: kept (decision 2026-11-25); the note is marked "optional", so it can be skipped live -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- caustics: the relation between water, light and air
- movement perturbs a stable optical state; the folds of light look like a floating body


With Turbulences, we started to work on caustics, these bright folds of light that you see at the bottom of a swimming pool, and that characterise the relation between water, light and air. In the installation, movement perturbs a stable optical state, and the turbulence of the luminous folds gives the illusion of a floating body.


- installation in situ, 2018, Fondation François Schneider, Wattwiller (collection of the foundation), opened 2018-10-27; see /post/2018-01-20_turbulences/
{{< /speaker_note >}}

---

## Perception as an emergent process

{{< figure src="https://laurentperrinet.github.io/post/2026-02-20_ososphere/643545855_18444436261109562_1480440487903792518_n.jpg" title="[Étienne Rey (2018-2019) Variable Density, Delaunay series, Ososphère 2026](https://laurentperrinet.github.io/post/2026-02-20_ososphere/)" width="61.8%" >}}
<!-- TODO: check the year in the caption (2025); the site dates the Variable Density series 2018-2019 and its Ososphère showing 2026-02-20 to 2026-03-08 -->
<!-- DONE: caption now gives the series dates from the site (2018-2019) and the Ososphère showing (2026), which is the source of the image -->

{{< speaker_note >}}
**≈ 1 min**

- Variable Density, Delaunay series: a graphical algorithm we designed together
- random points connected by tension rules: textures of bubbles or crystals
- shown this year at the Ososphère (Strasbourg)


How do we put the pieces of the puzzle together? In the series Variable Density, we designed together a graphical algorithm: random points are connected according to rules of tension, like in a Delaunay triangulation, and the space fills up with a texture that evokes bubbles or crystals. Where the density changes, our perception hesitates between order and disorder. This series was shown this year at the Ososphère festival in Strasbourg.


- see /post/2026-02-20_ososphere/; Ososphère, La Laiterie, Strasbourg, 2026-02-20 to 2026-03-08
{{< /speaker_note >}}


<!-- DONE: the disabled slide "Horizon faille: Sans gravité" was removed (decision 2026-11-25): its nested TODO closed the outer comment early, so its speaker note leaked onto the Variable Density slide; Densité floue is covered in the next section -->

---

## Horizon faille @ Interstice

{{< figure src="https://laurentperrinet.github.io/post/2021-10-04_interstices/featured.jpg" title="[Étienne Rey (2021) Horizon faille, festival Interstice, Caen](https://laurentperrinet.github.io/post/2021-10-04_interstices/)" width="80%" >}}
<!-- TODO: slide added from the works shown on the site; remove it if superfluous -->
<!-- DONE: kept (decision 2026-11-25); the note is marked "optional", so it can be skipped live -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- a global installation that defies gravity, in the orangery of a botanical garden
- the fault: a zone of transformation; the horizon: the threshold of vision of the landscape


Horizon faille travelled to Caen in 2021, in the orangery of the botanical garden. It is a global installation that seeks to defy gravity. The fault is a fracture, a zone of transformation from one state to another; the horizon is the intangible line that separates the earth from the sky, and that marks the threshold of our vision of the landscape.


- festival Interstice, Orangerie du jardin des plantes, Caen, 2021-10-05 to 2021-10-17; see /post/2021-10-04_interstices/
{{< /speaker_note >}}

---

## Public commissions (2026): Apparitions transitoires

{{< figure src="https://laurentperrinet.github.io/post/2026-10-24_apparitions-transitoires/featured.jpg" title="[Étienne Rey (2026) Apparitions transitoires, campus Doua, Villeurbanne (project view)](https://laurentperrinet.github.io/post/2026-10-24_apparitions-transitoires/)" width="80%" >}}
<!-- TODO: slide added from the works shown on the site; remove it if superfluous -->
<!-- DONE: kept (decision 2026-11-25); the note is marked "optional", so it can be skipped live -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- two superimposed pigment grids interact by moiré: the motif exists in neither layer
- it reconfigures with every shift of the gaze of the passers-by
- the work transposes a logic of observation: what we perceive depends on the act of observing


Our collaboration is now entering public space. Apparitions transitoires, for the Doua campus in Villeurbanne, is a pigment painting made of two superimposed grids, which interact by moiré. The motif does not exist in either layer: it emerges from their superposition, and reconfigures with every shift of the gaze of passers-by. I contributed to the algorithmic development. The work does not represent physics, but it makes us feel that what we perceive depends on the act of observing.


- pigment painting, two superimposed layers, 6 × 1.7 m and 4.1 × 1.7 m; public commission (1 % artistique), Métropole de Lyon; see /post/2026-10-24_apparitions-transitoires/
{{< /speaker_note >}}

---

## Public commissions (2026): Horizon commun

{{< figure src="https://laurentperrinet.github.io/post/2026-10-24_horizon-commun/featured.jpg" title="[Étienne Rey (2026) Horizon commun, lycée Robert Badinter, Créon (project view)](https://laurentperrinet.github.io/post/2026-10-24_horizon-commun/)" width="80%" >}}
<!-- TODO: slide added from the works shown on the site; remove it if superfluous -->
<!-- DONE: kept (decision 2026-11-25); the note is marked "optional", so it can be skipped live -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- a course of seven works in a high school
- outside: sculptures of reflection, multiplication and condensation of the landscape
- inside: six chromatic surfaces from our collaboration, on how the visual system builds images
- the gaze becomes an instrument of knowledge


The second commission, Horizon commun, is a course of seven works for a high school near Bordeaux. Outside, sculptures play with reflection, multiplication and condensation of the landscape, associated with three gestures of the gaze: crossing, traversing, observing. Inside, six chromatic surfaces, born from our collaboration, explore how the visual system builds our images of the world. For the students who walk past them every day, the gaze becomes an instrument of knowledge.


- seven works: outdoor sculptures and six *Surfaces chromatiques* (screen-printed aluminium); public commission (1 % artistique), Région Nouvelle-Aquitaine, lycée Robert Badinter, Créon; see /post/2026-10-24_horizon-commun/
{{< /speaker_note >}}

</section>

---

<section>

{{< figure src="https://laurentperrinet.github.io/post/2024-11-07_vibration-apparences/featured.jpg" width="50%" >}}
<!-- TODO: check the claim "a first for contemporary art at the Musée Granet" before saying it -->
<!-- DONE: neither the note nor the site makes this claim; do not say it -->

{{< speaker_note >}}
**≈ 45 s**

- 2024-2025: exhibition at the Musée Granet, Aix-en-Provence (CHRONIQUES biennale)
- gathers several works born from our collaboration


To bring all of this together, Étienne organised an exhibition at the Musée Granet in Aix-en-Provence, in the framework of the CHRONIQUES biennale of digital imaginaries. It gathered several works born from our collaboration, including the one on the poster that I will describe in a moment.


- *La vibration des apparences*, Musée Granet, 2024-11-08 to 2025-01-19; see /post/2024-11-07_vibration-apparences/
{{< /speaker_note >}}

---

## La vibration des apparences

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Montagne_Sainte-Victoire%2C_par_Paul_C%C3%A9zanne_108.jpg" title="[Paul Cézanne, Montagne Sainte-Victoire, 1904](https://en.wikipedia.org/wiki/Paul_C%C3%A9zanne)" width="62%" >}}

{{< speaker_note >}}
**≈ 45 s**

- the Musée Granet is Cézanne's museum
- the title of the exhibition refers to...


The Musée Granet is, in a way, Cézanne's museum, and the Montagne Sainte-Victoire is just behind it. The title of the exhibition, "the vibration of appearances", refers...
{{< /speaker_note >}}

---

## La vibration des apparences

{{< figure src="https://laurentperrinet.github.io/talk/2025-04-18-vibration-apparences/Merleau-Ponty_Sens-et-non-sens.png" title="[Merleau-Ponty, *Le Doute de Cézanne*, in *Sens et non-sens* (1948)](https://laurentperrinet.github.io/post/2024-11-07_vibration-apparences/)" width="62%" >}}
<!-- TODO: the caption links to Étienne Rey's profile; link to the text instead (Le Doute de Cézanne, in Sens et non-sens) or to the exhibition post -->
<!-- DONE: the caption now names the text and links to the exhibition post, which quotes it -->

{{< speaker_note >}}
**≈ 1 min**

- Merleau-Ponty, "Cézanne's Doubt": in daily life we ignore transient appearances to reach objects
- the painter does the opposite: he captures the vibration of appearances
- Étienne transposes this with interference: two waves reinforce or cancel


... to a text by Merleau-Ponty, "Cézanne's Doubt". In everyday life, we tend to ignore the transient appearances of things to reach the objects themselves. The painter does the opposite: he dwells on this vibration of appearances. Étienne transposes this idea with the physical concept of interference, where two superimposed waves reinforce or cancel each other. He takes motifs, shifts them, superimposes them, and lets optical interferences emerge. I will illustrate this with three of the works shown.


- Merleau-Ponty (1945), *Le Doute de Cézanne*, reprinted in *Sens et non-sens* (1948)
{{< /speaker_note >}}

---

{{< slide background-video="https://laurentperrinet.github.io/talk/2025-04-18-vibration-apparences/visite_virtuelle.mp4" background-video-loop="true" background-video-muted="true" >}}

{{< speaker_note >}}
**≈ 1 min**

- virtual tour of the two rooms of the exhibition


But let us start with a virtual tour of the two rooms of the exhibition. Notice how the works change as the camera moves: here again, the viewpoint is part of the work.
{{< /speaker_note >}}

---

{{< slide background-image="https://laurentperrinet.github.io/post/2019-06-22_ardemone/Avignon-02.jpg" height="80%" >}}
<!-- TODO: this image comes from Ardenome (Avignon, 2019); check whether Densité floue was also shown at the Musée Granet, as the note says -->
<!-- DONE: the site only documents Densité floue in Avignon (2019), so the note now says so; if it was also in the Granet rooms, say it orally -->

{{< speaker_note >}}
**≈ 1 min**

- Densité floue: high-entropy Delaunay networks
- a second layer on a glass plate 1 cm above: depth, halo, viewpoint-dependent perspective


The first work is Densité floue, here in the version shown in Avignon in 2019. It uses the Delaunay networks I just showed, with a high entropy, printed on two layers: one on the wall, and one on a glass plate one centimetre above. This tiny gap is enough to create an effect of depth and of halo, and a perspective that changes with your viewpoint.
{{< /speaker_note >}}

---

{{< figure src="https://laurentperrinet.github.io/post/2019-06-22_ardemone/Avignon-02.jpg" title="Étienne Rey (2019) Horizon faille - Densité floue - Sans gravité - une poétique de l’air à Ardenome Avignon https://www.enrevenantdelexpo.com" lightbox="true" height="80%" >}}

{{< speaker_note >}}
**≈ 30 s** (optional)

- the boundary between what is perceived and what is not


What we explore here is the boundary between what is perceived and what is not: at a distance the texture is uniform, and as you get closer, the structure appears.
{{< /speaker_note >}}

---

{{< slide background-video="https://github.com/NaturalPatterns/2020_caustiques/raw/main/iridiscence.mp4" background-video-loop="true" background-video-muted="true" >}}

{{< speaker_note >}}
**≈ 1 min 15 s**

- Caustiques: forms through transformation, a simulation of refraction
- the bottom of a swimming pool: uniform sunlight, new forms, iridescence
- forms that evolve between order and chaos


In Caustiques, we explore the notion of form through transformation. It is a simulation of refraction. Think of a swimming pool: with a mask, you look at the bottom. The sunlight is uniform, yet the surface of the water folds it into a network of bright lines, the caustics, with these iridescent colours. By changing the parameters of the simulation, we can make these forms evolve between order and chaos.


- earlier work on caustics: *Turbulences* (2018), Fondation François Schneider, Wattwiller; see /post/2018-01-20_turbulences/
- code: https://github.com/NaturalPatterns/2020_caustiques
{{< /speaker_note >}}

---

{{< slide background-image="https://laurentperrinet.github.io/talk/2025-04-18-vibration-apparences/2024-09-04_canaux_both.png" height="80%" >}}

{{< speaker_note >}}
**≈ 45 s**

- the central work, on the poster
- two hexagonal polar grids, two colours: those of supernovae (oxygen and hydrogen)


The central work is this one, the one on the poster. It consists of two hexagonal polar grids, in two colours, those of the emission lines of supernovae, oxygen and hydrogen, a wink to Vasarely's Supernovae.
{{< /speaker_note >}}

---

## La vibration des apparences

{{< figure src="https://laurentperrinet.github.io/talk/2026-01-19-art-and-science/featured.jpg" title="[Étienne Rey (2025) Polaire](https://laurentperrinet.github.io/author/etienne-rey/)" width="62%" >}}

{{< speaker_note >}}
**≈ 45 s**

- zoom: interferences, moiré patterns
- the motif is not in either grid; it emerges from their superposition


Zooming in, you can appreciate the interferences, the moiré patterns. The important point is that the motif you see is in neither of the two grids: it emerges from their superposition, in your visual system.
{{< /speaker_note >}}

---

## La vibration des apparences

```python

def retino_grid(cr, N_H, N_V, offset, size_mag, ecc_max, alpha, c1, c2, power,
                N_rho=34, N_phi=233):
    # https://laurentperrinet.github.io/sciblog/posts/2020-04-16-creating-an-hexagonal-grid.html
    phi_v, rho_v = np.meshgrid(np.linspace(0, 2*np.pi, N_phi, endpoint=False), 
                               np.linspace(0, ecc_max, N_rho+1, endpoint=True)[1:], sparse=False, indexing='xy')    
    phi_v[::2, :] += np.pi/N_phi

    offsets, colors = [-offset, offset], [c1, c2]
    for offset_, color in zip(offsets, colors):
        # convert to cartesian coordinates
        X, Y = (rho_v * np.sin(phi_v) + offset_+1)/2, (rho_v * np.cos(phi_v)+1)/2
        R = size_mag * rho_v**power / N_rho

        for x, y, r in zip(X.ravel(), Y.ravel(), R.ravel()):
            circle(cr, x, y, r)
            cr.set_source_rgba(*hue_to_rgba(color, alpha))
            cr.fill()
    return cr
c_blue, dc = 240, 60
opts = dict(N_rho=N_rho, N_phi=N_phi, N_H=N_H, N_V=N_V,
            offset=0.07, size_mag=0.3, ecc_max=0.8, alpha=0.80, 
            c1=c_blue-dc, c2=c_blue+dc)
@disp
def draw(cr, N_H=N_H, N_V=N_V): cr = retino_grid(cr, **opts)

```
<!-- TODO: the signature of retino_grid is not valid Python (arguments without defaults after N_rho=34, N_phi=233); fix it or present the snippet as pseudo-code -->
<!-- DONE: the arguments without defaults now come first, so the signature is valid Python; the calls use keywords (**opts), so they are unchanged -->

{{< speaker_note >}}
**≈ 45 s** (optional)

- my job, prosaically: writing code
- a polar grid drawn with Cairo, duplicated and shifted horizontally


My contribution is, prosaically, to write code, and here is a version of it. For the geeks: we create a polar grid, whose element size grows with eccentricity, draw it with Cairo, then duplicate it and shift the copy horizontally by a small offset. Note that this grid is exactly the retinotopic map we will meet in a minute.


- hexagonal grid: https://laurentperrinet.github.io/sciblog/posts/2020-04-16-creating-an-hexagonal-grid.html
{{< /speaker_note >}}

---

{{< slide background-video="https://laurentperrinet.github.io/talk/2025-04-18-vibration-apparences/2025-01-18_la-vibration-des-apparences.mp4" background-video-loop="true" background-video-muted="true" >}}

{{< speaker_note >}}
**≈ 1 min**

- varying the offset: the artistic experimentation
- first answer: vision puts things together, 1 + 1 > 2
- but what is it for? back to the lab


By varying this offset, we explore the space of possible works: this is the artistic experimentation, and it is very close to a parameter scan in a lab. A first answer emerges: vision is for putting things together, for creating something new, where one plus one makes more than two. But what is it for? Let us go back to the lab.
{{< /speaker_note >}}


---

{{< slide background-video="https://laurentperrinet.github.io/talk/2025-04-18-vibration-apparences/video1.mp4" background-video-loop="true" background-video-muted="true" >}}



{{< speaker_note >}}
**≈ 45 s**

- the central work, on the poster
- two hexagonal polar grids, two colours: those of supernovae (oxygen and hydrogen)


The central work is this one, the one on the poster. It consists of two hexagonal polar grids, in two colours, those of the emission lines of supernovae, oxygen and hydrogen, a wink to Vasarely's Supernovae.
{{< /speaker_note >}}

---

{{< slide background-image="https://raw.githubusercontent.com/laurentperrinet/sciblog/refs/heads/master/files/2026-07-31-pale-blue-dots.svg" height="100%" >}}

{{< speaker_note >}}
**≈ 45 s**

- made with Étienne Rey (2026): pale blue dots
- fixate one shape: it looks brighter than the others
- keep looking for a few seconds: the other shapes fade away (Troxler effect)
- it depends on the colours of the shapes and of the background, to which the fovea and the periphery are not equally sensitive
- bridge to the lab: so what is vision for, and why is it organised like this?


With Étienne, we made this image. Fixate one of the dots: it looks brighter than the others. Keep looking for a few seconds, and the others fade away: this is the Troxler effect. The colours matter, because the fovea and the periphery are not equally sensitive to them. So what is vision for, and why is it organised in this way?


- details: https://laurentperrinet.github.io/sciblog/posts/2026-07-31-pale-blue-dots.html
{{< /speaker_note >}}
<!-- DONE: speaker note written from the caption of /post/2026-11-18_intelligence-regard/ and the sciblog post -->


</section>

---

<section>

{{< slide background-video="https://laurentperrinet.github.io/talk/2025-12-12-main/50_fixation_sequence.mp4" background-video-loop="true" background-video-muted="true" >}}

{{< speaker_note >}}
**≈ 1 min 15 s**

- why saccades? a uniform retina would not need them (rabbits, mice)
- primates and many predators have a fovea: high acuity at the centre only
- simulation: information gathered over a sequence of fixations


Remember Yarbus: why do we move our eyes at all? If our retina were uniform, we would not need to; this is roughly the case of rabbits or mice. But primates, like many predators, have a foveal vision: the density of photoreceptors is highest at the centre of the visual field, and drops quickly in the periphery. We only see sharply in a tiny window, and we move it about three times a second. Here is a simulation from the lab: the reconstruction of an image from the information gathered over a sequence of fixations.


- about 3 saccades per second in natural viewing
- from the talk *A New Look for Convolutional Deep Networks* (2025-12-12); see /talk/2025-12-12-main/
{{< /speaker_note >}}

---

## What is vision for: foveal retinotopy

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/retinotopy_primate.jpg" title="[JN Jérémie, E Daucé and LP (2026)](https://laurentperrinet.github.io/publication/jeremie-25)" width="90%" >}}

{{< speaker_note >}}
**≈ 1 min**

- retinotopy: the map from the visual field to the visual cortex
- the fovea is magnified; well approximated by a log-polar map


This simulation is based on a model of retinotopy, the map that projects the visual field onto the primary visual cortex. In primates, the fovea occupies a much larger cortical area than the periphery. Mathematically, this map is well approximated by a log-polar transformation: a rotation of the image becomes a translation along one axis of the cortex, and a zoom a translation along the other.


- Schwartz (1977), *Spatial mapping in the primate sensory projection: analytic structure and relevance to perception*, Biological Cybernetics 25:181-194, doi:10.1007/bf01885636
{{< /speaker_note >}}

---

## What is vision for: foveal retinotopy

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/retinotopy_dolphin.jpg" title="[JN Jérémie, E Daucé and LP (2026)](https://laurentperrinet.github.io/publication/jeremie-25)" width="90%" >}}

{{< speaker_note >}}
**≈ 30 s**

- a great diversity of retinotopies across species (density maps)
- dolphins: one or two high-density areas per eye


Note the great diversity of retinotopies across species; we show here maps of photoreceptor density. Dolphins, for instance, may have not one but two high-density areas in each eye.
{{< /speaker_note >}}

---

## What is vision for: foveal retinotopy

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/retinotopy_hallucinations.jpg" title="[JN Jérémie, E Daucé and LP (2026)](https://laurentperrinet.github.io/publication/jeremie-25)" width="90%" >}}
<!-- TODO: the April deck mentioned "a beautiful theoretical paper" here without a reference; check that it is Bressloff et al. (2001) -->
<!-- DONE: the reference block of the note cites Bressloff et al. (2001), the standard theoretical paper on geometric hallucinations through the log-polar map (checked on Crossref); confirm it is the paper you meant in April -->

{{< speaker_note >}}
**≈ 45 s**

- we are blind to this change of precision
- it reveals itself in geometric hallucinations (migraine, drugs)


We are blind to this change of precision across the visual field. But retinotopy reveals itself in geometric hallucinations, during migraine auras or under certain drugs: simple patterns of waves in the cortex, once mapped back through the log-polar transformation, become spirals, tunnels and funnels in the visual field.


- Bressloff, Cowan, Golubitsky, Thomas & Wiener (2001), *Geometric visual hallucinations, Euclidean symmetry and the functional architecture of striate cortex*, Phil. Trans. R. Soc. B 356:299-330, doi:10.1098/rstb.2000.0769
{{< /speaker_note >}}

---

## What is vision for: foveal retinotopy

{{< figure src="https://laurentperrinet.github.io/2023-01-31_formes-et-perception/images/retinotopy.png" title="[E Rey and LP (2026) Formes & perception](https://laurentperrinet.github.io/2023-01-31_formes-et-perception/)" width="90%" >}}

{{< speaker_note >}}
**≈ 45 s**

- where art and modelling meet: essay with Étienne for a Vasarely catalogue (Nice, 2023)
- the same retinotopic grid underlies Polaire


This is where art and modelling meet. This figure comes from an essay that Étienne and I wrote for the catalogue of the exhibition "Vasarely, d'un art programmatique au numérique", in Nice in 2023. The retinotopic grid is the same as the one in Polaire: the artwork and the model share the same mathematics.


- exhibition at the Espace Culturel Départemental Lympia, Nice, 2023-06-17 to 2023-10-15
{{< /speaker_note >}}

---

## What is vision for: foveal retinotopy

{{< figure src="https://laurentperrinet.github.io/publication/jeremie-25/graphical.png" title="[JN Jérémie, E Daucé and LP (2026)](https://laurentperrinet.github.io/publication/jeremie-25)" width="90%" >}}
<!-- TODO: check the numbers of the note (80% -> 46% and 76% -> 66% under rotation, 85% vs 71% localisation) against the published version in Vision (2026) -->
<!-- DONE: checked against the preprint PDF in publication/jeremie-25 (the 66% was the Cartesian networks, not the retinotopic one; localisation is the pointing game). Not yet compared with the published version of Vision 10(2):17 -->

{{< speaker_note >}}
**≈ 1 min 15 s**

- we put a log-polar retinotopy in front of standard deep networks (ResNet)
- similar accuracy, much more robust to rotations
- localisation for free: the network is sensitive to the fixation point
- vision depends on our point of view


We tested this idea in artificial intelligence. We placed a foveated, log-polar retinotopy at the input of standard convolutional networks, and retrained them. Under the most deceptive rotation of each image, a standard ResNet drops from 82% to 46% accuracy; the retinotopic network keeps a comparable accuracy, about 76%, whatever the rotation. And, without any additional learning, the network becomes sensitive to where it fixates: the most likely fixation point falls on the object, which gives localisation almost for free. Again, vision depends on our point of view.


- Jérémie, Daucé & Perrinet (2026), *Foveated retinotopy improves classification and localization in CNNs*, Vision 10(2):17, doi:10.3390/vision10020017
- localisation (pointing game, ResNet101): 85% for the foveated CNN vs 71% for the baseline network and 79% for the Cartesian control
- figures read in the preprint of 2025-01-21 (publication/jeremie-25/jeremie-25.pdf): baseline 81.7%, 46.1% after the worst-case rotation, retinotopic minimum 76.4%
{{< /speaker_note >}}

---

{{< slide background-image="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/42_rotsnakes_main.jpg" >}}

{{< speaker_note >}}
**≈ 20 s**

- illustrated by this illusion


And this dependence on the point of view is beautifully illustrated by this illusion.
{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/)

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/42_rotsnakes_main.jpg" title="[Rotating Snakes *Akiyoshi KITAOKA*](http://www.ritsumei.ac.jp/~akitaoka/index-e.html)" width="70%" >}}

{{< speaker_note >}}
**≈ 45 s**

- Kitaoka again: the snakes rotate in the periphery, and stop where you fixate
- links the illusion to eye movements and peripheral vision


Akiyoshi Kitaoka again, a scientist and a true artist. The snakes seem to rotate in your peripheral vision, and stop wherever you fixate. The illusion is tied to the difference between central and peripheral vision, and to your own eye movements: once more, a surprise points to a mechanism.


- Kitaoka & Ashida (2003), *Phenomenal characteristics of the peripheral drift illusion*, VISION 15:261-262
- link with microsaccades: Otero-Millan, Macknik & Martinez-Conde (2012), Journal of Neuroscience 32(17):6043-6051, doi:10.1523/jneurosci.5823-11.2012
{{< /speaker_note >}}

---

{{< slide background-video="https://laurentperrinet.github.io/sciblog/files/2025-04-24-orienting-yourself-in-the-visual-flow.mp4" background-video-loop="true" background-video-muted="true" >}}

{{< speaker_note >}}
**≈ 45 s**

- generative stimuli, born from the art projects, become experimental tools
- optic flow while moving through space


How can these explorations serve neuroscience directly? The same generative tools we built for the artworks let us create controlled visual stimulations, here simulating the optic flow you experience while moving through space...


- see https://laurentperrinet.github.io/sciblog/ (post of 2025-04-24, *Orienting yourself in the visual flow*)
{{< /speaker_note >}}

---

{{< slide background-video="https://laurentperrinet.github.io/sciblog/files/2025-04-24-orienting-yourself-in-the-visual-flow-perturb.mp4" background-video-loop="true" background-video-muted="true" >}}

{{< speaker_note >}}
**≈ 45 s**

- add perturbations that force postural adaptation or eye movements


... and to add perturbations to this flow, which force a postural adaptation or eye movements. Exactly what Étienne's installations do to visitors, but now in a controlled experiment.
{{< /speaker_note >}}

---

## Art & science reveal vision in action

{{< figure src="https://laurentperrinet.github.io/author/ede-rancz/rancz_lite.png" title="[Ede Rancz, Role of neuromodulators in active perception](https://laurentperrinet.github.io/author/ede-rancz/)" height="70%" >}}

{{< speaker_note >}}
**≈ 45 s**

- with Ede Rancz (INMED): closed-loop virtual reality
- visual or motor perturbations: balance between vision and proprioception


With Ede Rancz, at the Mediterranean Institute of Neurobiology, we use such stimuli in a closed-loop virtual reality setup. By perturbing the visual flow or the motor feedback, we can study how the brain balances vision and proprioception, and how it handles a mismatch between what it predicts and what it senses.


- Ede Rancz, Institut de Neurobiologie de la Méditerranée (INMED), Marseille; see /author/ede-rancz/
{{< /speaker_note >}}

---

## Art & science reveal vision in action

{{< figure src="https://laurentperrinet.github.io/author/ede-rancz/rancz_free.png" title="[Ede Rancz, Role of neuromodulators in active perception](https://laurentperrinet.github.io/author/ede-rancz/)" height="70%" >}}
<!-- TODO: the April deck says "funded by an Arthur-Bertin grant" while the site mentions a CENTURI PhD (Hilde Langengen-Teigen); check which funding to acknowledge -->
<!-- DONE: the last slide acknowledges CENTURI, the only funding documented on the site; Arthur-Bertin is not mentioned until you confirm that it funds this project -->

{{< speaker_note >}}
**≈ 45 s**

- role of neuromodulators in active perception, in terms of predictive processing
- relevance for disorders such as schizophrenia


The question is the role of neuromodulators in active perception, in terms of predictive processing: how the brain weighs its predictions against the sensory evidence. An imbalance in this weighting is one of the hypotheses for disorders such as schizophrenia. This is a direct heir of the questions that art taught us to ask.


- PhD project co-directed with Ede Rancz: *Neuromodulatory control of predictive processing in visual cortical circuits* (CENTURI); see /post/2026-01-28_phd-position_neuromodulatory-predictive-processing/
- aberrant precision weighting in schizophrenia: Adams, Stephan, Brown, Frith & Friston (2013), *The computational anatomy of psychosis*, Frontiers in Psychiatry 4:47, doi:10.3389/fpsyt.2013.00047
{{< /speaker_note >}}

</section>

---

<section>

{{< slide background-video="https://laurentperrinet.github.io/post/2026-10-24_impermanence/A_impermanence.mp4" background-video-loop="true" background-video-muted="true" background-size="contain" background-color="#000" >}}
<!-- TODO: the videos of this slide and the next one are served from post/2026-10-24_impermanence, which is not committed yet; deploy it before the talk -->
<!-- DONE: the post is committed and pushed, and the five videos answer HTTP 200 on the site (checked 2026-11-25) -->
<!-- TODO: the post does not say whether you took part in Impermanence (only "image credit: Laurent Perrinet"); decide how you present your role -->
<!-- DONE: you are presented as the person who filmed the sculptures (decision 2026-11-25) -->

{{< speaker_note >}}
**≈ 1 min 15 s**

- last work, on show right now in Marseille: Impermanence (Étienne Rey, 2026)
- September 2023: a mountainside collapses into a Greenland fjord, weakened by global warming
- the mega-tsunami turns into a seiche: for nine days, the whole Earth vibrates at a single, perfectly regular frequency, a signal scientists first could not identify
- five water sculptures, driven by a mechatronic device; each vibration has a sonic echo; Heraclitus, *panta rhei*
- free entry at the Vieille Charité until 2026-12-13: go and see it


Let me end this journey with a work that you can see right now, a short walk from here, at the Vieille Charité, where I filmed these sculptures. It starts with an event that could have gone unnoticed. In September 2023, a mountainside, weakened by global warming, collapsed into a narrow fjord in Greenland. The resulting mega-tsunami turned into a standing wave, a seiche, sloshing back and forth in the fjord, and for nine days the whole Earth vibrated at a single, perfectly regular frequency, a signal that scientists at first could not identify. In Impermanence, Étienne Rey lets us relive this geological moment: five water sculptures, driven by a mechatronic device, constantly recompose themselves, and each vibration of their surface has a sonic echo. The title refers to Heraclitus: panta rhei, everything flows.


- *Impermanence* (2026), visual and sound installation (five water sculptures); team: Étienne Rey (visual artist), Max Bruckert (composer), Julien Réveillon and Hakim Hamdani (scientists, CORIA / INSA Rouen Normandie), Manoeuvre (construction), Sylvain Garnavault (mechatronics); project development: Oblique/s; coproduction CHRONIQUES, Station Mir, Ososphère, GMEM; see /post/2026-10-24_impermanence/
- exhibition *Souffles terrestres* (with Stéphanie Roland), Centre de la Vieille Charité, Marseille, 2026-10-24 to 2026-12-13, Tuesday to Sunday 9:00-18:00, free entry; curators Jean Paul Fourmentraux and Mathieu Vabre
- the seismic signal had a period of about 92 s: Svennevig et al. (2024), *A rockslide-generated tsunami in a Greenland fjord rang Earth for 9 days*, Science 385:1196-1205, doi:10.1126/science.adm9247
<!-- TODO: the 92 s period and the Svennevig et al. (2024) reference were cited from memory; check them -->
<!-- DONE: reference, volume, pages and DOI checked on Crossref; the abstract gives a 10.88 mHz (92 s) signal -->
{{< /speaker_note >}}

---

## Impermanence

<div class="r-stretch" style="display: flex; width: 100%; gap: 0;">
<video controls preload="none" playsinline poster="https://laurentperrinet.github.io/post/2026-10-24_impermanence/B1_impermanence.jpg" style="width: 25%; height: 100%; object-fit: cover; margin: 0;"><source src="https://laurentperrinet.github.io/post/2026-10-24_impermanence/B1_impermanence.mp4" type="video/mp4"></video>
<video controls preload="none" playsinline poster="https://laurentperrinet.github.io/post/2026-10-24_impermanence/B2_impermanence.jpg" style="width: 25%; height: 100%; object-fit: cover; margin: 0;"><source src="https://laurentperrinet.github.io/post/2026-10-24_impermanence/B2_impermanence.mp4" type="video/mp4"></video>
<video controls preload="none" playsinline poster="https://laurentperrinet.github.io/post/2026-10-24_impermanence/D_impermanence.jpg" style="width: 25%; height: 100%; object-fit: cover; margin: 0;"><source src="https://laurentperrinet.github.io/post/2026-10-24_impermanence/D_impermanence.mp4" type="video/mp4"></video>
<video controls preload="none" playsinline poster="https://laurentperrinet.github.io/post/2026-10-24_impermanence/E_impermanence.jpg" style="width: 25%; height: 100%; object-fit: cover; margin: 0;"><source src="https://laurentperrinet.github.io/post/2026-10-24_impermanence/E_impermanence.mp4" type="video/mp4"></video>
</div>

{{< speaker_note >}}
**≈ 45 s**

- click on each video to play it
- forms are born, deform and vanish: we never see the same thing twice
- transition: perception as an active process facing an unstable matter


Here are four of the sculptures, which I filmed at the Vieille Charité; I will start them one by one. Nothing is fixed: forms are born, deform and vanish in a continuous cycle where water, sound and light answer each other, so that you never see the same thing twice. Faced with such an unstable matter, our perception does what it always does: it actively builds stable forms out of a world in flux. This brings me to my conclusion.


- videos: Laurent Perrinet, *Souffles terrestres*, Vieille Charité, 2026
{{< /speaker_note >}}

</section>

---

<section>

# [Seeing, Surprising, Understanding: When Art Becomes Neuroscience](https://laurentperrinet.github.io/slides/2026-11-26-neurodays/?transition=fade)
## *[Laurent U Perrinet](https://laurentperrinet.github.io/talk/2026-11-26-neurodays/)*
### <u>[NeuroDays 2026: The Art of Neuroscience](https://neurodays2026.sciencesconf.org/resource/page/id/6)</u>
### [2026-11-26]
![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)
[Art-Sciences](https://laurentperrinet.github.io/project/art-science/) / 
Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

<small>Thanks to Étienne Rey, Jean-Nicolas Jérémie, Emmanuel Daucé and Ede Rancz, and to CENTURI for the co-supervised PhD project on predictive processing.</small>

<!-- TODO: add acknowledgements (Étienne Rey, JN Jérémie, E Daucé, E Rancz, funding) on this last slide -->
<!-- DONE: acknowledgements added above; Arthur-Bertin is not mentioned (unconfirmed funding) -->

{{< speaker_note >}}
**≈ 2 min, then questions**

- seeing: vision is active and creative
- surprising: art and science both hunt for what defies expectations
- understanding: artistic work is a form of research; the dialogue feeds both
- thanks: Étienne Rey, JN Jérémie, E Daucé, E Rancz; CENTURI
- embodied cognition (Varela); wish two inspiring days; thank you


To sum up. Seeing: vision is not a camera, it is an active and creative process, which constantly makes sense of our senses. Surprising: artists, like scientists, look for what defies our expectations, and these surprises reveal the hidden mechanisms of perception, from Kitaoka's illusions to Yarbus's eye movements. Understanding: artistic work is a form of research, and the dialogue between art and neuroscience feeds both sides; the same grid can be an artwork at the Musée Granet and the input layer of a deep network. As Francisco Varela put it, cognition is embodied: the intelligence of the gaze lies in a body that moves through the world. I thank Étienne Rey, Jean-Nicolas Jérémie, Emmanuel Daucé and Ede Rancz, as well as CENTURI, who support our work on predictive processing. I wish you two inspiring NeuroDays. Thank you, and I am happy to take your questions.


- Varela, Thompson & Rosch (1991), *The Embodied Mind: Cognitive Science and Human Experience*, MIT Press
{{< /speaker_note >}}

</section>

---

<section>

# Supplementary slides

---

## Victor Vasarely

{{< figure src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnqT-ltEk7fE-iUfHgea6HPeusGiz357ctHroJoxUxy02oXJ4U8EGbWoXPz0aEaTOtKQKNBCJ9IMsXMKBpS9ngmwWsAESV8Rrto9iM3mCBaYmRj6MiQqpyGy-uzomgMHtdXxE6QNwBqr8/s1600/fds.jpg" title="[Victor Vasarely](https://en.wikipedia.org/wiki/Victor_Vasarely)" width="100%" >}}

---

## Victor Vasarely

{{< figure src="https://upload.wikimedia.org/wikipedia/commons/1/14/Hungary_pecs_-_vasarely0.jpg" title="[Victor Vasarely (1977) Outdoor Vasarely artwork at the church of Pálos in Pécs](https://en.wikipedia.org/wiki/Victor_Vasarely)" width="100%" >}}

---

## Victor Vasarely

{{< figure src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUqb-w6zGJ8ul1sTnh0gXi2PWwDC4uNM0Ctj_XNerPS-BuJR6_ZGNsNWO8fv5fl3S5is8faHPrgSsD1f7_KR8JDxbaYlDFJQ9ZMmRQ5S1LzBxgq-qA3vDb-_spbICOqtVNExc2bHdIiNM/s320/Supernovae.jpg" title="[Victor Vasarely (1962) Supernovae](https://en.wikipedia.org/wiki/Victor_Vasarely)" width="60%" >}}

---

## Victor Vasarely

{{< figure src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_LmwCk716jFOMR8cAwmX96DUlrCFEGfgwJVp4SaDvk9AmlGiXA25N9-DViXxGW9zHE2AHBLxo1dVuHUg9TvRn2yEsmt-i_vvNX_h9rBqnnOFVqFUCbnXIPWVWtkv_tqKGcHRMzX4wUJQ/s1600/800px-FondationAix.JPG" title="[Victor Vasarely (1976) Fondation Vasarely, Aix-en-Provence](https://en.wikipedia.org/wiki/Fondation_Vasarely)" width="60%" >}}


</section>
