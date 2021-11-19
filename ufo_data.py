#Import libraries
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Takes UFO Shape Arguement and UFO sightings by City/State Arguement
def ufo_data_clean(ufos = "ufo_sighting_data.csv", states = "state_lat_long.csv", by_state = True):
    ''' Data cleaning function takes the ufo file and a latitude/longitude state map file and cleans and parses the ufo data to
        only include ufo for the US.
        Both files must have state abbreviasions and longitude and latitude data
        inputs:
        ufos: string, .csv file name with ufo data
        state: string, .csv file name with state longitude and latitude data
        outputs:
        ufo_df: dataframe of cleaned and filtered data
    '''
    
    #Imports data from files
    ufo_df = pd.read_csv(ufos, encoding='utf8')
    state_df = pd.read_csv(states, encoding='utf8')
    
    #Clean up of UFO data
    #Adds us flag for states in the us missing the flag
    ufo_df.loc[(ufo_df.country.str.lower() != "us") & (ufo_df["state/province"].str.upper().isin(state_df.abbr)),"country"] = "us"
    #removes non US data
    ufo_df = ufo_df[ufo_df.country.str.lower() == "us"]
    ufo_df = ufo_df[ufo_df["state/province"].isin(state_df.abbr.str.lower())].reset_index()
    #adds state latitude and longitude if requested
    if by_state == True:
        #Add state latitude & longitude to file and converts them to floats
        st_lat_dict = dict(zip(state_df.abbr.str.lower().value_counts().index,state_df.latitude))
        st_lon_dict = dict(zip(state_df.abbr.str.lower().value_counts().index,state_df.longtitude))
        ufo_df["st_lat"] = ufo_df["state/province"].str.lower().map(st_lat_dict).astype(float)
        ufo_df["st_lon"] = ufo_df["state/province"].str.lower().map(st_lon_dict).astype(float)
    #Converts empty spaces for UFO Shapte to N/A
    ufo_df["UFO_shape"] = ufo_df["UFO_shape"].fillna("N/A")
    #removes that one q in the latitude data
    ufo_df.latitude = ufo_df.latitude.str.replace("q","") 
    #updates ufo city latitude and longitude to floats
    ufo_df.latitude = ufo_df.latitude.astype(float)
    ufo_df.longitude = ufo_df.longitude.astype(float)

    return ufo_df

def ufo_type(df,shape = "all"):
    ''' Function optionally filters the data by ufo shape. The default value keeps all ufos
        inputs:
        df: dataframe of UFO data
        shape: string from options: 'cylinder', 'light', 'circle', 'sphere', 'disk', 'fireball',
       'unknown', 'oval', 'other', 'cigar', 'rectangle', 'chevron', 'triangle', 'formation', nan,
       'delta', 'changing', 'egg', 'diamond', 'flash', 'teardrop', 'cone', 'cross', 'pyramid',
       'round', 'crescent', 'flare', 'hexagon', 'dome', 'changed', 'all'
       
       outputs:
       df: filtered dataframe
    '''
    #filters dataframe when specific UFO shape is requested
    if shape != "all":
        df[df["UFO_shape"].str.lower() == shape.lower()].reset_index()
    return df

def ufo_counts(df,by_city = False):
    ''' Function adds counts of ufos either by city or by state.
        inputs:
        df: dataframe of UFO data
        by_city: boolean value, True or False
        returns:
        df: dataframe with count value
    '''
    #Counts ufos by city and state key if city data is requested
    if by_city == True:
        df["city_state_key"] = df.city + df["state/province"]
        ufo_count_dict = dict(zip(df.city_state_key.str.lower().value_counts().index,df.city_state_key.value_counts()))
        df["ufo_count"] = df.city_state_key.map(ufo_count_dict)
    #counts ufos by state if by city is not requested
    else:
        ufo_count_dict = dict(zip(df["state/province"].value_counts().index,df["state/province"].value_counts()))
        df["ufo_count"] = df["state/province"].map(ufo_count_dict)
    return df

def shape_counts(df):
    ''' Function adds counts of ufo shapes either by city or by state.
        inputs:
        df: dataframe of UFO data
        by_city: boolean value, True or False
        returns:
        df: dataframe with count value
    '''
    #Counts ufos by shape
    ufo_shape_dict = dict(zip(df.UFO_shape.value_counts().index, df.UFO_shape.value_counts()))
    df["shape_count"] = df.UFO_shape.map(ufo_shape_dict)
    return df

def shape_plot(df,by_city):
    ''' Returns a 3-cluster scatter plot that compares ufo shape to ufo count by either state or city
        inputs:
        df: data frame
        by_city: Boolean variable, same as used in ufo_counts
        outputs:
        graph: cluster plot object
    '''
    df = ufo_counts(df,by_city)
    df = shape_counts(df)

    #creates k means
    kmeans = KMeans(n_clusters=3, random_state=0)
    df["cluster"] = kmeans.fit_predict(df[["ufo_count","shape_count"]])
        
    #centroid creation
    centroid = kmeans.cluster_centers_
    x = [loc[0] for loc in centroid]
    y = [loc[1] for loc in centroid]
    df["x_centroid"] = df.cluster.map({0:x[0], 1:x[1], 2:x[2]})
    df["y_centroid"] = df.cluster.map({0:y[0], 1:y[1], 2:y[2]})
        
    #adds colors to each cluster
    colors = ['#DF2020', '#81DF20', '#2095DF']
    df['color'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})
        
    #builds graph
    graph = plt.scatter(df.ufo_count, df.shape_count, c=df.color, alpha = 0.6, s=10)
    return graph

def state_plot(df):
    ''' Creates a bar chart of the number of UFOs for each state
    '''
    df = ufo_counts(df,False)
    graph = plt.bar(df["state/province"].str.upper(), df.ufo_count)
    return graph
    
def main():
    #Import and clean data
    ufo_df = ufo_data_clean("ufo_sighting_data.csv", "state_lat_long.csv", True)
    #Filter data and add counts
    ufo_df = ufo_type(ufo_df,"all")
    ufo_df = ufo_counts(ufo_df, False)
    ufo_df = shape_counts(ufo_df)
    #builds plots
    cluster_plt = shape_plot(ufo_df,False)
    plt.title("3 Cluster Plot For K-Values of UFO Type and UFOs per State")
    plt.show(cluster_plt)
    plt.figure(figsize=(12, 4))
    bar_plt = state_plot(ufo_df)
    plt.xticks(rotation=90)
    plt.title("UFO Sightings Per State")
    plt.show(bar_plt)

if __name__ == '__main__':
    main()
