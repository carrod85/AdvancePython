# Homework 3

The aim of the homework is to practice working with the graphical environment and data and to combine data from different sources. The aim is also to learn how to install packages in more complex cases.

The task is to draw direct flights departing from Tallinn Airport on the map of Europe before and at the time of the covid-19. The OpenFlights Airports Database https://openflights.org/data.html has over 14,000 airports worldwide, but there are only a few dozen scheduled flights from Tallinn.

Airport data with geographical coordinates
https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat (without column headings)

or
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/airports.dat (with column headings).

Pre-covid-19 direct flights departing from Tallinn:
http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/otselennud.csv

Direct flights departing from Tallinn in February 2022 are included in the compressed file.

Based on these three tables, and using Python's cartography (eg cartopy) and drawing packages (eg matplotlib), a map of Europe must be created and the map must show one-color airports to which pre-covid and current colors can be flown from Tallinn. It is worth noting that due to the peculiarities of depicting the curvature of the globe, a geographical shortcut on a two-dimensional map is not a straight line, but a curve.

The created program must draw the map both on the screen and save it as a file (png, jpg, pdf or some other format) similar to the basic example: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.png The map must include the title and author's name. Other designs are at your choice.

The same data and sample files are also compressed in the task attachment.

Please upload the code and the image to Moodle.

-------------------------
How to do?
It is probably expedient to add coordinates to the table of direct flights departing from Tallinn.

One way (probably the best way) to do this is to use the 'pandas' library by importing the csv files (pandas.read_csv) and then merge. The common field is called 'IATA'. Note that one file has a comma separator in the field and a semicolon in the other.

Importing Pandas csv https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

An example of a table with aggregated data is: http://enos.itcollege.ee/~eikivi/python/kaug6pe/Koduylesanne3/lennud.txt This is an example, do not use it!

Some references:

https://scitools.org.uk/cartopy/docs/latest/installing.html

Installing Cartopy with the help of Conda.

Drawing maps (contour maps, etc.). Drawing flight paths.

https://scitools.org.uk/cartopy/docs/latest/matplotlib/intro.html

How to draw Europe map using Cartopy: https://techoverflow.net/2021/04/25/how-to-draw-europe-map-using-cartopy/

Further reading:

https://matplotlib.org/basemap/users/geography.html
https://matplotlib.org/basemap/users/installing.html
https://matplotlib.org/basemap/users/intro.html
https://towardsdatascience.com/planning-to-travel-around-the-world-with-python-42fac1d21a6e
https://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py

It is not necessary to use the above libraries, others can be used of your choice, the result is important.