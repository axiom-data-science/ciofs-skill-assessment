# Comparison skill assessment for two CIOFS hindcast models.

This project has the scripts and notebook/markdown report files to compare the performance of two hindcast versions of the Cook Inlet Operational Forecast System (CIOFS) ROMS model with data. The plots and pages from this project are in the report located at [ciofs-fresh.axds.co](https://ciofs-fresh.axds.co).


## Initial steps

Set up environment with `environment.yml`:

    mamba env create -f environment.yml

You can install the project with `pyproject.toml` file but I don't think this ends up being necessary.

## Run the comparison scripts

Activate environment with 

    conda activate ciofs-skill-assessment

The comparison scripts are located at `ciofs_skill_assessment/run_*.py`:
* `run_adcp_comparisons.py`
* `run_ctd_profiles_comparisons.py`
* `run_ctd_transects_comparisons.py`
* `run_hfradar_comparisons.py`
* `run_moorings_comparisons.py`
These scripts run [`ocean-model-skill-assessor`](https://github.com/axiom-data-science/ocean-model-skill-assessor) (OMSA) to compare each model with all of the available data from [`cook-inlet-catalogs`](https://github.com/axiom-data-science/cook-inlet-catalogs).


## Create the report pages


### Individual dataset pages

After the comparisons between the model and datasets have been run and plots have been made in the comparison step, the individual dataset pages can be created to show the plots together. These pages are created with the script `ciofs_skill_assessment/report/generate_comparison_pages.py`. Both notebooks and myst markdown files are made, but the myst markdown files are compiled by the Jupyter book ultimately.

Note that there is a variable in the script called `not_in_jupyter_book` that can be used to create either Markdown-friendly files for easy viewing when True or changed to False when ready to create files for the Jupyter book. These files use some syntax that cannot be viewed natively in Markdown but will work in Jupyter book.


### Overview pages

With the exception of the HF Radar overview page (which is made by `generate_comparison_pages.py` just discussed), the overview pages have been made manually originally as notebooks, then converted to Myst markdown files for compilation. They are made manually because they are difficult to generalize, though they are similar enough to copy and paste from each other as a starting point.


### HF Radar

The HF Radar data analysis has not been integrated as fully into OMSA as the other data types, partially due to it being a multidimensional vector and due to time constraints. Accordingly, some of the plots and analysis are run in separate files:
* `ciofs_skill_assessment/plot_hfradar_ss.py`
* `ciofs_skill_assessment/plot_tidal_ellipses.py`


## Now what?

Once these steps are complete, complete the other parts of the report. Then compile the Jupyter book report.