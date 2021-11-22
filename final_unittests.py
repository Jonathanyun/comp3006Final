import unittest
import covid_vaccinations as covid
import lat_lon as ll
#import ufo_covid_analysis as 
import ufo_data as ufo
import pandas as pd

class TestProject(unittest.TestCase):
    
    def test_lat_lon(self):
        ''' Unit test for the lat_lon module
        '''
        #Test variables
        test_file = 'state_lat_long.csv'
        test_abbr1 = 'tx'
        test_abbr2 = 'TX'
        test_state1 = 'texas'
        test_state2 = 'TEXAS'
        test_country1 = 'us'
        test_country2 = 'united states'
        
        tx_lon = float(-100)
        tx_lat = float(31)
        
        us_lat  = 37.0902
        us_lon = -95.7129
        
        #Tests for function get_lat_lon
        self.assertEqual(ll.get_lat_lon(test_abbr1,test_file),(tx_lat, tx_lon))
        self.assertEqual(ll.get_lat_lon(test_abbr2,test_file),(tx_lat, tx_lon))
        self.assertEqual(ll.get_lat_lon(test_state1,test_file),(tx_lat, tx_lon))
        self.assertEqual(ll.get_lat_lon(test_state2,test_file),(tx_lat, tx_lon))
        self.assertEqual(ll.get_lat_lon(test_country1,test_file),(us_lat, us_lon))
        self.assertEqual(ll.get_lat_lon(test_country2,test_file),(us_lat, us_lon))
        
    def test_ufo_data(self):
        ''' Unit tests for ufo_data module
        '''
        #test variables
        test_ufo_file = "ufo_sighting_data.csv"
        test_state_file = 'state_lat_long.csv'
        test_ufo_df = pd.read_csv(test_ufo_file, encoding='utf8')
        test_state_df = pd.read_csv(test_state_file, encoding='utf8')
        
        # updating test_ufo_df to match required output of ufo_data_clean and add all needed columns for other tests
        test_ufo_df.loc[(test_ufo_df.country.str.lower() != "us") & (test_ufo_df["state/province"].str.upper().isin(test_state_df.abbr)),"country"] = "us"
        test_ufo_df = test_ufo_df[test_ufo_df.country.str.lower() == "us"]
        test_ufo_df = test_ufo_df[test_ufo_df["state/province"].isin(test_state_df.abbr.str.lower())].reset_index()
        test_ufo_df.latitude = test_ufo_df.latitude.str.replace("q","")
        test_ufo_df.latitude = test_ufo_df.latitude.astype(float)
        test_ufo_df.longitude = test_ufo_df.longitude.astype(float)
        st_lat_dict = dict(zip(test_state_df.abbr.str.lower().value_counts().index,test_state_df.latitude))
        st_lon_dict = dict(zip(test_state_df.abbr.str.lower().value_counts().index,test_state_df.longtitude))
        test_ufo_df["st_lat"] = test_ufo_df["state/province"].str.lower().map(st_lat_dict).astype(float)
        test_ufo_df["st_lon"] = test_ufo_df["state/province"].str.lower().map(st_lon_dict).astype(float)
        test_ufo_df["UFO_shape"] = test_ufo_df["UFO_shape"].fillna("N/A")
        
        #ufo_data_clean function tests
        self.assertTrue(ufo.ufo_data_clean().equals(test_ufo_df))
        self.assertTrue(ufo.ufo_data_clean(test_ufo_file).equals(test_ufo_df))
        self.assertTrue(ufo.ufo_data_clean(test_ufo_file,test_state_file).equals(test_ufo_df))
        self.assertTrue(ufo.ufo_data_clean(test_ufo_file,test_state_file,True).equals(test_ufo_df))
        self.assertFalse(ufo.ufo_data_clean(test_ufo_file,test_state_file,False).equals(test_ufo_df))
        
        #ufo_type function tests
        #filtered dataframe to test ufo_type against
        egg_test_ufo_df = test_ufo_df[test_ufo_df["UFO_shape"].str.lower() == "egg"].reset_index()
        self.assertTrue(ufo.ufo_type(test_ufo_df,'egg').equals(egg_test_ufo_df))
        self.assertTrue(ufo.ufo_type(test_ufo_df,'all').equals(test_ufo_df))
        self.assertTrue(ufo.ufo_type(test_ufo_df).equals(test_ufo_df))
        
        #ufo_counts function tests
        #adds columns for count of ufos by state and ufos by city to test against ufo_counts
        test_ufo_df["city_state_key"] = test_ufo_df.city + test_ufo_df["state/province"]
        ufo_count_dict = dict(zip(test_ufo_df.city_state_key.str.lower().value_counts().index,test_ufo_df.city_state_key.value_counts()))
        test_ufo_df["ufo_count1"] = test_ufo_df.city_state_key.map(ufo_count_dict)
        ufo_count_dict = dict(zip(test_ufo_df["state/province"].value_counts().index,test_ufo_df["state/province"].value_counts()))
        test_ufo_df["ufo_count2"] = test_ufo_df["state/province"].map(ufo_count_dict)
        self.assertTrue(ufo.ufo_counts(test_ufo_df,True).ufo_count.equals(test_ufo_df.ufo_count1))
        self.assertTrue(ufo.ufo_counts(test_ufo_df,False).ufo_count.equals(test_ufo_df.ufo_count2))
        
        #shape_counts function tests
        #adding shape_count series to test against shape_counts
        ufo_shape_dict = dict(zip(test_ufo_df.UFO_shape.value_counts().index, test_ufo_df.UFO_shape.value_counts()))
        test_ufo_df["shape_count"] = test_ufo_df.UFO_shape.map(ufo_shape_dict)
        self.assertTrue(ufo.shape_counts(test_ufo_df).shape_count.equals(test_ufo_df.shape_count))
        
    def test_covid_vaccinations(self):
        """
            Unit Tests for covid_vaccinations.py
        """
        test_covid_file = 'clean_us_state_vacc.csv'
        test_covid_df = pd.read(test_covid_file)
        
        other_test_covid_file = 'updated_us_state_vacc.csv'
        other_test_covid_df = pd.read(other_test_covid_file)
        
        self.assertTrue(covid.merge_data().equals(other_test_covid_df))
        self.assertTrue(covid.create_new_data().equals(test_covid_file))
        
        
    
    #def test_ufo_covid_analysis(self):
        
if __name__ == '__main__':
    unittest.main()