import geopandas as gpd
from shapely.validation import explain_validity

wards = gpd.read_file("data/processed/ife_central_wards.gpkg")
boundary = gpd.read_file("data/processed/ife_central_boundary_utm31.gpkg")

for name, layer in [("wards", wards), ("boundary", boundary)]:
    invalid = (~layer.is_valid).sum()
    print(name, "invalid before:", invalid, "of", len(layer))
    for geom in layer.geometry[~layer.is_valid]:
        print("  Why:", explain_validity(geom))
    layer["geometry"] = layer.make_valid()
    print(name, "invalid after:", (~layer.is_valid).sum())
    print(name, "geometry types:", layer.geom_type.value_counts().to_dict())