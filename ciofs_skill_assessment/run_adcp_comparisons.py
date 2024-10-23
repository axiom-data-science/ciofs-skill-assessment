import ocean_model_skill_assessor as omsa
# import ciofs_hindcast_report as chr
import intake
import cf_xarray as cfx
import cf_pandas as cfp

# import model_catalogs as mc
import xarray as xr
import pandas as pd

import extract_model as em
import xroms
import oceans.filters
import cmocean.cm as cmo
import cook_inlet_catalogs as cic


cat_model = intake.open_catalog("ciofs_skill_assessment/models.yaml")


slugs = [
    "adcp_moored_noaa_coi_2005",
    "adcp_moored_noaa_coi_other",
]

# run for both models
models = ["ciofs_hindcast", "ciofs_fresh"]
# key_variables=["speed","along","across"]

# ds.xroms.east_rotated(angle=-90, reference="compass", isradians=False, name="along_channel")
# key_variables = [[{"data": "speed", "accessor": "xroms", "function": "speed",},]]
# key_variables = [[{"data": "east", "accessor": "xroms", "function": "east",},]]
key_variables = [[
                # {"data": "along", "accessor": "xroms", "function": "east_rotated", "add_to_inputs": "angle", 
                #    "inputs": {"reference": "compass", "isradians": False, "name": "along_channel"}},
                # {"data": "across", "accessor": "xroms", "function": "north_rotated", "add_to_inputs": "angle", 
                #    "inputs": {"reference": "compass", "isradians": False, "name": "across_channel"}},
                {"data": "speed", "accessor": "xroms", "function": "speed",},
                  ]]
skip_key_variable_check = True
model_only = False
override_mask_lon = "lon_rho"
need_xgcm_grid=True
kwargs_xroms=dict(include_3D_metrics=True, include_Z0=True)
override_chunks = {"s_rho": 30, "s_w": 31}

# use wetdry False to force the use of mask_rho since ADCP would be put out
# where there is no wetting/drying
wetdry = False

# vardescs = ["Along-Channel Velocity"]
# vardescs = ["Along-Channel Velocity"]#, "Across-Channel Velocity", "Horizontal Speed"]
vardescs = ["Horizontal Speed"]
# vardescs = ["Across-Channel Velocity"]#, "Horizontal Speed"]

# apply subtidal filter across dataset
def subtidal_dataset(ds):
    import cf_xarray
    
    if isinstance(ds, xr.Dataset):
        for var in list(ds.data_vars):
            # apply to variable in Dataset if it has Time
            if len(cf_xarray.accessor._get_all(ds[var], "T")) > 0:
                ds[var] = oceans.filters.pl33tn(ds[var], mode="same")
    elif isinstance(ds, xr.DataArray) and "T" in ds.cf.axes:
        ds = oceans.filters.pl33tn(ds, mode="same")

    return ds


ts_mods = [
    [{"function": subtidal_dataset, "inputs": dict(), "name_mod": "subtidal",},],
          [],
          ]

xcmocean_options=dict(divin={'along': cmo.delta, 'across': cmo.delta}, 
                      regexin={'along': 'along', 'across':'across'}, 
                      seqin={'along': cmo.speed, 'across': cmo.speed})

kwargs_plot = dict(figsize=(20,6))

for slug in slugs:
    cat = intake.open_catalog(cic.utils.cat_path(slug))
    cat.metadata["name"] = slug

    for model in models:
        project_name = f"{slug}_{model}"
        kwargs_plot.update({"model_title": model.upper()})
        
        for ts_mod, ts_mod_name in zip(ts_mods, ["Subtidal","Tidal"]):

            for key_variable, vardesc in zip(key_variables,vardescs):
                plot_description = f"{ts_mod_name.capitalize()} {vardesc.lower()} from moored ADCP"
                
                if slug == "adcp_moored_noaa_coi_2005":
                    source_names = list(cat)
                elif slug == "adcp_moored_noaa_coi_other":
                    source_names = [name for name in list(cat) if "COI03" in name or "COI04" in name or "COI12" in name]
                
                omsa.run(project_name=project_name, catalogs=cat, model_name=cat_model,
                         preprocess=True,
                         vocabs=cic.utils.vocab,
                        #  vocabs=None,#"general", 
                         mode="a",
                         key_variable=key_variable, 
                         alpha=5, dd=5, 
                         interpolate_horizontal=False,
                         want_vertical_interp=True,
                         model_source_name=model,
                         catalog_source_names=source_names,
                         model_only=model_only,
                         # user_min_time=start_time_use, user_max_time=end_time_use,
                         check_in_boundary=False,
                         need_xgcm_grid=need_xgcm_grid,  
                         kwargs_xroms=kwargs_xroms,
                         ts_mods=ts_mod,
                         plot_map=False,
                         plot_count_title=False,
                         vocab_labels="vocab_labels",
                         xcmocean_options=xcmocean_options,
                         # override_model=False,
                         override_processed=True,
                         override_stats=True,
                         override_plot=True,
                         plot_description=plot_description,
                         kwargs_plot=kwargs_plot,
                         
                         skip_key_variable_check=skip_key_variable_check,
                         override_mask_lon=override_mask_lon,
                         override_chunks=override_chunks,
                         wetdry=wetdry,
                        )
