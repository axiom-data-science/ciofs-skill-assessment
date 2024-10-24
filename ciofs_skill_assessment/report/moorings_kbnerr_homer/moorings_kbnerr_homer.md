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

# Moorings (KBNERR): Kachemak Bay, Homer stations

* moorings_kbnerr_homer

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/moorings_kbnerr_homer.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/moorings_kbnerr_homer.html).

```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("moorings_kbnerr_homer"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## homer-dolphin-surface-water-q


+++

### Sea water salinity: 

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01.png
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

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal.png
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
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

### Sea surface height: mean subtracted

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````



`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
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

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01.png
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

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal.png
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
```{figure} moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_homer-dolphin-surface-water-q_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

## nerrs_kach3wq


+++

### Sea water salinity: 

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01.png
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

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01_subtidal.png
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
```{figure} moorings_kbnerr_homer_nerrs_kach3wq_salt_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

### Sea surface height: mean subtracted

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````



`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
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

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01.png
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

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01_subtidal.png
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
```{figure} moorings_kbnerr_homer_nerrs_kach3wq_temp_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kach3wq_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

## nerrs_kachdwq


+++

### Sea water salinity: 

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01.png
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

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01_subtidal.png
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
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_salt_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_salt_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

### Sea surface height: mean subtracted

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2012-01-01_2013-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2013-01-01_2014-01-01_subtract-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2014-01-01_2015-01-01_subtract-mean.png
---
name: 
---

```
````



`````

+++

### Sea surface height: mean subtracted, then tidally-filtered

+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2003-01-01_2004-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2004-01-01_2005-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2005-01-01_2006-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2006-01-01_2007-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2012-01-01_2013-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2013-01-01_2014-01-01_subtract-mean_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_ssh_2014-01-01_2015-01-01_subtract-mean_subtidal.png
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

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01.png
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

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01_subtidal.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01_subtidal.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01_subtidal.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01_subtidal.png
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
```{figure} moorings_kbnerr_homer_nerrs_kachdwq_temp_mean.png
---
name: 
---

```
````


+++

#### CIOFS_HINDCAST



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_hindcast/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````

+++

#### CIOFS_FRESH



`````{dropdown} Comparison plots by year

##### 2003



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2003-01-01_2004-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2004



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2004-01-01_2005-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2005



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2005-01-01_2006-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2006



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2006-01-01_2007-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2012



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2012-01-01_2013-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2013



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2013-01-01_2014-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````

##### 2014



````{div} full-width                
```{figure} moorings_kbnerr_homer_ciofs_fresh/moorings_kbnerr_homer_nerrs_kachdwq_temp_2014-01-01_2015-01-01_subtidal_subtract-monthly-mean.png
---
name: 
---

```
````



`````
