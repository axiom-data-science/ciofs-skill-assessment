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

(page:overview_adcp)=
# Overview ADCP Data

[60MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/adcp.zip)

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

slugs = ["adcp_moored_noaa_coi_2005",
        "adcp_moored_noaa_coi_other",
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
                coastline=False, xlabel="Longitude", ylabel="Latitude", title="ADCP Moorings",
                width=600, height=700, marker="o")
labels_plot = df.hvplot.labels(x="lon", y="lat", text="station", geo=True, text_alpha=0.5,
            hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='10pt', text_color="k")

fmap = pts_plot * labels_plot
glue("fig_map", fmap, display=False)
```

````{div} full-width   
```{glue:figure} fig_map
:name: "fig-overview-adcp-map"

All ADCP deployments.
```
````

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, model_name, key_variable, which):
    paths = omsa.Paths(f"{slug}_{model_name}")
    if which == "tidal":
        stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}.yaml"))
    elif which == "subtidal":
        stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}_{which}.yaml"))
    return stats_fnames

def load_ss(index, stats_fnames, model_name, key_variable):
    ds = pd.Series(index=index, dtype=float)
    for stats_fname in stats_fnames:
        with open(stats_fname, "r") as stream:
            stats = yaml.safe_load(stream)
            ss = stats["ss"]["value"]
            mse = stats["mse"]["value"]
            if ss == 1.0 and np.isnan(mse):
                # import pdb; pdb.set_trace()
                ss = np.nan
            station = stats_fname.name.split(slug)[1].split(key_variable)[0].strip("_")
            ds.loc[station] = ss
    return ds
```

```{code-cell} ipython3
:tags: [remove-input]

model_names, key_variables, whichs = mu.models, ["speed","along","across"], ["tidal","subtidal"]

dfalls = []
for slug in slugs:
    dfs = {}
    stations_this_slug = df[df["slug"] == slug]["station"]
    for model_name in model_names:
        for key_variable in key_variables:
            for which in whichs:
                stats_fnames = return_paths(slug, model_name, key_variable, which)
                dfout = load_ss(stations_this_slug, stats_fnames, model_name, key_variable)
                dfs[f"{model_name}_{key_variable}_{which}"] = dfout
    mindex = pd.MultiIndex.from_product([model_names, key_variables, whichs])
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
plot_kwargs = dict(geo=True, tiles=True, size=200, width=600, height=700, clim=(-1,1), cmap=newcmap,
                  coastline="10m", xlabel="Longitude", ylabel="Latitude",
                  fontscale=1.5)
```

## Tidal

+++

### Horizontal Speed

```{code-cell} ipython3
:tags: [full-width, remove-input]

key_variable, which = "speed", "tidal"

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for ADCP moorings for {key_variable.lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

tidal_speed = left + right
glue("tidal_speed", tidal_speed, display=False)
```

````{div} full-width   
```{glue:figure} tidal_speed
:name: "fig-overview-adcp-tidal-speed"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with ADCP moorings for horizontal speed.
```
````

+++ {"tags": ["full-width"]}

### Along-Channel Velocity

```{code-cell} ipython3
:tags: [full-width, remove-input]

key_variable, which = "along", "tidal"

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for ADCP moorings for {key_variable.lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(), clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(), clabel=clabel)

tidal_along = left + right
glue("tidal_along", tidal_along, display=False)
```

````{div} full-width   
```{glue:figure} tidal_along
:name: "fig-overview-adcp-tidal-along"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with ADCP moorings for along-channel velocity.
```
````

+++

### Across-Channel Velocity

```{code-cell} ipython3
:tags: [full-width, remove-input]

key_variable, which = "across", "tidal"

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for ADCP moorings for {key_variable.lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(), clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),  clabel=clabel)

tidal_across = left + right
glue("tidal_across", tidal_across, display=False)
```

````{div} full-width   
```{glue:figure} tidal_across
:name: "fig-overview-adcp-tidal-across"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with ADCP moorings for across-channel velocity.
```
````

+++

## Subtidal

+++

### Horizontal Speed

```{code-cell} ipython3
:tags: [full-width, remove-input]

key_variable, which = "speed", "subtidal"

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for ADCP moorings for {which} {key_variable.lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(), clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(), clabel=clabel)

subtidal_speed = left + right
glue("subtidal_speed", subtidal_speed, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_speed
:name: "fig-overview-adcp-subtidal-speed"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with ADCP moorings for subtidal horizontal speed.
```
````

+++

### Along-Channel Velocity

```{code-cell} ipython3
:tags: [full-width, remove-input]

key_variable, which = "along", "subtidal"

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for ADCP moorings for {which} {key_variable.lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(), clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(), clabel=clabel)

subtidal_along = left + right
glue("subtidal_along", subtidal_along, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_along
:name: "fig-overview-adcp-subtidal-along"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with ADCP moorings for subtidal along-channel velocity.
```
````

+++

### Across-Channel Velocity

```{code-cell} ipython3
:tags: [full-width, remove-input]

key_variable, which = "across", "subtidal"

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for ADCP moorings for {which} {key_variable.lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(), clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(), clabel=clabel)

subtidal_across = left + right
glue("subtidal_across", subtidal_across, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_across
:name: "fig-overview-adcp-subtidal-across"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with ADCP moorings for subtidal across-channel velocity.
```
````
