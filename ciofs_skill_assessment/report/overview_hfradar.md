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


[8MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/hfradar.zip)

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("hfradar"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

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
