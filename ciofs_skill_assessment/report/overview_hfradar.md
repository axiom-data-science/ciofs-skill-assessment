---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
---

```{code-cell}
:tags: [remove-input]

import intake
import hvplot.pandas  # noqa
import ocean_model_skill_assessor as omsa
import pandas as pd
import cmocean.cm as cmo
from IPython.display import Image, display
import cook_inlet_catalogs as cic
```

(page:overview_hfradar)=
# Overview HF Radar Data

Detailed model-data comparison page: {ref}`HF Radar model-data comparison page <page:hfradar-comparison>`

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/hfradar.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/hfradar.html).

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

[8MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/hfradar.zip)

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("hfradar"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
map = cat.metadata["map"]
maplabels = cat.metadata["maplabels"]
imatches = dd["station"].str.fullmatch("|".join(['lower-ci_system-B_2006-2007', 'upper-ci_system-A_2002-2003', 'upper-ci_system-A_2009']))
dduse = dd.loc[imatches]
ddlabelsuse = ddlabels.loc[imatches].copy()
ddlabelsuse["Station names"] = ['Lower Cook Inlet System B (2006-2007)', 'Upper Cook Inlet System A (2002-2003)', 'Upper Cook Inlet System A (2009)']
maplabels = cat.metadata["maplabels"].copy()
maplabels["text"] = "Station names"
dduse.hvplot(**cat.metadata["map"]) * ddlabelsuse.hvplot(**maplabels)
```

## Taylor Diagrams

Taylor diagrams summarize the skill of the two models in capturing the HF Radar datasets. The data has been grouped by region (Figs. {numref}`{number}<fig-hfradar_by_region_north>` and {numref}`{number}<fig-hfradar_by_region_east>`). Correlations are higher for the northward tidal component of velocity, which is most along-channel oriented for the HF Radar areas, than for the eastward component, and CIOFS Hindcast and Fresh perform similarly. The subtidal components are poorly captured by both models: low correlations for the eastward component and even lower and negative (not shown on plot) for the northward component. Skill scores are shown in the next plots for each dataset.



```{figure} ../figures/taylor_diagrams/hfradar_by_region_north.png
---
name: fig-hfradar_by_region_north
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for north-south velocity component for the full tidal signal (left) and subtidal signal (right), grouped by region of Cook Inlet, for HF Radar data.
```

```{figure} ../figures/taylor_diagrams/hfradar_by_region_east.png
---
name: fig-hfradar_by_region_east
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for east-west velocity component for the full tidal signal (left) and subtidal signal (right), grouped by region of Cook Inlet, for HF Radar data.
```

+++

## CIOFS_HINDCAST


+++

### lower-ci_system-B_2006


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_lower-ci_system-B_2006_ciofs_hindcast_tidal.png
---
name: fig-overview-hfradar-lower-ci_system-B_2006-ciofs_hindcast-tidal
---
Tidal surface currents skill score for CIOFS_HINDCAST and dataset lower-ci_system-B_2006
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_lower-ci_system-B_2006_ciofs_hindcast_subtidal.png
---
name: fig-overview-hfradar-lower-ci_system-B_2006-ciofs_hindcast-subtidal
---
Subtidal surface currents skill score for CIOFS_HINDCAST and dataset lower-ci_system-B_2006
```
````


+++

### upper-ci_system-A_2003


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2003_ciofs_hindcast_tidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2003-ciofs_hindcast-tidal
---
Tidal surface currents skill score for CIOFS_HINDCAST and dataset upper-ci_system-A_2003
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2003_ciofs_hindcast_subtidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2003-ciofs_hindcast-subtidal
---
Subtidal surface currents skill score for CIOFS_HINDCAST and dataset upper-ci_system-A_2003
```
````


+++

## CIOFS_FRESH


+++

### lower-ci_system-B_2006


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_lower-ci_system-B_2006_ciofs_fresh_tidal.png
---
name: fig-overview-hfradar-lower-ci_system-B_2006-ciofs_fresh-tidal
---
Tidal surface currents skill score for CIOFS_FRESH and dataset lower-ci_system-B_2006
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_lower-ci_system-B_2006_ciofs_fresh_subtidal.png
---
name: fig-overview-hfradar-lower-ci_system-B_2006-ciofs_fresh-subtidal
---
Subtidal surface currents skill score for CIOFS_FRESH and dataset lower-ci_system-B_2006
```
````


+++

### upper-ci_system-A_2003


+++

#### Tidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2003_ciofs_fresh_tidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2003-ciofs_fresh-tidal
---
Tidal surface currents skill score for CIOFS_FRESH and dataset upper-ci_system-A_2003
```
````

#### Subtidal



````{div} full-width                
```{figure} overview_hfradar/hfradar_upper-ci_system-A_2003_ciofs_fresh_subtidal.png
---
name: fig-overview-hfradar-upper-ci_system-A_2003-ciofs_fresh-subtidal
---
Subtidal surface currents skill score for CIOFS_FRESH and dataset upper-ci_system-A_2003
```
````
