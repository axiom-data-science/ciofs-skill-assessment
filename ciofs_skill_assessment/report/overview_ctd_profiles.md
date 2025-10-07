---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: ciofs-freshwater-report
  language: python
  name: python3
---

# Overview CTD Profiles

CTD profiles are compared between data and each model and summarized on plots below by variable using the skill score. A higher skill score is better with 1 giving perfect skill.

Results show that CIOFS hindcast and CIOFS fresh have similar skill for temperature, but CIOFS fresh has better skill than CIOFS hindcast for salinity.

[122MB zipfile of plots and stats files](https://files.axds.co/ciofs_fresh/zip/ctd_profiles.zip)

```{code-cell} ipython3
:tags: [remove-input]

import intake
import numpy as np
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    import matplotlib.pyplot as plt
    import ocean_model_skill_assessor as omsa
import cook_inlet_catalogs as cic
import pandas as pd
import xarray as xr
import hvplot.pandas
import cmocean
import yaml
from myst_nb import glue
from datetimerange import DateTimeRange
from holoviews import opts
from bokeh.models import FixedTicker
import holoviews as hv
import os
from pathlib import Path
import subprocess


ins_type = "ctd_profiles"  # instrument name
models = ["ciofs_hindcast", "ciofs_fresh"]
years = [2003, 2004, 2005, 2006, 2012, 2013, 2014]
```

```{code-cell} ipython3
:tags: [remove-input]

def save_png(abs_path, figname):
    # Define the command and its arguments
    cmd = [
        "playwright",
        "screenshot",
        f"file://{abs_path}",
        f"{figname}.png",
        # "--full-page",
        "--wait-for-timeout=30000"
    ]

    # Run the command
    if not Path(f"{figname}.png").exists():
        result = subprocess.run(cmd, capture_output=True, text=True)
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
slug_names = {
    "ctd_profiles_2005_noaa": "NOAA 2005",
    "ctd_profiles_kachemack_kuletz_2005_2007": "Kachemak Kuletz 2005-2007",
    "ctd_profiles_kb_small_mesh_2006": "Kachemak Bay Small Mesh 2006",
}
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
        rows.append([source_name, lon, lat, pd.Timestamp(start_time), slug, slug_names[slug]])
df = pd.DataFrame(rows, columns=["station","lon","lat","date_time", "slug", "slug_names"])
df["slug_names"] = df["slug_names"].astype("category")
```

```{code-cell} ipython3
:tags: [remove-input, full-width]

figname = f"{ins_type}_map"
abs_path = os.path.abspath(f"{figname}.html")

fmap = df.hvplot.points(x="lon", y="lat", by="slug_names",
                legend="top_left", geo=True, tiles=True, size=40, hover_cols=["station","date_time"],
                coastline=False, xlabel="Longitude", ylabel="Latitude", title="CTD Profiles",
                width=600, height=700, marker="o", alpha=0.75, fontscale=1.25)
if not Path(f"{figname}.png").exists():
    hv.save(fmap, figname, fmt='html')
    save_png(abs_path, figname)

glue("fig_map", fmap, display=False)
```

```{glue:figure} fig_map
:name: "fig-overview-ctd-profiles-map"

All CTD profiles, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```

+++

````{div} full-width                
```{figure} ctd_profiles_map.png
:name: "fig-overview-ctd-profiles-map"

All CTD profiles, by project. (PNG screenshot, available for PDF and for saving image.)
```
````

+++

## Taylor Diagrams

Taylor diagrams summarize the skill of the two models in capturing the CTD profile datasets. The data has been grouped by region ({numref}`Fig. {number}<fig-ctd_profiles_by_region>`) and season ({numref}`Fig. {number}<fig-ctd_profiles_by_season>`). By region for temperature, CIOFS Fresh has higher skill than CIOFS Hindcast, either by a little or a lot, except CIOFS Hindcast performs much better for Upper Cook Inlet. By region for salinity, CIOFS Fresh has much too high of variability in Kachemak Bay and Upper Cook Inlet while CIOFS Hindcast has much too low variability. For other regions, CIOFS Fresh performs clearly better than CIOFS Hindcast except for outside of Cook Inlet, for which CIOFS Fresh actually performs similarly to CIOFS Hindcast and neither are good. By season, data is only available in spring and summer. CIOFS Fresh is better for temperature in spring but similar for summer. For salinity, CIOFS Fresh again has much too high variability and CIOFS Hindcast much too low.

Skill scores are shown in the next plots for each dataset.


```{figure} ../figures/taylor_diagrams/ctd_profiles_by_region.png
---
name: fig-ctd_profiles_by_region
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for temperature (left) and salinity (right), grouped by region of Cook Inlet, for CTD profiles datasets.
```


```{figure} ../figures/taylor_diagrams/ctd_profiles_by_season.png
---
name: fig-ctd_profiles_by_season
---
Taylor Diagram summarizing skill of CIOFS Hindcast (stars) and CIOFS Fresh (triangles) for temperature (left) and salinity (right), grouped by season, for CTD profiles datasets.
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, model_name, key_variable, stations_this_slug):
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = sorted(paths.OUT_DIR / f"{slug}_{station.replace('.', '_')}_{key_variable}.yaml" for station in stations_this_slug)
    # stats_fnames = sorted(paths.OUT_DIR.glob(f"*{key_variable}.yaml"))
    return stats_fnames

def load_ss(index, stats_fnames, key_variable):
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

model_names, key_variables = models, ["temp", "salt"]
vardescs = ["sea temperature", "salinity"]

dfalls = []
for slug in slugs:
    dfs = {}
    stations_this_slug = df[df["slug"] == slug]["station"]
    for model_name in model_names:
        for key_variable in key_variables:
            stats_fnames = return_paths(slug, model_name, key_variable, stations_this_slug)
            dfout = load_ss(stations_this_slug.str.replace(".","_"), stats_fnames, key_variable)
            dfs[f"{model_name}_{key_variable}"] = dfout
            # print(len(stations_this_slug), len(dfout), model_name, key_variable, slug)
    mindex = pd.MultiIndex.from_product([model_names, key_variables])
    data = pd.concat(dfs, axis=1).values
    dfalltemp = pd.DataFrame(data, index=stations_this_slug, columns=mindex)
    dfalls.append(dfalltemp)
dfall = pd.concat(dfalls, axis=0)
inds = ["lon", "lat", "date_time", "slug", "slug_names"]
dfall[inds] = df.set_index("station")[inds]
dfall = dfall.reset_index().set_index(["station", *inds])
```

```{code-cell} ipython3
:tags: [remove-input]

newcmap = cmocean.cm.matter

hovers = [("Slug", "@slug_names"),
          ("Station", "@station"),
          ("Time", "@date_time"),
          ("Longitude", "@lon"),
          ("Latitude", "@lat"),
          ("SS bin", "@ss_range"),
          ]
hover_cols = ["slug_names", "station", "date_time", "lon", "lat", "ss_range"]

# inputs = dict(x="lon", y="lat", c="ss", hover=False, by="slug_names",)
inputs = dict(x="lon", y="lat", c="ss_code", hover_cols=hover_cols, by="slug_names",)
plot_kwargs = dict(geo=True, tiles=True, size=100, width=600, height=700, clim=(0,1), cmap=newcmap,
                #   coastline="10m", 
                  xlabel="Longitude", ylabel="Latitude", legend="top_left",
                  fontscale=1.25)


# setup for changing colorbar from continuous to categorical
# which saves SO MUCH MEMORY
nbins = 11
cat_bins = np.linspace(0,1,nbins)
ticks = list(range(0,nbins))
tick_labels = {i: f"{i/(nbins-1):.1f}" for i in ticks}


opts_pts = hv.opts.Points(
    color_levels=10,
    clim=(0,10),
    colorbar_opts={'ticker': FixedTicker(ticks=ticks), 'major_label_overrides': tick_labels},
    tools=["hover"], hover_tooltips=hovers
    )
```

```{code-cell} ipython3
:tags: [remove-input]

def plot(model_name, key_variable, vardesc):
    clabel = f"Model skill scores for CTD profiles for {vardesc}"
    # dfallsub = dfall.loc[:,(model_names,key_variable)]
    dfallsubsub = dfall.loc[:,(model_name,key_variable)].dropna().rename("ss")
    cats = pd.cut(dfallsubsub, cat_bins).to_frame()
    cats["ss_code"] = cats["ss"].cat.codes
    cats["ss_range"] = cats["ss"].astype(str)

    # we plot the category codes but then label the colorbar correctly
    # so we don't have to plot a continuous colorbar with many levels
    return cats.hvplot.points(**inputs, **plot_kwargs, title=model_name.upper(), clabel=clabel).opts(opts_pts)
```

```{code-cell} ipython3
:tags: [remove-input]

def make_figures(key_variable, vardesc):
    figname = f"{ins_type}_{key_variable}"
    abs_path = os.path.abspath(f"{figname}.html")

    plots = []
    for model in models:
        plots.append(plot(model, key_variable, vardesc))

    variable_plot = plots[0] + plots[1]

    if not Path(f"{figname}.png").exists():
        hv.save(variable_plot, figname, fmt='html')
        save_png(abs_path, figname)

    return variable_plot, figname, abs_path
```

## Sea Temperature

```{code-cell} ipython3
:tags: [remove-input]

ivar = 0
key_variable, vardesc = key_variables[ivar], vardescs[ivar]

temp, figname, abs_path = make_figures(key_variable, vardesc)
glue("temp", temp, display=False)
```

````{div} full-width                
```{glue:figure} temp
:name: "fig-overview-ctd-profiles-temp"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD profiles for sea temperature, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```
````

+++

```{figure} ctd_profiles_temp.png
:name: "fig-overview-ctd-profiles-temp"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD profiles for sea temperature, by project. (PNG screenshot, available for PDF and for saving image.)
```

+++

## Salinity

```{code-cell} ipython3
:tags: [remove-input]

ivar = 1
key_variable, vardesc = key_variables[ivar], vardescs[ivar]

salt, figname, abs_path = make_figures(key_variable, vardesc)
glue("salt", salt, display=False)
```

````{div} full-width   
```{glue:figure} salt
:name: "fig-overview-ctd-profiles-salt"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD profiles for salinity, by project. Click on a legend entry to toggle the transparency. (HTML plot, won't show up correctly in PDF.)
```
````

+++

```{figure} ctd_profiles_salt.png
:name: "fig-overview-ctd-profiles-salt"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD profiles for salinity, by project. (PNG screenshot, available for PDF and for saving image.)
```
