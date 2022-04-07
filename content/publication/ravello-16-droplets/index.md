---
authors:
- Cesar U Ravello
- Maria-José Escobar
- Adrián G Palacios
- Laurent U Perrinet
date: 2016-11-07
doi: 10.5281/zenodo.5823016
featured: false
grants:
- anr-trajectory
projects:
- motion-clouds
publication: ''
publication_types:
- '3'
tags:
- Biologically Inspired Computer vision
- Image texture
- Retina
- sparse coding
title: Differential response of the retinal neural code with respect to the sparseness
  of natural images
url_pdf: https://laurentperrinet.github.io/publication/ravello-16-droplets
url_preprint: https://arxiv.org/abs/1611.06834
---

See [supplementray code](https://laurentperrinet.github.io//sciblog/posts/2017-11-21_retina_sparseness.html).
# How does the retina respond to stimuli with different sparseness?
This stimulus is generated simply using the [Motion Clouds library](https://github.com/NeuralEnsemble/MotionClouds/blob/master/MotionClouds/MotionClouds.py#L282) by defining a sparse draw of events:
```python
import numpy as np
import MotionClouds as mc
import matplotlib.pyplot as plt
# PARAMETERS
seed = 2042
np.random.seed(seed=seed)
N_sparse = 5
sparse_base = 2.e5
sparseness =  np.logspace(-1, 0, N_sparse, base=sparse_base, endpoint=True)
print(sparseness)
# TEXTON
N_X, N_Y, N_frame = 256, 256, 1
fx, fy, ft = mc.get_grids(N_X, N_Y, 1)
mc_i = mc.envelope_gabor(fx, fy, ft, sf_0=0.05, B_sf=0.025, B_theta=np.inf)
values = np.random.randn(N_X, N_Y, N_frame)
chance = np.argsort(-np.abs(values.ravel()))
chance = np.array(chance, dtype=np.float)
chance /= chance.max()
chance = chance.reshape((N_X, N_Y, N_frame))
fig, axs = plt.subplots(1, N_sparse, figsize=(fig_width, fig_width/N_sparse))
for i_ax, l0_norm in enumerate(sparseness):
    threshold = 1 - l0_norm
    mask = np.zeros_like(chance)
    mask[chance > threshold] = 1.
    im = 2*mc.rectif(mc.random_cloud(mc_i, events=mask*values))-1
    axs[i_ax].imshow(im[:, :, 0], vmin=-1, vmax=1, cmap=plt.gray())
    #axs[i_ax].text(9, 80, r'$n=%.0f\%%$' % (noise*100), color='white', fontsize=10)
    axs[i_ax].text(4, 40, r'$\epsilon=%.0e$' % l0_norm, color='white', fontsize=8)
    axs[i_ax].set_xticks([])
    axs[i_ax].set_yticks([])
plt.tight_layout()
fig.subplots_adjust(hspace = .0, wspace = .0, left=0.0, bottom=0., right=1., top=1.)
```
