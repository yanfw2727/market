import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.DataFrame
url = 'http://amis.afa.gov.tw/veg/VegProdDayTransInfo.aspx'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')
print(sp)