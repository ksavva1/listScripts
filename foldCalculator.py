import os, webbrowser, zipfile, time
import SimpleITK as sitk
#import numpy as np

#download and get array from energy.mhd
def getArray(dlCounter):
    try:
        requestURL = 'http://api.brain-map.org/grid_data/download/' + str(dlCounter)
        webbrowser.open(requestURL)
        time.sleep(6) #to give time for file to actually download

        dirName = '/Users/katiesavva/Downloads'
        extension = ".zip"
        os.chdir(dirName) #change directory from working dir to dir with files

        for item in os.listdir(dirName): 
            if item.endswith(extension): 
                fileName = os.path.abspath(item) #get full path of files
                zipRef = zipfile.ZipFile(fileName) #create zipfile object
                zipRef.extractall(dirName) 
                zipRef.close()
                os.remove(fileName) #delete zipped file
        
        #rename energy files
        oldName = 'energy.mhd'
        newName = str(dlCounter) + '.mhd'
        os.rename(oldName, newName)

        #save intensity data as an array
        itkImage = sitk.ReadImage(newName)
        #convert the image to a numpy array and shuffle dimensions to get axis in the order z,y,x
        sitkArray = sitk.GetArrayFromImage(itkImage)

        zAxis = int(sitkArray.shape[0])
        yAxis = int(sitkArray.shape[1])
        xAxis = int(sitkArray.shape[2])

        return sitkArray, fileName, zAxis, yAxis, xAxis
    
    except:
        pass

targetCounter = 2

for i in range(1,900000,1): #change to 0,max,1 after tests are done and add clause for when the url doesnt download anything
    try:
        seedArray, seedName, zAxis, yAxis, xAxis = getArray(i)
        targetArray, targetName, zAxis, yAxis, xAxis = getArray(targetCounter) # +1 after each round of comparisons to compare the og array with the next array.

        #loop through all points in downloaded file
        for z1 in range(zAxis-1):
            for z2 in range(zAxis-1):
                for y1 in range(yAxis-1):
                    for y2 in range(yAxis-1):
                        for x1 in range(xAxis-1):
                            for x2 in range(xAxis-1):
                                #coordinates for seed and target points
                                seed = str(x1) + "," + str(y1) + "," + str(z1)
                                target = str(x2) + "," + str(y2) + "," + str(z2)
                                #open file for that location
                                f = open('%s.csv' % seed, 'a')
                                #for every gene present, compare expression values in the 2 locations = fold change
                                foldChange = (seedArray[z1][y1][x1]) / (targetArray[z2][y2][x2])
                                #write fold change, experiment id, seed & target voxel to seed gene file
                                f.write("Seed Gene: " + seedName + "Target Gene: " + targetName + " Experiment ID: " + str(i) + "Target Coordinates: " + target + " Fold Change: " + str(foldChange))
                                f.close()

        targetCounter += 1

    except:
        targetCounter += 1