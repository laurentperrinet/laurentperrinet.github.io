---
abstract: 'Meanwhile biorthogonal wavelets got a very popular image processing tool,
  alternative multiresolution transforms have been proposed for solving some of their
  drawbacks, namely the poor selectivity in orientation and the lack of translation
  invariance due to the aliasing between subbands. These transforms are generally
  overcomplete and consequently offer huge degrees of freedom in their design. At
  the same time their optimization get a challenging task. We proposed here a log-Gabor
  wavelet transform gathering the excellent mathematical properties of the Gabor functions
  with a carefully construction to maintain the properties of the filters and to permit
  exact reconstruction. Two major improvements are proposed: first the highest frequency
  bands are covered by narrowly localized oriented filters. And second, all the frequency
  bands including the highest and lowest frequencies are uniformly covered so as exact
  reconstruction is achieved using the same filters in both the direct and the inverse
  transforms (which means that the transform is self-invertible). The transform is
  optimized not only mathematically but it also follows as much as possible the knowledge
  on the receptive field of the simple cells of the Primary Visual Cortex (V1) of
  primates and on the statistics of natural images. Compared to the state of the art,
  the log-Gabor wavelets show excellent behavior in their ability to segregate the
  image information (e.g. the contrast edges) from incoherent Gaussian noise by hard
  thresholding and to code the image features through a reduced set of coefficients
  with large magnitude. Such characteristics make the transform a promising tool for
  general image processing tasks.'
authors:
- Sylvain Fischer
- Filip Šroubek
- Laurent U Perrinet
- Rafael Redondo
- Gabriel Cristóbal
date: 2007-01-13
doi: 10.1007/s11263-006-0026-8
featured: false
grants:
- facets
links:
- name: Code
  url: https://github.com/bicv/LogGabor
- name: URL
  url: https://doi.org/10.1007/s11263-006-0026-8
publication: '*International Journal of Computer Vision*'
publication_types:
- article-journal
title: Self-Invertible 2D Log-Gabor Wavelets
tags: ["log-gabor", "primary-visual-cortex", "sparse-coding", "visual-illusions"]
categories: ["Computer Vision", "Education", "NeuroAI & Machine Learning", "Outreach & Public Engagement", "Theoretical Neuroscience", "Visual Neuroscience"]
projects: [""]
---
This library defines the set of [LogGabor](https://pythonhosted.org/LogGabor/) kernels. These are generic edge-like filters at different scales, phases and orientations. The library develops a simple method to construct a simple multi-scale linear transform.
* [Web-site](https://pythonhosted.org/LogGabor)
* [Source code](https://github.com/bicv/LogGabor/)
* logGabor filters are used in numerous computer vision applications and reaches 177 citations on [Google Scholar](https://scholar.google.com/scholar?cluster=15692697050569088559&hl=fr&as_sdt=7,39) (last updated 22/10/2021).
{{< figure src="figure1.png" width="80%" title="**Figure 1** Multiresolution schemes. (a) Schematic contours of the log-Gabor filters in the Fourier domain with 5 scales and 8 orientations (only the contours at 78% of the filter maximum are drawn). (b) The real part of the corresponding filters is drawn in the spatial domain. The two first scales are drawn at the bottom magnified by a factor of 4 for a better visualization. The different scales are arranged in rows and the orientations in columns. The low-pass filter is drawn in the upper-left part. (c) The corresponding imaginary parts of the filters are shown in the same arrangement. Note that the low-pass filter does not have imaginary part. Insets (b) and (c) show the final filters built through all the processes described in Section 2. (d) In the proposed scheme the elongation of log-Gabor wavelets increases with the number of orientations nt . Here the real parts (left column) and imaginary parts (right column) are drawn for the 3, 4, 6, 8, 10, 12 and 16 orientation schemes. (e) As a comparison orthogonal wavelet filters ‘Db4’ are shown. Horizontal, vertical and diagonal wavelets are arranged on columns (low-pass on top). (f) As a second comparison, steerable pyramid filters (Portilla et al., 2003) are shown. The arrangement over scales and orientations is the same as for the log-Gabor scheme." >}}
