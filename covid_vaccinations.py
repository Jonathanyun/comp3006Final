import csv
import pandas as pd
import numpy as np
import folium as fl
import geopandas as gpd
from folium import plugins
from folium.plugins import HeatMap
import webbrowser
import datetime
import bar_chart_race as bcr
from IPython.display import HTML




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

def time_barplot(state, variable, option):
    df = pd.read_csv('updated_us_state_vacc.csv')
    highest_pop = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania']
    lowest_pop = ['Wyoming', 'Vermont', 'Alaska', 'North Dakota', 'South Dakota']
    state_check = False

    if option == 'high':
        for i in highest_pop:
            if state == i:
                state_check = True
    
        if state_check == True:
            california = df.loc[df['location'] == 'California'][variable].reset_index(drop = True)
            texas = df.loc[df['location'] == 'Texas'][variable].reset_index(drop = True)
            florida = df.loc[df['location'] == 'Florida'][variable].reset_index(drop = True)
            new_york = df.loc[df['location'] == 'New York State'][variable].reset_index(drop = True)
            penn = df.loc[df['location'] == 'Pennsylvania'][variable].reset_index(drop = True)
            
            CALI, TEX, FLO, NEW, PENN = [], [], [], [], []
            
            for i in range (0, 100):
                CALI.append(california[i])
                TEX.append(texas[i])
                FLO.append(florida[i])
                NEW.append(new_york[i])
                PENN.append(penn[i])
            
            cali = pd.Series(CALI)
            tex = pd.Series(TEX)
            flo = pd.Series(FLO)
            new = pd.Series(NEW)
            penn = pd.Series(PENN)

            date = []
            for i in range(0, 100):
                date.append(df.date[i])

            DATE = pd.Series(date)

            data = {"California": cali,
                    "Texas": tex,
                    "Florida": flo, 
                    "New York": new,
                    "Pennsylvania": penn,
                    "Date": DATE
                    }
            
            corona = pd.concat(data, axis = 1)
            corona.set_index("Date", inplace = True)
            corona = corona.dropna()

            bcr_html = bcr.bar_chart_race(df = corona, filename = "barchart.html", orientation = 'h', title = f"{variable} Test", figsize = (12,4))
            HTML(bcr_html)

        # else:
        #     california = df.loc[df['location'] == 'California'][variable].reset_index(drop = True)
        #     texas = df.loc[df['location'] == 'Texas'][variable].reset_index(drop = True)
        #     florida = df.loc[df['location'] == 'Florida'][variable].reset_index(drop = True)
        #     new_york = df.loc[df['location'] == 'New York State'][variable].reset_index(drop = True)
        #     penn = df.loc[df['location'] == 'Pennsylvania'][variable].reset_index(drop = True)
            
        #     CALI, TEX, FLO, NEW, PENN = [], [], [], [], []
            
        #     for i in range (0, 100):
        #         CALI.append(california[i])
        #         TEX.append(texas[i])
        #         FLO.append(florida[i])
        #         NEW.append(new_york[i])
        #         PENN.append(penn[i])
            
        #     cali = pd.Series(CALI)
        #     tex = pd.Series(TEX)
        #     flo = pd.Series(FLO)
        #     new = pd.Series(NEW)
        #     penn = pd.Series(PENN)

        #     date = []
        #     for i in range(0, 100):
        #         date.append(df.date[i])

        #     DATE = pd.Series(date)

        #     data = {"California": cali,
        #             "Texas": tex,
        #             "Florida": flo, 
        #             "New York": new,
        #             "Pennsylvania": penn,
        #             "Date": DATE
        #             }

        #     corona = pd.concat(data, axis = 1)
        #     corona.set_index("Date", inplace = True)

        #     bcr_html = bcr.bar_chart_race(df = corona, filename = None, orientation = 'h', title = f"{variable} Test", figsize = (12,4))
        #     HTML(bcr_html) 
            




def main():
    time_barplot('Texas', 'total_vaccinations', 'high')
    
    # create_new_data()

    
    # orig_data = pd.read_csv('clean_us_state_vacc.csv')
    # clean_data = pd.DataFrame(orig_data)
    
    # lat = 37.0902
    # long = -95.7129
    
    # total_map = fl.Map(location = [lat, long], zoom_start = 3)
    # url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
    # state_geo = f"{url}/us-states.json"
    

if __name__ == "__main__":
    main()
	