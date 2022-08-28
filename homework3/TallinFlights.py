import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cf
from matplotlib import pyplot as plt

"""
https://www.adamsmith.haus/python/answers/how-to-get-rows-from-a-dataframe-that-are-not-in-another-dataframe-in-python
dataframe1 = pd.DataFrame(data={"column1": [1, 2, 3, 4, 5]})
dataframe2 = pd.DataFrame(data={"column1": [1, 2, 6]})

#common flights, current flights active
common = dataframe1.merge(dataframe2, on=["column1"])
#flights from the past
result = dataframe1[~dataframe1.column1.isin(common.column1)]

#new flights
result2 = dataframe2[~dataframe2.column1.isin(common.column1)]

common.insert(loc =1, column='active', value= False)
print(common)
result.insert(loc =1, column='active', value= True)
#result['active'] = False
print(result)

result2.insert(loc =1, column='active', value= True)
print(result2)
"""

flights = pd.read_csv('flightsPreCovid.csv', sep=';')

active_flights = pd.read_csv('flights22.csv', sep=';')

# Common flights will be active flights
common = flights.merge(active_flights, on=["IATA", "City"])
common.insert(loc=2, column='active', value=True)

# Flights that are no longer happening
flightsNotLongerUsed = flights[~flights.IATA.isin(common.IATA)]
flightsNotLongerUsed.insert(loc=2, column='active', value=False)

# Flights that are new Flights
flightsNew = active_flights[~active_flights.IATA.isin(common.IATA)]
flightsNew.insert(loc=2, column='active', value=True)

totalFlights = pd.concat([common, flightsNotLongerUsed, flightsNew], ignore_index=True, sort=False)

airports = pd.read_csv('airports.dat')
totalFlights = pd.merge(totalFlights, airports[['IATA', 'Latitude', 'Longitude']], on="IATA")

proj = ccrs.Miller()
ax = plt.axes(projection=proj)
ax.set_extent([-30, 70, 10, 70], crs=ccrs.PlateCarree())
ax.stock_img()
ax.add_feature(cf.COASTLINE, lw=2)
ax.add_feature(cf.BORDERS)
# Make figure larger
plt.gcf().set_size_inches(20, 10)

plt.title('Author: Carlos Rodriguez, RED: Cancelled flights, GREEN: Active flights',
          font={'family': 'sans-serif', 'weight': 'bold', 'size': 15})

i = 0

while i < 58:

    if totalFlights.active[i] == True:

        plt.plot([totalFlights.Longitude[0], totalFlights.Longitude[i]],
                 [totalFlights.Latitude[0], totalFlights.Latitude[i]],
                 color='green', linewidth=1.5, marker='o', markersize=3,
                 transform=ccrs.PlateCarree())

    else:

        plt.plot([totalFlights.Longitude[0], totalFlights.Longitude[i]],
                 [totalFlights.Latitude[0], totalFlights.Latitude[i]],
                 color='red', linewidth=1.5, marker='o', markersize=3,
                 transform=ccrs.PlateCarree())

    plt.text(totalFlights.Longitude[i] - 0.3, totalFlights.Latitude[i] - 0.5, totalFlights.IATA[i],
             horizontalalignment='right',
             font={'family': 'sans-serif', 'weight': 'bold', 'size': 5},
             transform=ccrs.Geodetic())

    i += 1

if __name__ == "__main__":
    #print(totalFlights)
    plt.show()
    #plt.savefig("TallinFlights.png")
