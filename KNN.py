import csv
import random
import math
import operator

def loadDataset(filename,data=[]):
	with open(filename,'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		for x in range(len(dataset)-1):
			for y in range(len(dataset[x])-1):
				dataset[x][y]=float(dataset[x][y])
			data.append(dataset[x])

def Kfoldvalidation(banyakData,banyakFold,SisaFold,pilihan,data,k):
	trainingSet=[]
	predictions=[]
	testSet=[]
	banyak=0
	total=0
	for x in range(10):
		tambah=banyakFold
		if(x<SisaFold):
			tambah=tambah+1
		for y in range(tambah):
			testSet.append(data[banyak])
			banyak=banyak+1
		

		print ('banyak = '+repr(banyak))
		print ('tambah = '+repr(tambah))
		for z in range(banyakData):
			if z<banyak-tambah:
				trainingSet.append(data[z])
			elif z>=banyak:
				trainingSet.append(data[z])
		print "============Mulai Debug===================="
		for y in range(len(testSet)):
			neighbors=getNeighbors(trainingSet,testSet[y],k,pilihan)
			result=getResponse(neighbors)
			predictions.append(result)
			print('> predicted=' + repr(result) + ', actual=' + repr(testSet[y][-1]))
		accuracy=getAccuracy(testSet,predictions)
		print('Accuracy '+repr(x+1)+': '+repr(accuracy)+'%')
		print "================Akhir Debug=============="
		total=total+accuracy
		testSet=[]
		trainingSet=[]
		predictions=[]
	return total

def euclideandistance(instance1,instance2,length):
    	distance=0
    	distance=int(distance)
    	for x in range(length):
    		m=instance1[x]
    		m=float(m)
    		y=instance2[x]
    		y=float(y)
    		distance=distance + pow((m - y), 2)
    	return math.sqrt(distance)
     
def cosineSimilarity(instance1,instance2,length):
    	total=float(0)
    	dis1=float(0)
    	dis2=float(0)
    	for x in range(length):
    		m=float(instance1[x])
    		y=float(instance2[x])
    		total=total+(m*y)
    		dis1=dis1+(m*m)
    		dis2=dis2+(y*y)
    	dis1=math.sqrt(dis1)
    	dis2=math.sqrt(dis2)
    	result=total/dis1/dis2
    	return 1-result
     
def manhattan(testSet,trainingSet, length):
        distance = 0
        for x in range(length):
            distance += abs(testSet[x] - trainingSet[x])
        return distance

def getNeighbors(trainingSet,testInstance,k,pilihan):
	distances=[]
	length=len(testInstance)-1
	for x in range(len(trainingSet)):
		if(pilihan==1):
			dist=euclideandistance(testInstance,trainingSet[x],length)
		elif(pilihan==2):
			dist=cosineSimilarity(testInstance, trainingSet[x], length)	
		elif(pilihan==3):
			dist=manhattan(testInstance, trainingSet[x], length)	
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
		print "===========Mulai=========="
		if testSet[x][-1] == predictions[x]:
			print "benar"
			correct+=1
		print testSet[x][-1]
		print predictions[x]
		print "=========Akhir==========="
	return (correct/float(len(testSet)))*100.0

def main():
	data=[]
	loadDataset('iris.data',data)
	print("Pilih algoritma mencari jarak")
	print("1. Eucledian Distance")
	print("2. Cosine Distance")
	print("3. Manhattan Distance")
	pilihan=input("Pilihan :")
	pilihan=int(pilihan)
	k=input("K= ")		
	banyakData=len(data)
	banyakFold=banyakData/10
	SisaFold=banyakData%10
	total=Kfoldvalidation(banyakData,banyakFold,SisaFold,pilihan,data,k)	
	mean_accuracy=total/10
	print "Mean Accuracy = "+repr(mean_accuracy)+'%'
	print repr(banyakData)
main()
