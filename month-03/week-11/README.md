# Week 11: CRS and spatial operations

## What this folder contains

### Guided Practical:
- area_wrong_and_right.py: area in degrees compared with area in square kilometres after reprojecting.
- set_vs_to.py: set_crs only changes the label, to_crs changes the coordinates.
- one_point.py: transform a single coordinate with pyproj.
- spatial_ops.py: buffer facilities and count them per ward.
- coverage_gap.py: find the parts of each ward more than 2 km from a facility.
- nearest.py: distance from each ward centre to the nearest facility.
- clip_dissolve.py: clip roads to one ward and dissolve wards into one LGA.
- fix_geometry.py: find and fix an invalid geometry.


### My own scripts, on my Ife Central data:

- my_crs.py: prints the CRS of each layer, reprojects the wards to EPSG:32631 and measures their area in km2.
- my_count.py: counts my 48 facilities in each of the 11 wards with sjoin and groupby, keeps wards with zero, and checks the total.
- my_reach.py: coverage gap. Buffers all 48 facilities by 2 km, dissolves the buffers and finds the ward area left uncovered.
- my_validity.py: counts invalid geometries in the wards and the LGA boundary, repairs them with make_valid and counts again.
- my_map.py: draws the uncovered areas in red over the wards, with the older LGA boundary and the facilities.

Outputs: my_map.png. Result layers in data/processed: my_wards_utm31.gpkg, my_wards_counts.gpkg and my_uncovered.gpkg.

## How to run it

From the repository root:

uv run month-03/week-11/my_crs.py
uv run month-03/week-11/my_count.py
uv run month-03/week-11/my_reach.py
uv run month-03/week-11/my_validity.py
uv run month-03/week-11/my_map.py

## What I found

CRS: My ward layer arrived in EPSG:4326 (degrees). I reprojected it to EPSG:32631 (WGS 84 / UTM zone 31N) before measuring, because estimate_utm_crs() suggested it and Ife lies in UTM zone 31N. UTM is in metres, so areas and buffers are real distances. My facilities and boundary layers were already in EPSG:32631.

Area: The 11 wards add up to 83.51 km2, and GRID3's own area_sqkm column gives 83.52 km2, so my reprojection agrees with the source. My Ife Central LGA boundary measures 143.2 km2.

Counts: 43 of my 48 facilities fall inside the 11 wards, and 5 fall outside every ward. Mooreojaja has the most (15). The five outside have ward_bdry values Moore (3), Moro (1) and Osu III (1). From the GRID3 map I checked, these are in Ife East, Ife North and Atakumosa West.

Distance: I used 2 km because I used the same distance in Month 1, so my results are comparable.

Coverage: About 25.1 km2 of the ward area is more than 2 km from a facility: 23.36 km2 in Iremo I (42.1% of the ward) and 1.75 km2 in Mooreojaja (12.0%). The other nine wards are fully covered.

Validity: Both layers had 0 invalid geometries before and after, so no repair was needed. All geometries are MultiPolygon.

## Limitation

The ward layer and the LGA boundary are two GRID3 layers that disagree. The wards (Operational Wards v4, data updated 20 October 2026) cover 83.5 km2, while the LGA boundary (data updated 4 September 2025) covers 143.2 km2. They overlap by only about 71 km2, and on the GRID3 map I saw Ife North wards over the northern part of the old Ife Central boundary. GRID3's pages do not say why they differ, so I cannot say which layer is correct. This means my per-ward counts and coverage results describe only the 83.5 km2 that the wards cover, and the 25.1 km2 uncovered area is probably too small for the whole LGA, because the northern part has no wards to measure. It is also an area share, not a population share, so I cannot compare it with my Month 1 result of 6.83%, which used the older boundary. Finally, a 2 km straight-line buffer ignores roads and rivers, so real travel distances are longer.

## Data credit

Ward and LGA boundaries: GRID3 Nigeria. The wards are licensed CC BY-SA 4.0 and the LGA boundary CC BY 4.0.