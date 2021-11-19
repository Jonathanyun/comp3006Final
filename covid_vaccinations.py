import csv
import pandas as pd
import numpy as np
import folium as fl
import geopandas
from folium import plugins
from folium.plugins import HeatMap
import webbrowser

def total_vaccinations(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'total_vaccinations'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'total_vaccinations.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)

def total_distributed(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'total_distributed'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'total_distributed.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)

def people_vaccinated(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_vaccinated'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'people_vaccinated.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def people_fully_vaccinated(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_fully_vaccinated'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'people_fully_vaccinated.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def total_vaccinations_per_hundred(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'total_vaccinations_per_hundred'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'total_vaccinations_per_hundred.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def people_fully_vaccinated(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_fully_vaccinated'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'people_fully_vaccinated.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def people_vaccinated_per_hundred(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_vaccinated_per_hundred'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'people_vaccinated_per_hundred.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def distributed_per_hundred(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'distributed_per_hundred'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'distributed_per_hundred.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def daily_vaccinations_raw(state, data, map):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'daily_vaccinations_raw'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)

	output_file = 'daily_vaccinations_raw.html'
	map.save(output_file)
	webbrowser.open(output_file, new = 2)
 
def daily_vaccinations(state, data, map):
    fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'daily_vaccinations'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)
    
    output_file = 'daily_vaccinations.html'
    map.save(output_file)
    webbrowser.open(output_file, new = 2)
    
def daily_vaccinations_per_million(state, data, map):
    fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'daily_vaccinations_per_million'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)
    
    output_file = 'daily_vaccination_per_million.html'
    map.save(output_file)
    webbrowser.open(output_file, new = 2)
    
def share_doses_used(state, data, map):
    fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'share_doses_used'],
		key_on = "feature.properties.name", 
		fill_color = "YlGn",
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)
    
    output_file = 'share_doses_used.html'
    map.save(output_file)
    webbrowser.open(output_file, new = 2)
 
def main():
    orig_data = pd.read_csv('clean_us_state_vacc.csv')
    clean_data = pd.DataFrame(orig_data)
    
    lat = 37.0902
    long = -95.7129
    
    total_map = fl.Map(location = [lat, long], zoom_start = 3)
    url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
    state_geo = f"{url}/us-states.json"
    
    total_vaccinations(state_geo, clean_data, total_map)
    total_distributed(state_geo, clean_data, total_map)
    

if __name__ == "__main__":
    main()
	