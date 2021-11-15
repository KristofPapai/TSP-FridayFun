import math

import numpy as np

cities = ["Berlin","Moscow","Denver","Budapest","Tokyo","Helsinki"]
cities_cordinates = [[4,3],[2,4],[5,3],[7,2],[1,1],[3,11]]
pathIndex = []

def bruteForce(arr):
    for rows in len(cities_cordinates):
        for search in range(rows,len(cities_cordinates)):
            




def cordinateDistance(x1,y1,x2,y2):
    firstX = math.pow((x1 - x2),2)
    firstY = math.pow((y1 - y2),2)
    distance = firstX + firstY
    return math.sqrt(distance)
