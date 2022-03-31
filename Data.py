import pandas as pd
import flask


data_html = pd.read_csv('Resources/cities.csv').to_html()

data_file = open('data_raw.html','w')
data_file.write(data_html)
data_file.close()