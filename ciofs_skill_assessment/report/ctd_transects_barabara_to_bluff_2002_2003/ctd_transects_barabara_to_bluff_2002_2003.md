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

(page:ctd_transects_barabara_to_bluff_2002_2003-comparison)=
# CTD transects: Barabara to Bluff

* ctd_transects_barabara_to_bluff_2002_2003

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_barabara_to_bluff_2002_2003.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_barabara_to_bluff_2002_2003.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_barabara_to_bluff_2002_2003"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## Cruise 10


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_10_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_10_temp.png
---
name: 
---

```
````


+++

### Salinity


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_10_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_10_salt.png
---
name: 
---

```
````


+++

## Cruise 11


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_11_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_11_temp.png
---
name: 
---

```
````


+++

### Salinity


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_11_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_11_salt.png
---
name: 
---

```
````


+++

## Cruise 6


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_6_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_6_temp.png
---
name: 
---

```
````


+++

### Salinity


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_6_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_6_salt.png
---
name: 
---

```
````


+++

## Cruise 7


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_7_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_7_temp.png
---
name: 
---

```
````


+++

### Salinity


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_7_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_7_salt.png
---
name: 
---

```
````


+++

## Cruise 8


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_8_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_8_temp.png
---
name: 
---

```
````


+++

### Salinity


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_8_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_8_salt.png
---
name: 
---

```
````


+++

## Cruise 9


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_9_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_9_temp.png
---
name: 
---

```
````


+++

### Salinity


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_hindcast/ctd_transects_barabara_to_bluff_2002_2003_Cruise_9_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_barabara_to_bluff_2002_2003_ciofs_fresh/ctd_transects_barabara_to_bluff_2002_2003_Cruise_9_salt.png
---
name: 
---

```
````
