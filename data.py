import pandas as pd



"""
We first get the list of all the countries in our list
"""
df = pd.read_csv("winemag-data_first150k.csv")
countries = list(set(df['country'].dropna()))

"""
We are now going to take the list of all the provinces for each countries
"""

provinces_of_countries = {}
for country in countries:
    
    
    temp = df[df['country']== country]
    
    prov_list = list(set(temp['province'].dropna()))
    province_dict = {"country": [temp['price'].mean(),temp['points'].mean()]}
    for prov in prov_list:
        stats_list = []
        new_temp = temp[temp['province']==prov]
        
        stats_list.append(new_temp['price'].mean())
        stats_list.append(new_temp['points'].mean())
        
        province_dict[prov] = stats_list
        
    provinces_of_countries[country] = province_dict


print(provinces_of_countries)

