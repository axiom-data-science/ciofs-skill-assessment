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

# Moorings (KBNERR): Lower Cook Inlet Mooring

* moorings_kbnerr

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_kbnerr.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_kbnerr.html).

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_kbnerr"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## Deployment1


+++

### Sea water salinity: tidally-filtered

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_hindcast/moorings_kbnerr_Deployment1_salt_subtidal.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_fresh/moorings_kbnerr_Deployment1_salt_subtidal.png
---
name: 
---

```
````


+++

### Sea water salinity: 

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_hindcast/moorings_kbnerr_Deployment1_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_fresh/moorings_kbnerr_Deployment1_salt.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_hindcast/moorings_kbnerr_Deployment1_temp_subtidal.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_fresh/moorings_kbnerr_Deployment1_temp_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: 

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_hindcast/moorings_kbnerr_Deployment1_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_ciofs_fresh/moorings_kbnerr_Deployment1_temp.png
---
name: 
---

```
````
