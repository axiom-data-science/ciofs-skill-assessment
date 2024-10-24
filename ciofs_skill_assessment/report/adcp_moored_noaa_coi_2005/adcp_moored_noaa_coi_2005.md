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

(page:adcp_moored_noaa_coi_2005-comparison)=
# Moored ADCP (NOAA): ADCP survey Cook Inlet 2005

* adcp_moored_noaa_coi_2005

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/adcp_moored_noaa_coi_2005.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/adcp_moored_noaa_coi_2005.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("adcp_moored_noaa_coi_2005"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## COI0501


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0501_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0501_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0501_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0501_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0501_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0501_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0501_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0501_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0501_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0501_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0501_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0501_across_subtidal.png
---
name: 
---

```
````


+++

## COI0502


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0502_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0502_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0502_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0502_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0502_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0502_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0502_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0502_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0502_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0502_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0502_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0502_across_subtidal.png
---
name: 
---

```
````


+++

## COI0503


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0503_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0503_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0503_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0503_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0503_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0503_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0503_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0503_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0503_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0503_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0503_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0503_across_subtidal.png
---
name: 
---

```
````


+++

## COI0504


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0504_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0504_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0504_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0504_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0504_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0504_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0504_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0504_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0504_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0504_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0504_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0504_across_subtidal.png
---
name: 
---

```
````


+++

## COI0505


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0505_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0505_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0505_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0505_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0505_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0505_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0505_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0505_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0505_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0505_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0505_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0505_across_subtidal.png
---
name: 
---

```
````


+++

## COI0506


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0506_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0506_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0506_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0506_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0506_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0506_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0506_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0506_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0506_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0506_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0506_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0506_across_subtidal.png
---
name: 
---

```
````


+++

## COI0507


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0507_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0507_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0507_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0507_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0507_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0507_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0507_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0507_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0507_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0507_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0507_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0507_across_subtidal.png
---
name: 
---

```
````


+++

## COI0508


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0508_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0508_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0508_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0508_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0508_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0508_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0508_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0508_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0508_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0508_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0508_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0508_across_subtidal.png
---
name: 
---

```
````


+++

## COI0509


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0509_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0509_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0509_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0509_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0509_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0509_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0509_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0509_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0509_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0509_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0509_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0509_across_subtidal.png
---
name: 
---

```
````


+++

## COI0510


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0510_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0510_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0510_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0510_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0510_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0510_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0510_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0510_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0510_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0510_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0510_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0510_across_subtidal.png
---
name: 
---

```
````


+++

## COI0511


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0511_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0511_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0511_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0511_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0511_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0511_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0511_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0511_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0511_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0511_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0511_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0511_across_subtidal.png
---
name: 
---

```
````


+++

## COI0512


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0512_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0512_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0512_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0512_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0512_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0512_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0512_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0512_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0512_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0512_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0512_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0512_across_subtidal.png
---
name: 
---

```
````


+++

## COI0513


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0513_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0513_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0513_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0513_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0513_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0513_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0513_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0513_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0513_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0513_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0513_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0513_across_subtidal.png
---
name: 
---

```
````


+++

## COI0514


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0514_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0514_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0514_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0514_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0514_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0514_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0514_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0514_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0514_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0514_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0514_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0514_across_subtidal.png
---
name: 
---

```
````


+++

## COI0515


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0515_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0515_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0515_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0515_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0515_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0515_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0515_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0515_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0515_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0515_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0515_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0515_across_subtidal.png
---
name: 
---

```
````


+++

## COI0516


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0516_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0516_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0516_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0516_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0516_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0516_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0516_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0516_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0516_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0516_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0516_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0516_across_subtidal.png
---
name: 
---

```
````


+++

## COI0517


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0517_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0517_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0517_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0517_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0517_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0517_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0517_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0517_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0517_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0517_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0517_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0517_across_subtidal.png
---
name: 
---

```
````


+++

## COI0518


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0518_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0518_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0518_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0518_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0518_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0518_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0518_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0518_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0518_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0518_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0518_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0518_across_subtidal.png
---
name: 
---

```
````


+++

## COI0519


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0519_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0519_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0519_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0519_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0519_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0519_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0519_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0519_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0519_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0519_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0519_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0519_across_subtidal.png
---
name: 
---

```
````


+++

## COI0520


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0520_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0520_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0520_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0520_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0520_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0520_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0520_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0520_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0520_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0520_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0520_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0520_across_subtidal.png
---
name: 
---

```
````


+++

## COI0521


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0521_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0521_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0521_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0521_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0521_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0521_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0521_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0521_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0521_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0521_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0521_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0521_across_subtidal.png
---
name: 
---

```
````


+++

## COI0522


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0522_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0522_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0522_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0522_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0522_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0522_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0522_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0522_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0522_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0522_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0522_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0522_across_subtidal.png
---
name: 
---

```
````


+++

## COI0523


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0523_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0523_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0523_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0523_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0523_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0523_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0523_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0523_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0523_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0523_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0523_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0523_across_subtidal.png
---
name: 
---

```
````


+++

## COI0524


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0524_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0524_speed.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0524_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0524_along.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0524_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0524_across.png
---
name: 
---

```
````


+++

### Subtidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0524_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0524_speed_subtidal.png
---
name: 
---

```
````


+++

#### Along-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0524_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0524_along_subtidal.png
---
name: 
---

```
````


+++

#### Across-channel velocity


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_hindcast/adcp_moored_noaa_coi_2005_COI0524_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_2005_ciofs_fresh/adcp_moored_noaa_coi_2005_COI0524_across_subtidal.png
---
name: 
---

```
````
