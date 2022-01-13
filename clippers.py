import os
import zipfile
import webbrowser, time

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
            file_name = os.path.abspath(item) #get full path of files
            zip_ref = zipfile.ZipFile(file_name) #create zipfile object
            zip_ref.extractall(dir_name) 
            zip_ref.close()
            os.remove(file_name) #delete zipped file

    oldName = 'energy.mhd'
    newName = str(j) + '.mhd'
    os.rename(oldName, newName)