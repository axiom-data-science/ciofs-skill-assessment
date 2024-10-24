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

# Moorings (UAF): Kodiak Island, Peterson Bay

* moorings_uaf

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_uaf.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_uaf.html).

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_uaf"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## uaf_ocean_acidification_resea_ko


+++

### Sea water salinity: 

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

### Sea water salinity: tidally-filtered

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

### Sea water salinity: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_uaf_uaf_ocean_acidification_resea_ko_salt_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

### Sea water temperature: 

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

### Sea water temperature: tidally-filtered

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

### Sea water temperature: tidally-filtered, then monthly mean from data subtracted

+++



````{div} full-width                
```{figure} moorings_uaf_uaf_ocean_acidification_resea_ko_temp_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_hindcast/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2013



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_uaf_ciofs_fresh/moorings_uaf_uaf_ocean_acidification_resea_ko_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````
