import pandas as pd
from pyodide.http import open_url
from js import localStorage

url = (
    "https://raw.githubusercontent.com/sunse523/ormi-dev-project-1/master/data/TOURISM.csv"
)

# read dataset to create bunddle
rawData = pd.read_csv(open_url(url), sep=',', encoding='unicode_escape')

# save rawData to local storage to be used in other pages
localStorage.setItem('rawdata', rawData.to_json(orient="split"))


