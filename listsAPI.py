import requests 
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

seedPoint = input("Input seed point (x,y,z): ") #6800,4200,5600
requestURL = 'http://mouse.brain-map.org/api/v2/data/query.xml?criteria=service::mouse_agea%5Bset$eq%27mouse_coronal%27%5D%5Bseed_point$eq'+seedPoint+'%5D%5Bseed_age$eqP56%5D%5Bmap_age$eqP56%5D%5Bcorrelation_threshold1$eq0.7%5D%5Bthreshold1$eq%271,50%27%5D%5Bcorrelation_threshold2$eq0.8799999999999999%5D%5Bthreshold2$eq%270,50%27%5D%5Bstart_row$eq0%5D%5Bnum_rows$eq2000%5D'

r = requests.get(requestURL)
soup = BeautifulSoup(r.content, 'html.parser')
list(soup.children)
geneIDList = soup.find_all('gene-id')
foldChangeList = soup.find_all('fold-change')

geneDF = pd.DataFrame({'geneID':geneIDList, 'foldChange':foldChangeList}) #convert list to dataframe

print(geneDF)