# Data notes

## GRID3 Nigeria Health Facilities

- Source: https://data.grid3.org.
- Downloaded: 9-4-2026.
- 48 features, points.
- Columns: fid, OBJECTID, unique_id, latitude, longitude, country, iso, state_standard, lga_standard, ward_standard,
  ward_bdry, ward_in_grid3_ward_list, facility_name, alt_name, settlement_name, facility_level, facility_type,
  facility_ownership, facility_ownership_type, functional, date_created, sett_ext_type, mgrs_code, input_data_record_ids, 
  input_data_sources, nhfr_facility_code, gps_accuracy, sett_ext_dist_km, dist_ward_grid3_bdry_km, flag1, flag2, flag3,
  flag4, flag5, flag6, issues, flag_count.
- Nulls: alt_name has some nulls; settlement_name and nhfr_facility_code are completely blank; gps_accuracy has some nulls; 
  dist_ward_grid3_bdry_km is mostly null; flag1–flag6 are mostly or completely null.
- Coverage looks correct for the study area.

## Roads

- Source: OpenStreetMap (OSM), downloaded using QuickOSM.
- Downloaded: 9-4-2026.
- Road features, lines.
- Columns: fid, full_id, osm_id, osm_type, highway, surface, covered, track_type, maxspeed, service, layer, bridge, 
  lane_markings, residential, junction, width, sidewalk, ref, one_way, foot, and others.
- Nulls: covered, track_type, maxspeed, service, layer, bridge, lane_markings, residential, junction, width, sidewalk, ref,
  one_way, foot, and other road attribute fields contain null values.
- Coverage looks correct for the study area.

## NGA_LGA_Boundaries

- Source: GRID3.
- Downloaded: 9-4-2026.
- 1 feature, polygon.
- Columns: FID, globalid, uniq_id, timestamp, editor, lganame, lgacode, statename, statecode, source, map code.
- Nulls: no null feature.
- Coverage looks correct for the study area.

  ## CRS and preparation

- All source layers arrived in EPSG:4326.
- Study area: Ife Central, extracted from GRID3 LGA boundary (lgacode 30011).
- Layers clipped to study area in EPSG:4326, then reprojected to EPSG:32631 (UTM 31N).
- Working files: data/processed/ife_central_boundary_utm31.gpkg,
  data/processed/roads_ife_central_utm31.gpkg,
  data/processed/health_facilities_utm31.gpkg.
- Area check: Ife Central boundary = 143.21 km2 (area_wrong and area_m2 identical —
  QGIS computes ellipsoidal area regardless of layer CRS; reprojection still applied
  as standard practice).
- Sanity check: published estimates for Ife Central LGA area range from ~ 111 km2 to 136.3 km2 depending on source
  (wikipedia/general web sources). The GRID3-derived boundary used here gives 143.21 km2, slightly above thisvrange but
  in the same order of magnitude.
- Raw files in data/raw/ untouched.

## Week 10: GeoPandas data

### Starter data (from Classroom, guided practical)
- ward_population: ward-level population table (12 wards), used for the join practice. In the guided practical the first join matched 9 of 12 wards, and after cleaning the ward names it matched 12 of 12.
- health_facilities.csv: facility table with coordinates, used in csv_to_points.py.
- Location: data/raw/
- Guided outputs: facilities_map.png and wards_table.csv (month-03/week-10/)

### GRID3 Operational Wards v4 (Ife Central)
- Source: GRID3 Nigeria, Operational Wards v4, downloaded for Ife Central LGA
- Content: 11 wards, ward names in the `ward` column
- File: ife_central_wards.gpkg
- CRS: EPSG:4326 as downloaded (reprojected to EPSG:32631 for analysis)
- Date downloaded: 8 Nov 2026
- Location in repo: data/processed/
- Notes: the layer was last updated by GRID3 on 20 Oct 2026. In QGIS some ward boundaries extended beyond the Ife Central LGA boundary, which I recorded for further investigation.

### My health facility data (cleaned)
- Source: GRID3 health facilities, 48 points, from Month 1 (health_facilities.csv)
- Cleaning in my_points.py:
  - 5 missing facility levels labelled "Unknown"
  - "Health Centre" merged into "Primary Health Centre" (both are primary healthcare level), giving 22 Primary Health Centres
- CRS: EPSG:32631

### Derived data (Week 10)
- data/processed/my_ward_counts.gpkg: ward layer with a `facility_count` column (health facilities per ward), made by my_join.py
- month-03/week-10/my_map.png: map of the study area made in Python

## Week 11: CRS and spatial operations data

### Layers used (no new downloads this week)
- GRID3 Operational Wards v4 (ife_central_wards.gpkg): 11 wards, data updated 20 Oct 2026, license CC BY-SA 4.0. Arrived in EPSG:4326 (degrees) and was reprojected to EPSG:32631 before measuring.
- GRID3 operational LGA boundary (Ife Central): data last updated 4 Sept 2025, license CC BY 4.0, 143.2 km2. Already in EPSG:32631.
- Health facilities (48 points): already in EPSG:32631.
- Credit: ward and LGA boundaries are from GRID3 Nigeria.

### CRS and area checks
- Working CRS: EPSG:32631 (WGS 84 / UTM zone 31N), chosen because estimate_utm_crs() suggested it and Ife lies in UTM zone 31N. Units are metres, so areas and buffers are real distances.
- The 11 wards total 83.51 km2, and GRID3's own area_sqkm column gives 83.52 km2, so the reprojection agrees with the source.
- Validity: 0 invalid geometries in both layers before and after make_valid, so no repair was needed. All geometries are MultiPolygon.

### Known data issue: ward layer and LGA boundary disagree
- The wards (83.5 km2, updated 20 Oct 2026) and the LGA boundary (143.2 km2, updated 4 Sept 2025) overlap by only about 71 km2.
- On the GRID3 map, Ife North wards sit over the northern part of the old Ife Central boundary. GRID3's pages do not explain the difference, so it is unconfirmed which layer is correct.
- Effect: per-ward counts and coverage results describe only the 83.5 km2 the wards cover. The uncovered area is probably too small for the whole LGA.

### Derived data (Week 11, in data/processed/)
- my_wards_utm31.gpkg: wards reprojected to EPSG:32631
- my_ward_counts.gpkg: wards with facility counts per ward (the same file as in Week 10; Week 11 results: 43 of 48 facilities fall inside the wards; 5 fall outside every ward, with ward_bdry values Moore (3), Moro (1) and Osu III (1); Mooreojaja has the most, 15)
- my_uncovered.gpkg: ward area more than 2 km from a facility (about 25.1 km2 in total: Iremo I 23.36 km2 or 42.1% of the ward, Mooreojaja 1.75 km2 or 12.0%; the other nine wards are fully covered)
- month-03/week-11/my_map.png: uncovered areas in red over the wards, with the older LGA boundary and the facilities
- Buffer distance: 2 km straight line, the same as Month 1, so results are comparable. It ignores roads and rivers.

## Week 12: raster data (downloaded 2026-11-23)

### Landsat surface reflectance
- Product: Landsat 8 OLI/TIRS Collection 2 Level-2 (surface reflectance)
- Scene ID: LC08_L2SP_190055_20250110_20250122_02_T1
- Path/row: 190 / 055
- Date acquired: 2025-01-10 (dry season)
- Land cloud cover: 0.22%
- Bands downloaded: SR_B4 (red) and SR_B5 (near-infrared)
- Source: USGS EarthExplorer (earthexplorer.usgs.gov)
- Location in repo: data/raw/landsat/ (not uploaded to GitHub)
- Notes: values are scaled integers; convert with value x 0.0000275 - 0.2. Raw value 0 is fill.

### Elevation (DEM)
- Product: SRTM 1 Arc-Second Global
- Tile: N07E004, version 3 (covers 7-8 degrees N, 4-5 degrees E)
- Original file name: n07_e004_1arc_v3.tif
- Format: GeoTIFF, int16, 3601 x 3601 pixels, EPSG:4326, pixel size 0.000278 degrees (about 30 m)
- Nodata value: -32767
- Source: USGS EarthExplorer
- Location in repo: data/raw/srtm_ife.tif (renamed so it does not overwrite the teaching dem.tif; not uploaded to GitHub)

### Derived data (Week 12)
- data/processed/ndvi_20250110.tif: NDVI from SR_B4 and SR_B5 (pixels with reflectance outside 0 to 1 masked; values between -0.12 and 0.9999)
- month-03/week-12/zonal_ndvi.csv: mean NDVI per ward, using data/processed/my_ward_counts.gpkg as the zones
- month-03/week-12/my_map.png: NDVI map with ward boundaries