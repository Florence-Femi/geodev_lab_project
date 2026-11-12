import geopandas as gpd

wards = gpd.read_file("data/processed/ife_central_wards.gpkg")
facilities = gpd.read_file("data/processed/my_facilities.gpkg", layer="my_facilities")
boundary = gpd.read_file("data/processed/ife_central_boundary_utm31.gpkg")

print("Wards CRS:", wards.crs)
print("Facilities CRS:", facilities.crs)
print("Boundary CRS:", boundary.crs)

print("Suggested UTM:", wards.estimate_utm_crs())

wards_utm = wards.to_crs(epsg=32631)
wards_utm["area_km2"] = wards_utm.area / 1_000_000
print(wards_utm[["ward", "area_km2"]].round(2))
print("Total ward area:", round(wards_utm["area_km2"].sum(), 2), "km2")
print("Boundary area:", round(boundary.area.sum() / 1_000_000, 2), "km2")

wards_utm.to_file("data/processed/my_wards_utm31.gpkg", layer="my_wards_utm31")
print("area_sqkm column total:", round(wards["area_sqkm"].sum(), 2), "km2")