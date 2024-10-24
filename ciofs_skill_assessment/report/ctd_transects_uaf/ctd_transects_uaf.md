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

(page:ctd_transects_uaf-comparison)=
# CTD Transects (UAF): Repeated in central Cook Inlet

* ctd_transects_uaf

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_uaf.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_uaf.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_uaf"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## Transect_01


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_01_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_01_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_01_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_01_salt.png
---
name: 
---

```
````


+++

## Transect_02


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_02_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_02_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_02_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_02_salt.png
---
name: 
---

```
````


+++

## Transect_03


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_03_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_03_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_03_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_03_salt.png
---
name: 
---

```
````


+++

## Transect_04


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_04_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_04_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_04_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_04_salt.png
---
name: 
---

```
````


+++

## Transect_05


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_05_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_05_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_05_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_05_salt.png
---
name: 
---

```
````


+++

## Transect_06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_06_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_06_salt.png
---
name: 
---

```
````


+++

## Transect_07


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_07_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_07_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_07_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_07_salt.png
---
name: 
---

```
````


+++

## Transect_08


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_08_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_08_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_08_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_08_salt.png
---
name: 
---

```
````


+++

## Transect_09


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_09_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_09_temp.png
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
```{figure} ctd_transects_uaf_ciofs_hindcast/ctd_transects_uaf_Transect_09_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_uaf_ciofs_fresh/ctd_transects_uaf_Transect_09_salt.png
---
name: 
---

```
````
