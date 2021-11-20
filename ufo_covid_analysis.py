#  _,~-'
#    \ \
#     \ \  ,                     .-"""-.
#     _,~-'\                   /        \
#    '\     \                 /_        _\
#      \     \               // \     / \ \
#       \     \             | \__\   /__/ |
#        \_,~-'\            \     ||     /
#         \_,~-'\            \          /
#          \_,~-'\             \  __  /
#           \_,~-'              '.__.'
#               \
#                \
#                 \
#                  \
#                   \


#Python Libraries
import argparse
import sys
import matplotlib.pyplot as plt
import folium as fl
from folium import plugins
from folium.plugins import HeatMap
#Python Modules
import ufo_data as ufo
import covid_vaccinations as covid
import lat_lon as ll


#Creates parser for command line arguements
parser = argparse.ArgumentParser(description="Parse arguements to filter and combine both data sets")
parser.add_argument('-c', '--city', action='store_true', dest = "ufo_state", help="Flags if UFO data is mapped by city or by state")
parser.add_argument('-s', '--shape', choices=['cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball',
                                              'unknown', 'oval', 'other', 'cigar', 'rectangle', 'chevron',
                                              'triangle', 'formation', 'N/A', 'delta', 'changing', 'egg',
                                              'diamond', 'flash', 'teardrop', 'cone', 'cross', 'pyramid',
                                              'round', 'crescent', 'flare', 'hexagon', 'dome', 'changed',
                                              'all'], dest='ufo_shape', type=str, help="Filters UFO type")
parser.add_argument('-v','--vaccine',)
parser.add_argument('-t','--time',)

#Color for map inputs
parser.add_argument('-p','--palette', choices=['BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 
                                               'RdPu', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'],
                    nargs=2, default=['PuRd','BuGn'], dest="colors", help="Picks the Color palette for the map")
parser.add_argument('-l','--location',type=str,dest = "state")
args = parser.parse_args()

## Insert & Clean UFO Data
#Filtering UFO data based off command line arguements and ufo_data module functions
if ("-c" in str(sys.argv)):
    ufo_df = ufo.ufo_data_clean("ufo_sighting_data.csv","state_lat_long.csv", False)
    ufo_df = ufo.ufo_counts(ufo_df,True)
else:
    ufo_df = ufo.ufo_data_clean("ufo_sighting_data.csv","state_lat_long.csv", True)
    ufo_df = ufo.ufo_counts(ufo_df,False)
    
if ("-s" in str(sys.argv)) and (args.ufo_shape.lower() != 'all'):
    ufo_df = ufo.ufo_type(ufo_df,args.ufo_shape.lower())

ufo_df = ufo.shape_counts(ufo_df)
#UFO Plots
ufo_plt_1 = plt.figure(1)
cluster_plt = ufo.shape_plot(ufo_df,False)
plt.title("3 Cluster Plot For K-Values of UFO Type and UFOs per State")
ufo_plt_2 = plt.figure(2)
plt.figure(figsize=(12, 4))
bar_plt = ufo.state_plot(ufo_df)
plt.xticks(rotation=90)
plt.title("UFO Sightings Per State")
plt.show()

## Instert & Clean Vaccine Data
#Filtering Vaccine data based off command line arguements and ___ module functions


## Map building with Folium
#latitude and longitude variables for folium map
#add latitude & longitude chooser
lat, lon = ll.get_lat_lon(str(args.state),"state_lat_long.csv")
#Creates Map
map_usa = fl.Map(location=[lat,lon],zoom_start=3)
#UFO map data section
if ("-c" in str(sys.argv)):
    #Creates Heat Map overlay on built map of UFO information
    heat_data = [[row['latitude'],row['longitude']] for index, row in ufo_df.iterrows()]
    HeatMap(heat_data, name="UFOs",min_opacity=0, radius=20,blur=0).add_to(map_usa)
else:
    #Creates Choropleth over on built map for the USA
    #builds state lines
    url = (
        "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
    )
    state_geo = f"{url}/us-states.json"


    fl.Choropleth(
    
          # geographical locations
        geo_data = state_geo,                     
        name = "test",
    
          # the data set we are using
        data = ufo_df,                        
        columns = ["state_upper", "ufo_count"],
    
          # YlGn refers to yellow and green
        fill_color = str(args.colors[0]),                      
        fill_opacity = 0.7,
        line_opacity = .1,
          key_on = "feature.id",
        legend_name = "UFO Sighting Rate (%)",
    ).add_to(map_usa)     
    

#combine data in one map