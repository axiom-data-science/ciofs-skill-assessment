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

(page:ctd_transects_cmi_uaf-comparison)=
# CTD Transect (CMI UAF): from East Foreland Lighthouse

* ctd_transects_cmi_uaf

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_cmi_uaf.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_cmi_uaf.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_cmi_uaf"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## Cruise-01


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-01_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-01_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-01_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-01_salt.png
---
name: 
---

```
````


+++

## Cruise-02


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-02_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-02_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-02_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-02_salt.png
---
name: 
---

```
````


+++

## Cruise-03


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-03_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-03_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-03_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-03_salt.png
---
name: 
---

```
````


+++

## Cruise-04


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-04_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-04_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-04_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-04_salt.png
---
name: 
---

```
````


+++

## Cruise-05


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-05_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-05_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-05_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-05_salt.png
---
name: 
---

```
````


+++

## Cruise-06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-06_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-06_salt.png
---
name: 
---

```
````


+++

## Cruise-07


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-07_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-07_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-07_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-07_salt.png
---
name: 
---

```
````


+++

## Cruise-08


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-08_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-08_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-08_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-08_salt.png
---
name: 
---

```
````


+++

## Cruise-09


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-09_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-09_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-09_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-09_salt.png
---
name: 
---

```
````


+++

## Cruise-10


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-10_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-10_temp.png
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
```{figure} ctd_transects_cmi_uaf_ciofs_hindcast/ctd_transects_cmi_uaf_Cruise-10_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_cmi_uaf_ciofs_fresh/ctd_transects_cmi_uaf_Cruise-10_salt.png
---
name: 
---

```
````
