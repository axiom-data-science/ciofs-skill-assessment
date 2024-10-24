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

(page:adcp_moored_noaa_coi_other-comparison)=
# Moored ADCP (NOAA): ADCP survey Cook Inlet, multiple years

* adcp_moored_noaa_coi_other

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/adcp_moored_noaa_coi_other.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/adcp_moored_noaa_coi_other.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("adcp_moored_noaa_coi_other"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## COI0301


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0301_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0301_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0301_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0301_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0301_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0301_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0301_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0301_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0301_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0301_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0301_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0301_across_subtidal.png
---
name: 
---

```
````


+++

## COI0302


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0302_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0302_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0302_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0302_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0302_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0302_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0302_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0302_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0302_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0302_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0302_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0302_across_subtidal.png
---
name: 
---

```
````


+++

## COI0303


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0303_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0303_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0303_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0303_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0303_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0303_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0303_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0303_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0303_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0303_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0303_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0303_across_subtidal.png
---
name: 
---

```
````


+++

## COI0306


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0306_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0306_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0306_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0306_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0306_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0306_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0306_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0306_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0306_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0306_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0306_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0306_across_subtidal.png
---
name: 
---

```
````


+++

## COI0307


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0307_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0307_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0307_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0307_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0307_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0307_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0307_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0307_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0307_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0307_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0307_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0307_across_subtidal.png
---
name: 
---

```
````


+++

## COI0418


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0418_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0418_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0418_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0418_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0418_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0418_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0418_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0418_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0418_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0418_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0418_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0418_across_subtidal.png
---
name: 
---

```
````


+++

## COI0419


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0419_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0419_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0419_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0419_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0419_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0419_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0419_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0419_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0419_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0419_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0419_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0419_across_subtidal.png
---
name: 
---

```
````


+++

## COI0420


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0420_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0420_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0420_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0420_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0420_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0420_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0420_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0420_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0420_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0420_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0420_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0420_across_subtidal.png
---
name: 
---

```
````


+++

## COI0421


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0421_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0421_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0421_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0421_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0421_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0421_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0421_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0421_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0421_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0421_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0421_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0421_across_subtidal.png
---
name: 
---

```
````


+++

## COI0422


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0422_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0422_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0422_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0422_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0422_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0422_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0422_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0422_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0422_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0422_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI0422_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI0422_across_subtidal.png
---
name: 
---

```
````


+++

## COI1201


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1201_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1201_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1201_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1201_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1201_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1201_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1201_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1201_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1201_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1201_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1201_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1201_across_subtidal.png
---
name: 
---

```
````


+++

## COI1202


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1202_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1202_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1202_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1202_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1202_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1202_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1202_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1202_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1202_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1202_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1202_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1202_across_subtidal.png
---
name: 
---

```
````


+++

## COI1203


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1203_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1203_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1203_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1203_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1203_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1203_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1203_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1203_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1203_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1203_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1203_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1203_across_subtidal.png
---
name: 
---

```
````


+++

## COI1204


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1204_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1204_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1204_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1204_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1204_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1204_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1204_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1204_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1204_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1204_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1204_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1204_across_subtidal.png
---
name: 
---

```
````


+++

## COI1205


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1205_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1205_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1205_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1205_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1205_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1205_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1205_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1205_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1205_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1205_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1205_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1205_across_subtidal.png
---
name: 
---

```
````


+++

## COI1207


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1207_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1207_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1207_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1207_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1207_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1207_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1207_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1207_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1207_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1207_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1207_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1207_across_subtidal.png
---
name: 
---

```
````


+++

## COI1208


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1208_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1208_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1208_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1208_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1208_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1208_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1208_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1208_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1208_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1208_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1208_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1208_across_subtidal.png
---
name: 
---

```
````


+++

## COI1209


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1209_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1209_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1209_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1209_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1209_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1209_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1209_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1209_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1209_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1209_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1209_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1209_across_subtidal.png
---
name: 
---

```
````


+++

## COI1210


+++

### Tidal


+++

#### Horizontal speed


+++

##### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1210_speed.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1210_speed.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1210_along.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1210_along.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1210_across.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1210_across.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1210_speed_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1210_speed_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1210_along_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1210_along_subtidal.png
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
```{figure} adcp_moored_noaa_coi_other_ciofs_hindcast/adcp_moored_noaa_coi_other_COI1210_across_subtidal.png
---
name: 
---

```
````


+++

##### CIOFS_FRESH


+++



````{div} full-width                
```{figure} adcp_moored_noaa_coi_other_ciofs_fresh/adcp_moored_noaa_coi_other_COI1210_across_subtidal.png
---
name: 
---

```
````
