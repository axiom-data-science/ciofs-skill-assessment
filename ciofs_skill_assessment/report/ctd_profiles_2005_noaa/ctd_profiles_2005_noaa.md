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

(page:ctd_profiles_2005_noaa-comparison)=
# CTD Profiles (NOAA): across Cook Inlet

* ctd_profiles_2005_noaa

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_2005_noaa.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_2005_noaa.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_2005_noaa"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## 501


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_501_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_501_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_501_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_501_salt.png
:width: 49%
```

+++

## 502


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_502_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_502_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_502_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_502_salt.png
:width: 49%
```

+++

## 503


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_503_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_503_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_503_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_503_salt.png
:width: 49%
```

+++

## 504


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_504_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_504_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_504_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_504_salt.png
:width: 49%
```

+++

## 505


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_505_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_505_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_505_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_505_salt.png
:width: 49%
```

+++

## 506


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_506_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_506_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_506_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_506_salt.png
:width: 49%
```

+++

## 507


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_507_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_507_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_507_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_507_salt.png
:width: 49%
```

+++

## 508


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_508_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_508_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_508_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_508_salt.png
:width: 49%
```

+++

## 509


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_509_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_509_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_509_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_509_salt.png
:width: 49%
```

+++

## 510


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_510_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_510_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_510_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_510_salt.png
:width: 49%
```

+++

## 511


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_511_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_511_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_511_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_511_salt.png
:width: 49%
```

+++

## 512


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_512_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_512_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_512_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_512_salt.png
:width: 49%
```

+++

## 513


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_513_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_513_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_513_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_513_salt.png
:width: 49%
```

+++

## 514


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_514_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_514_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_514_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_514_salt.png
:width: 49%
```

+++

## 515


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_515_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_515_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_515_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_515_salt.png
:width: 49%
```

+++

## 516


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_516_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_516_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_516_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_516_salt.png
:width: 49%
```

+++

## 517


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_517_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_517_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_517_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_517_salt.png
:width: 49%
```

+++

## 518


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_518_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_518_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_518_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_518_salt.png
:width: 49%
```

+++

## 519


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_519_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_519_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_519_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_519_salt.png
:width: 49%
```

+++

## 520


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_520_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_520_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_520_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_520_salt.png
:width: 49%
```

+++

## 521


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_521_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_521_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_521_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_521_salt.png
:width: 49%
```

+++

## 522


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_522_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_522_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_522_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_522_salt.png
:width: 49%
```

+++

## 523


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_523_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_523_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_523_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_523_salt.png
:width: 49%
```

+++

## 524


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_524_temp.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_524_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_2005_noaa_ciofs_hindcast/ctd_profiles_2005_noaa_524_salt.png
:width: 49%
```

```{image} ctd_profiles_2005_noaa_ciofs_fresh/ctd_profiles_2005_noaa_524_salt.png
:width: 49%
```
