---
authors:
- Laurent U Perrinet
date: 2023-01-23
publishDate: 2023-01-21
tags:
- Bayesian model
- neuroscience
- psychophysics

slides:
 theme: "white" # Reveal JS theme name

title: 2023-01-23_game-theory-and-the-brain

---

# Game theory and brain strategies

<img src="https://laurentperrinet.github.io/publication/perrinet-21-hasard/featured.jpg" width="50%" >

__[2023-01-23] Atelier jeu et cerveau__

<p style="color:blue;font-size:25px;">
<a href="https://laurentperrinet.github.io/talk/2023-01-23-game-theory-and-the-brain">https://laurentperrinet.github.io/talk/2023-01-23-game-theory-and-the-brain</a></p>

{{< speaker_note >}}

- Only the speaker can read these notes
- Press `S` key to view
- Photo by Naser Tamimi on Unsplash https://unsplash.com/fr/photos/yG9pCqSOrAg

{{< /speaker_note >}}

---

# Game theory and brain strategies

<img src="https://laurentperrinet.github.io/publication/perrinet-21-hasard/featured.jpg" width="80%" >

<a href="https://theconversation.com/le-jeu-du-cerveau-et-du-hasard-159388">Le jeu du cerveau et du hasard, <i>The Conversation</i></a></p>


{{< speaker_note >}}

- What is noise? The uncertainty due to noise is symbolized by dices: a throw of fair dices, even if they are optimally simulated can not be predicted: the outcome is uniformly one facet from 1 to 6,
- I am interested in vision, and uncertainty exists in different forms,
- If we consider the image, can be noise at low contrast, complexity of the object, pose of the dice,
- in this presentation, we will see different facets of noise and uncertainty, and illustrate how our brains may play with it - and delineate a theory for this game. We will also see how it may harness the noise by explicitly representing it in the neural activity.

{{< /speaker_note >}}

---

# Aleatoric noise

---

<!-- {{< figure src="https://a5huynh.github.io/img/2019/rng-example.png" title="Random points  (A)." width="49%" >}}{{< figure src="https://a5huynh.github.io/img/2019/poisson-disk-example.png" title="Random points  (B)." width="49%" >}} -->

<img src="https://a5huynh.github.io/img/2019/rng-example.png" width="70%" >
<img src="https://a5huynh.github.io/img/2019/poisson-disk-example.png" width="70%" >

[A Huynh, generating Poisson disk noise](https://a5huynh.github.io/posts/2019/poisson-disk-sampling/)

{{< speaker_note >}}

- what is noise? it exists at quantum level, but if I were to ask you to draw random points how would it look like?
- Aleatoric comes from alea, the Latin word for “dice.” Aleatoric uncertainty is the uncertainty introduced by the randomness of an event. For example, the result of flipping a coin is an aleatoric event.
- In your opinion, which of the two is the most random pattern?
- from your responses ...
- the answer is that ...


When it comes to true randomness, one of its stranger aspects is that it often behaves differently to people’s expectations. Take the two diagrams below – which one do you think is a random distribution, and which has been deliberately created/adjusted?

randomized dots
Only one of these panels shows a random distribution of dots | Source: Bully for Brontosaurus – Stephen Jay Gould

If you said the right panel, you are in good company, as this is most people’s expectation of what randomness looks like. However, this relatively uniform distribution has been adjusted to ensure the dots are evenly spread. In fact, it is the left panel, with its clumps and voids, that reflects a true random distribution. It is also this tendency for randomness to produce clumps and voids that leads to some unintuitive outcomes.

https://theconversation.com/daniel-kahneman-on-noise-the-flaw-in-human-judgement-harder-to-detect-than-cognitive-bias-160525

{{< /speaker_note >}}

---

{{< figure src="https://laurentperrinet.github.io/post/2018-09-09_artorama/featured.png" title="[Instabilité, Etienne Rey.](https://laurentperrinet.github.io/post/2018-09-09_artorama/)" width="100%" >}}

{{< speaker_note >}}

- this was for instance used by the artist Etienne Rey to generate large panels
- our perception will generate objects out of nowhere: surfaces, groups, holes...

- this explains many cognitive biases, for instance that we expect noise to have some regularity and that we wish to explain any cluster of events by some god-like divinity...

{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/) : [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure width="50%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Face-on-mars.jpg" title="[Cydonia Mensae (1976) *Viking Orbiter image*](https://fr.wikipedia.org/wiki/Cydonia_Mensae)" >}}

{{< speaker_note >}}

- going further ...

{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/) : [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure width="50%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Viking_moc_face_20m_low.png" title="[Cydonia Mensae (2007) *Mars Global Surveyor*](https://fr.wikipedia.org/wiki/Cydonia_Mensae)" >}}

{{< speaker_note >}}

- when going to the same place a few years later ...

{{< /speaker_note >}}

---

## [Visual illusions](https://laurentperrinet.github.io/publication/perrinet-19-illusions/) : [Pareidolia](https://en.wikipedia.org/wiki/Pareidolia)

{{< figure width="50%" src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/Viking_moc_face_20m_high.png" title="[Cydonia Mensae (2007) *Mars Global Surveyor*](https://fr.wikipedia.org/wiki/Cydonia_Mensae)" >}}

{{< speaker_note >}}

- the face was gone ...
- conclusion 1: information pops out from noise
- conclusion 2: further information may change the interpretation


{{< /speaker_note >}}

---

# Sequence prediction

{{< video src="https://github.com/chloepasturel/AnticipatorySPEM/raw/master/2020-03_video-abstract/Bet_eyeMvt/eyeMvt.mp4" autoplay="yes" controls="yes" >}}

{{< speaker_note >}}

- to test this in the lab, we analyzed the response of observers to a sequences of left / right moving dots
- These were presented in multiple blocks of 50 trials for which we recorded eye movements and, on a subsequent day, asked them

{{< /speaker_note >}}

---

# Sequence prediction

```

A: 👍👍👍👍🤘👍👍👍👍👍🤘👍👍👍👍🤘👍👍👍👍👍🤘👍🤘👍👍👍👍👍🤘 ?
```

```

B: 👍🤘🤘🤘👍👍👍🤘🤘👍🤘👍🤘👍👍🤘👍🤘👍👍👍🤘👍🤘👍🤘🤘🤘👍🤘 ?
```

```

C: 👍🤘🤘🤘👍🤘👍👍🤘🤘🤘🤘🤘🤘👍👍🤘👍🤘🤘🤘👍🤘👍🤘🤘🤘🤘🤘👍 ?
```

```

D: 🤘🤘🤘🤘🤘👍🤘🤘🤘👍🤘🤘🤘🤘👍🤘👍👍👍👍👍🤘👍🤘👍👍👍👍👍🤘 ?
```

{{< speaker_note >}}

- to simplify the problem, let's show these sequences as the sequence of these 2 emojis
- In sequence A, what do you think the next

- the same question could be asked in an online fashion

- in sequence B, it's certainly the same answer, yet with lower certitude

- in sequence C, you go metal 🤘

- in sequence D, it's different there is a clearly a tendance for 🤘but that it switches to 👍

- is it possible that the brain may detect such switches?

{{< /speaker_note >}}

---

# Sequence prediction


{{< figure src="https://laurentperrinet.github.io/publication/pasturel-montagnini-perrinet-20/synthesis.png" title="([Pasturel *et al*, 2020](https://laurentperrinet.github.io/publication/pasturel-montagnini-perrinet-20/))." width="70%" >}}

{{< speaker_note >}}

- to synthesize, we have a generative model

- we found the mathematically optimal problem - and found that both eye movements + bets follow the model with switches

- The aleatoric noise is transformed into a measure of knowledge = epistemic noise

{{< /speaker_note >}}


---

# Epistemic noise
<!-- 
---

# Playing with noise


{{< figure src="https://upload.wikimedia.org/wikipedia/commons/6/67/Rock-paper-scissors.svg" title="Nash equilibrium ([Rock paper scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors))." width="70%" >}}

{{< speaker_note >}}

- let's go back to game theory

- Rock paper scissors: Its French name, "Chi-fou-mi", is based on the Old Japanese words for "one, two, three" ("hi, fu, mi").

- Nash Equilibrium is a game theory concept that determines the optimal solution in a non-cooperative game in which each player lacks any incentive to change his/her initial strategy. Under the Nash equilibrium, a player does not gain anything from deviating from their initially chosen strategy, assuming the other players also keep their strategies unchanged.

- https://www.quantamagazine.org/the-game-theory-math-behind-rock-paper-scissors-20180402/

{{< /speaker_note >}}

---

{{< figure src="http://www.salemmarafi.com/wp-content/uploads/2011/10/prisoners_dilemma.jpg" title="Prisoner’s Dilemma ([Salem Marafi](http://www.salemmarafi.com/business/prisoners-dilemma/))." width="60%" >}}


{{< speaker_note >}}

- Only the speaker can read these notes
- uncertainty comes not from aleatoric noise but from not knowing: epistemic uncertainty

{{< /speaker_note >}} -->


---

# Representing uncertainty

{{< figure src="https://images.theconversation.com/files/407867/original/file-20210623-17-ai1gc3.png" title="Visual epistemic uncertainty ([Hugo Ladret](https://theconversation.com/le-jeu-du-cerveau-et-du-hasard-159388))." width="100%" >}}

{{< speaker_note >}}

- in the case of images, a local patch may have the same most likely orientation, yet with different bandwidth (textures)
- the primary visual cortex of mammals like humans is to detect orientations
- will the response be the same for both cases?

{{< /speaker_note >}}

---

# Representing uncertainty

{{< figure src="https://laurentperrinet.github.io/publication/ladret-23/featured_hubbf63d8d7d25b21f139c2f10354080fc_466086_720x2500_fit_q75_h2_lanczos_3.webp" title="Visual epistemic uncertainty ([Hugo Ladret](https://laurentperrinet.github.io/publication/ladret-23/))." width="80%" >}}


{{< speaker_note >}}

- Only the speaker can read these notes
- Press `S` key to view

{{< /speaker_note >}}

---

# Conclusion

---

# Game theory and brain strategies

<img src="https://laurentperrinet.github.io/publication/perrinet-21-hasard/featured.jpg" width="80%" >

{{< speaker_note >}}

- In face of noise, the brain plays a game
- Evolution favors not fitness but adaptability

{{< /speaker_note >}}

---

# Game theory and brain strategies

{{< figure src="https://laurentperrinet.github.io/publication/pasturel-montagnini-perrinet-20/synthesis.png" title="Aleatoric uncertainty ([Pasturel *et al*, 2020](https://laurentperrinet.github.io/publication/pasturel-montagnini-perrinet-20/))." width="70%" >}}

{{< speaker_note >}}

- The brain uses predictive coding, for instance for sequence learning

{{< /speaker_note >}}

---

# Game theory and brain strategies

{{< figure src="https://images.theconversation.com/files/407867/original/file-20210623-17-ai1gc3.png" title="Epistemic uncertainty ([Hugo Ladret](https://theconversation.com/le-jeu-du-cerveau-et-du-hasard-159388))." width="100%" >}}


{{< speaker_note >}}

- For this, it represents explictly uncertainty (epistemic noise)

{{< /speaker_note >}}


---
# Questions?

Ask info @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)

More info @ [web-site](https://laurentperrinet.github.io/slides/2023-01-23_game-theory-and-the-brain).
