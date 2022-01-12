import cv2, os
import numpy as np
import requests, zipfile, io 

#download file
for j in range(1,100,1):
    requestURL = 'http://api.brain-map.org/grid_data/download/' + j
    r = requests.get(requestURL, stream=True)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(/Users/katiesavva/Downloads)

    #delete file or whole folder (so I dont clog up my computer)
    #os.remove("FileName")
    #os.rmdir("myfolder")

#save intensity data as an array
img = cv2.imread('path/to/img', 1)

#function to get expression energy
def expression(i,x,y,z):
    #rip expression values out of file or matrix


#loop through all points in downloaded file
for z1 in zAxis:
    for z2 in zAxis:
        for y1 in yAxis:
            for y2 in yAxis:
                for x1 in xAxis:
                    for x2 in xAxis:
                        #coordinates for seed and target points
                        seed = str(x1) + "," + str(y1) + "," + str(z1)
                        target = str(x2) + "," + str(y2) + "," + str(z2)
                        #open file for that location
                        f = open('%s.csv' % seed, 'a')
                        #for every gene present, compare expression values in the 2 locations = fold change
                        foldChange = expression(i,x1,y1,z1) / expression(i,x2,y2,z2)
                        #write fold change, gene id, seed & target voxel to location file
                        f.write("Target: " + target + " ID: " + geneID + " Fold Change: " + foldChange)
                        f.close()