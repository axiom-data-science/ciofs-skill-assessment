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

# Overview CTD Transects

In these CTD transect overview plots, each colored square marker represents a visit to the transect. The length of each transect was split into the number of visits with a square for each visit; if there were many repeat visits there are a lot of squares along a transect and only one for a single visit.

[244MB zipfile of plots](https://files.axds.co/ciofs_fresh/zip/ctd_transects.zip)

```{code-cell}
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
import fnmatch
from datetimerange import DateTimeRange
import more_utils as mu

years = [2003, 2004, 2005, 2006, 2012, 2013, 2014]
```

## Map of Stations

```{code-cell}
:tags: [remove-input]

slugs = [        "ctd_transects_barabara_to_bluff_2002_2003",
        "ctd_transects_cmi_kbnerr", 
        "ctd_transects_cmi_uaf",  
        "ctd_transects_gwa", 
        "ctd_transects_otf_kbnerr",
        "ctd_transects_uaf",  
        ]
# hand-selected source names to use since often repeated
source_names = {"ctd_transects_barabara_to_bluff_2002_2003": ["Cruise 1"],
                "ctd_transects_cmi_kbnerr": ["Cruise_14-Line_1",
                                             "Cruise_14-Line_2",
                                             "Cruise_14-Line_3",
                                             "Cruise_14-Line_4",
                                             "Cruise_14-Line_6",
                                             "Cruise_14-Line_7",
                                            "sue_shelikof"],
                "ctd_transects_cmi_uaf": ["Cruise-01"],
        "ctd_transects_gwa": ['transect_3-2012-05-02',
                              'transect_4-2012-05-02',
                              'transect_6-2012-05-03',
                              'transect_7-2012-07-30',
                              'transect_9-2012-02-14',
                              'transect_AlongBay-2012-08-15',], 
        "ctd_transects_otf_kbnerr": ['2003-07-01'],
        "ctd_transects_uaf": ['Transect_01'], 
               }
# hand-written names to label with
line_names = {"ctd_transects_barabara_to_bluff_2002_2003": ["Barabara to Bluff (repeated)"],
                "ctd_transects_cmi_kbnerr": ["CMI KBNERR: Line 1 (repeated)",
                                             "CMI KBNERR: Line 2 (repeated)",
                                             "CMI KBNERR: Line 3 (repeated)",
                                             "CMI KBNERR: Line 4 (repeated)",
                                             "CMI KBNERR: Line 6 (repeated)",
                                             "CMI KBNERR: Line 7 (repeated)",
                                            "CMI KBNERR: Sue Shelikof"],
                "ctd_transects_cmi_uaf": ["CMI UAF (repeated)"],
        "ctd_transects_gwa": ['GWA: Transect 3 (repeated)',
                              'GWA: Transect 4 (repeated)',
                              'GWA: Transect 6 (repeated)',
                              'GWA: Transect 7 (repeated)',
                              'GWA: Transect 9 (repeated)',
                              'GWA: Transect AlongBay (repeated)',], 
        "ctd_transects_misc_2002": ['Bear Jul 02',
                                     'Cohen',
                                     'Glacier',
                                     'Peterson Jul 02',
                                     'PtAdam Jul 02',
                                     'Pogibshi Jul 02'],
        "ctd_transects_otf_kbnerr": ['OTF KBNERR (repeated)'],
        "ctd_transects_uaf": ['UAF (repeated)'], 
               }

rows = []
for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    for source_name, station in zip(source_names[slug], line_names[slug]):
        # can't use min/max lon/lat because doesn't get orientation of transect correct
        dfd = cat[source_name].read()
        dfd = dfd.reset_index()
        minlon, maxlon = dfd.cf["longitude"].iloc[0], dfd.cf["longitude"].iloc[-1]
        minlat, maxlat = dfd.cf["latitude"].iloc[0], dfd.cf["latitude"].iloc[-1]
        midlon, midlat = 0.5*(minlon + maxlon), 0.5*(minlat + maxlat)
        if slug == "ctd_transects_cmi_kbnerr":
            # midlon += 0.01
            midlat += 0.03
        elif slug == "ctd_transects_gwa":
            midlat -= 0.025
        elif slug == "ctd_transects_otf_kbnerr":
            midlat -= 0.04
        # minlon, minlat = cat[source_name].metadata["minLongitude"], cat[source_name].metadata["minLatitude"]
        # maxlon, maxlat = cat[source_name].metadata["maxLongitude"], cat[source_name].metadata["maxLatitude"]
        start_time = cat[source_name].metadata["minTime"]
        rows.append([source_name, station, minlon, minlat, midlon, midlat, start_time, slug])
        rows.append([source_name, station, maxlon, maxlat, midlon, midlat, start_time, slug])
        rows.append([source_name, station, np.nan, np.nan, midlon, midlat, start_time, slug])
df = pd.DataFrame(rows, columns=["source_name", "station","lon","lat","midlon","midlat","date_time", "slug"])
```

```{code-cell}
:tags: [remove-input]

pts_plot = df.hvplot.paths(x="lon", y="lat", geo=True, tiles=True,
                                   #  # xlim=[-153, -150], ylim=[59,60], 
                                    # hover_cols=["station","date_time","slug"],
                                   legend=False, line_width=5, coastline=False, 
                                    xlabel="Longitude", ylabel="Latitude", 
                                    title="CTD Transects",
                                    width=600, height=700)
labels_plot = df.drop_duplicates(subset=["date_time"]).hvplot.labels(x="midlon", y="midlat", text="station", geo=True, text_alpha=0.5,
            hover=False, text_baseline='bottom', fontscale=1.5, text_font_size='10pt', text_color="k")

fmap = pts_plot * labels_plot
glue("fig_map", fmap, display=False)
```

````{div} full-width   
```{glue:figure} fig_map
:name: "fig-overview-ctd-transects-map"

All CTD transects (repeats indicated but not plotted).
```
````

```{code-cell}
:tags: [remove-input]

# hand-written globs to select transects
line_globs = {"ctd_transects_barabara_to_bluff_2002_2003": ["*"],
                "ctd_transects_cmi_kbnerr": ["*Line_1*",
                                             "*Line_2*",
                                             "*Line_3*",
                                             "*Line_4*",
                                             "*Line_6*",
                                             "*Line_7*",
                                            "*sue_shelikof*"],
                "ctd_transects_cmi_uaf": ["*"],
        "ctd_transects_gwa": ['*transect_3*',
                              '*transect_4*',
                              '*transect_6*',
                              '*transect_7*',
                              '*transect_9*',
                              '*transect_AlongBay*',], 
        "ctd_transects_misc_2002": ['*Bear_Jul-02*',
                                     '*Cohen*',
                                     '*Glacier*',
                                     '*Peterson_Jul-02*',
                                     '*PtAdam_jul-02*',
                                     '*pogibshi_Jul-02*'],
        "ctd_transects_otf_kbnerr": ['*'],
        "ctd_transects_uaf": ['*'], 
               }
```

```{code-cell}
:tags: [remove-input]

def return_paths(slug, model_name, key_variable, glob_source_names):
    # ctd_transects_barabara_to_bluff_2002_2003_Cruise 10_temp.yaml
    paths = omsa.Paths(f"{slug}_{model_name}")
    stats_fnames = []
    for source_name in glob_source_names:
        stats_fnames.extend(list(paths.OUT_DIR.glob(f"*{source_name}_{key_variable}.yaml")))
    return sorted(stats_fnames)

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

```{code-cell}
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

```{code-cell}
:tags: [remove-input]

# go through every cat
# read stats files for all sources by transect
# input them into temp dataframe tracking that
# get end points lon/lat from original df and calculate mid points, append to list, combine at the end

model_names, key_variables = mu.models, ["temp", "salt"]
vardescs = ["sea temperature", "salinity"]
mindex = pd.MultiIndex.from_product([model_names, key_variables])

slugs = [       
    "ctd_transects_barabara_to_bluff_2002_2003",
        "ctd_transects_cmi_kbnerr", 
        "ctd_transects_cmi_uaf",  
        "ctd_transects_gwa", 
        "ctd_transects_otf_kbnerr",
        "ctd_transects_uaf",  
        ]

dfs = {}
for model_name in model_names:
    for key_variable in key_variables:
        dfouts = []
        all_source_names, all_slugs, all_times = [], [], []
        all_lons, all_lats = [], []
        for slug in slugs:
            cat = intake.open_catalog(cic.utils.cat_path(slug))
            source_names = list(cat)
            skip_source_names = []
            # check which source_names from catalog are in time frame
            for source_name in source_names:
                minTime, maxTime = pd.Timestamp(cat[source_name].metadata["minTime"].replace("Z","")), pd.Timestamp(cat[source_name].metadata["maxTime"].replace("Z",""))
                if not station_intersect_with_years(minTime, maxTime):
                    # print(f"Skipping {source_name} because min time {minTime} and max time {maxTime} are not in {years}")
                    skip_source_names.append(source_name)
                    continue
            
            for lglob in line_globs[slug]:
                
                glob_source_names = fnmatch.filter(source_names,lglob)  # these are the source names for this part of dataframe
                # skip_source_names
                glob_source_names = sorted(list(set(glob_source_names) - set(skip_source_names)))
                all_source_names.extend(glob_source_names)
                all_slugs.extend([slug]*len(glob_source_names))
                all_times.extend([cat[source_name].metadata["minTime"][:13] for source_name in glob_source_names])
                stats_fnames = return_paths(slug, model_name, key_variable, glob_source_names)
                # stats_fnames = return_paths(slug, model_name, key_variable, lglob)
                # import pdb; pdb.set_trace()
                dfouttemp = load_ss(glob_source_names, stats_fnames, model_name, key_variable)
                
                whichrows = fnmatch.filter(df[df["slug"] == slug]["source_name"],lglob)
                
                lon_endpoints = df[df["source_name"].isin(whichrows)]["lon"].dropna().to_list()
                lat_endpoints = df[df["source_name"].isin(whichrows)]["lat"].dropna().to_list()
                lons = np.linspace(*lon_endpoints, len(glob_source_names))
                lats = np.linspace(*lat_endpoints, len(glob_source_names))

                if slug == "ctd_transects_cmi_kbnerr":
                    lats += 0.03
                elif slug == "ctd_transects_gwa":
                    lats -= 0.025
                elif slug == "ctd_transects_otf_kbnerr":
                    lats -= 0.04

                all_lons.extend(lons)
                all_lats.extend(lats)
                dfouts.append(dfouttemp)
        dfout = pd.concat(dfouts, axis=0)
        dfs[f"{model_name}_{key_variable}"] = dfout
    
data = pd.concat(dfs, axis=1).values
dfall = pd.DataFrame(data, index=all_source_names, columns=mindex)
dfall.index.name = "source_name"
dfall["lon"] = all_lons
dfall["lat"] = all_lats
dfall["date_time"] = all_times
dfall["slug"] = all_slugs
dfall = dfall.reset_index().set_index(["source_name","lon","lat","date_time","slug"])
```

```{code-cell}
:tags: [remove-input]

cmap = cmocean.cm.curl
newcmap = cmocean.tools.crop_by_percent(cmap, 20, which='both', N=None)

inputs = dict(x="lon", y="lat", c="ss", hover_cols=["source_name","date_time","slug"])
plot_kwargs = dict(geo=True, tiles=True, size=50, width=600, height=700, clim=(-1,1), cmap=newcmap,
                  coastline="10m", xlabel="Longitude", ylabel="Latitude",
                  fontscale=1.5, marker='s')
```

## Sea Temperature

```{code-cell}
:tags: [remove-input]

ivar = 0
key_variable, vardesc = key_variables[ivar], vardescs[ivar]

dfallsub = dfall.loc[:,(model_names,key_variable)]
clabel = f"Model skill scores for CTD transects for {vardesc}"

model_name = model_names[0]
left = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = model_names[1]
right = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

plot = left + right
glue("temp", plot, display=False)
```

````{div} full-width   
```{glue:figure} temp
:name: "fig-overview-ctd-transects-temp"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD transects for sea temperature.
```
````

+++

## Salinity

```{code-cell}
:tags: [remove-input]

ivar = 1
key_variable, vardesc = key_variables[ivar], vardescs[ivar]

dfallsub = dfall.loc[:,(model_names,key_variable)]
clabel = f"Model skill scores for CTD transects for {vardesc}"

model_name = model_names[0]
left = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                  title=model_name.upper(),clabel=clabel)
                           
model_name = model_names[1]
right = dfallsub.loc[:,(model_name,key_variable)].dropna().rename("ss").hvplot.points(**inputs, **plot_kwargs, 
                                                                                   title=model_name.upper(),clabel=clabel)

plot = left + right
glue("salt", plot, display=False)
```

````{div} full-width   
```{glue:figure} salt
:name: "fig-overview-ctd-transects-salt"

Skill scores for CIOFS Hindcast (left) and CIOFS Freshwater (right) with CTD transects for salinity.
```
````
