#function to get expression energy
def expression(i,x,y,z)):



#loop through all points in downloaded file
for z1 in zAxis:
    for z2 in zAxis:
        for y1 in yAxis:
            for y2 in yAxis:
                for x1 in xAxis:
                    for x2 in xAxis:
                        #open file for that location
                        seed = str(x1) + "," + str(y1) + "," + str(z1)
                        target = str(x2) + "," + str(y2) + "," + str(z2)
                        f = open('%s.csv' % location, 'a')
                        #for every gene present, compare expression values in the 2 locations = fold change
                        foldChange = expression(i,x1,y1,z1) / expression(i,x2,y2,z2)
                        #write fold change, gene id, seed % target voxel to location file
                        f.write("Target: " + target + " ID: " + geneID + " Fold Change: " + foldChange)
                        f.close()