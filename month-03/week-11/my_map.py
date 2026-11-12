import geopandas as gpd
import matplotlib.pyplot as plt

wards = gpd.read_file("data/processed/my_wards_utm31.gpkg", layer="my_wards_utm31")
uncovered = gpd.read_file("data/processed/my_uncovered.gpkg", layer="my_uncovered")
facilities = gpd.read_file("data/processed/my_facilities.gpkg", layer="my_facilities")
boundary = gpd.read_file("data/processed/ife_central_boundary_utm31.gpkg")

fig, ax = plt.subplots(figsize=(7, 8))
boundary.plot(ax=ax, color="none", edgecolor="#C0392B", linestyle="--")
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
uncovered.plot(ax=ax, color="#D62828")
facilities.plot(ax=ax, color="#094923", markersize=10)
ax.set_title("Ife Central: areas beyond 2 km of a facility (red)")
ax.set_axis_off()

fig.savefig("month-03/week-11/my_map.png", dpi=150, bbox_inches="tight")
print("Map saved")