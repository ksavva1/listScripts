import os, webbrowser
import zipfile
import time, glob

#download file
for j in range(123,127,1):
    requestURL = 'http://api.brain-map.org/grid_data/download/' + str(j)
    webbrowser.open(requestURL)
    time.sleep(5)
    #----------------
    dir_name = '/Users/katiesavva/Downloads'
    extension = ".zip"

    os.chdir(dir_name) # change directory from working dir to dir with files

    for item in os.listdir(dir_name): # loop through items in dir
        if item.endswith(extension): # check for ".zip" extension
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(dir_name) # extract file to dir
            zip_ref.close() # close file
            os.remove(file_name) # delete zipped file