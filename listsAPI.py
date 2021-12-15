import requests 
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd

#create dictionary for xml data to be stored in
#geneData = {}

seedPoint = input("Input seed point (x,y,z): ")
requestURL = 'http://mouse.brain-map.org/api/v2/data/query.xml?criteria=service::mouse_agea%5Bset$eq%27mouse_coronal%27%5D%5Bseed_point$eq'+seedPoint+'%5D%5Bseed_age$eqP56%5D%5Bmap_age$eqP56%5D%5Bcorrelation_threshold1$eq0.7%5D%5Bthreshold1$eq%271,50%27%5D%5Bcorrelation_threshold2$eq0.8799999999999999%5D%5Bthreshold2$eq%270,50%27%5D%5Bstart_row$eq0%5D%5Bnum_rows$eq2000%5D'

r = requests.get(requestURL)
root = ET.fromstring(r.content) #parse XML

geneIDList = []
foldChangeList = []

for geneID in root.iter('gene-id'):
    geneIDList.extend(geneID)
    

for foldChange in root.iter('fold-change'):
    foldChangeList.extend(foldChange)
    print(foldChange)

geneDF = pd.DataFrame({'geneID':geneIDList, 'foldChange':foldChangeList}) #convert list to dataframe

#geneDF\
#.style.set_properties(subset=['geneID']) \
#.hide_index() #show dataframe

print(geneDF)

#not getting raw data from xml. maybe look into using soup again?