import geopandas as gpd

wards = gpd.read_file("data/processed/my_wards_utm31.gpkg", layer="my_wards_utm31")
facilities = gpd.read_file("data/processed/my_facilities.gpkg", layer="my_facilities")
print("Same CRS:", wards.crs == facilities.crs)

wards["area_km2"] = wards.area / 1_000_000

reach = facilities[["geometry"]].copy()
reach["geometry"] = reach.buffer(2000)
reach = reach.dissolve()

uncovered = gpd.overlay(wards, reach, how="difference")
uncovered["uncovered_km2"] = uncovered.area / 1_000_000

gaps = uncovered[["ward", "uncovered_km2"]]
result = wards.merge(gaps, on="ward", how="left")
result["uncovered_km2"] = result["uncovered_km2"].fillna(0)
share = result["uncovered_km2"] / result["area_km2"] * 100
result["uncovered_pct"] = share.round(1)
print(result[["ward", "area_km2", "uncovered_km2", "uncovered_pct"]].round(2))

uncovered.to_file("data/processed/my_uncovered.gpkg", layer="my_uncovered")
print("Saved", len(uncovered), "uncovered pieces")