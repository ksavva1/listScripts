import webbrowser
from bs4 import BeautifulSoup 

#create dictionary for xml data to be stored in
geneData = {}

#get xml file for a seed point
seedPoint = input()
url = "http://mouse.brain-map.org/api/v2/data/query.xml?criteria=service::mouse_agea%5Bset$eq%27mouse_coronal%27%5D%5Bseed_point$eq"+seedPoint+"%5D%5Bseed_age$eqP56%5D%5Bmap_age$eqP56%5D%5Bcorrelation_threshold1$eq0.7%5D%5Bthreshold1$eq%271,50%27%5D%5Bcorrelation_threshold2$eq0.8799999999999999%5D%5Bthreshold2$eq%270,50%27%5D%5Bstart_row$eq0%5D%5Bnum_rows$eq2000%5D"
webbrowser.open_new_tab(url)

#scrape the geneID and foldChange tag data from xml file
infile = open("FILENAME.xml","r")
contents = infile.read()
soup = BeautifulSoup(contents,'xml')
geneID = soup.find_all('gene-id')
foldChange = soup.find_all('fold-change')

#add data to dictionary
geneData.update(list of data pulled using beautifulSoup)