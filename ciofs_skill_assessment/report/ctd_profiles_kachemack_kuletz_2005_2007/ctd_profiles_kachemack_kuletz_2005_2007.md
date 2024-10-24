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

(page:ctd_profiles_kachemack_kuletz_2005_2007-comparison)=
# CTD Profiles (Kachemak Kuletz 2005-2007)

* ctd_profiles_kachemack_kuletz_2005_2007

See the original full dataset description page in the [original report](https://ciofs.axds.co/outputs/pages/data/ctd_profiles_kachemack_kuletz_2005_2007.html) for more information or the new [catalog page](https://cook-inlet-catalogs.readthedocs.io/en/latest/demo_notebooks/ctd_profiles_kachemack_kuletz_2005_2007.html).


```{code-cell}
:tags: [remove-input]

cat = intake.open_catalog(cic.utils.cat_path("ctd_profiles_kachemack_kuletz_2005_2007"))
dd, ddlabels = cic.utils.combine_datasets_for_map(cat)
dd.hvplot(**cat.metadata["map"]) * ddlabels.hvplot(**cat.metadata["maplabels"])
```

## 1.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_1_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_1_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_1_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_1_0_salt.png
:width: 49%
```

+++

## 1.1


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_1_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_1_1_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_1_1_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_1_1_salt.png
:width: 49%
```

+++

## 10.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_10_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_10_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_10_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_10_0_salt.png
:width: 49%
```

+++

## 101.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_101_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_101_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_101_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_101_0_salt.png
:width: 49%
```

+++

## 103.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_103_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_103_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_103_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_103_0_salt.png
:width: 49%
```

+++

## 104.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_104_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_104_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_104_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_104_0_salt.png
:width: 49%
```

+++

## 105.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_105_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_105_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_105_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_105_0_salt.png
:width: 49%
```

+++

## 107.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_107_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_107_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_107_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_107_0_salt.png
:width: 49%
```

+++

## 109.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_109_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_109_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_109_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_109_0_salt.png
:width: 49%
```

+++

## 11.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_11_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_11_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_11_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_11_0_salt.png
:width: 49%
```

+++

## 111.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_111_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_111_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_111_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_111_0_salt.png
:width: 49%
```

+++

## 12.1


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_1_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_1_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_1_salt.png
:width: 49%
```

+++

## 12.2


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_2_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_2_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_2_salt.png
:width: 49%
```

+++

## 12.3


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_3_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_3_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_3_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_3_salt.png
:width: 49%
```

+++

## 12.4


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_4_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_4_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_4_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_4_salt.png
:width: 49%
```

+++

## 12.5


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_5_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_5_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_12_5_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_12_5_salt.png
:width: 49%
```

+++

## 2.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_0_salt.png
:width: 49%
```

+++

## 2.02


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_02_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_02_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_02_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_02_salt.png
:width: 49%
```

+++

## 2.03


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_03_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_03_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_03_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_03_salt.png
:width: 49%
```

+++

## 2.2


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_2_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_2_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_2_salt.png
:width: 49%
```

+++

## 2.3


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_3_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_3_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_2_3_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_2_3_salt.png
:width: 49%
```

+++

## 202.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_202_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_202_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_202_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_202_0_salt.png
:width: 49%
```

+++

## 203.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_203_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_203_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_203_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_203_0_salt.png
:width: 49%
```

+++

## 204.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_204_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_204_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_204_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_204_0_salt.png
:width: 49%
```

+++

## 205.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_205_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_205_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_205_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_205_0_salt.png
:width: 49%
```

+++

## 206.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_206_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_206_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_206_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_206_0_salt.png
:width: 49%
```

+++

## 207.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_207_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_207_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_207_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_207_0_salt.png
:width: 49%
```

+++

## 209.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_209_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_209_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_209_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_209_0_salt.png
:width: 49%
```

+++

## 211.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_211_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_211_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_211_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_211_0_salt.png
:width: 49%
```

+++

## 3.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_0_salt.png
:width: 49%
```

+++

## 3.01


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_01_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_01_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_01_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_01_salt.png
:width: 49%
```

+++

## 3.02


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_02_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_02_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_02_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_02_salt.png
:width: 49%
```

+++

## 3.1


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_1_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_1_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_1_salt.png
:width: 49%
```

+++

## 3.2


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_2_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_2_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_3_2_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_3_2_salt.png
:width: 49%
```

+++

## 302.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_302_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_302_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_302_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_302_0_salt.png
:width: 49%
```

+++

## 304.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_304_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_304_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_304_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_304_0_salt.png
:width: 49%
```

+++

## 305.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_305_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_305_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_305_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_305_0_salt.png
:width: 49%
```

+++

## 306.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_306_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_306_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_306_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_306_0_salt.png
:width: 49%
```

+++

## 309.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_309_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_309_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_309_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_309_0_salt.png
:width: 49%
```

+++

## 311.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_311_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_311_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_311_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_311_0_salt.png
:width: 49%
```

+++

## 4.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_4_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_4_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_4_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_4_0_salt.png
:width: 49%
```

+++

## 4.1


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_4_1_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_4_1_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_4_1_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_4_1_salt.png
:width: 49%
```

+++

## 5.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_5_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_5_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_5_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_5_0_salt.png
:width: 49%
```

+++

## 6.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_6_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_6_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_6_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_6_0_salt.png
:width: 49%
```

+++

## 7.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_7_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_7_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_7_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_7_0_salt.png
:width: 49%
```

+++

## 8.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_8_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_8_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_8_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_8_0_salt.png
:width: 49%
```

+++

## 9.0


+++

### Sea Temperature [C]


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_9_0_temp.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_9_0_temp.png
:width: 49%
```

+++

### Salinity


+++


```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_hindcast/ctd_profiles_kachemack_kuletz_2005_2007_9_0_salt.png
:width: 49%
```

```{image} ctd_profiles_kachemack_kuletz_2005_2007_ciofs_fresh/ctd_profiles_kachemack_kuletz_2005_2007_9_0_salt.png
:width: 49%
```
