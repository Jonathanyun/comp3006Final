import csv
import pandas as pd
import numpy as np
import folium as fl
from folium import plugins
from folium.plugins import HeatMap
import matplotlib.pyplot as plt

def total_vaccinations(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'total_vaccinations'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations'
	).add_to(map)
    
def total_distributed(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'total_distributed'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations Distributed'
	).add_to(map)


def people_vaccinated(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_vaccinated'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'People Vaccinated'
	).add_to(map)

 
def people_fully_vaccinated(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_fully_vaccinated'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'People Fully Vaccinated'
	).add_to(map)

 
def total_vaccinations_per_hundred(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'total_vaccinations_per_hundred'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Total Vaccinations per Hundred'
	).add_to(map)

 
def people_fully_vaccinated(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_fully_vaccinated'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'People Fully Vaccinated'
	).add_to(map)


 
def people_vaccinated_per_hundred(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'people_vaccinated_per_hundred'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'People Vaccinated per Hundred'
	).add_to(map)

 
def distributed_per_hundred(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'distributed_per_hundred'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Vaccinations Distributed per Hundred'
	).add_to(map)

 
def daily_vaccinations_raw(state, data, map, color):
	fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'daily_vaccinations_raw'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Daily Vaccinations Raw'
	).add_to(map)

 
def daily_vaccinations(state, data, map, color):
    fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'daily_vaccinations'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Daily Vaccinations'
	).add_to(map)

    
def daily_vaccinations_per_million(state, data, map, color):
    fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'daily_vaccinations_per_million'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Daily Vaccinations per Million'
	).add_to(map)

    
def share_doses_used(state, data, map, color):
    fl.Choropleth(
		geo_data = state,
		name = 'choropleth',
		data = data, 
		columns = ['location', 'share_doses_used'],
		key_on = "feature.properties.name", 
		fill_color = color,
		fill_opacity = 0.7,
		line_opacity = 0.2,
		legend_name = 'Share Doses Used'
	).add_to(map)
    
 
def merge_data(file_name, df1, df2, variables):
    new_data = pd.merge(df1, df2, on = 'location')
    
    with open(file_name, 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter = ',')
        csv_writer.writerow(variables)
        for row, info in new_data.iterrows():
            csv_writer.writerow([info['date'], info['location'], info['total_vaccinations'], info['total_distributed'], info['people_vaccinated'], info['people_fully_vaccinated_per_hundred'], info['total_vaccinations_per_hundred'], info['people_fully_vaccinated'], info['people_vaccinated_per_hundred'], info['distributed_per_hundred'], info['daily_vaccinations_raw'], info['daily_vaccinations'], info['daily_vaccinations_per_million'], info['share_doses_used'], info['latitude'], info['longtitude'], info['abbr']])
            
    return new_data

def clean_data(file_name, df1, state_name, variables):
    with open(file_name, 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter = ',')
        csv_writer.writerow(variables)
        for row, info in df1.iterrows():
            for state in state_name:
                if (info['location'] == state):
                    if (info['date'] == '2021-10-28'):
                        if (info['location'] == "New York State"):
                            info["location"] = "New York"
                            csv_writer.writerow([info['date'], info['location'], info['total_vaccinations'], info['total_distributed'], info['people_vaccinated'], info['people_fully_vaccinated_per_hundred'], info['total_vaccinations_per_hundred'], info['people_fully_vaccinated'], info['people_vaccinated_per_hundred'], info['distributed_per_hundred'], info['daily_vaccinations_raw'], info['daily_vaccinations'], info['daily_vaccinations_per_million'], info['share_doses_used'], info['latitude'], info['longtitude'], info['abbr']])
                        else:
                            csv_writer.writerow([info['date'], info['location'], info['total_vaccinations'], info['total_distributed'], info['people_vaccinated'], info['people_fully_vaccinated_per_hundred'], info['total_vaccinations_per_hundred'], info['people_fully_vaccinated'], info['people_vaccinated_per_hundred'], info['distributed_per_hundred'], info['daily_vaccinations_raw'], info['daily_vaccinations'], info['daily_vaccinations_per_million'], info['share_doses_used'], info['latitude'], info['longtitude'], info['abbr']])

    
def create_new_data():
    orig_vacc_data = pd.read_csv('us_state_vaccinations.csv')
    vacc_data = pd.DataFrame(orig_vacc_data)
    
    orig_state_data = pd.read_csv('state_lat_long.csv')
    state_data = pd.DataFrame(orig_state_data)	
    
    fields = ['date', 'location', 'total_vaccinations', 'total_distributed', 'people_vaccinated', 'people_fully_vaccinated_per_hundred', 'total_vaccinations_per_hundred', 'people_fully_vaccinated', 'people_vaccinated_per_hundred', 'distributed_per_hundred', 'daily_vaccinations_raw', 'daily_vaccinations', 'daily_vaccinations_per_million', 'share_doses_used', 'latitude', 'longtitude', 'abbr']
    state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York State", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
    
    file_one = 'updated_us_state_vacc.csv'
    file_two = 'clean_us_state_vacc.csv'
    
    new_data = merge_data(file_one, vacc_data, state_data, fields)
    clean_data(file_two, new_data, state_names, fields)
    return file_two


def time_plot(state, variable):
    df = pd.read_csv('updated_us_state_vacc.csv')
    dates = df.loc[df['location'] == state]['date'].reset_index(drop = True)
    variable_data = df.loc[df['location'] == state][variable].reset_index(drop = True)

    ylabel = f"{variable}"
    ylabel = ylabel.replace('_', ' ')
    ylabel = ylabel.title()
    
    fig = plt.plot_date(x = dates, y = variable_data)
    plt.title(f"{state} {ylabel}")
    plt.xlabel('Dates from 1.12.21 to 10.28.21')
    plt.ylabel(ylabel)
    plt.tick_params(axis = 'x', which = 'both', bottom = False, top = False)
    plt.xticks([])
    plt.show() 
    print(fig)

def total_vaccinations_bar_plot():
    df = pd.read_csv('clean_us_state_vacc.csv')
    state_names = df['abbr']
    total_vacc = df['total_vaccinations']

    plt.bar(state_names, total_vacc)
    plt.title("Total Vaccinations in the US by State")
    plt.ylabel('Total Vaccinations')
    plt.xlabel('State')
    plt.xticks(fontsize = 5)
    plt.figure(figsize = (12,4))
    plt.show()

    




def main():
    total_vaccinations_bar_plot()
    # time_plot('Alabama', 'distributed_per_hundred')
    # create_new_data()

    
    # orig_data = pd.read_csv('clean_us_state_vacc.csv')
    # clean_data = pd.DataFrame(orig_data)
    
    # lat = 37.0902
    # long = -95.7129
    
    # total_map = fl.Map(location = [lat, long], zoom_start = 3)
    # url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
    # state_geo = f"{url}/us-states.json"
    # color = "YlGn"

    # share_doses_used(state_geo, clean_data, total_map, color)
    

if __name__ == "__main__":
    main()
	