
import math

import numpy as np

cities = ["Berlin","Moscow","Denver","Budapest","Tokyo","Helsinki"]
cities_cordinates = [[4,3],[2,4],[5,3],[7,2],[1,1],[3,11]]
pathIndex = []

#CSAK % DARAB LÉPÉS KELL PLUSZ AZ UTOLSO ÉS AZ ELSŐ KÖZÖTT

def bruteForce(arr):
    matrixLength = len(arr)
    pathTaken = []
    #lehet while ciklus kéne inkább
    usedMinValues = []

    #TALÁN ITT VAN PROBLÉMA?
    rows = 0
    while(len(pathTaken) != len(arr)-1):
        distances = cordinetDistance2nd(arr, rows)
        forbiddenFruit = 0
        #itt lehet rosszul kezelem az utolso viszgaltok
        #mindindex nem lehet 0-a mert az a kiindulo pont
        #EMLÉKEZTETŐ I EGY ÉRTÉK NEM PEDIG EGY INDEX.....
        #VALAHOL AZ A GOND HOGY A KEZDŐPONT BEKAVAR
        minValue = min(i for i in distances if i > 0 and i != forbiddenFruit)
        minIndex = distances.index(minValue)
        if(minIndex in pathTaken or minValue in usedMinValues):
            minValue = min(i for i in distances if i not in usedMinValues and i > 0 and i != forbiddenFruit)
            minIndex = distances.index(minValue)
            usedMinValues.append(minValue)
        else:
            print("belép ide valaha ez a szar?")
            usedMinValues.append(minValue)
        rows = minIndex
        pathTaken.append(minIndex)
        #print(minIndex)
    print("--------------------")
    print("Útvonal: ",pathTaken)
    print("Értékek: ",usedMinValues)
    return True


#ez itt végül lehet nem kell majd


def cordinetDistance2nd(arr,baseRow):
    distances = []
    arrLength = len(arr)
    for i in range(0, arrLength):
        distance = math.sqrt(((arr[baseRow][0]-arr[i][0])**2)+((arr[baseRow][1]-arr[i][1])**2))
        distances.append(distance)
    print(distances)
    return distances

print(bruteForce(cities_cordinates))
