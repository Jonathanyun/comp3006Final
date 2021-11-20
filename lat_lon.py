import pandas as pd

def get_lat_lon(loc,file):
    ''' Function grabs the latitude and longitude from state .csv file
        inputs:
            loc: str, State name or abbreviation, also takes united states
            file: str, name of state .csv file
    '''
    state_df = pd.read_csv(file, encoding='utf8')
    if "us" in loc.lower() or "united states" in loc.lower():
        lat  = 37.0902
        lon = -95.7129
    elif len(loc) > 2:
        state_df = state_df[state_df.location.str.lower == loc.lower()].reset_index()
        lat = float(state_df.latitude[0])
        lon = float(state_df.longtitude[0])
    elif len(loc) == 2:
        state_df = state_df[state_df.abbr.str.lower() == loc.lower()].reset_index()
        lat = float(state_df.latitude[0])
        lon = float(state_df.longtitude[0])
    else:
        lat  = 37.0902
        lon = -95.7129
    return lat, lon

def main():
    #Import data
    lat, lon = get_lat_lon("CO", "state_lat_long.csv")
    print("Latitude:" + str(lat) + " Longitude:"+ str(lon))

if __name__ == '__main__':
    main()