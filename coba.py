import csv
import random
import math
import operator
from sklearn.metrics.pairwise import cosine_similarity
def loadDataset(filename,split,trainingSet=[],testSet=[]):
	with open(filename,'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		for x in range(len(dataset)-1):
			for y in range(4):
				dataset[x][y]=float(dataset[x][y])
			if random.random()<split:
				trainingSet.append(dataset[x])
			else:
				testSet.append(dataset[x])

def euclideandistance(instance1,instance2,length):
	distance=0
	distance=int(distance)
#	distance=0
	for x in range(length):
		m=instance1[x]
		m=float(m)
		y=instance2[x]
		y=float(y)
		distance=distance + pow((m - y), 2)
		#print instance1[x]
	return math.sqrt(distance)

def cosineSimilarity(instance1,instance2,length):
	#distance=0
	#Data1=[]
	#Data2=[]
	total=0
	total=float(total)
	dis1=0
	dis1=float(dis1)
	dis2=0
	dis2=float(dis2)
	for x in range(length):
		m=instance1[x]
		m=float(m)
		y=instance2[x]
		y=float(y)
		total=total+(m*y)
		dis1=dis1+(m*m)
		dis2=dis2+(y*y)
	dis1=math.sqrt(dis1)
	dis2=math.sqrt(dis2)
	result=total/dis1/dis2
	#for x in range(length):
	#	Data1.append(instance1[x])
	#	Data2.append(instance2[x])
	#result=cosine_similarity(Data1,Data2)
	cos_sim=result
	#if(cos_sim>1.0):
	#	cos_sim=1.0
	#elif(cos_sim< -1.0):
	#	cos_sim=-1.0
	#angle_in_radians=math.acos(cos_sim)
	#return math.degrees(angle_in_radians)
	return 1-cos_sim

def getNeighbors(trainingSet,testInstance,k):
	distances=[]
	length=len(testInstance)-1
	for x in range(len(trainingSet)):
		dist=euclideandistance(testInstance,trainingSet[x],length)
		#dist=cosineSimilarity(testInstance, trainingSet[x], length)	
		#print dist
		distances.append((trainingSet[x],dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors=[]
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def getResponse(neighbors):
	classvotes={}
	for x in range(len(neighbors)):
		response=neighbors[x][-1]
		if response in classvotes:
			classvotes[response]+=1
		else:
			classvotes[response]=1
	sortedvotes=sorted(classvotes.iteritems(),key=operator.itemgetter(1),reverse=True)
	return sortedvotes[0][0]
def getAccuracy(testSet,predictions):
	correct=0
	for x in range(len(testSet)):
		if testSet[x][-1]==predictions[x]:
			correct+=1
	return (correct/float(len(testSet)))*100.0

def main():
	trainingSet=[]
	testSet=[]
	split=0.67
	loadDataset('iris.data',split,trainingSet,testSet)
	print 'Train set'+repr(len(trainingSet))
	print 'Test set: ' + repr(len(testSet))
	y=len(trainingSet)
	predictions=[]
	#read k
	k=input("Masukkan K: ")
	k=int(k)
	print k
	for x in range(len(testSet)):
		neighbors=getNeighbors(trainingSet,testSet[x],k)
		result=getResponse(neighbors)
		predictions.append(result)
		#print result
		print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))

	accuracy=getAccuracy(testSet,predictions)
	print('Accuraccy: '+repr(accuracy)+'%')
	#print y
	#for x in range(repr(len(trainingSet))):
	#	print "hehe\n"
	#for x in range (y):
	#	print trainingSet[x]
main()
