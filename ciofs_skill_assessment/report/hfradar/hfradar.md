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

(page:hfradar-comparison)=
# HF Radar (UAF)

* hfradar

See the full dataset page for more information: {ref}`page:hfradar`

Note that the map shows all datasets from the catalog; it is not limited to the current report time periods.

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

## lower-ci_system-B_2006


+++

### M2 Tidal Ellipses


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_M2_ellipses.png
---
name: fig-lower-ci_system-B_2006-ciofs_hindcast-M2 Tidal Ellipses_K1 Tidal Ellipses
---
M2 tidal ellipses from surface currents for CIOFS_HINDCAST and dataset lower-ci_system-B_2006
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_M2_ellipses.png
---
name: fig-lower-ci_system-B_2006-ciofs_fresh-M2 Tidal Ellipses_K1 Tidal Ellipses
---
M2 tidal ellipses from surface currents for CIOFS_FRESH and dataset lower-ci_system-B_2006
```
````


+++

### K1 Tidal Ellipses


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K1_ellipses.png
---
name: fig-lower-ci_system-B_2006-ciofs_hindcast-M2 Tidal Ellipses_K1 Tidal Ellipses
---
K1 tidal ellipses from surface currents for CIOFS_HINDCAST and dataset lower-ci_system-B_2006
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K1_ellipses.png
---
name: fig-lower-ci_system-B_2006-ciofs_fresh-M2 Tidal Ellipses_K1 Tidal Ellipses
---
K1 tidal ellipses from surface currents for CIOFS_FRESH and dataset lower-ci_system-B_2006
```
````


+++

## upper-ci_system-A_2003


+++

### M2 Tidal Ellipses


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_M2_ellipses.png
---
name: fig-upper-ci_system-A_2003-ciofs_hindcast-M2 Tidal Ellipses_K1 Tidal Ellipses
---
M2 tidal ellipses from surface currents for CIOFS_HINDCAST and dataset upper-ci_system-A_2003
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_M2_ellipses.png
---
name: fig-upper-ci_system-A_2003-ciofs_fresh-M2 Tidal Ellipses_K1 Tidal Ellipses
---
M2 tidal ellipses from surface currents for CIOFS_FRESH and dataset upper-ci_system-A_2003
```
````


+++

### K1 Tidal Ellipses


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K1_ellipses.png
---
name: fig-upper-ci_system-A_2003-ciofs_hindcast-M2 Tidal Ellipses_K1 Tidal Ellipses
---
K1 tidal ellipses from surface currents for CIOFS_HINDCAST and dataset upper-ci_system-A_2003
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K1_ellipses.png
---
name: fig-upper-ci_system-A_2003-ciofs_fresh-M2 Tidal Ellipses_K1 Tidal Ellipses
---
K1 tidal ellipses from surface currents for CIOFS_FRESH and dataset upper-ci_system-A_2003
```
````


+++

## lower-ci_system-B_2006-2007


+++

### Subtidal Mean


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006-2007_east_north_2006-11-12_2007-01-01_remove-under-50-percent-data_units-to-meters_subtidal_mean.png
---
name: fig-lower-ci_system-B_2006-2007-ciofs_hindcast-Subtidal Mean_Hourly_Subtidal, 6-Hourly
---
Subtidal mean from surface currents for CIOFS_HINDCAST and dataset lower-ci_system-B_2006-2007
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006-2007_east_north_2006-11-12_2007-01-01_remove-under-50-percent-data_units-to-meters_subtidal_mean.png
---
name: fig-lower-ci_system-B_2006-2007-ciofs_fresh-Subtidal Mean_Hourly_Subtidal, 6-Hourly
---
Subtidal mean from surface currents for CIOFS_FRESH and dataset lower-ci_system-B_2006-2007
```
````


+++

### Hourly


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006-2007_east_north_2006-11-12_2007-01-01_remove-under-50-percent-data_units-to-meters.mp4
---
name: fig-lower-ci_system-B_2006-2007-ciofs_hindcast-Hourly
class: video controls
width: 1000px
---
Hourly from surface currents for CIOFS_HINDCAST and dataset lower-ci_system-B_2006-2007
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006-2007_east_north_2006-11-12_2007-01-01_remove-under-50-percent-data_units-to-meters.mp4
---
name: fig-lower-ci_system-B_2006-2007-ciofs_fresh-Hourly
class: video controls
width: 1000px
---
Hourly from surface currents for CIOFS_FRESH and dataset lower-ci_system-B_2006-2007
```
````


+++

### Subtidal, 6-Hourly


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006-2007_east_north_2006-11-12_2007-01-01_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H.mp4
---
name: fig-lower-ci_system-B_2006-2007-ciofs_hindcast-Subtidal, 6-Hourly
class: video controls
width: 1000px
---
Subtidal, 6-hourly from surface currents for CIOFS_HINDCAST and dataset lower-ci_system-B_2006-2007
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006-2007_east_north_2006-11-12_2007-01-01_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H.mp4
---
name: fig-lower-ci_system-B_2006-2007-ciofs_fresh-Subtidal, 6-Hourly
class: video controls
width: 1000px
---
Subtidal, 6-hourly from surface currents for CIOFS_FRESH and dataset lower-ci_system-B_2006-2007
```
````


+++

## upper-ci_system-A_2002-2003


+++

### Subtidal Mean


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2002-2003_east_north_2003-01-01_2003-06-09_remove-under-50-percent-data_units-to-meters_subtidal_mean.png
---
name: fig-upper-ci_system-A_2002-2003-ciofs_hindcast-Subtidal Mean_Hourly_Subtidal, 6-Hourly
---
Subtidal mean from surface currents for CIOFS_HINDCAST and dataset upper-ci_system-A_2002-2003
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2002-2003_east_north_2003-01-01_2003-06-09_remove-under-50-percent-data_units-to-meters_subtidal_mean.png
---
name: fig-upper-ci_system-A_2002-2003-ciofs_fresh-Subtidal Mean_Hourly_Subtidal, 6-Hourly
---
Subtidal mean from surface currents for CIOFS_FRESH and dataset upper-ci_system-A_2002-2003
```
````


+++

### Hourly


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2002-2003_east_north_2003-01-01_2003-06-09_remove-under-50-percent-data_units-to-meters.mp4
---
name: fig-upper-ci_system-A_2002-2003-ciofs_hindcast-Hourly
class: video controls
width: 1000px
---
Hourly from surface currents for CIOFS_HINDCAST and dataset upper-ci_system-A_2002-2003
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2002-2003_east_north_2003-01-01_2003-06-09_remove-under-50-percent-data_units-to-meters.mp4
---
name: fig-upper-ci_system-A_2002-2003-ciofs_fresh-Hourly
class: video controls
width: 1000px
---
Hourly from surface currents for CIOFS_FRESH and dataset upper-ci_system-A_2002-2003
```
````


+++

### Subtidal, 6-Hourly


+++

#### CIOFS_HINDCAST


+++



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2002-2003_east_north_2003-01-01_2003-06-09_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H.mp4
---
name: fig-upper-ci_system-A_2002-2003-ciofs_hindcast-Subtidal, 6-Hourly
class: video controls
width: 1000px
---
Subtidal, 6-hourly from surface currents for CIOFS_HINDCAST and dataset upper-ci_system-A_2002-2003
```
````


+++

#### CIOFS_FRESH


+++



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2002-2003_east_north_2003-01-01_2003-06-09_remove-under-50-percent-data_units-to-meters_subtidal_resample-6H.mp4
---
name: fig-upper-ci_system-A_2002-2003-ciofs_fresh-Subtidal, 6-Hourly
class: video controls
width: 1000px
---
Subtidal, 6-hourly from surface currents for CIOFS_FRESH and dataset upper-ci_system-A_2002-2003
```
````


+++

## lower-ci_system-B_2006


+++

### Tidal Constants


+++


`````{dropdown} CIOFS_HINDCAST
### Major Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_M2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_S2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_N2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_O1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_Q1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_P1-major.png
---
name: 
---

```
````

### Minor Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_M2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_S2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_N2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_O1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_Q1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_P1-minor.png
---
name: 
---

```
````

### Phase



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_M2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_S2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_N2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_O1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_Q1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_P1-phase.png
---
name: 
---

```
````

### Inclination



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_M2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_S2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_N2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_O1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_Q1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_K2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_lower-ci_system-B_2006_P1-inclination.png
---
name: 
---

```
````



`````

+++


`````{dropdown} CIOFS_FRESH
### Major Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_M2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_S2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_N2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_O1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_Q1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_P1-major.png
---
name: 
---

```
````

### Minor Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_M2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_S2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_N2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_O1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_Q1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_P1-minor.png
---
name: 
---

```
````

### Phase



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_M2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_S2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_N2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_O1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_Q1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_P1-phase.png
---
name: 
---

```
````

### Inclination



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_M2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_S2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_N2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_O1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_Q1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_K2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_lower-ci_system-B_2006_P1-inclination.png
---
name: 
---

```
````



`````

+++

## upper-ci_system-A_2003


+++

### Tidal Constants


+++


`````{dropdown} CIOFS_HINDCAST
### Major Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_M2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_S2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_N2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_O1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_Q1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_P1-major.png
---
name: 
---

```
````

### Minor Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_M2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_S2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_N2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_O1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_Q1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_P1-minor.png
---
name: 
---

```
````

### Phase



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_M2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_S2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_N2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_O1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_Q1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_P1-phase.png
---
name: 
---

```
````

### Inclination



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_M2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_S2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_N2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_O1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_Q1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_K2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_hindcast/hfradar_upper-ci_system-A_2003_P1-inclination.png
---
name: 
---

```
````



`````

+++


`````{dropdown} CIOFS_FRESH
### Major Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_M2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_S2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_N2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_O1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_Q1-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K2-major.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_P1-major.png
---
name: 
---

```
````

### Minor Amplitude



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_M2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_S2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_N2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_O1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_Q1-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K2-minor.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_P1-minor.png
---
name: 
---

```
````

### Phase



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_M2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_S2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_N2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_O1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_Q1-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K2-phase.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_P1-phase.png
---
name: 
---

```
````

### Inclination



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_M2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_S2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_N2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_O1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_Q1-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_K2-inclination.png
---
name: 
---

```
````



````{div} full-width                
```{figure} hfradar_ciofs_fresh/hfradar_upper-ci_system-A_2003_P1-inclination.png
---
name: 
---

```
````



`````
