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

(page:ctd_transects_gwa-comparison)=
# CTD Transects (GWA): Six repeat transects in Cook Inlet

* ctd_transects_gwa

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_transects_gwa.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_transects_gwa.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_transects_gwa"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## transect_3-2012-05-02


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2012-05-02_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2012-05-02_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2012-05-02_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2012-05-02_salt.png
---
name: 
---

```
````


+++

## transect_3-2012-07-29


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2012-07-29_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2012-07-29_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2012-07-29_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2012-07-29_salt.png
---
name: 
---

```
````


+++

## transect_3-2012-10-29


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2012-10-29_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2012-10-29_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2012-10-29_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2012-10-29_salt.png
---
name: 
---

```
````


+++

## transect_3-2013-04-20


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2013-04-20_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2013-04-20_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2013-04-20_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2013-04-20_salt.png
---
name: 
---

```
````


+++

## transect_3-2013-07-19


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2013-07-19_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2013-07-19_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2013-07-19_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2013-07-19_salt.png
---
name: 
---

```
````


+++

## transect_3-2013-11-08


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2013-11-08_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2013-11-08_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2013-11-08_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2013-11-08_salt.png
---
name: 
---

```
````


+++

## transect_3-2014-04-11


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2014-04-11_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2014-04-11_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2014-04-11_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2014-04-11_salt.png
---
name: 
---

```
````


+++

## transect_3-2014-07-22


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2014-07-22_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2014-07-22_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2014-07-22_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2014-07-22_salt.png
---
name: 
---

```
````


+++

## transect_3-2014-10-13


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2014-10-13_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2014-10-13_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_3-2014-10-13_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_3-2014-10-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-05-02


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-05-02_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-05-02_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-05-02_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-05-02_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-05-31


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-05-31_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-05-31_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-05-31_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-05-31_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-06-05_A


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-06-05_A_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-06-05_A_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-06-05_A_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-06-05_A_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-06-05_B


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-06-05_B_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-06-05_B_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-06-05_B_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-06-05_B_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-07-31


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-07-31_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-07-31_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-07-31_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-07-31_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-08-15


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-08-15_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-08-15_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-08-15_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-08-15_salt.png
---
name: 
---

```
````


+++

## transect_4-2012-10-29


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-10-29_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-10-29_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2012-10-29_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2012-10-29_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-02-12


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-02-12_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-02-12_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-02-12_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-02-12_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-04-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-04-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-04-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-04-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-04-21_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-06-06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-06-06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-06-06_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-06-06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-06-06_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-07-19


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-07-19_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-07-19_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-07-19_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-07-19_salt.png
---
name: 
---

```
````


+++

## transect_4-2013-10-29


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-10-29_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-10-29_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2013-10-29_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2013-10-29_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-02-15


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-02-15_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-02-15_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-02-15_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-02-15_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-04-11


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-04-11_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-04-11_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-04-11_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-04-11_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-07-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-07-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-07-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-07-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-07-21_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-08-13


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-08-13_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-08-13_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-08-13_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-08-13_salt.png
---
name: 
---

```
````


+++

## transect_4-2014-10-13


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-10-13_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-10-13_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_4-2014-10-13_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_4-2014-10-13_salt.png
---
name: 
---

```
````


+++

## transect_6-2012-05-03


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2012-05-03_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2012-05-03_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2012-05-03_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2012-05-03_salt.png
---
name: 
---

```
````


+++

## transect_6-2012-07-30


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2012-07-30_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2012-07-30_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2012-07-30_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2012-07-30_salt.png
---
name: 
---

```
````


+++

## transect_6-2012-10-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2012-10-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2012-10-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2012-10-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2012-10-28_salt.png
---
name: 
---

```
````


+++

## transect_6-2013-04-19


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2013-04-19_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2013-04-19_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2013-04-19_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2013-04-19_salt.png
---
name: 
---

```
````


+++

## transect_6-2013-07-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2013-07-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2013-07-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2013-07-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2013-07-21_salt.png
---
name: 
---

```
````


+++

## transect_6-2013-11-06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2013-11-06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2013-11-06_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2013-11-06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2013-11-06_salt.png
---
name: 
---

```
````


+++

## transect_6-2014-04-06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2014-04-06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2014-04-06_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2014-04-06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2014-04-06_salt.png
---
name: 
---

```
````


+++

## transect_6-2014-07-23


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2014-07-23_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2014-07-23_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2014-07-23_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2014-07-23_salt.png
---
name: 
---

```
````


+++

## transect_6-2014-10-18


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2014-10-18_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2014-10-18_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_6-2014-10-18_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_6-2014-10-18_salt.png
---
name: 
---

```
````


+++

## transect_7-2012-07-30


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2012-07-30_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2012-07-30_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2012-07-30_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2012-07-30_salt.png
---
name: 
---

```
````


+++

## transect_7-2012-10-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2012-10-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2012-10-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2012-10-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2012-10-28_salt.png
---
name: 
---

```
````


+++

## transect_7-2013-04-20


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2013-04-20_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2013-04-20_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2013-04-20_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2013-04-20_salt.png
---
name: 
---

```
````


+++

## transect_7-2013-07-18


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2013-07-18_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2013-07-18_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2013-07-18_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2013-07-18_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-02-17


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-02-17_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-02-17_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-02-17_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-02-17_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-04-07


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-04-07_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-04-07_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-04-07_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-04-07_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-07-24


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-07-24_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-07-24_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-07-24_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-07-24_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-10-17


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-10-17_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-10-17_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-10-17_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-10-17_salt.png
---
name: 
---

```
````


+++

## transect_7-2014-10-18


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-10-18_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-10-18_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_7-2014-10-18_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_7-2014-10-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-02-14


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-02-14_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-02-14_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-02-14_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-02-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-03-14


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-03-14_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-03-14_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-03-14_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-03-14_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-04-10


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-04-10_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-04-10_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-04-10_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-04-10_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-04-26


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-04-26_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-04-26_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-04-26_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-04-26_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-05-31_A


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-05-31_A_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-05-31_A_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-05-31_A_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-05-31_A_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-05-31_B


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-05-31_B_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-05-31_B_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-05-31_B_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-05-31_B_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-06-05_A


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-06-05_A_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-06-05_A_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-06-05_A_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-06-05_A_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-06-05_B


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-06-05_B_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-06-05_B_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-06-05_B_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-06-05_B_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-06-27


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-06-27_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-06-27_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-06-27_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-06-27_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-07-02


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-07-02_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-07-02_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-07-02_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-07-02_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-07-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-07-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-07-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-07-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-07-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-03


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-03_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-03_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-03_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-03_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-15


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-15_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-15_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-15_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-26


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-26_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-26_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-26_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-26_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-08-31


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-31_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-31_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-08-31_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-08-31_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_A


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_A_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_A_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_A_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_A_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_B


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_B_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_B_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_B_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_B_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_C


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_C_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_C_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_C_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_C_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_D


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_D_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_D_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_D_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_D_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-09-21_E


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_E_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_E_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-09-21_E_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-09-21_E_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-10-12


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-10-12_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-10-12_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-10-12_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-10-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2012-10-29


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-10-29_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-10-29_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2012-10-29_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2012-10-29_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-01-04


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-01-04_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-01-04_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-01-04_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-01-04_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-02-12


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-02-12_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-02-12_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-02-12_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-02-12_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-03-15


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-03-15_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-03-15_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-03-15_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-03-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-04-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-04-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-04-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-04-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-04-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-05-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-05-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-05-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-05-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-05-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-06-06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-06-06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-06-06_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-06-06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-06-06_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-06-19


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-06-19_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-06-19_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-06-19_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-06-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-06-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-06-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-06-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-06-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-06-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-07-05


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-07-05_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-07-05_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-07-05_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-07-05_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-07-09


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-07-09_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-07-09_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-07-09_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-07-09_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-07-22


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-07-22_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-07-22_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-07-22_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-07-22_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-08-07


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-08-07_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-08-07_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-08-07_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-08-07_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-08-30


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-08-30_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-08-30_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-08-30_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-08-30_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-09-25


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-09-25_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-09-25_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-09-25_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-09-25_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-10-29


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-10-29_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-10-29_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-10-29_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-10-29_salt.png
---
name: 
---

```
````


+++

## transect_9-2013-12-03


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-12-03_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-12-03_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2013-12-03_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2013-12-03_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-01-09


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-01-09_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-01-09_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-01-09_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-01-09_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-02-15


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-02-15_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-02-15_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-02-15_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-02-15_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-03-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-03-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-03-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-03-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-03-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-04-11


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-04-11_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-04-11_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-04-11_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-04-11_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-05-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-05-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-05-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-05-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-05-28_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-06-18


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-06-18_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-06-18_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-06-18_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-06-18_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-07-21


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-07-21_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-07-21_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-07-21_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-07-21_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-08-13


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-08-13_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-08-13_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-08-13_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-08-13_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-10-19


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-10-19_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-10-19_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-10-19_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-10-19_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-11-25


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-11-25_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-11-25_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-11-25_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-11-25_salt.png
---
name: 
---

```
````


+++

## transect_9-2014-12-17


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-12-17_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-12-17_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_9-2014-12-17_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_9-2014-12-17_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2012-08-15


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2012-08-15_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2012-08-15_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2012-08-15_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2012-08-15_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-02-12


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-02-12_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-02-12_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-02-12_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-02-12_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-02-13_A


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-02-13_A_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-02-13_A_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-02-13_A_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-02-13_A_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-02-13_B


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-02-13_B_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-02-13_B_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-02-13_B_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-02-13_B_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2013-06-06


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-06-06_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-06-06_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2013-06-06_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2013-06-06_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2014-03-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-03-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-03-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-03-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-03-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2014-05-28


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-05-28_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-05-28_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-05-28_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-05-28_salt.png
---
name: 
---

```
````


+++

## transect_AlongBay-2014-08-14


+++

### Sea Temperature [C]


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-08-14_temp.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-08-14_temp.png
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
```{figure} ctd_transects_gwa_ciofs_hindcast/ctd_transects_gwa_transect_AlongBay-2014-08-14_salt.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} ctd_transects_gwa_ciofs_fresh/ctd_transects_gwa_transect_AlongBay-2014-08-14_salt.png
---
name: 
---

```
````
