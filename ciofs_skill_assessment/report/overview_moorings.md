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

# Overview Mooring Data

In the map below, some stations are at the same or nearly same location, in which case the marker representing their location is shifted slightly to allow for both to be seen.

In the skill score plots below, datasets that span more than 1 year are represented by the number of years they span: one marker per year. By necessity these markers are moved in space from the actual station location and arranged into a grid so they can all be seen. Therefore, their locations in the skill score plots do not represent their actual locations.

[75MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/moorings.zip)

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

slugs = [        "moorings_aoos_cdip",
        "moorings_circac",
        "moorings_kbnerr",
        "moorings_kbnerr_bear_cove_seldovia",
        "moorings_kbnerr_historical",
        "moorings_kbnerr_homer",
        "moorings_noaa",
        "moorings_uaf",
        ]
rows = []
icount = 1
icount2 = 1
icount3 = 1
source_names_present = {}
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    source_names = list(cat)
    source_names_present[slug] = []
    for source_name in source_names:
        lon, lat = cat[source_name].metadata["minLongitude"], cat[source_name].metadata["minLatitude"]
        minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
        # data_time_range = DateTimeRange(minTime, maxTime)
        # not data_time_range.is_intersection(model_time_range)
        if not station_intersect_with_years(minTime, maxTime):
            # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
            continue
        # print(f"Adding {source_name} because min time {minTime} and max time {maxTime} are in {years}")
        source_names_present[slug].append(source_name)
        if "moorings_kbnerr_homer" in slug or "moorings_kbnerr_historical" in slug:
            # print(icount, source_name)
            if np.mod(icount, 2) == 0:  # even
                lat += icount*0.0025
            elif np.mod(icount, 2) == 1:  # odd
                lat -= icount*0.0025
            icount += 1
        elif "moorings_kbnerr_bear_cove" in slug:
            lat += icount2*0.0025
            icount2+= 1
        elif slug == "moorings_kbnerr":
            lat += icount3*0.0025            
            icount3+= 1
        start_time = cat[source_name].metadata["minTime"]
        rows.append([source_name, lon, lat, start_time, slug])
df = pd.DataFrame(rows, columns=["station","lon","lat","date_time", "slug"])
```

```{code-cell} ipython3
:tags: [remove-input, full-width]

pts_plot = df.hvplot.points(x="lon", y="lat", color="k",
                legend=False, geo=True, tiles=True, size=35, hover_cols=["station","date_time","slug"],
                coastline=False, xlabel="Longitude", ylabel="Latitude", title="Moorings",
                width=600, height=700, marker="o")
labels_plot = df.hvplot.labels(x="lon", y="lat", text="station", geo=True, text_alpha=0.5,
            hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='10pt', text_color="k")

fmap = pts_plot * labels_plot
glue("fig_map", fmap, display=False)
```

```{glue:figure} fig_map
:name: "fig-overview-moorings-map"

All mooring stations.
```

```{code-cell} ipython3
:tags: [remove-input]

def return_paths(slug, source_name, model_name, key_variable, which):
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = sorted(paths.OUT_DIR.glob(f"{slug}_{source_name}_{key_variable}{which}.yaml"))
    has_dates = False
    if len(stats_fnames) == 0:
        stats_fnames = sorted(paths.OUT_DIR.glob(f"{slug}_{source_name}_{key_variable}_????-??-??_????-??-??{which}.yaml"))
        has_dates = True
    return stats_fnames, has_dates

def load_ss(index, stats_fnames, model_name, key_variable):
    ds = pd.Series(index=index, dtype=float)
    for station, stats_fname in zip(index, stats_fnames):
        with open(stats_fname, "r") as stream:
            ss = yaml.safe_load(stream)["ss"]["value"]
            ds.loc[station] = ss
    return ds
```

```{code-cell} ipython3
:tags: [remove-input]

model_names, key_variables = ["ciofs_hindcast","ciofs_fresh"], ["ssh","temp","salt"]
whichs = ["_subtract-mean_subtidal", "_subtract-mean", "", "_subtidal_subtract-monthly-mean", "_subtidal"]

dfalls = []
all_slugs, all_times = [], []
all_lons, all_lats = [], []
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    dfs = {}
    # stations_this_slug = df[df["slug"] == slug]["station"]
    # every source_name needs lons/lats
    slug_lons, slug_lats = {}, {}
    for model_name in model_names:
        for key_variable in key_variables:
            for which in whichs:
                dfouts = []
                have_counted = False
                for source_name in source_names_present[slug]:
                    stats_fnames, has_dates = return_paths(slug, source_name, model_name, key_variable, which)
                    baselon = df[df["station"] == source_name]["lon"].iloc[0]
                    baselat = df[df["station"] == source_name]["lat"].iloc[0]
                    if has_dates:
                        # make a station name to represent each year of comparison
                        source_name_years = [f"{source_name}: {stats_fname.stem.split(f'{key_variable}_')[1][:4]}" for stats_fname in stats_fnames] 
                        dfout = load_ss(source_name_years, stats_fnames, model_name, key_variable)
                        
                        if len(dfout) > 1:
                            # calculate lon/lat locations
                            nrows = np.ceil(np.sqrt(len(dfout)))
                            ncols = nrows
                            Dlon = 1  # max overall delta lon
                            Dlat = 0.5  # max overall delta lat
                            dlat = Dlat/(nrows-1)  # delta per point
                            dlon = Dlon/(nrows-1)

                            dlats = np.linspace(0, Dlat, int(nrows)) - dlat
                            dlons = np.linspace(0, Dlon, int(ncols)) - dlon

                            Dlons, Dlats = np.meshgrid(dlons, dlats)

                            lon = (baselon + Dlons).flatten()[:len(dfout)]
                            lat = (baselat + Dlats).flatten()[:len(dfout)]
                        else:
                            lon = [baselon]
                            lat = [baselat]
                        
                    else:
                        dfout = load_ss([source_name], stats_fnames, model_name, key_variable)
                        lon = [baselon]
                        lat = [baselat]

                    if (len(dfout) > 0) and (source_name not in slug_lons.keys()):
                        slug_lons[source_name] = lon
                        slug_lats[source_name] = lat
                        
                    
                    dfouts.append(dfout)
                
                dfs[f"{model_name}_{key_variable}_{which}"] = pd.concat(dfouts, axis=0)
                
    mindex = pd.MultiIndex.from_product([model_names, key_variables, whichs])
    dfs_concat = pd.concat(dfs, axis=1)
    data = dfs_concat.values
    slug_times = []
    for source_name in source_names_present[slug]:
        # print(slug, source_name)
        # years
        rows_for_source_name = dfs_concat.index[dfs_concat.index.str.contains(source_name)]
        # if source_name == "kacsewq":
        #     import pdb; pdb.set_trace()
        if len(rows_for_source_name) > 1:
            new_times = rows_for_source_name.str[-4:]
            slug_times.extend(new_times)  # grab years from names
        else:
            new_times = [df[df["station"] == source_name]["date_time"].iloc[0][:13]]
            slug_times.extend(new_times)
    
    all_slugs.extend([slug]*len(dfs_concat))
    all_times.extend(slug_times)
    for source_name, lons in slug_lons.items():
        all_lons.extend(lons)
    for source_name, lats in slug_lats.items():
        all_lats.extend(lats)

    dfalltemp = pd.DataFrame(data, index=dfs_concat.index, columns=mindex)
    dfalls.append(dfalltemp)
dfall = pd.concat(dfalls, axis=0)
dfall.index.name = "station"

dfall["lon"] = all_lons
dfall["lat"] = all_lats
# dfall["date_time"] = all_times
dfall["slug"] = all_slugs
dfall = dfall.reset_index().set_index(["station","lon","lat","slug"])
# dfall = dfall.reset_index().set_index(["station","lon","lat","date_time","slug"])
```

```{code-cell} ipython3
:tags: [remove-input]

cmap = cmocean.cm.curl
newcmap = cmocean.tools.crop_by_percent(cmap, 20, which='both', N=None)

inputs = dict(x="lon", y="lat", c="ss", hover_cols=["station","date_time","slug"])
plot_kwargs = dict(geo=True, tiles=True, size=100, width=600, height=700, clim=(-1,1), cmap=newcmap,
                  coastline="10m", xlabel="Longitude", ylabel="Latitude",
                  fontscale=1.5)

vardescs = {"temp": "Sea temperature", "salt": "Salinity", "ssh": "Sea surface height"}
```

## Sea Surface Height

+++

### Full signal, mean subtracted

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "ssh", '_subtract-mean'

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings, {vardescs[key_variable].lower()}, minus mean"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

ssh = left + right
glue("tidal_ssh", ssh, display=False)
```

````{div} full-width   
```{glue:figure} tidal_ssh
:name: "fig-overview-moorings-tidal-ssh"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for sea surface height with mean subtracted.
```
````

+++

### Subtidal, mean subtracted

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "ssh", '_subtract-mean_subtidal'

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings, subtidal {vardescs[key_variable].lower()}, minus mean"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)
ssh = left + right
glue("subtidal_ssh", ssh, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_ssh
:name: "fig-overview-moorings-subtidal-ssh"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for subtidal sea surface height with mean subtracted.
```
````

+++

## Temperature

+++

### Full signal

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "temp", ''

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings for {vardescs[key_variable].lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

temp = left + right
glue("tidal_temp", temp, display=False)
```

````{div} full-width   
```{glue:figure} tidal_temp
:name: "fig-overview-moorings-tidal-temp"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for temperature.
```
````

+++

### Subtidal

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "temp", '_subtidal'

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings for subtidal {vardescs[key_variable].lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

temp_subtidal = left + right
glue("subtidal_temp", temp_subtidal, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_temp
:name: "fig-overview-moorings-subtidal-temp"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for subtidal temperature.
```
````

+++

### Subtidal with monthly-averaged climatology subtracted

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "temp", '_subtidal_subtract-monthly-mean'

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings for subtidal {vardescs[key_variable].lower()} anomaly"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

temp = left + right
glue("subtidal_temp_minus_clm", temp, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_temp_minus_clm
:name: "fig-overview-moorings-subtidal-temp-minus-clm"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for subtidal temperature anomaly.
```
````

+++

## Salinity

+++

### Full signal

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "salt", ''

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings for {vardescs[key_variable].lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

salt = left + right
glue("tidal_salt", salt, display=False)
```

````{div} full-width   
```{glue:figure} tidal_salt
:name: "fig-overview-moorings-tidal-salt"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for salinity.
```
````

+++

### Subtidal

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "salt", '_subtidal'

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings for subtidal {vardescs[key_variable].lower()}"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

salt_subtidal = left + right
glue("salt_subtidal", salt_subtidal, display=False)
```

````{div} full-width   
```{glue:figure} salt_subtidal
:name: "fig-overview-moorings-subtidal-salt"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for subtidal salinity.
```
````

+++

### Subtidal with monthly-averaged climatology subtracted

```{code-cell} ipython3
:tags: [remove-input]

key_variable, which = "salt", '_subtidal_subtract-monthly-mean'

dfallsub = dfall.loc[:,(model_names,key_variable,which)]
clabel = f"Model skill scores for moorings for subtidal {vardescs[key_variable].lower()} anomaly"

model_name = mu.models[0]
left = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = mu.models[1]
right = dfallsub.loc[:,(model_name,key_variable,which)].rename("ss").dropna().hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

salt = left + right
glue("subtidal_salt_minus_clm", salt, display=False)
```

````{div} full-width   
```{glue:figure} subtidal_salt_minus_clm
:name: "fig-overview-moorings-subtidal-salt-minus-clm"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with moorings for subtidal salinity anomaly.
```
````
