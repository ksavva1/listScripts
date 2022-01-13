import cv2, os, webbrowser
import numpy as np
import zipfile
import time

#download and unzip file
for j in range(123,127,1):
    requestURL = 'http://api.brain-map.org/grid_data/download/' + str(j)
    webbrowser.open(requestURL)

    time.sleep(6)

    dir_name = '/Users/katiesavva/Downloads'
    extension = ".zip"
    os.chdir(dir_name) #change directory from working dir to dir with files

    for item in os.listdir(dir_name): 
        if item.endswith(extension): 
            fileName = os.path.abspath(item) #get full path of files
            zipRef = zipfile.ZipFile(fileName) #create zipfile object
            zipRef.extractall(dir_name) 
            zipRef.close()
            os.remove(fileName) #delete zipped file

    oldName = 'energy.mhd'
    newName = str(j) + '.mhd'
    os.rename(oldName, newName)

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