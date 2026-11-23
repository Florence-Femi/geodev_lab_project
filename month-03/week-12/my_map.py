import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
from rasterio.windows import from_bounds

wards_path = "data/processed/my_ward_counts.gpkg"   
ndvi_path = "data/processed/ndvi_20250110.tif"

wards = gpd.read_file(wards_path)

with rasterio.open(ndvi_path) as src:
    wards = wards.to_crs(src.crs)
    minx, miny, maxx, maxy = wards.total_bounds
    pad = 1000  # metres of margin around the wards
    win = from_bounds(minx - pad, miny - pad, maxx + pad, maxy + pad, src.transform)
    win = win.round_offsets().round_lengths()
    data = src.read(1, window=win)
    t = src.window_transform(win)

left = t.c
top = t.f
right = left + t.a * data.shape[1]
bottom = top + t.e * data.shape[0]

fig, ax = plt.subplots(figsize=(8, 8))
im = ax.imshow(data, extent=(left, right, bottom, top),
               cmap="RdYlGn", vmin=0, vmax=0.9)
wards.boundary.plot(ax=ax, color="black", linewidth=0.8)

for _, w in wards.iterrows():
    p = w.geometry.representative_point()
    ax.annotate(w["ward"], (p.x, p.y), fontsize=6, ha="center")

fig.colorbar(im, ax=ax, shrink=0.7, label="NDVI")
ax.set_title("NDVI, Ife Central wards (Landsat 8, 10 Jan 2025)")
ax.set_xlabel("Easting (m, EPSG:32631)")
ax.set_ylabel("Northing (m)")
fig.savefig("month-03/week-12/my_map.png", dpi=200, bbox_inches="tight")