# comp3006Final

# Final Project Proposal

## Group Members
-Ainsley McCutcheon
-Jonathan Yun

## Research Question
-What is the relationship between UFO sightings and COVID vaccinations in the USA?


## Datasets Used
-UFO Sighting Data downloaded from -> https://www.kaggle.com/camnugent/ufo-sightings-around-the-world?select=ufo_sighting_data.csv
-COVID Vaccine Data downloaded from -> https://www.kaggle.com/paultimothymooney/usa-covid19-vaccinations

## Python Functionality
-Amazing Visualizations (folium library)

## Analysis Conclusion

## Usage

```bash
python nba_covid_analysis.py [command] [optional arguments]
```

### Dependencies

package dependencies listed in requirements.txt

### [command]
**__**: info if vaccine command exists

### [optional arguments]

-**c**: filters UFO dataset by city instead of state. No input implies UFO data is filtered by state
-**s**: filters UFO data set by ufo shape, requires shape from the following list. No input implies all UFO shapes are selected
  'cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball','unknown', 'oval', 
  'other', 'cigar', 'rectangle', 'chevron', 'triangle', 'formation', 'N/A', 'delta',
  'changing', 'egg', 'diamond', 'flash', 'teardrop', 'cone', 'cross', 'pyramid',
  'round', 'crescent', 'flare', 'hexagon', 'dome', 'changed','all']
 -**v**:
 -**t**:
 -**p**: changes colors schemes of cholopleth plots, requires two arguments from the following list. No inputs will cause plot to use automatic colors
  'BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'RdPu', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'
 -**l**: changes the starting point on the map generated based off state, full name or abbreviation, given. No state given implies starting at the latitude and longitude in the    middle of the US.
