# Web Mapping of Health Facility Accessibility in Ife Central LGA, Osun State

## The question

How accessible are health facilities to the population of Ife Central LGA, Osun State, Nigeria?

## The data I need

- **Ife Central LGA boundary** — GRID3, NGA LGA Boundaries — GeoPackage — approximately 120 KB. The Ife Central LGA boundary was selected from the Nigeria-wide LGA boundary dataset.
  - Source: https://data.grid3.org/
- **Health facilities** — GRID3, Nigeria Health Facilities — GeoPackage — approximately 72 KB.
  - Source: https://data.grid3.org/
- **Population** — GRID3, NGA Population v3.0 Gridded — raster — approximately 44,661 KB (43.6 MB). The population raster was clipped to the Ife Central LGA boundary.
  - Source: https://data.grid3.org/
- **Road network** — OpenStreetMap (OSM), extracted using QuickOSM for Ife Central — vector layer — approximately 1,124 KB (1.1 MB).
  - Source: https://www.openstreetmap.org/

## Why I need these data

The LGA boundary defines the study area. Health-facility locations show where healthcare services are available, population data show where potential healthcare demand is concentrated, and the road network provides information for assessing physical accessibility to health facilities.

## What I expect to produce

The main output will be an **interactive web map** of health facility accessibility in Ife Central LGA. The web map will allow users to explore the LGA boundary, health facilities, population distribution, road network, and the results of the accessibility analysis. It will include appropriate map layers, symbology, and interactive information such as feature pop-ups. The analysis will help identify areas where access to health facilities may be relatively poor and provide a basis for highlighting potentially underserved areas.

## Data checks and limitations

The datasets were checked in QGIS before analysis. The LGA boundary and health-facility data use WGS 84 (EPSG:4326). The population raster was clipped to the Ife Central LGA boundary, and the road network was extracted for the study area using QuickOSM. The health-facility points will be spatially checked against the official Ife Central administrative boundary before the accessibility analysis.

The boundary represents the administrative extent of Ife Central LGA. Some health-facility points in the wider Ile-Ife area may therefore fall outside the study boundary and will not automatically be included in the analysis. The web map and its conclusions will depend on the completeness, positional accuracy, date, and coverage of the source datasets.
