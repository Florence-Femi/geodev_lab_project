# geodev_lab_project
## How accessible are health facilities to the population of Ife Central LGA ,Osun State,Nigeria ?

A twelve-month project with GeoDev Lab Africa, Cohort One.
See project-brief.md for full brief.

### Month 1 : GIS foundation and data ecosystem
Set up the GIS workflow in QGIS, acquired and assessed the GRID3 and OSM datasets,selected the GRID3 boundary, and prepared 
the Ife Central study layers through CRS checks,reprojection,clipping, and data documentation. The month concluded with a 
2 Km health-facility buffer and population coverage analysis to identify the proportion of the population located outside
the buffer,supported by a final map layout.

### Month 2 : development environment and early Python
- week 5: set up Python, VS Code and the terminal.
- week 6: set up the project with uv and added pandas. check.py prints the pandas version.
- week 7: analyse.py reads wards.csv,converts each area and classifies each ward.
- week 8: inspect_data.py summarises distance to ward boundary (dist_ward_grid3_bdry_km) and latitude in my GRID3 health facilities data for Ife Central.
- week 9: summary.py refactors my Week 8 inspection into read_rows, clean_values, summarise and summarise_all, and summarises dist_ward_grid3_bdry_km, latitude and longitude in my GRID3 health facilities data for Ife Central.

   ### Month 2 reflection
- Idea that finally clicked this month is the difference between print and return: return hands a result back so other code can use it, while print only shows it on the screen. 
- I can now use VS Code and the terminal with ease to write and run my scripts.
- Nothing from this month feels fuzzy.
- My capstone showed that only 17 of my 48 health facilities have a value in dist_ward_grid3_bdry_km, so that column does not have enough information to rely on, while latitude and longitude are complete.

### Month 3: geospatial Python and automation
- Week 10: GeoPandas. Loaded, checked, joined and mapped my wards layer in code.