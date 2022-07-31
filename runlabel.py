# from tkinter.font import names
# import yaml
# from yaml.loader import SafeLoader
import pandas as pd 
# name = []
# # Open the file and load the file
# with open('data.yaml') as f:
#     data = yaml.load(f, Loader=SafeLoader)
#     name.append(data['names'])


df= pd.read_excel("name.xlsx")
print(df)
