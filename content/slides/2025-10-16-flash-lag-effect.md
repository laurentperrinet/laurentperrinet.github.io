---
 slides:
  # Choose a theme from https://github.com/hakimel/reveal.js#theming
  theme: white
  transition: 'fade'
  title: "Mislocalization by Design: The Flash-Lag Effect as Prediction"

# Talk start and end times. 2023-05-13-master-m-4-nc
#   End time can optionally be hidden by prefixing the line with `#`.
date: '2025-10-16'
all_day: false

# Schedule page publish date (NOT talk date).
publishDate: "2025-10-14T06:47:11+02:00"

title: 2025-10-16-flash-lag-effect

summary: Suresh Krishna's lab meeting

---
<section>

# [Mislocalization by Design<br> The Flash-Lag Effect as Prediction](https://laurentperrinet.github.io/slides/2025-10-16-flash-lag-effect/?transition=fade)
###	*[Laurent Perrinet, CNRS/AMU, Marseille, France](https://laurentperrinet.github.io)*

<table width="100%"> 
<tr>
	<th width="80%">
	<img src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/header.png" width="100%" >
	<th width="20%">
	<img src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/coverart.jpg" width="100%" >
	</th>
</tr>
</table>


###	<u>[[2025-10-16]](https://laurentperrinet.github.io/talk/2025-10-16-flash-lag-effect/) [Suresh Krishna's lab meeting](https://neuromod.univ-cotedazur.eu)</u>

Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)


{{< speaker_note >}}

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)

 Mislocalization by Design: The Flash-Lag Effect as Prediction »

Why do we sometimes misjudge where visual objects are? This talk explores how predictive processing may cause systematic perceptual mislocalizations. Indeed, the early visual system doesn't passively process information—it actively predicts the world, compensating for neural delays by extrapolating motion trajectories. Using a Bayesian computational model, I show how this predictive mechanism explains the flash-lag effect: moving objects appear ahead of flashed ones because the brain forecasts their current position while the unpredictable flash cannot be anticipated. This framework reveals that mislocalization isn't a bug but a feature of efficient visual coding. I'll discuss how these principles illuminate both biological vision and artificial visual system design, demonstrating that what we perceive as "now" is actually the brain's best prediction of the present.

{{< /speaker_note >}}

</section>


</section>

---

<section>

## Timing in the visual pathways

---

{{< figure src="../../publication/grimaldi-22-polychronies/featured.jpg" title="Ultra-rapid visual processing ([see review](https://laurentperrinet.github.io/publication/grimaldi-22-polychronies/))." width="80%" >}}

---

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/tsonga.jpg" title="Compensating visual delays ([Perrinet, Adams & Friston 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))." width="80%" >}}

---

{{< figure src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/figure-tsonga.jpg" title="Compensating visual delays ([Perrinet Adams & Friston, 2014](https://laurentperrinet.github.io/publication/perrinet-adams-friston-14/))." width="80%" >}}

---
## Travelling waves?

{{< video src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/line_motion.mp4" autoplay="yes" title="Line-motion" >}}

---

{{< video src="https://laurentperrinet.github.io/2022-01-12_NeuroCercle/figures/phi_motion.mp4" autoplay="yes" title="Phi motion" >}}

---

{{< figure src="https://raw.githubusercontent.com/laurentperrinet/2019-04-18_JNLF/master/figures/Chemla_etal2019.png" title="Suppressive travelling waves ([Chemla *et al*, 2019](https://laurentperrinet.github.io/publication/chemla-19/))." width="50%" >}}

</section>

---

<section>

## Predictive coding

---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/aperture_aperture.mp4" autoplay="yes" width="100%" >}}
<!--
---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/aperture_box.mp4" autoplay="yes" width="100%" >}} -->

---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/aperture_cube.mp4" autoplay="yes" width="300%" >}}

---

{{< figure src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/navier.svg" title="Motion-based prediction ([Perrinet *et al*, 2012](https://laurentperrinet.github.io/publication/perrinet-12-pred/))." width="80%" >}}

---

{{< figure src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/perrinet12pred_figure2.png" title="Motion-based prediction ([Perrinet *et al*, 2012](https://laurentperrinet.github.io/publication/perrinet-12-pred/))." width="61%" >}}

<!-- ---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/line-nopred_particles.mp4" autoplay="yes" >}}

---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/line_particles.mp4" autoplay="yes" >}}
 -->

---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/line_particles.mp4" autoplay="no" controls="yes" >}}

Motion-based prediction ([Perrinet *et al*, 2012](https://laurentperrinet.github.io/publication/perrinet-12-pred/)).


</section>

---

<section>

## Flash-lag effect

---

{{< video src="https://laurentperrinet.github.io/publication/perrinet-19-temps/flash_lag.mp4" autoplay="yes" >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_cartoon.jpg" width="95%" title="Flash-lag effect ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov.jpg" width="100%" title="Diagonal markov model ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

<!--
---

{{< figure src="https://journals.plos.org/ploscompbiol/article/figure/image?size=large&id=10.1371/journal.pcbi.1005068.g002" width="100%" title="Diagonal markov model ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

https://journals.plos.org/ploscompbiol/article/figure/image?size=large&id=10.1371/journal.pcbi.1005068.g002
---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov.jpg" width="95%" title="Diagonal markov" >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov_simple.jpg" width="95%" title="Diagonal markov" >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov_pull.jpg" width="95%" title="Diagonal markov (pull)" >}} -->
<!--
---


{{< video src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/blob/master/figures/PBP_flash_spatial_readout.mp4?raw=true" autoplay="yes" >}}


---


{{< video src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/blob/master/figures/PBP_dot_spatial_readout.mp4?raw=true" autoplay="yes" >}}


---


{{< video src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/blob/master/figures/MBP_flash_spatial_readout.mp4?raw=true" autoplay="yes" >}}

---


{{< video src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/blob/master/figures/MBP_dot_spatial_readout.mp4?raw=true" autoplay="yes" >}} -->

<!-- ---

{{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/PBP_spatial_readout.mp4"  autoplay="yes" >}}

Flash-lag effect: MBP ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/)).

---

{{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/MBP_spatial_readout.mp4"  autoplay="yes" >}}

Flash-lag effect: MBP ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/)). -->

---

{{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/PBP_spatial_readout.mp4"  autoplay="yes" >}}{{< video src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/MBP_spatial_readout.mp4"  autoplay="yes" >}}

Flash-lag effect: MBP ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/)).

---

{{< video src="https://laurentperrinet.github.io/sciblog/files/2016-07-07_EDP-proba/figures/positional-delay.mp4" autoplay="yes" >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE.jpg" title="Flash-lag effect ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." width="95%" >}}

<!--


---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE.jpg" width="95%" title="Qauntitative result" >}}


https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE.jpg


https://github.com/laurentperrinet/Khoei_2017_PLoSCB/blob/master/figures/MBP_dot_spatial_readout.mp4?raw=true
MBP_dot_spatial_readout.mp4
MBP_flash_spatial_readout.mp4
MBP_spatial_readout.mp4
PBP_dot_spatial_readout.mp4
PBP_flash_spatial_readout.mp4

https://github.com/laurentperrinet/Khoei_2017_PLoSCB/blob/master/figures/MBP_dot_spatial_readout.mp4?raw=true

PBP_spatial_readout.mp4


src="../../publication/khoei-masson-perrinet-17/MBP_spatial_readout.mp4" khoei-masson-perrinet-17


 create mode 100644 publication/khoei-masson-perrinet-17/MBP_spatial_readout.mp4
 create mode 100644 publication/khoei-masson-perrinet-17/PBP_spatial_readout.mp4

 -->


---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_histogram.jpg" width="95%" title="Probability distributions ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_histogram_comp.jpg" width="95%" title="Probability distributions ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}


---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_MotionReversal_MBP.jpg" width="95%" title="Motion reversal ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_MotionReversal.jpg" width="95%" title="Motion reversal (smoothed) ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}


---

{{< video src="https://laurentperrinet.github.io/publication/perrinet-19-temps/flash_lag_stop.mp4" autoplay="yes" >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_histogram.jpg" width="95%" title="Probability distributions ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}

---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_limit_cycles.jpg" width="100%" title="Limit cycles ([Khoei *et al*, 2017](https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/))." >}}
<!--
---

{{< figure src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/FLE_DiagonalMarkov_neural.jpg" width="95%" title="Diagonal neural" >}} -->



</section>

---

<section>



# [Mislocalization by Design<br> The Flash-Lag Effect as Prediction](https://laurentperrinet.github.io/slides/2025-10-16-flash-lag-effect/?transition=fade)
###	*[Laurent Perrinet, CNRS/AMU, Marseille, France](https://laurentperrinet.github.io)*

<table width="100%"> 
<tr>
	<th width="80%">
	<img src="https://laurentperrinet.github.io/publication/khoei-masson-perrinet-17/header.png" width="100%" >
	<th width="20%">
	<img src="https://github.com/laurentperrinet/Khoei_2017_PLoSCB/raw/master/figures/coverart.jpg" width="100%" >
	</th>
</tr>
</table>


###	<u>[[2025-10-16]](https://laurentperrinet.github.io/talk/2025-10-16-flash-lag-effect/) [Suresh Krishna's lab meeting](https://neuromod.univ-cotedazur.eu)</u>

Contact me @ [laurent.perrinet@univ-amu.fr](mailto:laurent.perrinet@univ-amu.fr)


{{< speaker_note >}}

![logo](https://github.com/laurentperrinet/perrinet_curriculum-vitae.tex/raw/master/logotypes/troislogos.jpg)

 Mislocalization by Design: The Flash-Lag Effect as Prediction »

Why do we sometimes misjudge where visual objects are? This talk explores how predictive processing may cause systematic perceptual mislocalizations. Indeed, the early visual system doesn't passively process information—it actively predicts the world, compensating for neural delays by extrapolating motion trajectories. Using a Bayesian computational model, I show how this predictive mechanism explains the flash-lag effect: moving objects appear ahead of flashed ones because the brain forecasts their current position while the unpredictable flash cannot be anticipated. This framework reveals that mislocalization isn't a bug but a feature of efficient visual coding. I'll discuss how these principles illuminate both biological vision and artificial visual system design, demonstrating that what we perceive as "now" is actually the brain's best prediction of the present.

{{< /speaker_note >}}

</section>