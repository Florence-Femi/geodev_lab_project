import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    values = []
    for row in rows:
        raw = row[column].strip()
        if raw == "":
            continue
        values.append(float(raw))
    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }

dist_result = inspect_column("health_facilities.csv", "dist_ward_grid3_bdry_km")
lat_result = inspect_column("health_facilities.csv", "latitude")

print("Distance to ward boundary (km):", dist_result)
print("Latitude:", lat_result)