

#loop through all points in downloaded file
for z1 in zAxis:
    for z2 in zAxis:
        for y1 in yAxis:
            for y2 in yAxis:
                for x1 in xAxis:
                    for x2 in xAxis:
                        #open file for that location
                        location = str(x1) + str(y1) + str(z1)
                        f = open('%s.csv' % location, 'a')
                        #for every gene present, compare expression values in the 2 locations = fold change

                        #write fold change, gene id, seed % target voxel to location file