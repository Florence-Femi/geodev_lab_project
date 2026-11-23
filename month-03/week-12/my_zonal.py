import geopandas as gpd
import numpy as np
import pandas as pd
import rasterio
from rasterio.mask import mask

wards_path = "data/processed/ife_central_wards.gpkg"   
ndvi_path = "data/processed/ndvi_20250110.tif"
name_col = "ward"                            

wards = gpd.read_file(wards_path)
print(wards.columns.tolist())

rows = []
with rasterio.open(ndvi_path) as src:
    wards = wards.to_crs(src.crs)
    print("Raster CRS:", src.crs)

    for _, w in wards.iterrows():
        out, _ = mask(src, [w.geometry], crop=True, nodata=np.nan, filled=True)
        vals = out[0]
        vals = vals[~np.isnan(vals)]
        rows.append({
            "ward": w[name_col],
            "mean_ndvi": float(vals.mean()) if vals.size else np.nan,
            "valid_pixels": int(vals.size),
        })

result = pd.DataFrame(rows).sort_values("mean_ndvi")
print(result)
result.to_csv("month-03/week-12/zonal_ndvi.csv", index=False)