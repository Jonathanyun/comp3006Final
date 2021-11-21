#Python Libraries
import argparse
import sys
import matplotlib.pyplot as plt
import folium as fl
from folium import plugins
from folium.plugins import HeatMap
#Python Modules
import ufo_data as ufo
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
#parser.add_argument('-v','--vaccine',)
#parser.add_argument('-t','--time',)
parser.add_argument('-p','--palette', choices=['BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 
                                               'RdPu', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'],
                    nargs=2, default=['PuRd','BuGn'], dest="colors", help="Picks the Color palette for the map")
parser.add_argument('-l','--location',type=str,dest = "state")
args = parser.parse_args()

## Insert & Clean UFO Data
#Filtering UFO data based off command line arguements and ufo_data module functions
if args.ufo_state == True:
    ufo_df = ufo.ufo_data_clean("ufo_sighting_data.csv","state_lat_long.csv", False)
    ufo_df = ufo.ufo_counts(ufo_df,True)
else:
    ufo_df = ufo.ufo_data_clean("ufo_sighting_data.csv","state_lat_long.csv", True)
    ufo_df = ufo.ufo_counts(ufo_df,False)

if ("-s" in str(sys.argv)) and (args.ufo_shape.lower() != 'all'):
    ufo_df = ufo.ufo_type(ufo_df,args.ufo_shape.lower())
#Adds count of ufo shapes seen, will return same value for every row if a shape is selected in command line
ufo_df = ufo.shape_counts(ufo_df)   

class map_maker:
    def __init__(self, ufo_data):
        ''' Module initializes class
        '''
        self.ufo_data = ufo_data
        #Creates Map and adds data to it
        self.get_lat_lon()
        self.build_basemap()
        self.add_ufo_data()
        self.add_vaccine_data()
    
    def get_lat_lon(self,state_input = str(args.state), state_filename = "state_lat_long.csv"):
        ''' Method gets the latitude and longitude for the lat and lon variables from command line input
            using the lat_lon module
            inputs:
            state_input: string, state requested in command line
            state_filename: string, .csv file with state and longitude/latitude data
            outputs:
            self.lat: float, latitude variable
            self.lon: float, longitude variable
        '''
        #intializes self.state_filename and self.state_input
        self.state_filename = state_filename
        self.state_input = state_input
        #Creates self.lat and self.lon using lat_lon module
        self.lat, self.lon = ll.get_lat_lon(self.state_input,self.state_filename)
        return self.lat, self.lon
    
    def build_basemap(self):
        ''' Method creates map data and imports state lines for choropleth plot
            output:
            self.usa_map: map data used in folium maps
        '''
        #uses the folium map function and specified starting latitude and longitude to create map data
        self.usa_map = fl.Map(location=[self.lat,self.lon],zoom_start=3)
        #imports state lines
        self.url = (
            "https://raw.githubusercontent.com/python-visualization/folium/master/examples/data"
            )
        self.state_geo = f"{self.url}/us-states.json"
        return self.usa_map
    
    def add_ufo_data(self,city_arg = args.ufo_state,color_arg = args.colors[0], ufo_data=ufo_df):
        ''' Method adds UFO layer to map object. UFO layer is either a heatmap or a choropleth plot.
            inputs:
            city_arg: Boolean, whether or not ufo data is by city  or state
            color_arg: str, if plot is choropleth, changes the color scheme
            ufo_data: dataframe, ufo data used to make map layer
        '''
        #initializes variables related to ufo_data and command line inputs
        self.city_arg = city_arg
        self.color_arg = color_arg
        self.ufo_data = ufo_data
        
        #Changes type of map layer created depending on city_arg variable
        if self.city_arg == True:
            #creates heatmap from ufo data
            self.ufo_heat = [[row['latitude'],row['longitude']] for index, row in self.ufo_data.iterrows()]
            HeatMap(self.ufo_heat, name="UFOs",min_opacity=0, radius=20,blur=0).add_to(self.usa_map)
        else:
            #changes ufo_data state abbreiviations to capital to match data from us-states.json
            self.ufo_data["state/province"] = self.ufo_data["state/province"].str.upper()
            #creates Choropleth
            fl.Choropleth(
                #adds state lines and names map layer
                geo_data = self.state_geo,                     
                name = "UFOs",
                #uses the state abbreviations and ufo count data for plot
                data = self.ufo_data,                        
                columns = ["state/province", "ufo_count"],
                #changes plot color based of command input
                fill_color = str(self.city_arg),                      
                fill_opacity = 0.7,
                line_opacity = .1,
                  key_on = "feature.id",
                legend_name = "UFO Sighting Rate (%)",
            ).add_to(self.usa_map)
        return self.usa_map
    
    #def add_vaccine_data(self,):
        #return
    
def main():

    
    ## UFO Plots
    #K-Value 3 Cluster Plot for UFO data, ignores shape input to see relationship between UFO Shape Sightings
    #and sightings per location
    ufo_plt_1 = plt.figure(1)
    cluster_plt = ufo.shape_plot(ufo_df,args.ufo_state)
    plt.title("3 Cluster Plot For K-Values of UFO Type and UFOs per State")
    #Plot of UFO Sightings per state Bar Chart, ignores -c input data filter because that would be too many bars
    ufo_plt_2 = plt.figure(2)
    plt.figure(figsize=(12, 4))
    bar_plt = ufo.state_plot(ufo_df)
    plt.xticks(rotation=90)
    plt.title("UFO Sightings Per State")
    plt.show()
    
    ## Vaccine Stuff -
    
    #Show combined map
    Map_made = map_maker()
    Map_made.usa_map.save(outfile= "test.html")
    
if __name__ == '__main__':
    main()