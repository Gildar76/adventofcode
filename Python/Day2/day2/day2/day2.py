
def calculateWrappings(allLines):
    wrappingNeeded = 0;
    ribbonLength = 0
    for line in allLines:
        currentLineList = []
        currentLineListInt = []
        currentLineList = line.split("x")
        for l in range(0,len(currentLineList)):
            currentLineList[l] = int(currentLineList[l])


        currentLineList.sort()
        l = int(currentLineList[0])
        w = int(currentLineList[1])
        h = int(currentLineList[2])
        #print(l,w,h)
        area = 2*l*w + 2*w*h + 2*h*l + l*w
        print(l,w,h)
        wrappingNeeded += area
        ribbonLength += l+l+w+w+l*w*h
        print (area)
    return (wrappingNeeded, ribbonLength)

def fileToList(filename):
    listOfLines = [];
    f = open("input.txt");
    for line in f:
        listOfLines.append(line)
        
    return listOfLines

allLines = fileToList("input.txt")
result = calculateWrappings(allLines)
print("Total area, ribbon length", result)