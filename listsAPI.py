import requests 
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

seedPoint = input("Input seed point (x,y,z): ") #6800,4200,5600
requestURL = 'http://mouse.brain-map.org/api/v2/data/query.xml?criteria=service::mouse_agea%5Bset$eq%27mouse_coronal%27%5D%5Bseed_point$eq'+seedPoint+'%5D%5Bseed_age$eqP56%5D%5Bmap_age$eqP56%5D%5Bcorrelation_threshold1$eq0.7%5D%5Bthreshold1$eq%271,50%27%5D%5Bcorrelation_threshold2$eq0.8799999999999999%5D%5Bthreshold2$eq%270,50%27%5D%5Bstart_row$eq0%5D%5Bnum_rows$eq5000%5D'

r = requests.get(requestURL)
soup = BeautifulSoup(r.content, 'html.parser')
list(soup.children)

#get data
geneIDList = soup.find_all('gene-id')
geneSymbolList = soup.find_all('gene-symbol')
fold = soup.find_all('fold-change')

foldChangeList = []

for i in fold:
    i = str(i)
    temp = i[:-14]
    temp2 = temp[13:]
    foldChangeList.append(float(temp2))

geneDF = pd.DataFrame({'geneID':geneIDList, 'geneSymbol':geneSymbolList, 'foldChange':foldChangeList}) #convert list to dataframe

#print(geneDF.dtypes)
print(geneDF)

#data splicing
highCorr = geneDF[(geneDF['foldChange'] > 0.9) & (geneDF['foldChange'] < 1.1)]
print(highCorr)