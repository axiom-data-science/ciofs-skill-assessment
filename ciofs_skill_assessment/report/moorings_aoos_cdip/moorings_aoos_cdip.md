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

# Moorings (CDIP): Lower and Central Cook Inlet, Kodiak Island

* moorings_aoos_cdip

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_aoos_cdip.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_aoos_cdip.html).

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_aoos_cdip"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## aoos_204


+++

### Sea water temperature: 

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_hindcast/moorings_aoos_cdip_aoos_204_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_fresh/moorings_aoos_cdip_aoos_204_temp_2013-01-01_2014-01-01.png
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
```{figure} moorings_aoos_cdip_ciofs_hindcast/moorings_aoos_cdip_aoos_204_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_fresh/moorings_aoos_cdip_aoos_204_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_hindcast/moorings_aoos_cdip_aoos_204_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_fresh/moorings_aoos_cdip_aoos_204_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

## central-cook-inlet-175


+++

### Sea water temperature: 

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_hindcast/moorings_aoos_cdip_central-cook-inlet-175_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_fresh/moorings_aoos_cdip_central-cook-inlet-175_temp_2012-01-01_2013-01-01.png
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
```{figure} moorings_aoos_cdip_ciofs_hindcast/moorings_aoos_cdip_central-cook-inlet-175_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_fresh/moorings_aoos_cdip_central-cook-inlet-175_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````


+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++

#### CIOFS_HINDCAST



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_hindcast/moorings_aoos_cdip_central-cook-inlet-175_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````


+++

#### CIOFS_FRESH



````{div} full-width                
```{figure} moorings_aoos_cdip_ciofs_fresh/moorings_aoos_cdip_central-cook-inlet-175_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````
