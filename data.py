import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import neighbors, datasets

"""
We first get the list of all the countries in our list
"""
df = pd.read_csv("winemag-data_first150k.csv")
df = df.dropna(subset= ['price'])
df = df.dropna(subset= ['points'])
countries = list(set(df['country'].dropna()))
"""
We are now going to take the list of all the provinces for each countries
"""


provinces_of_countries = {}
for country in countries:

    temp = df[df['country']== country]
    
    prov_list = list(set(temp['province'].dropna()))
    
    province_dict = {"country": [round(temp['price'].mean(),2),round(temp['points'].mean(),2)]}
    
    for prov in prov_list:
        stats_list = []
        new_temp = temp[temp['province']==prov]
        
        stats_list.append(round(new_temp['price'].mean(),2))
        stats_list.append(round(new_temp['points'].mean(),2))
        
        province_dict[prov] = stats_list
        
    provinces_of_countries[country] = province_dict


"""
def country_plot(country):
    
    if provinces_of_countries[country] != None:
        dict_of_provinces = provinces_of_countries[country]
        
        province_list = list(dict_of_provinces.keys())
        stats = list(dict_of_provinces.values())
        
        x_price = []
        y_points = []
        
        for i in range(len(stats)):
            
            x_price.append(stats[i][0])
            y_points.append(stats[i][1])
        
        m,b = np.polyfit(x_price,y_points,1)
        x_temp = np.array(x_price)
        plt.scatter(x_price,y_points)
        plt.plot(x_price,m*x_temp+b)
        plt.xlabel("Average Price")
        plt.ylabel("Average Points")
        plt.title(f"Average Price and Points of wine in {country} per Province")
        plt.show()
    
""" 
#country_plot("US")


def world_plot(country):
    
    temp = df[df['country']== country ]
    x_price = list(temp['price'])
    y_points = list(temp['points'])
    m, b = np.polyfit(np.log(x_price), y_points, 1)
    
    x_temp = np.array(x_price)
    size = [5] * len(x_price)
    plt.scatter(x_price, y_points, size, 'k')

    x_log_line = np.arange(min(x_price)-0.5, max(x_price)+0.5, 0.5)
    log_line = m * np.log(x_log_line) + b
    plt.plot(log_line, 'r')

    # plt.plot(x_temp,m*np.log(x_temp)+b)
    plt.xlabel("Price")
    plt.ylabel("Points")
    plt.xlim(left=min(x_price)-0.015*(min(x_price)), right=max(x_price)+0.015*(max(x_price)))
    plt.title(f"Price and Points of wine in {country}")
    plt.show()
    
world_plot("Spain")


