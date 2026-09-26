 # Month 1 Summary

## Question:
What proportion of Ife Central's population falls outside a 2km buffer 
of the nearest health facility?

## Operation used:
Buffer (2km, dissolved) on health_facilities_utm31, followed by a 
Difference operation against the LGA boundary to isolate the uncovered 
area, then population raster statistics (sum) on both the total and 
uncovered population rasters to calculate the proportion.

## What I expected
I expected facility buffers to cluster around the built-up central/eastern 
part of Ife Central, where most facilities are concentrated, leaving 
western and southern parts of the LGA with population but no nearby 
coverage.

## What I got
Total population (population_clipped_utm31): 278,466.44
Uncovered population (population_uncovered_utm31): 19,028.70
Proportion outside 2km coverage: ~6.83%
So roughly 93% of the population lives within 2km of a health facility.

## What surprised me
Coverage turned out much better than expected — I predicted more 
significant gaps, especially in the north, but the dissolved buffer 
actually covers the vast majority of the built-up/populated area. The 
uncovered zone is smaller than anticipated, concentrated mainly in the 
less populated northern section of the LGA.

Also unexpected: reprojecting the boundary layer to EPSG:32631 produced 
an identical area value to the EPSG:4326 calculation (both 143.21 km2), 
because current QGIS computes ellipsoidal area by default regardless of 
layer CRS — this differs from older QGIS behaviour, where a geographic 
CRS would return a meaningless square-degrees value.

## What data I still need
- A more precise population figure to sanity-check against (e.g., 
  census/NPC ward-level population for Ife Central) to confirm the raw 
  population raster sums are plausible
- Facility-type/capacity data (e.g., primary health center vs. hospital) 
  would let the accessibility question distinguish between basic and 
  higher-level care access, rather than treating all 48 facilities equally
- Road network travel-time data, to eventually move from simple 
  straight-line buffers to a more realistic network-based accessibility 
  analysis
