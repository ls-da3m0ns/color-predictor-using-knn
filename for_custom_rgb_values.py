import csv
import random 
import math
import operator

def loadDataset(filename, split ,r,g,b, trainingSet=[],testSet=[]):
    with open(filename,'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(3):
                dataset[x][y] = float(dataset[x][y])
            trainingSet.append(dataset[x])
        test=[[r,g,b,'Green']]
        #,[254, 253, 218,'Green']]
        
        for x in range(3):
            test[0][x]=int(test[0][x])
            #test[1][x]=int(test[1][x])
        testSet.append(test[0])    
      

def euclidDistance(instance1,instance2,length):
    distance = 0
    for x in range(length):
        #print(instance1[x])
        distance += pow((instance1[x] - instance2[x]), 2)
        #print(distance)
    return math.sqrt(distance)    

def getNeighbours(trainingSet , testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclidDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distances[x][0])
    return neighbours    

def getResponse(neighbours):
    classVotes = {}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]  
   

def main():
    trainingSet = []
    testSet = []
    split = 0.95
    r=input("enter the values of r :")
    g=input("enter the values of g :")
    b=input("enter the values of b :")
    
    loadDataset('data.data',split,r,g,b,trainingSet,testSet)
    print('Train set :' + repr(len(trainingSet)))
    print('Test set :' + repr(len(testSet)))

    predictions = []
    k = 1
    for x in range(len(testSet)):
        neighbours = getNeighbours(trainingSet, testSet[x],k)
        results = getResponse(neighbours)
        predictions.append(results)
        print('Predicted=' + repr(results))
    
    

main()