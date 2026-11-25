"""
Pearce Tectonic Granites Classifier
====================

Trace element discrimination diagrams for the tectonic setting of granites
(VAG, syn-COLG, WPG and ORG) from Pearce et al. (1984), in four variants:
Nb-Y, Ta-Yb, Rb-(Y+Nb) and Rb-(Yb+Ta).
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from pyrolite.util.classification import PearceTectonicGranites

# sphinx_gallery_thumbnail_number = 2
########################################################################################
# We'll first generate some synthetic granite trace element compositions (ppm)
# to play with:
#
rng = np.random.default_rng(49)
cols = ["Y", "Nb", "Yb", "Ta", "Rb"]

# cluster medians (ppm, illustrative only)
centres = {
    "VAG":      [25, 8, 2.5, 0.7, 100],
    "syn-COLG": [15, 10, 1.5, 2.0, 300],
    "WPG":      [80, 100, 20, 8.0, 250],
    "ORG":      [80, 8, 8, 1.0, 5],
}

frames = []
for name, mu in centres.items():
    vals = np.exp(np.log(mu) + rng.normal(0, 0.2, size=(50, len(cols))))
    frames.append(pd.DataFrame(vals, columns=cols).assign(true=name))
df = pd.concat(frames, ignore_index=True)

df["Y+Nb"] = df.Y + df.Nb
df["Yb+Ta"] = df.Yb + df.Ta
########################################################################################
# Each variant of the diagram uses a different pair of axes:
models = {
    "Nb_Y": ["Y", "Nb"],
    "Ta_Yb": ["Yb", "Ta"],
    "Rb_YNb": ["Y+Nb", "Rb"],
    "Rb_YbTa": ["Yb+Ta", "Rb"],
}

########################################################################################
# We can visualise how this chemistry corresponds to each of the diagrams:
fig, ax = plt.subplots(2, 2, figsize=(10, 9))
for a, (model, xy) in zip(ax.flat, models.items()):
    a.set_title(model)
    cm = PearceTectonicGranites(which_model=model)
    cm.add_to_axes(a, alpha=0.5, linewidth=0.5, add_labels=True)
    df[xy].pyroplot.scatter(ax=a, c="k", alpha=0.2, axlabels=False)
plt.show()
########################################################################################
# We can now classify this data according to the fields of each diagram, and
# add these as columns to the dataframe:
#
for model in models:
    df[model] = PearceTectonicGranites(which_model=model).predict(df)

########################################################################################
# We could now take the classes and use them to colorize our points for plotting
# on the diagram, or more likely, on another plot. Here the relationship to the
# diagrams is illustrated, coloring also the populated fields:
#
fig, ax = plt.subplots(2, 2, figsize=(10, 9))
for a, (model, xy) in zip(ax.flat, models.items()):
    a.set_title(model)
    cm = PearceTectonicGranites(which_model=model)
    cm.add_to_axes(
        a,
        alpha=0.5,
        linewidth=0.0,
        zorder=-2,
        add_labels=True,
        which_ids=np.unique(df[model]),
        fill=True,
        facecolor=[0.9, 0.8, 1.0],
    )
    cm.add_to_axes(a, alpha=0.5, linewidth=0.5, zorder=-1, add_labels=True)
    df[xy].pyroplot.scatter(ax=a, c=df[model], alpha=0.7, axlabels=False)
plt.show()
########################################################################################
# References & Citation
# ~~~~~~~~~~~~~~~~~~~~~
#
#   Pearce, J.A., Harris, N.B.W., and Tindle, A.G., 1984, Trace Element Discrimination Diagrams
#   for the Tectonic Interpretation of Granitic Rocks: Journal of Petrology, v. 25, p. 956–983,
#   `doi: 10.1093/petrology/25.4.956 <https://doi.org/10.1093/petrology/25.4.956>`__.

