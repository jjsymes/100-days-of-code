from numpy import nan
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_count = data["Primary Fur Color"].value_counts().to_dict()

squirrel_color_dict = {"Fur Color": [], "Count": []}

for key, value in color_count.items():
    squirrel_color_dict["Fur Color"].append(key)
    squirrel_color_dict["Count"].append(value)

squirrel_color_dataframe = pandas.DataFrame(squirrel_color_dict)

squirrel_color_dataframe.to_csv("color_count.csv")