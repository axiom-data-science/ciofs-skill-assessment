import intake

# I don't think we need this since the models are built into PTM

cat = intake.entry.Catalog()

# Old CIOFS hindcast
dataset_id = "ciofs_hindcast"
url = "/mnt/vault/ciofs/HINDCAST/ciofs_kerchunk.parq"
data = intake.readers.datatypes.HDF5(url)
initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
cat[dataset_id] = initial_reader
cat.aliases[dataset_id] = dataset_id

# New CIOFS freshwater
dataset_id = "ciofs_fresh"
url = "/home/kristen/projects/kerchunk_setup/ciofs_fresh_kerchunk.parq"
data = intake.readers.datatypes.HDF5(url)
initial_reader = data.to_reader("xarray:Dataset", engine="kerchunk", chunks={})
cat[dataset_id] = initial_reader
cat.aliases[dataset_id] = dataset_id

cat.to_yaml_file("models.yaml")