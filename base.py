import math
import numpy as np

cities = ["Berlin","Moscow","Denver","Budapest","Tokyo","Helsinki"]
cities_cordinates = [[4,3],[2,4],[9,3],[7,2],[1,6],[3,11]]
pathIndex = []

def bruteForce(arr):
    matrixLength = len(arr)
    pathTaken = []
    usedMinValues = []

    rows = 0
    while(len(pathTaken) != len(arr)-1):
        distances = cordinetDistance2nd(arr, rows)
        minValue = min(i for i in distances if i > 0 and distances.index(i) not in pathTaken and distances.index(i) != 0)
        minIndex = distances.index(minValue)
        if(minIndex in pathTaken or minValue in usedMinValues):
            minValue = min(i for i in distances if i not in usedMinValues and i > 0 and distances.index(i) not in pathTaken and distances.index(i) != 0)
            minIndex = distances.index(minValue)
            usedMinValues.append(minValue)
        else:
            usedMinValues.append(minValue)

        rows = minIndex
        pathTaken.append(minIndex)
        if(len(pathTaken) == len(arr)-1):
            usedMinValues.append(distances[0])
    print("--------------------")
    print("Távolság amit a kereskedő bejárt: ",usedMinValues)
    print("A kereskedő által bejárt teljes távolság: ",round(sum(usedMinValues),2),"km")
    return pathTaken


#ez itt végül lehet nem kell majd


def cordinetDistance2nd(arr,baseRow):
    distances = []
    arrLength = len(arr)
    for i in range(0, arrLength):
        distance = math.sqrt(((arr[baseRow][0]-arr[i][0])**2)+((arr[baseRow][1]-arr[i][1])**2))
        distances.append(distance)
    print(distances)
    return distances

outerPathTaken = bruteForce(cities_cordinates)
print("Az útvonal amit a kereskedő bejárt: ",outerPathTaken)
szoveg = "Meglátogatott városok: "
for i in outerPathTaken:
    szoveg += cities[i] + " "
szoveg += cities[0]
print(szoveg)
print("Az utolsó város egyben a kiinduló város is.")
