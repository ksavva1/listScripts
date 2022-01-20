N = 2.3

lastLine = str("L")
#check if there is only 1 row required or just in case a number <0 is input
if N <= 1:
    print("L")
else:
    #loop n-1 times to print stem of the L
    for i in range(N-1): 
        print("L")
        #add 1 L to build the width of the last line
        lastLine += str("L")
        
    #After stem has printed output last line
    print(lastLine)