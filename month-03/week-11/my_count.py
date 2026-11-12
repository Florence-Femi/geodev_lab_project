import geopandas as gpd

wards = gpd.read_file("data/processed/my_wards_utm31.gpkg", layer="my_wards_utm31")
facilities = gpd.read_file("data/processed/my_facilities.gpkg", layer="my_facilities")
print("Same CRS:", wards.crs == facilities.crs)

joined = gpd.sjoin(
    facilities, wards[["ward", "geometry"]], how="inner", predicate="within"
)
counts = joined.groupby("ward").size().rename("facility_count").reset_index()

result = wards.merge(counts, on="ward", how="left")
result["facility_count"] = result["facility_count"].fillna(0).astype(int)
print(result[["ward", "facility_count"]])

counted = result["facility_count"].sum()
print("Total counted:", counted, "of", len(facilities))
print("Facilities outside every ward:", len(facilities) - counted)

result.to_file("data/processed/my_ward_counts.gpkg", layer="my_ward_counts")