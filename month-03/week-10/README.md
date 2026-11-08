# Week 10: GeoPandas

## What this folder contains
 - explore_pandas.py: first look at the ward population table.
 - filter_sort.py: filter,sort and add a column.
 - explore_layer.py: open a vector layer.
 - geom_props.py: look inside one geometry.
 - csv_to_points.py: turn a CSV of coordinates into points.
 - join_population.py: join population to wards,and fix what does not match.
 - make_map.py: draw a map and save it.
 - save_outputs.py: save outputs.

Outputs: facilities_map.png and wards_table.csv.

The first join matched 9 of 12 wards. After cleaning the names, it matched 12 of 12.



- my_explore.py: explores my main vector layer, including its geometry, CRS, and spatial bounds.
- my_points.py: cleans health facility point data by handling missing facility levels and standardising facility categories.
- my_join.py: joins health facility data to the Ife Central ward dataset.
- my_map.png: map of my study area generated using Python.

How to run it

From the repository root:

uv run month-03/week-10/my_explore.py
uv run month-03/week-10/my_points.py
uv run month-03/week-10/my_join.py

What I found

My main vector layer is in WGS 84 / UTM Zone 31N (EPSG:32631), so its spatial bounds are expressed in metres, with the bounding box spanning approximately 16 km across. In my health facility data, I replaced five missing facility-level values with "Unknown" and merged "Health Centre" with "Primary Health Centre" because both belong to the primary healthcare level.

I downloaded the GRID3 Ife Central ward dataset, which contains 11 wards. The join was successful, with every health facility matching its corresponding ward before cleaning.

What went wrong and how I fixed it

During my inspection in QGIS, I noticed that some ward boundaries extended beyond the Ife Central LGA boundary. I documented this observation for further investigation, as it may indicate a spatial boundary alignment issue.