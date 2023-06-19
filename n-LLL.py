import math
import numpy as np
from random import randrange
import collections
import sys

sys.setrecursionlimit(3000)

def LatticeVectorGen(n,d):
    g = []
    for i in range(d):
        a = [randrange(100) for i in range(n)]
        g.append(a)
    #print(g)
    return g
    
def vectorlength(a):
    g = 0
    for i in a:
        b = i*i
        g += b
    h = math.sqrt(g)
    return h

def mucalc(a,b):
    c = np.dot(b,a)/np.dot(a,a)
    return c

def GramSchmidt(A):
    vklist = []
    muklist = []
    vklist.append(listofvectors[0])
    muklist.append([0])
    for i in range(1,len(listofvectors)):
        minimuklist = []
        ukvector = listofvectors[i]
        for j in range(i):
            #print(vklist[j])
            #print(listofvectors)
            insertmu = mucalc(vklist[j],listofvectors[i])
            minimuklist.append(insertmu)
            #print(insertmu)
            subtraction = np.multiply(insertmu,vklist[j])
            #subtraction = np.multiply(insertmu,vklist[j])
            ukvector = np.subtract(ukvector,subtraction).tolist()
        muklist.append(minimuklist)
        vklist.append(ukvector)
    return (listofvectors, vklist, muklist)

def OrthGen(n,k):
    listofvectors = LatticeVectorGen(n,k)
    #listofvectors = [[1,1,1], [-1, 0, 2], [3,5,6]]
    #listofvectors = [[2,1,5], [6, 19, 11], [0, 7, 6]]
    #listofvectors = [[8, 33, 88, 31, 30, 16, 43, 1, 87, 77, 80, 40, 43, 46, 39, 69, 99, 72, 55, 99, 61, 11, 16, 7, 27, 65, 41, 79, 14, 69, 22, 97, 51, 81, 64, 42, 82, 31, 77, 38, 96, 87, 51, 33, 48, 51, 48, 61, 36, 96], [19, 42, 51, 29, 1, 19, 5, 84, 65, 60, 16, 85, 82, 67, 85, 3, 35, 89, 99, 79, 21, 57, 56, 3, 24, 55, 31, 84, 38, 13, 82, 77, 87, 59, 34, 71, 61, 32, 34, 97, 6, 98, 79, 88, 76, 59, 56, 84, 38, 76], [68, 24, 23, 37, 17, 5, 60, 26, 46, 1, 93, 13, 76, 62, 14, 13, 96, 82, 94, 82, 54, 72, 96, 53, 79, 46, 91, 92, 84, 39, 31, 84, 74, 88, 28, 77, 82, 99, 68, 57, 33, 91, 39, 98, 4, 56, 58, 22, 50, 42], [41, 44, 1, 33, 12, 38, 17, 29, 47, 84, 29, 57, 8, 58, 54, 94, 26, 51, 39, 38, 43, 77, 65, 49, 99, 33, 29, 86, 29, 48, 22, 52, 61, 72, 78, 13, 48, 77, 58, 36, 46, 29, 98, 91, 69, 25, 73, 52, 85, 91], [29, 28, 13, 26, 7, 6, 62, 97, 78, 73, 17, 53, 16, 3, 48, 48, 68, 22, 81, 15, 56, 26, 73, 12, 37, 54, 85, 7, 78, 83, 3, 97, 83, 37, 34, 74, 49, 8, 95, 12, 37, 58, 52, 50, 70, 45, 73, 13, 25, 35], [68, 91, 54, 35, 29, 94, 36, 6, 84, 40, 40, 6, 78, 88, 29, 36, 23, 20, 88, 29, 9, 49, 74, 22, 26, 75, 53, 59, 48, 0, 45, 74, 70, 45, 2, 14, 84, 75, 44, 26, 17, 74, 97, 37, 86, 24, 41, 60, 26, 64], [78, 96, 51, 48, 17, 66, 15, 16, 8, 13, 96, 73, 94, 28, 70, 92, 9, 6, 52, 5, 64, 19, 75, 78, 30, 5, 99, 16, 93, 92, 76, 88, 33, 33, 62, 97, 3, 62, 59, 24, 7, 33, 1, 41, 18, 1, 42, 76, 85, 93], [3, 88, 76, 17, 4, 65, 78, 27, 91, 84, 76, 61, 7, 90, 96, 72, 36, 48, 56, 88, 83, 44, 75, 98, 10, 98, 54, 67, 23, 33, 2, 90, 0, 2, 39, 4, 54, 5, 56, 73, 41, 6, 52, 78, 12, 5, 35, 43, 96, 90], [89, 39, 2, 80, 82, 34, 39, 81, 44, 52, 0, 75, 53, 33, 66, 39, 65, 12, 4, 54, 81, 79, 59, 73, 36, 90, 65, 87, 74, 89, 70, 54, 27, 1, 64, 37, 13, 77, 8, 23, 72, 33, 39, 71, 32, 51, 72, 46, 23, 64], [61, 66, 25, 96, 6, 28, 68, 34, 12, 99, 19, 82, 35, 49, 47, 16, 85, 88, 84, 24, 14, 97, 3, 26, 84, 57, 83, 41, 45, 19, 25, 86, 24, 98, 25, 45, 72, 64, 11, 95, 52, 49, 67, 31, 28, 94, 94, 52, 67, 0], [36, 78, 47, 99, 83, 12, 67, 56, 54, 17, 19, 58, 27, 62, 41, 49, 51, 76, 68, 66, 36, 26, 67, 16, 81, 43, 11, 6, 38, 2, 39, 31, 48, 68, 2, 46, 73, 36, 4, 45, 64, 25, 95, 95, 61, 17, 90, 53, 14, 78], [24, 35, 2, 70, 85, 64, 88, 56, 39, 75, 29, 41, 28, 26, 76, 47, 29, 86, 72, 80, 4, 41, 41, 49, 59, 70, 69, 98, 72, 18, 22, 5, 79, 18, 1, 63, 79, 74, 75, 47, 16, 53, 19, 98, 18, 24, 33, 79, 97, 16], [98, 16, 75, 76, 64, 79, 76, 56, 69, 51, 74, 22, 44, 66, 28, 13, 35, 93, 21, 86, 44, 28, 30, 14, 48, 35, 87, 2, 11, 17, 16, 95, 93, 54, 22, 18, 78, 28, 40, 95, 27, 77, 72, 73, 88, 25, 28, 44, 11, 65], [33, 28, 33, 72, 49, 1, 51, 3, 6, 89, 67, 88, 70, 64, 57, 10, 94, 83, 15, 71, 16, 71, 48, 74, 23, 19, 71, 87, 38, 22, 46, 66, 76, 35, 39, 11, 58, 85, 70, 46, 23, 20, 51, 39, 25, 96, 78, 92, 82, 91], [55, 53, 41, 75, 36, 40, 9, 82, 67, 27, 38, 29, 14, 37, 62, 76, 87, 26, 18, 52, 61, 74, 72, 24, 79, 71, 35, 39, 66, 27, 78, 59, 5, 10, 98, 36, 37, 6, 53, 95, 54, 50, 43, 48, 15, 78, 41, 93, 95, 37], [49, 98, 61, 54, 44, 67, 57, 10, 40, 82, 20, 29, 29, 55, 0, 9, 89, 30, 43, 73, 38, 50, 95, 12, 96, 4, 30, 64, 78, 94, 92, 98, 18, 37, 18, 11, 78, 68, 18, 41, 16, 14, 45, 92, 46, 24, 36, 9, 23, 66], [45, 95, 0, 36, 23, 57, 43, 24, 8, 67, 8, 38, 62, 45, 98, 44, 78, 75, 5, 0, 4, 15, 30, 11, 61, 6, 35, 7, 67, 16, 76, 55, 39, 74, 18, 73, 73, 6, 33, 25, 59, 85, 26, 80, 93, 53, 79, 5, 74, 83], [73, 90, 55, 27, 46, 55, 28, 6, 53, 62, 59, 54, 65, 27, 77, 58, 0, 82, 36, 12, 61, 8, 42, 55, 64, 10, 7, 88, 62, 82, 56, 35, 65, 20, 85, 69, 69, 92, 43, 99, 59, 59, 80, 51, 11, 31, 39, 42, 27, 74], [83, 87, 70, 34, 9, 73, 81, 54, 30, 32, 68, 26, 41, 80, 75, 96, 49, 33, 51, 70, 48, 16, 23, 87, 11, 52, 26, 94, 16, 28, 53, 90, 90, 14, 40, 86, 28, 37, 1, 29, 3, 41, 45, 1, 31, 41, 30, 48, 19, 50], [49, 7, 68, 6, 66, 51, 42, 28, 28, 26, 96, 55, 19, 16, 62, 12, 65, 27, 75, 44, 76, 58, 50, 90, 4, 71, 16, 24, 25, 58, 14, 81, 33, 42, 71, 34, 66, 12, 98, 11, 20, 38, 45, 30, 95, 65, 73, 43, 44, 59], [75, 21, 5, 44, 40, 42, 92, 10, 94, 0, 80, 16, 25, 48, 97, 21, 35, 86, 57, 60, 30, 66, 7, 39, 2, 69, 10, 73, 80, 41, 64, 5, 84, 30, 28, 7, 35, 89, 43, 92, 73, 10, 46, 84, 82, 72, 26, 93, 23, 54], [15, 51, 91, 72, 26, 57, 39, 98, 27, 44, 76, 39, 66, 38, 0, 13, 78, 62, 18, 56, 47, 11, 86, 79, 62, 82, 95, 77, 4, 56, 50, 88, 7, 32, 96, 43, 7, 51, 17, 40, 54, 13, 92, 43, 87, 61, 62, 40, 70, 87], [62, 71, 3, 84, 99, 18, 97, 77, 77, 83, 87, 61, 48, 68, 86, 0, 82, 73, 58, 22, 10, 19, 16, 87, 49, 51, 53, 83, 86, 13, 10, 78, 8, 50, 72, 64, 95, 89, 83, 88, 86, 29, 33, 74, 60, 8, 44, 87, 82, 82], [30, 75, 13, 65, 44, 66, 53, 5, 36, 49, 50, 25, 35, 56, 56, 65, 33, 43, 48, 34, 5, 9, 47, 63, 65, 24, 5, 21, 96, 81, 49, 74, 37, 45, 66, 62, 22, 4, 55, 74, 97, 84, 24, 55, 63, 88, 87, 72, 27, 21], [34, 36, 60, 86, 37, 91, 90, 1, 22, 50, 85, 4, 61, 49, 57, 40, 48, 32, 78, 89, 15, 71, 86, 89, 47, 92, 31, 45, 59, 17, 97, 87, 92, 64, 25, 74, 53, 81, 75, 22, 23, 63, 31, 12, 99, 96, 78, 41, 8, 62], [54, 37, 49, 44, 1, 80, 86, 17, 86, 58, 10, 82, 49, 17, 56, 16, 12, 4, 18, 86, 71, 67, 82, 83, 86, 22, 29, 93, 57, 87, 9, 88, 20, 0, 40, 13, 94, 55, 40, 28, 68, 50, 57, 90, 92, 47, 36, 63, 9, 17], [0, 66, 79, 48, 47, 29, 99, 40, 7, 83, 42, 90, 57, 69, 48, 37, 28, 18, 58, 58, 84, 7, 72, 18, 56, 48, 79, 10, 2, 21, 42, 97, 8, 28, 16, 31, 77, 82, 24, 58, 21, 69, 84, 30, 21, 17, 71, 43, 48, 97], [87, 52, 73, 55, 38, 20, 91, 16, 66, 94, 98, 83, 67, 69, 36, 84, 27, 44, 33, 14, 5, 15, 10, 6, 85, 67, 77, 4, 38, 25, 22, 35, 52, 6, 93, 38, 8, 53, 15, 91, 50, 89, 19, 28, 87, 51, 37, 1, 57, 82], [37, 31, 89, 87, 85, 21, 60, 1, 49, 20, 84, 93, 63, 54, 75, 88, 99, 99, 45, 16, 86, 86, 87, 97, 29, 59, 23, 27, 5, 32, 2, 1, 23, 23, 72, 81, 58, 41, 27, 37, 85, 7, 59, 68, 27, 74, 27, 23, 95, 6], [47, 15, 95, 21, 57, 6, 14, 68, 5, 15, 7, 9, 38, 52, 84, 51, 73, 64, 79, 87, 50, 8, 53, 85, 47, 81, 58, 41, 1, 53, 63, 28, 44, 43, 8, 77, 52, 36, 34, 29, 39, 8, 71, 35, 72, 95, 76, 48, 85, 59], [63, 25, 15, 63, 29, 45, 73, 64, 11, 55, 26, 53, 85, 52, 69, 83, 7, 68, 62, 81, 5, 54, 98, 68, 36, 72, 10, 48, 36, 63, 67, 31, 58, 69, 83, 49, 87, 9, 79, 42, 22, 41, 56, 65, 88, 53, 19, 66, 39, 95], [90, 18, 70, 52, 27, 97, 22, 91, 42, 14, 95, 76, 70, 0, 93, 48, 68, 67, 24, 66, 15, 8, 72, 19, 98, 1, 45, 5, 11, 51, 85, 73, 46, 47, 97, 75, 39, 59, 67, 12, 63, 6, 6, 73, 96, 97, 1, 59, 61, 20], [27, 61, 19, 47, 40, 2, 90, 11, 78, 45, 81, 2, 97, 77, 35, 28, 52, 38, 17, 93, 84, 55, 89, 57, 96, 93, 72, 2, 62, 13, 16, 80, 92, 78, 3, 94, 73, 7, 11, 38, 28, 66, 29, 94, 75, 83, 29, 87, 67, 27], [63, 8, 55, 59, 82, 7, 35, 84, 61, 44, 71, 16, 39, 35, 65, 78, 17, 46, 64, 14, 33, 54, 24, 31, 33, 40, 50, 50, 54, 28, 57, 42, 81, 43, 10, 47, 78, 32, 98, 43, 92, 52, 40, 13, 51, 93, 12, 64, 87, 45], [93, 24, 43, 41, 8, 65, 36, 74, 9, 82, 25, 93, 55, 35, 27, 40, 73, 89, 72, 82, 7, 60, 28, 75, 28, 49, 67, 11, 67, 80, 13, 7, 79, 75, 16, 54, 57, 49, 60, 17, 19, 53, 73, 45, 90, 67, 36, 62, 64, 27], [62, 89, 27, 96, 96, 62, 8, 74, 35, 89, 36, 83, 46, 6, 51, 60, 50, 45, 60, 70, 71, 45, 74, 57, 32, 85, 25, 0, 83, 57, 95, 2, 96, 67, 49, 68, 32, 75, 33, 36, 66, 93, 99, 58, 70, 87, 21, 78, 12, 69], [50, 38, 33, 44, 95, 36, 2, 16, 43, 8, 17, 45, 26, 80, 16, 57, 76, 53, 65, 41, 13, 19, 36, 85, 41, 64, 6, 0, 53, 43, 76, 66, 58, 92, 98, 95, 55, 25, 91, 88, 49, 11, 45, 36, 49, 54, 96, 0, 84, 90], [28, 28, 42, 81, 14, 78, 88, 73, 58, 6, 31, 33, 57, 90, 64, 66, 54, 66, 16, 65, 5, 19, 99, 94, 38, 53, 32, 13, 58, 35, 51, 75, 55, 76, 69, 47, 7, 35, 14, 32, 29, 92, 96, 86, 24, 65, 76, 52, 32, 26], [11, 18, 67, 27, 73, 29, 78, 84, 66, 79, 78, 86, 4, 28, 88, 85, 41, 25, 89, 67, 66, 94, 1, 13, 17, 0, 93, 30, 58, 43, 32, 73, 10, 17, 23, 66, 34, 87, 66, 65, 26, 1, 93, 43, 38, 28, 63, 71, 10, 46], [24, 35, 30, 76, 11, 97, 99, 52, 62, 38, 58, 95, 6, 56, 96, 45, 70, 61, 70, 47, 27, 55, 34, 86, 75, 92, 5, 33, 15, 20, 51, 38, 8, 31, 44, 90, 65, 30, 78, 86, 37, 3, 73, 93, 10, 97, 35, 44, 57, 19], [2, 67, 30, 43, 34, 56, 26, 48, 63, 97, 28, 59, 31, 20, 30, 51, 23, 57, 4, 79, 42, 93, 47, 82, 27, 47, 12, 35, 40, 3, 61, 5, 55, 21, 77, 22, 38, 64, 96, 67, 7, 5, 24, 66, 3, 16, 82, 49, 1, 27], [64, 30, 47, 82, 13, 53, 6, 86, 21, 82, 69, 76, 64, 54, 83, 55, 22, 16, 73, 31, 4, 63, 83, 66, 93, 87, 65, 99, 18, 59, 85, 57, 45, 53, 72, 72, 77, 76, 89, 8, 42, 33, 68, 71, 25, 0, 71, 19, 76, 64], [94, 34, 68, 34, 86, 63, 55, 39, 57, 83, 99, 97, 0, 57, 2, 60, 47, 81, 26, 74, 83, 22, 26, 72, 61, 58, 52, 69, 50, 35, 89, 73, 25, 74, 17, 29, 77, 90, 9, 50, 97, 39, 18, 74, 48, 11, 90, 37, 4, 68], [44, 2, 37, 1, 1, 43, 58, 83, 34, 61, 6, 34, 31, 86, 84, 7, 12, 43, 19, 63, 63, 46, 72, 52, 99, 76, 39, 50, 4, 13, 72, 51, 0, 72, 70, 65, 17, 21, 66, 65, 5, 91, 9, 85, 87, 10, 63, 64, 93, 48], [96, 14, 6, 53, 31, 21, 62, 57, 8, 37, 83, 61, 75, 91, 96, 29, 6, 41, 62, 4, 34, 80, 53, 28, 11, 64, 30, 27, 35, 44, 72, 18, 11, 51, 94, 30, 62, 61, 47, 95, 10, 88, 23, 65, 98, 55, 41, 0, 45, 81], [52, 94, 61, 75, 73, 87, 72, 25, 49, 5, 33, 47, 49, 93, 52, 22, 61, 42, 93, 30, 36, 9, 37, 6, 21, 77, 18, 56, 22, 21, 40, 39, 31, 44, 16, 21, 57, 1, 5, 69, 87, 67, 82, 2, 21, 21, 67, 66, 18, 34], [91, 36, 40, 14, 57, 97, 44, 64, 56, 49, 32, 86, 29, 17, 18, 21, 22, 42, 32, 6, 88, 44, 42, 73, 85, 10, 70, 41, 26, 26, 93, 21, 9, 30, 59, 74, 63, 40, 29, 27, 35, 17, 76, 91, 3, 53, 12, 69, 86, 13], [17, 13, 34, 97, 55, 73, 87, 66, 24, 58, 53, 31, 50, 89, 77, 59, 41, 16, 2, 17, 78, 46, 82, 94, 85, 20, 17, 51, 95, 37, 29, 21, 10, 87, 99, 17, 23, 6, 80, 22, 42, 29, 86, 42, 17, 73, 78, 94, 61, 1], [87, 75, 21, 67, 70, 23, 7, 22, 47, 23, 91, 68, 30, 33, 51, 21, 38, 78, 95, 32, 20, 78, 61, 8, 97, 88, 64, 26, 65, 18, 19, 44, 55, 13, 18, 97, 37, 0, 56, 50, 41, 5, 40, 86, 57, 29, 47, 83, 19, 81], [82, 98, 25, 53, 74, 95, 13, 99, 81, 66, 86, 68, 91, 46, 62, 16, 9, 57, 53, 17, 52, 37, 77, 59, 14, 73, 37, 42, 14, 39, 85, 98, 4, 91, 66, 42, 40, 83, 90, 95, 85, 75, 71, 66, 48, 30, 51, 81, 66, 57]]
    #listofvectors = [[604, 8314, -3214, -1177, -2103, -7086, -387, -137, -3034, -376, -4063, 10268, -246, -3357, 433, 73, -5421, 7459, 4694, 759], [-2996, -5656, 965, 2639, 17586, -8205, 2981, -784, 8303, 84, -4332, 3662, -8599, 8493, 5248, -3066, 10514, 1540, 1658, 11064], [1862, -5347, -633, 1035, -2609, -1873, -4602, 1037, 6534, -66, 3330, 31, 8221, 9167, 6517, 1546, 2853, 487, -5985, 1199], [901, 1963, -2284, 1078, 606, -10574, -2198, 2479, 3387, -268, -6672, 7057, 3115, 6964, 4492, 1070, 8962, 5437, -5949, 7212], [292, 4316, 1156, 514, -10944, -142, -4045, 3344, 857, 138, -5168, 5231, -7585, 194, 2864, 867, 2256, -3032, 1388, 2244], [-4643, 276, 516, -1869, -2140, -7345, 3460, -7548, -14565, 12, -11031, 1541, -3125, 1890, -6020, -1875, -6928, 5120, 3828, 2337], [-155, -3916, -2173, 1073, 6567, -11457, 836, -3264, -2704, -268, -9936, 1230, 4456, 10725, 12785, 114, 7248, 6896, -5764, 7953], [3150, 5958, -2075, 6, -2129, -3436, -4832, 3622, 789, -226, -273, 4774, -2917, -13446, 7040, 1979, 2048, 2714, 4579, -3541], [1408, -1306, 2324, 1678, -9528, 11473, -1043, -1035, 3305, 302, 2823, -4685, -4940, 3242, -1348, -227, -1328, -9397, 127, -5579], [-2384, 2160, 3108, -1841, -2471, 13912, 4491, -3502, -10939, 364, 1707, -12975, -5470, -8395, -7239, -1794, -8327, -7398, 4090, -9359], [-1878, -10782, 4443, 2267, 2497, 4599, 5906, -3779, -727, 507, -5008, -5832, -5952, 11031, 2041, -808, 6728, -8629, -3805, 8215], [-2305, 3563, 2448, -1744, -7362, 10455, 5680, -3915, -7296, 282, 2418, -540, 523, 1327, -15313, -1297, -11221, -5214, 847, -447], [-6366, 1274, 2670, -944, -5269, -2431, 3749, -5556, -7836, 261, -9067, 4049, -8608, 8268, -12883, -3829, -5148, 442, 4540, 5541], [-453, -1309, 418, 307, 1022, -474, 1684, -1312, -546, 45, -1131, -512, -477, 2048, -717, -234, 345, -461, -451, 1237], [3231, 3200, -2009, -543, -1303, 4105, 2262, 4180, -2600, -200, -1393, -4206, 1595, -6110, 6842, 1689, 3338, 49, -2527, -1770], [1711, 11654, -303, -1086, -4421, 4597, -4331, 8912, 795, -13, 562, 3692, -11116, -18679, 3681, 882, 997, -2266, 7453, -3618], [-1436, 1223, -521, -814, 9595, -296, 4702, -75, -1597, -63, 219, -1952, -5614, -5953, -4001, -1650, -3857, 1380, 5439, -2636], [4483, -4915, -1802, 686, 3126, 2310, 1136, 637, 3958, -178, 8195, -8975, 10170, -3499, 6894, 2639, 1856, -27, -4162, -6081], [-6471, -1628, 2260, -1823, 2734, -1125, 6053, -8184, -9625, 206, -3461, 2619, 5563, 12412, -12264, -3359, -6209, 2348, -2743, 10194], [-4238, 737, -535, -3132, -5924, -8813, -487, -4180, -11290, -117, -5755, 6644, 1923, -444, -10483, -1208, -9406, 8407, 4612, 2088]]
    #listofvectors = [[-691, -52, 228, -28, 424, 104, -860, -56, 514, -886, 46, -345, 1244, 576, -766], [-228, -365, 163, 270, -392, 1191, -386, -1228, -679, -703, 21, -474, -169, 1590, -3074], [244, -468, 100, 321, 209, 524, -545, -675, -630, -1148, 1, -510, 413, -940, -802], [276, 442, -166, -168, -186, -354, 105, 356, -51, 551, -26, 359, -389, -436, 1251], [156, 486, -288, -318, -5, -784, 518, 522, 581, 1140, -42, 745, 192, 949, 1003], [461, 553, -392, -69, -1711, 526, -42, -1057, -1029, -185, -69, 736, -1920, 1246, -927], [-433, -939, 141, 276, -318, 546, 58, -600, 260, -704, 25, -163, -64, 594, -1195], [629, 563, -323, -169, -449, -652, -350, 130, -449, -21, -58, 578, -235, -1188, 1691], [-1401, -1007, 854, 285, 1492, 693, -474, 463, 962, -702, 156, -1546, 1607, -101, -1488], [-408, 106, 296, -106, 514, -599, -955, 915, 244, -117, 63, -416, 1005, -1445, 1894], [-896, -954, 197, 209, -224, 615, -199, -732, 755, -935, 41, -140, 555, 1601, -1948], [-481, -98, 140, -33, -141, 150, -200, 20, 271, 65, 34, -85, 108, 834, -507], [-231, -47, 139, -9, 235, 83, 257, 298, 224, 299, 28, -212, -108, 131, -153], [103, 196, -189, -60, -1080, 132, -401, -566, -490, -21, -28, 474, -638, 931, -283], [-45, -888, 104, 397, -314, 640, -682, -1043, -455, -1502, 7, -347, 309, -521, -1021]]
    #listofvectors = [[-19049, -8424, -404, -795, -12594, 8050, -5756, 9586, -1674, -6277, -2986, 13928, 1422, -9285, 2217], [-15454, 704, 316, -13753, 2370, 3056, 2735, 3228, 2812, 16186, 2609, 1963, -168, -7309, 8024], [-35074, -3418, 386, -24716, -4193, 1149, 13867, 14678, 11267, 30340, 3597, 17388, 1735, -23298, 23312], [15637, 11233, 638, -8393, 8145, -11471, 9186, -6244, 9200, 26434, 4904, -12453, -1754, 3927, -6228], [-20073, -6235, -197, -11769, -10276, 957, 7159, 17458, 18108, 10976, -893, 17487, 3518, -19876, 2002], [-3108, -177, 48, -2755, 3089, -8145, 10518, 2251, -204, -754, 429, 3405, 43, -3364, 11926], [398, 194, 67, 552, 558, -349, 1773, -851, -1361, -1448, 548, 12, 85, -44, 2676], [-9206, 1834, 568, -4397, 3650, 1156, 6496, -4614, -14061, -6794, 4383, 21, -1462, -2328, 14927], [-21506, -6334, -84, -4710, -4880, 6065, 597, 7869, -4320, -4715, -474, 12987, 811, -10956, 3260], [28383, 3996, -210, 15299, -176, -530, -9957, -9715, -455, -4085, -1909, -13654, -440, 15678, -21395], [-6311, -2347, -130, -2538, 1540, -1555, 3265, 4853, 7482, 6026, -921, 8202, 566, -4647, 2532], [-27454, -6009, 85, -11224, -12523, 14344, -4213, 8388, -1886, 13979, 1074, 10608, 1946, -13614, 7874], [18214, -4409, -571, 22526, 2441, 7140, -10460, -4859, -7085, -31853, -4504, -4637, 1749, 10491, -18097], [2615, 741, 131, 4109, 13146, -12780, 15140, -3660, -7571, -26308, 840, 2191, -1309, 2192, 20533], [-5675, -1623, -59, -3001, 985, -2955, 5183, 3398, 5234, 11744, -367, 6635, 510, -3689, 8586]]
    #print(listofvectors)
    #vectorlengths = [vectorlength(a) for a in listofvectors]
    gramschmidtvmulist = GramSchmidt(listofvectors)
    return listofvectors, gramschmidtvmulist

def vectororder(listofvectors):
    vectorlengths = [vectorlength(a) for a in listofvectors]
    #dict0 = dict(zip(listofvectors, mu))
    dict1 = dict(zip(vectorlengths, listofvectors))
    od = collections.OrderedDict(sorted(dict1.items()))
    ascending = list(od.values())
    #descending = [ascending[i] for i in range(len(ascending)-1, -1, -1)]
    return ascending

def checkOrth(a,b,c):
    moda = vectorlength(a)
    modb = vectorlength(b)
    g = np.arccos(np.divide(np.dot(a,b),np.multiply(moda,modb)))
    if g - math.pi/2 < 0.1 and g - math.pi/2 > -0.1:
        return True , g
    else:
        return False , g

###LLL Begins here###

def LovaszCondition(v, mu, k, sigma):
    #print(v)
    #print(v)
    k = k-1
    #print(vectorlength(np.add(v[k],np.multiply(mu[k][k-1],v[k-1]))))
    #print(vectorlength(v[k-1]))
    left = vectorlength(np.add(v[k],np.multiply(mu[k][k-1],v[k-1])))
    right = vectorlength(v[k-1])
    if left**2 > sigma*(right**2):
        #print("true")
        return True
    else:
        #print("false")
        #print("Swap")
        return False

def LovaszConditionmod(reductionparam, v, mu, k, sigma):
    #print(v)
    #print(mu)
    #k = k-1
    leftlist = []
    limit = min(k+reductionparam-4, len(v))
    #print("k", k)
    #print("limit", limit)
    for i in range(k, limit):
        g = 0
        #print("i", i, "limit", limit)
        for j in range(k-1, i):
            #print("j", j)
            minusnumbers = vectorlength(np.multiply(mu[i][j], v[j]))**2
            g += minusnumbers
        left2 = np.add(vectorlength(v[i])**2, g)
        leftlist.append(left2)
    #print(leftlist)
    #for j in range(k, len(v)):
        #g = 0
        #for i in range(k-1, limit):
            #print("gg", k + reductionparam -3)
            #print("gg", i)
            #minusnumbers = vectorlength(np.multiply(mu[k + reductionparam -3][i-1], v[i-1]))
            #g += minusnumbers
        #left2 = np.add(vectorlength(v[k-1 + reductionparam -3]), g)
        #print(left)
        #leftlist.append(left2)
    #print(leftlist)
    left = min(leftlist)
    #left = vectorlength(np.add(v[k],np.multiply(mu[k][k-1],v[k-1])))
    right = vectorlength(v[k-1])
    if left > sigma*(right**2):
        #print("true")
        return True
    else:
        #print("false")
        return False

def LovaszLoc(reductionparam, v, mu, k, sigma):
    #k = k-1
    leftlist = []
    limit = min(k+reductionparam-4, len(v))
    #print("k", k)
    #print("limit", limit)
    for i in range(k, limit):
        g = 0
        #print("i", i, "limit", limit)
        for j in range(k-1, i):
            #print("j", j)
            minusnumbers = vectorlength(np.multiply(mu[i][j], v[j]))**2
            g += minusnumbers
        left2 = np.add(vectorlength(v[i])**2, g)
        leftlist.append(left2)
    #print(leftlist)
    left = min(leftlist)
    #print(left)
    res = leftlist.index(left) + k
    #print("t", res)
    return res

def reduction(oldv, v, mu, k):
    k = k-1
    #print("k", k)
    vlist = oldv.copy()
    muklist = mu.copy()
    #subtractiontotal = [i==0 for i in oldv[0]]
    for j in range(k-1,-1,-1):
        muklist[k][j] = mucalc(v[j],vlist[k])
        m = round(muklist[k][j])
        vlist[k] = np.subtract(vlist[k],np.multiply(m,vlist[j])).tolist()
    x, y, z = GramSchmidt(vlist)
    return x, y, z

def reductionmod(oldv, v, mu, k):
    k = k-1
    vlist = oldv.copy()
    muklist = mu.copy()
    subtractiontotal = [i==0 for i in oldv[0]]
    for j in range(k-1,-1,-1):
        muklist[k][j] = mucalc(v[j],vlist[k])
        m = round(muklist[k][j])
        vlist[k] = np.subtract(vlist[k],np.multiply(m,vlist[j])).tolist()
    x, y, z = GramSchmidt(vlist)
    return x, y, z
        
def LLL(oldv, v,mu,k,sigma,count):
    if k == len(v)+1:
        #print("Route1")
        #count += 1
        global solution
        solution = oldv
        global finalcount
        finalcount = count
        #print(oldv)
        #print(count)
        return solution,finalcount
    else:
        #print(v)
        #print("Route2")
        #count+=1
        #print(k)
        #print(f"oldv: {oldv}")
        v2, v2prime, mu2 = reduction(oldv, v, mu, k)
        #print(f"v2: {v2}")
        #v2 = vectororder(v2)
        #oldvprime, vprime, muprime = GramSchmidt(v2)
        #print(vprime)
        #print(muprime)
        #print(count)
        #LLL(v2, vprime,muprime,k,sigma,count)
        if (LovaszCondition(v2prime, mu2, k, sigma)):
            #print("Route3")
            kprime = k+1
            #count += 1
            LLL(v2,v2prime,mu2,kprime,sigma,count)
        else:
            #print("Route4")
            swap1 = v2[k-1].copy()
            swap2 = v2[k-2].copy()
            v2[k-1] = swap2
            v2[k-2] = swap1
            #shortestv = vectororder(v2)[0].copy()
            #shortindex = v2.index(shortestv)
            #v2.pop(shortindex)
            #v2.insert(0, shortestv)
            count += 1
            #print(f"Swap: {k}")
            #print(v2)
            #v2 = vectororder(v2)
            oldvprime2, vprime2, muprime2 = GramSchmidt(v2)
            #print(vprime2)
            kprime = 2#max(k-1, 2)
            LLL(oldvprime2,vprime2,muprime2,kprime,sigma,count)
    return solution, finalcount

def LLLmod(oldv, v,mu,k,sigma,count, reductionparam):
    if k == len(v):
        #print("Route1")
        #count += 1
        global solution
        solution = oldv
        global finalcount
        finalcount = count
        #print(oldv)
        #print(count)
        return solution,finalcount
    else:
        #print(v)
        #print("Route2")
        #count+=1
        #print(k)
        #print(f"oldv: {oldv}")
        #print(mu)
        v2, v2prime, mu2 = reductionmod(oldv, v, mu, k)
        #print(f"v2: {v2}")
        #v2 = vectororder(v2)
        #oldvprime, vprime, muprime = GramSchmidt(v2)
        #print(vprime)
        #print(muprime)
        #print(count)
        #LLL(v2, vprime,muprime,k,sigma,count)
        if (LovaszConditionmod(reductionparam, v2prime, mu2, k, sigma)):
            #print("Route3")
            kprime = k+1
            #count += 1
            LLLmod(v2,v2prime,mu2,kprime,sigma,count, reductionparam)
        else:
            #print("Route4")
            h = LovaszLoc(reductionparam, v2prime, mu2, k, sigma)
            #print(h)
            #print("cap", len(v2))
            swap1 = v2[k-1].copy()
            swap2 = v2[h].copy()
            #print(swap1, swap2)
            v2[k-1] = swap2
            v2[h] = swap1
            #shortestv = vectororder(v2)[0].copy()
            #shortindex = v2.index(shortestv)
            #v2.pop(shortindex)
            #v2.insert(0, shortestv)
            #print(f"Swap: {k}")
            #print(v2)
            #v2 = vectororder(v2)
            count+=1
            oldvprime2, vprime2, muprime2 = GramSchmidt(v2)
            #print(vprime2)
            kprime = 2#max(k-1, 2)
            LLLmod(oldvprime2,vprime2,muprime2,kprime,sigma,count, reductionparam)
    return solution, finalcount

def test(finalv, listofvectors):
    detfinalv = np.linalg.det(listofvectors)
    #print(1/(pow(4/(4*sigma-1), ((n-1)/2))))
    invertedmatrix = np.linalg.inv(listofvectors)
    factors = np.multiply(detfinalv,np.dot(invertedmatrix,finalv[0])).tolist()
    #factors = np.dot(invertedmatrix,finalv[0]).tolist()
    print(factors)
    counterint = 0
    for i in factors:
      #print(i - round(i))
      if i - float(round(i)) < 0.1 and i - float(round(i)) > -0.1:
        counterint += 1
    if counterint == len(finalv[0]):
        integer = True
    else:
        integer = False
    return integer

#No. elements in vector (x)
n = 20
#No. dimensions (y)
d = 20
#Reduction Param
reductionparam = 19
count = 0
count2 = 0
count3 = 0
sigma = 1
startk = 2
startk2 = 2
startk3 = 2

import time
starttime = time.time()
listofvectors, gramschmidtvmulist = OrthGen(n,d)
print(listofvectors)
original = listofvectors.copy()
'''gsvmu = gramschmidtvmulist
oldv1, v1 , mu1 = gsvmu
finalv, finalcount = LLL(oldv1,v1,mu1,startk,sigma,count)
finalvlength = vectorlength(finalv[0])
#print(f"Original: {original}{vectorlength(original[0])} \nNumber: {n} \nSwaps: {finalcount} \nFinal V: {finalv}, {finalvlength} \n_____________________________")
print(finalcount)
shortestv = vectororder(finalv)[0]
LLLmatrix = []
while shortestv != finalv[0]:
    shortindex = finalv.index(shortestv)
    #finalv[0], finalv[shortindex] = finalv[shortindex], finalv[0]
    #LLLmatrix.append(finalv[shortindex])
    #finalv.pop(shortindex)
    #print(finalv)
    temp = finalv[shortindex]
    finalv.pop(shortindex)
    finalv.insert(0, temp)
    startkprime = 2
    count = 0
    #originalprime = finalv.copy()
    oldv1, v1, mu1 = GramSchmidt(finalv)
    #print(mu1)
    finalv, finalcount = LLL(oldv1,v1,mu1,startkprime,sigma,count)
    finalvlength = vectorlength(finalv[0])
    #print(f"Original: {originalprime}{vectorlength(originalprime[0])} \nNumber: {n} \nSwaps: {finalcount} \nFinal V: {finalv}, {finalvlength} \n_____________________________")
    print(finalcount)
    shortestv = vectororder(finalv)[0]
print("Complete")
print([vectorlength(i) for i in finalv])
#print(finalv)
endtime = time.time()
print(f"Time taken {endtime-starttime} seconds")'''

#x, y, z = GramSchmidt(finalv)
#print(x)
#print(z)

original2 = original.copy()
starttime = time.time()
gsvmu2 =GramSchmidt(original2)
oldv2, v2, mu2 = gsvmu2
finalv2, finalcount2 = LLLmod(oldv2,v2,mu2,startk2,sigma,count2, reductionparam)
finalvlength2 = vectorlength(finalv2[0])
#print(f"Original: {original2}{vectorlength(original2[0])} \nNumber: {n} \nSwaps: {finalcount2} \nFinal V: {finalv2}, {finalvlength2} \n_____________________________")
print(finalcount2)
shortestv2 = vectororder(finalv2)[0]
LLLmatrix2 = []
while shortestv2 != finalv2[0]:
    shortindex2 = finalv2.index(shortestv2)
    #finalv2[0], finalv2[shortindex2] = finalv2[shortindex2], finalv2[0]
    #LLLmatrix2.append(finalv2[shortindex2])
    temp = finalv2[shortindex2]
    finalv2.pop(shortindex2)
    finalv2.insert(0, temp)
    #print(finalv)
    startkprime = 2
    count = 0
    #originalprime2 = finalv2.copy()
    oldv2, v2, mu2 = GramSchmidt(finalv2)
    #print(mu2)
    finalv2, finalcount2 = LLLmod(oldv2,v2,mu2,startkprime,sigma,count,reductionparam)
    finalvlength2 = vectorlength(finalv2[0])
    #print(f"Original: {originalprime2}{vectorlength(originalprime2[0])} \nNumber: {n} \nSwaps: {finalcount2} \nFinal V: {finalv2}, {finalvlength2} \n_____________________________")
    print(finalcount2)
    shortestv2 = vectororder(finalv2)[0]
print("Complete")
print([vectorlength(i) for i in finalv2])
endtime = time.time()
print(f"Time taken {endtime-starttime} seconds")
#print(test(finalv2, original2))

#x, y, z = GramSchmidt(finalv2)
#print(x)
#print(z)

'''original3 = finalv.copy()
gsvmu3 =GramSchmidt(finalv)
oldv3, v3, mu3 = gsvmu3
finalv3, finalcount3 = LLLmod(oldv3,v3,mu3,startk3,sigma,count3, reductionparam)
finalvlength3 = vectorlength(finalv3[0])
print(f"Original: {original3} \nNumber: {n} \nSwaps: {finalcount3} \nFinal V: {finalv3}, {finalvlength3} \n_____________________________")
print(test(finalv3, original3))'''
