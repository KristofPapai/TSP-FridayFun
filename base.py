import numpy as np

#this solution is based on the brute force algorithm its not the best and most efficient method of solving the TSP problem


cities = ["Berlin", "Moscow", "Madrid", "Tokyo"]
citi_distance = [[0, 29, 15, 35],
                 [29, 0, 57, 42],
                 [15, 57, 0, 61],
                 [35, 42, 61, 0]]
pathTake = []


#kezelni kell hogy ne mehessen ugyan abba a városba vissza
#maybe változóba tárolni az előző távot vagy indexet és nem engedni neki hogy ugyan oda menjen vissza

def shortestPath(arr):
    path = np.min(arr, axis=1)
    return path

pathTake = shortestPath(citi_distance)

print(pathTake)