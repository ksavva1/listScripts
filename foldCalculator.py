import os, webbrowser, zipfile, time
import SimpleITK as sitk
import numpy as np

#download and get array from energy.mhd
def getArray(dlCounter):
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

    zAxis = sitkArray.shape[0]
    yAxis = sitkArray.shape[1]
    xAxis = sitkArray.shape[2]

    return sitkArray, fileName, zAxis, yAxis, xAxis

targetCounter = 124

for i in range(123,127,1): #change to 0,max,1 after tests are done and add clause for when the url doesnt download anything
    seedArray, seedName, zAxis, yAxis, xAxis = getArray(i)
    targetArray, targetName, zAxis, yAxis, xAxis = getArray(targetCounter) # +1 after each round of comparisons to compare the og array with the next array.

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
                            foldChange = (seedArray[x1][y1][z1]) / (targetArray[x2][y2][z2])
                            #write fold change, experiment id, seed & target voxel to seed gene file
                            f.write("Seed Gene: " + seedName + "Target Gene: " + targetName + " Experiment ID: " + str(i) + "Target Coordinates: " + target + " Fold Change: " + str(foldChange)
                            f.close()

    targetCounter += 1