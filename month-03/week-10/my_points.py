import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

table = pd.read_csv("health_facilities.csv")
print("Rows:", len(table))
print("Before cleaning:")
print(table["facility_type"].value_counts(dropna=False))

table["facility_type"] = table["facility_type"].str.strip()
table["facility_type"] = table["facility_type"].replace(
    {"Health Center": "Primary Health Center"}
)
table["facility_type"] = table["facility_type"].fillna("Unknown")

print("After cleaning:")
print(table["facility_type"].value_counts(dropna=False))

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)
print("CRS before:", facilities.crs)

boundary = gpd.read_file("data/processed/ife_central_boundary_utm31.gpkg")
facilities = facilities.to_crs(boundary.crs)
print("CRS after:", facilities.crs)

facilities.to_file("data/processed/my_facilities.gpkg", layer="my_facilities")

fig, ax = plt.subplots(figsize=(7, 8))
boundary.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_axis_off()
fig.savefig("month-03/week-10/my_map.png", dpi=150, bbox_inches="tight")
print("Check map saved")