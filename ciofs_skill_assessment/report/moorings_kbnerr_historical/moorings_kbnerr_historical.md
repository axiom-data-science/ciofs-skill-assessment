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

# Moorings (KBNERR): Historical, Kachemak Bay

* moorings_kbnerr_historical

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_kbnerr_historical.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_kbnerr_historical.html).

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_kbnerr_historical"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## kacdlwq


+++

### Sea water salinity: tidally-filtered

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs_hindcast/moorings_kbnerr_historical_kacdlwq_salt_subtidal.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs_fresh/moorings_kbnerr_historical_kacdlwq_salt_subtidal.png
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
```{figure} moorings_kbnerr_historical_ciofs_hindcast/moorings_kbnerr_historical_kacdlwq_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs_fresh/moorings_kbnerr_historical_kacdlwq_salt.png
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
```{figure} moorings_kbnerr_historical_ciofs_hindcast/moorings_kbnerr_historical_kacdlwq_temp_subtidal.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs_fresh/moorings_kbnerr_historical_kacdlwq_temp_subtidal.png
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
```{figure} moorings_kbnerr_historical_ciofs_hindcast/moorings_kbnerr_historical_kacdlwq_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_kbnerr_historical_ciofs_fresh/moorings_kbnerr_historical_kacdlwq_temp.png
---
name: 
---

```
````
