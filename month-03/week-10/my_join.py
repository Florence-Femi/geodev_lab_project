import pandas as pd
import geopandas as gpd

wards = gpd.read_file("data/processed/ife_central_wards.gpkg")
facilities = gpd.read_file("data/processed/my_facilities.gpkg", layer="my_facilities")

print("Ward polygons:", len(wards))
print("Ward names in layer:", sorted(wards["ward"]))
print("Ward names in facilities:", sorted(facilities["ward_standard"].unique()))

# Table: facilities per official ward
ward_counts = (
    facilities.groupby("ward_standard")
    .size()
    .reset_index(name="facilities_in_ward")
)
ward_counts.to_csv("month-03/week-10/ward_counts.csv", index=False)
print(ward_counts)
print("Total in table:", ward_counts["facilities_in_ward"].sum())

# First try: join the table onto the ward layer
first_try = wards.merge(
    ward_counts, left_on="ward", right_on="ward_standard", how="left"
)
matched = first_try["facilities_in_ward"].notna().sum()
print("Matched on first try:", matched, "of", len(wards))


def clean_key(text):
    return " ".join(str(text).strip().upper().replace("-", " ").split())


wards["join_key"] = wards["ward"].apply(clean_key)
ward_counts["join_key"] = ward_counts["ward_standard"].apply(clean_key)

joined = wards.merge(
    ward_counts[["join_key", "facilities_in_ward"]], on="join_key", how="left"
)
matched = joined["facilities_in_ward"].notna().sum()
print("Matched after cleaning:", matched, "of", len(wards))
print("Rows after join:", len(joined))

joined["facilities_in_ward"] = joined["facilities_in_ward"].fillna(0).astype(int)
print(joined[["ward", "facilities_in_ward"]])
print("Facilities counted:", joined["facilities_in_ward"].sum(), "of", len(facilities))

joined.to_file("data/processed/my_wards_joined.gpkg", layer="my_wards_joined")