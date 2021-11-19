import pandas as pd
import numpy as np
import csv

orig_vacc_data = pd.read_csv('us_state_vaccinations.csv')
vacc_data = pd.DataFrame(orig_vacc_data)

orig_state_data = pd.read_csv('state_lat_long.csv')
state_data = pd.DataFrame(orig_state_data)

fields = ['date', 'location', 'total_vaccinations', 'total_distributed', 'people_vaccinated', 'people_fully_vaccinated_per_hundred', 'total_vaccinations_per_hundred', 'people_fully_vaccinated', 'people_vaccinated_per_hundred', 'distributed_per_hundred', 'daily_vaccinations_raw', 'daily_vaccinations', 'daily_vaccinations_per_million', 'share_doses_used', 'latitude', 'longtitude', 'abbr']
state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York State", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

new_data = pd.merge(vacc_data, state_data, on = 'location')

with open('updated_us_state_vacc.csv', 'w') as csvfile:
	csv_writer = csv.writer(csvfile, delimiter = ',')
	csv_writer.writerow(fields)
	for row, info in new_data.iterrows():
		csv_writer.writerow([info['date'], info['location'], info['total_vaccinations'], info['total_distributed'], info['people_vaccinated'], info['people_fully_vaccinated_per_hundred'], info['total_vaccinations_per_hundred'], info['people_fully_vaccinated'], info['people_vaccinated_per_hundred'], info['distributed_per_hundred'], info['daily_vaccinations_raw'], info['daily_vaccinations'], info['daily_vaccinations_per_million'], info['share_doses_used'], info['latitude'], info['longtitude'], info['abbr']])

file_name = 'clean_us_state_vacc.csv'

with open(file_name, 'w') as csvfile:
	csv_writer = csv.writer(csvfile, delimiter = ',')
	csv_writer.writerow(fields)
	for row, info in new_data.iterrows():
		for state in state_names:
			if (info['location'] == state):
				if (info['date'] == '2021-10-28'):
					if (info['location'] == "New York State"):
						info["location"] = "New York"
						csv_writer.writerow([info['date'], info['location'], info['total_vaccinations'], info['total_distributed'], info['people_vaccinated'], info['people_fully_vaccinated_per_hundred'], info['total_vaccinations_per_hundred'], info['people_fully_vaccinated'], info['people_vaccinated_per_hundred'], info['distributed_per_hundred'], info['daily_vaccinations_raw'], info['daily_vaccinations'], info['daily_vaccinations_per_million'], info['share_doses_used'], info['latitude'], info['longtitude'], info['abbr']])
					else:
						csv_writer.writerow([info['date'], info['location'], info['total_vaccinations'], info['total_distributed'], info['people_vaccinated'], info['people_fully_vaccinated_per_hundred'], info['total_vaccinations_per_hundred'], info['people_fully_vaccinated'], info['people_vaccinated_per_hundred'], info['distributed_per_hundred'], info['daily_vaccinations_raw'], info['daily_vaccinations'], info['daily_vaccinations_per_million'], info['share_doses_used'], info['latitude'], info['longtitude'], info['abbr']])




