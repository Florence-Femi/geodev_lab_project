import math
import rasterio

path = "data/raw/srtm_ife.tif"

with rasterio.open(path) as src:
    print("File:", path)
    print("Width x height:", src.width, "x", src.height)
    print("Bands:", src.count)
    print("Data type:", src.dtypes)
    print("CRS:", src.crs)
    print("Pixel size:", src.res)
    print("Bounds:", src.bounds)
    print("Nodata:", src.nodata)
    print("Transform:")
    print(src.transform)

    # Check: width x resolution should equal right minus left
    # (and height x resolution should equal top minus bottom)
    b = src.bounds
    x_size, y_size = src.res
    width_extent = src.width * x_size
    height_extent = src.height * y_size
    print()
    print("Width x pixel size:", width_extent, "| right - left:", b.right - b.left)
    print("Height x pixel size:", height_extent, "| top - bottom:", b.top - b.bottom)
    print("Width matches:", math.isclose(width_extent, b.right - b.left, rel_tol=1e-6))
    print("Height matches:", math.isclose(height_extent, b.top - b.bottom, rel_tol=1e-6))