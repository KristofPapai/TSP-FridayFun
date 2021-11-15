import math
import numpy as np

cities = ["Berlin","Moscow","Denver","Budapest","Tokyo","Helsinki"]
cities_cordinates = [[4,3],[2,4],[5,3],[7,2],[1,1],[3,11]]
pathIndex = []


def bruteForce(arr):
    matrixLength = len(cities_cordinates)
    for rows in range(0, matrixLength):
        distances = cordinetDistance2nd(cities_cordinates, rows)
        minValue = min(i for i in distances if i > 0)
        minIndex = distances.index(minValue)
        print(minIndex)
    return True

def cordinetDistance2nd(arr,baseRow):
    distances = []
    arrLength = len(arr)
    for i in range(1, arrLength):
        distance = math.sqrt(((arr[baseRow][0]-arr[i][0])**2)+((arr[baseRow][1]-arr[i][1])**2))
        distances.append(distance)
    print(distances)
    return distances

print(bruteForce(cities_cordinates))
