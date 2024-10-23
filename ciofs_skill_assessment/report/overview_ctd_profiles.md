---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: ciofs-skill-assessment
  language: python
  name: python3
---

# Overview CTD Profiles

[19MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/ctd_profiles.zip)

```{code-cell} ipython3
:tags: [remove-input]

import intake
import numpy as np
import ocean_model_skill_assessor as omsa
import cook_inlet_catalogs as cic
import pandas as pd
import xarray as xr
import hvplot.pandas
import cmocean
import yaml
from myst_nb import glue
from datetimerange import DateTimeRange
import more_utils as mu

years = [2003, 2004, 2005, 2006, 2012, 2013, 2014]
```

## Map of Stations

```{code-cell} ipython3
:tags: [remove-input]

def station_intersect_with_years(minTime, maxTime):
    # if there is any overlap between data and years, include
    data_time_range = DateTimeRange(minTime, maxTime)
    flag = False
    for year in years:
        start = pd.Timestamp(f"{year}-01-01")
        end = pd.Timestamp(f"{year}-12-31")
        model_time_range = DateTimeRange(start, end)
        flag += data_time_range.is_intersection(model_time_range)
    return flag
```

```{code-cell} ipython3
:tags: [remove-input]

slugs = [        "ctd_profiles_2005_noaa",
        "ctd_profiles_kachemack_kuletz_2005_2007",
        "ctd_profiles_kb_small_mesh_2006",
        ]
rows = []
source_names_present = {}
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names_present[slug] = []
    for source_name in list(cat):
        lon, lat = cat[source_name].metadata["minLongitude"], cat[source_name].metadata["minLatitude"]
        start_time = cat[source_name].metadata["minTime"]
        minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
        if not station_intersect_with_years(minTime, maxTime):
            # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
            continue
        # print(f"Adding {source_name} because min time {minTime} and max time {maxTime} are in {years}")
        source_names_present[slug].append(source_name)
        rows.append([source_name, lon, lat, start_time, slug])
df = pd.DataFrame(rows, columns=["station","lon","lat","date_time", "slug"])
```

```{code-cell} ipython3
:tags: [remove-input, full-width]

pts_plot = df.hvplot.points(x="lon", y="lat", color="k",
                legend=False, geo=True, tiles=True, size=35, hover_cols=["station","date_time","slug"],
                coastline=False, xlabel="Longitude", ylabel="Latitude", title="CTD Profiles",
                width=600, height=700, marker="o")
labels_plot = df.hvplot.labels(x="lon", y="lat", text="station", geo=True, text_alpha=0.5,
            hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='10pt', text_color="k")

fmap = pts_plot * labels_plot
glue("fig_map", fmap, display=False)
```

```{glue:figure} fig_map
:name: "fig-overview-ctd-profiles-map"

All CTD profiles.
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, model_name, key_variable):
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}.yaml"))
    return stats_fnames

def load_ss(index, stats_fnames, model_name, key_variable):
    ds = pd.Series(index=index, dtype=float)
    for stats_fname in stats_fnames:
        with open(stats_fname, "r") as stream:
            stats = yaml.safe_load(stream)
            ss = stats["ss"]["value"]
            mse = stats["mse"]["value"]
            if ss == 1.0 and np.isnan(mse):
                ss = np.nan
            station = stats_fname.name.split(slug)[1].split(key_variable)[0].strip("_")
            ds.loc[station] = ss
    return ds
```

```{code-cell} ipython3
:tags: [remove-input]

model_names, key_variables = mu.models, ["temp", "salt"]
vardescs = ["sea temperature", "salinity"]

dfalls = []
for slug in slugs:
    dfs = {}
    stations_this_slug = df[df["slug"] == slug]["station"]
    for model_name in model_names:
        for key_variable in key_variables:
            stats_fnames = return_paths(slug, model_name, key_variable)
            dfout = load_ss(stations_this_slug.str.replace(".","_"), stats_fnames, model_name, key_variable)
            dfs[f"{model_name}_{key_variable}"] = dfout
    mindex = pd.MultiIndex.from_product([model_names, key_variables])
    data = pd.concat(dfs, axis=1).values
    dfalltemp = pd.DataFrame(data, index=stations_this_slug, columns=mindex)
    dfalls.append(dfalltemp)
dfall = pd.concat(dfalls, axis=0)
dfall[["lon","lat","date_time","slug"]] = df.set_index("station")[["lon","lat","date_time","slug"]]
dfall = dfall.reset_index().set_index(["station","lon","lat","date_time","slug"])
```

```{code-cell} ipython3
:tags: [remove-input]

cmap = cmocean.cm.curl
newcmap = cmocean.tools.crop_by_percent(cmap, 20, which='both', N=None)

inputs = dict(x="lon", y="lat", c="ss", hover_cols=["station","date_time","slug"])
plot_kwargs = dict(geo=True, tiles=True, size=100, width=600, height=700, clim=(-1,1), cmap=newcmap,
                  coastline="10m", xlabel="Longitude", ylabel="Latitude",
                  fontscale=1.5)
```

## Sea Temperature

```{code-cell} ipython3
:tags: [full-width, remove-input]

ivar = 0
key_variable, vardesc = key_variables[ivar], vardescs[ivar]

dfallsub = dfall.loc[:,(model_names,key_variable)]
clabel = f"Model skill scores for CTD profiles for {vardesc}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

temp = left + right
glue("temp", temp, display=False)
```

````{div} full-width                
```{glue:figure} temp
:name: "fig-overview-ctd-profiles-temp"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD profiles for sea temperature.
```
````

+++

## Salinity

```{code-cell} ipython3
:tags: [full-width, remove-input]

ivar = 1
key_variable, vardesc = key_variables[ivar], vardescs[ivar]

dfallsub = dfall.loc[:,(model_names,key_variable)]
clabel = f"Model skill scores for CTD profiles for {vardesc}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

salt = left + right
glue("salt", salt, display=False)
```

````{div} full-width   
```{glue:figure} salt
:name: "fig-overview-ctd-profiles-salt"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD profiles for salinity.
```
````
