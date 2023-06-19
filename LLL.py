import math
import numpy as np
from random import randrange
import collections

def LatticeVectorGen(n,d):
    g = []
    for i in range(d):
        a = [randrange(3329) for i in range(n)]
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

def GramSchmidt(listofvectors):
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
    #listofvectors = [[59, 54, 55], [81, 86, 58], [90, 51, 91]]
    #listofvectors = [[-6,2,-5], [4,-6,-2], [-6, 3, -7]]
    #print(listofvectors)
    vectorlengths = [vectorlength(a) for a in listofvectors]
    dict1 = dict(zip(vectorlengths, listofvectors))
    od = collections.OrderedDict(sorted(dict1.items()))
    #print(od)
    q = list(od.values())
    n = [q[i] for i in range(len(q)-1, -1, -1)]
    #print(q)
    #listofvectors = [[32, 41, 41], [33, 40, 40], [-72, -85, -101]]
    gramschmidtvmulist = GramSchmidt(listofvectors)
    gramschmidtvmuordered = GramSchmidt(q)
    gramschmidtreversed = GramSchmidt(n)
    return listofvectors, q, n, gramschmidtvmulist, gramschmidtvmuordered, gramschmidtreversed

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
    #print(mu)
    k = k-1
    left = vectorlength(np.add(v[k],np.multiply(mu[k][k-1],v[k-1])))
    right = vectorlength(v[k-1])
    if left**2 >= sigma*(right**2):
        #print("true")
        return True
    else:
        #print("false")
        return False

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
    return vlist, muklist
        
def LLL(oldv, v,mu,k,sigma,count):
    if k == len(v):
        #print("Route1")
        count += 1
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
        v2, mu2 = reduction(oldv, v, mu, k)
        #print(f"v2: {v2}")
        oldvprime, vprime, muprime = GramSchmidt(v2)
        #print(vprime)
        #print(muprime)
        #print(count)
        #LLL(v2, vprime,muprime,k,sigma,count)
        if (LovaszCondition(vprime, muprime, k, sigma)):
            #print("Route3")
            kprime = k+1
            count += 1
            LLL(oldvprime,vprime,muprime,kprime,sigma,count)
        else:
            #print("Route4")
            swap1 = v2[k-1].copy()
            swap2 = v2[k-2].copy()
            v2[k-1] = swap2
            v2[k-2] = swap1
            #print(v2)
            oldvprime2, vprime2, muprime2 = GramSchmidt(v2)
            #print(vprime2)
            if k >= 2:
                #print("Route5")
                kprime = k-1
                count += 1
                LLL(oldvprime2,vprime2,muprime2,kprime,sigma,count)
            else:
                #print("Route6")
                count += 1
                #print(count)
                LLL(oldvprime2,vprime2,muprime2,k,sigma,count)
    return solution, finalcount        
###Driver Code###

countermain = 3
errormain = 0
while countermain in range(3,10):
    #No. elements in vector (x)
    n = countermain
    #No. dimensions (y)
    d = countermain
    sigma = 0.75
    startk = 2
    startk2 = 2
    startk3 = 2
    count = 0
    count2 = 0
    count3 = 0
    listofvectors, orderedvectors, reversedvectors, gramschmidtvmulist, gramschmidtvmuordered, gramschmidtreversed = OrthGen(n,d)
    print(listofvectors)
    listofvectorlengths = [vectorlength(i) for i in listofvectors]
    (oldv1, v1 , mu1) = gramschmidtvmulist
    listoforderedlengths = [vectorlength(i) for i in orderedvectors]
    (oldv2, v2 , mu2) = gramschmidtvmuordered
    listofreversedlengths = [vectorlength(i) for i in reversedvectors]
    (oldv3, v3 , mu3) = gramschmidtreversed
    #print(oldv1)
    #print(v1)
    #print(mu1)
    #print(checkOrth(*v))
    finalv, finalcount = LLL(oldv1,v1,mu1,startk,sigma,count)
    finalv2, finalcount2 = LLL(oldv2,v2,mu2,startk2,sigma,count2)
    finalv3, finalcount3 = LLL(oldv3,v3,mu3,startk3,sigma,count3)
    finalvlength2 = vectorlength(finalv2[0])
    finalvlength3 = vectorlength(finalv3[0])
    print("Ascending Length: ", finalvlength2)
    print("Descending Length: ", finalvlength3)
    print(f"Number: {countermain} \nIterations: {finalcount} \nErrors: {errormain} \nFinal V: {finalv} \n_____________________________")
    detfinalv = np.linalg.det(finalv)
    #print(1/(pow(4/(4*sigma-1), ((n-1)/2))))
    invertedmatrix = np.linalg.inv(listofvectors)
    factors = np.multiply(detfinalv,np.dot(invertedmatrix,finalv[0])).tolist()
    counterint = 0
    for i in factors:
      #print(i - round(i))
      if i - float(round(i)) < 0.1 and i - float(round(i)) > -0.1:
        counterint += 1
    if counterint == len(finalv[0]):
        integer = True
    else:
        integer = False
    finalvlength = vectorlength(finalv[0])
    if any(finalvlength > i for i in listofvectorlengths):
      print("Error!")
      print(listofvectors)
      errormain += 1
    countermain += 1
    print(f"Number: {countermain} \nIterations: {finalcount} \nErrors: {errormain} \nFinal V: {finalv}, {finalvlength} \nExistence in Lattice: {integer} \n_____________________________")
