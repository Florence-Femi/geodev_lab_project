import numpy as np
import rasterio

base = "data/raw/landsat/LC08_L2SP_190055_20250110_20250122_02_T1_SR_"

with rasterio.open(base + "B4.TIF") as src:
    red = src.read(1).astype("float32")
    profile = src.profile
with rasterio.open(base + "B5.TIF") as src:
    nir = src.read(1).astype("float32")

# Fill value is 0; mask it before applying the scale factor
# Scale to surface reflectance
red = red * 0.0000275 - 0.2
nir = nir * 0.0000275 - 0.2

# Valid reflectance is between 0 and 1; anything else is fill, shadow or edge noise
valid = (red > 0) & (red < 1) & (nir > 0) & (nir < 1)

ndvi = np.full(red.shape, np.nan, dtype="float32")
ndvi[valid] = (nir[valid] - red[valid]) / (nir[valid] + red[valid])

print("NDVI min:", np.nanmin(ndvi))
print("NDVI max:", np.nanmax(ndvi))
print("NDVI mean:", np.nanmean(ndvi))

profile.update(dtype="float32", nodata=np.nan, count=1)
with rasterio.open("data/processed/ndvi_20250110.tif", "w", **profile) as dst:
    dst.write(ndvi, 1)