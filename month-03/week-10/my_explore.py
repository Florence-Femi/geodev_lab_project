import geopandas as gpd

path = "data/processed/ife_central_boundary_utm31.gpkg"

print(gpd.list_layers(path))

layer = gpd.read_file(path)

print(layer.head())
print("Rows and columns:", layer.shape)
print(layer.geom_type.value_counts())
print("CRS:", layer.crs)
print("Bounds:", layer.total_bounds)
