import math
import numpy as np

cities = ["Berlin","Moscow","Denver","Budapest","Tokyo","Helsinki"]
cities_cordinates = [[4,3],[2,4],[5,3],[7,2],[1,1],[3,11]]
pathIndex = []


def bruteForce(arr):
    matrixLength = len(arr)
    pathTaken = []
    rows = 0
    while(len(pathTaken) != len(arr)):
        distances = cordinetDistance2nd(arr, rows)
        minValue = min(i for i in distances if i > 0)
        minIndex = distances.index(minValue)
        if(minIndex in pathTaken):
            minValue = min(i for i in distances if i != minValue and i > 0)
            minIndex = distances.index(minValue)
        rows = minIndex
        #print(minIndex)
        pathTaken.append(minIndex)
    print(pathTaken)
    return True

def cordinetDistance2nd(arr,baseRow):
    distances = []
    arrLength = len(arr)
    for i in range(0, arrLength):
        distance = math.sqrt(((arr[baseRow][0]-arr[i][0])**2)+((arr[baseRow][1]-arr[i][1])**2))
        distances.append(distance)
    print(distances)
    return distances

print(bruteForce(cities_cordinates))
