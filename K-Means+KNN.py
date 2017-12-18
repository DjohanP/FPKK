import csv
import math
import copy
import operator
import random
def loadDataset(filename,k,dataSet=[]):
	with open(filename,'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		normalize(dataset)
<<<<<<< HEAD
		counter = 1
		dummydict = {}  # buat nyimpen konversi string ke float
		banyak = len(dataset) / k
		mulai = 0
	for x in range(len(dataset)):
		for y in range(len(dataset[x])):
			try:
				dataset[x][y] = float(dataset[x][y])
			except ValueError:
				if dummydict.has_key(str(dataset[x][y])) == True:
					dataset[x][y] = float(dummydict[str(dataset[x][y])])
				else:
					dummydict[str(dataset[x][y])] = counter
					dataset[x][y] = float(counter)
					counter = counter + 1
		if x==len(dataset)-1:
			z=copy.copy(dataset[len(dataset)-1])
			mulai = 0 #biar nggak keiterasi lagi
			centroid.append(z)
		elif x == mulai:
			z=copy.copy(dataset[mulai])
			mulai = mulai + banyak
			centroid.append(z)
	return dataset, centroid
=======
		banyak=len(dataset)/k
		mulai=0 
		for x in range(len(dataset)):
			for y in range(len(dataset[x])-1):#kalau gakada kelasnya seperti Iris-virginica hapus -1nya
				dataset[x][y]=float(dataset[x][y])
			dataset[x].append(0)#buat kelas baru
			dataSet.append(dataset[x])

def loadDataset2(filename,k,centroid=[]):
	with open(filename,'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		normalize(dataset)
		banyak=len(dataset)/k
		mulai=0 
		for x in range(k):
			if x==k-1:
				z=dataset[len(dataset)-1]
			else:
				z=dataset[mulai]
			for y in range(len(z)-1):#kalau gakada kelasnya seperti Iris-virginica hapus -1nya
				z[y]=float(z[y])
			z.append(0)#buat kelas baru
			centroid.append(z)
			mulai=mulai+banyak
>>>>>>> parent of a7fcd5b... Merge pull request #1 from DjohanP/K-Means+KNN-Enhanced

def normalize(dataset):
    for m in range(len(dataset[0]) - 1):
        temp = []
        for n in range(len(dataset)):
            temp.append(float(dataset[n][m]))
        minimal = min(temp)
        maksimal = max(temp)
        for o in range(len(dataset)):
            if maksimal - minimal == 0:
                dataset[o][m] = temp[o]
            else:
                dataset[o][m] = (temp[o] - minimal) / (maksimal - minimal)

def carijarak(dataset,centroid):
	distance=0
	distance=int(distance)
	#print "---------hitungmulai-------"
	for x in range(len(dataset)-2):#ganti -1 kalau gakada kelas seperti Iris-virginica
		dif=dataset[x]-centroid[x]
		#print dataset[x]
		#print centroid[x]
		distance=distance+(dif*dif)
	#print "--------hitungakhir--------"
	return math.sqrt(distance)

def carikelas(dataset,k,centroid):
	terpendek=9223372036854775807
	kelas=0
	for y in range(k):
		a=carijarak(dataset,centroid[y])
		#print a
		if a<terpendek:
			terpendek=a
			kelas=y+1
			#print a
	#print "kelas"
	return kelas

def printdataset(dataset):
	for x in range(len(dataset)):
		print dataset[x]

def updatecentroid(dataset,k,centroid=[]):

	awal=[]
	for x in range(k):
		for y in range(len(centroid[x])):
			centroid[x][y]=0
<<<<<<< HEAD
<<<<<<< HEAD

=======
#	atribut=len(dataset[0])
	#print atribut
	#print 'centroid'+str(centroid)
	#print 'dataset ='+str(len(dataset))
>>>>>>> parent of 1f2e0ff... Centroid Masuk
	for x in range(len(dataset)):#mencari jumlah total atribut
		kls=dataset[x][-1]
		for y in range(len(dataset[0])-1):#ganti -0 kalau gak ada kelas
#			print str(kls-1) + ' ' + str (y) + ' ' + str(x)
			centroid[kls-1][y]=centroid[kls-1][y]+dataset[x][y]
		centroid[kls-1][-1]=centroid[kls-1][-1]+1#terakhir sendiri
<<<<<<< HEAD
	#printdataset(centroid)
=======
	atribut=len(dataset[0])
	#print atribut
	for x in range(len(dataset)):#mencari jumlah total atribut
		kls=dataset[x][atribut-1]
		for y in range(atribut-2):#ganti -1 kalau gak ada kelas
			centroid[kls-1][y]=centroid[kls-1][y]+dataset[x][y]
		centroid[kls-1][atribut-1]=centroid[kls-1][atribut-1]+1#terakhir sendiri
>>>>>>> parent of a7fcd5b... Merge pull request #1 from DjohanP/K-Means+KNN-Enhanced
=======
>>>>>>> parent of 1f2e0ff... Centroid Masuk
	for x in range(k):#mencari jumlah rata-ratanya
		for y in range(atribut-2):#ganti -1 kalau gak ada kelas
			centroid[x][y]=centroid[x][y]/centroid[x][atribut-1]


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

def getNeighbors(trainingSet,testInstance,k):
	distances=[]
	length=len(testInstance)-2#ganti -1 jika gakada kelas
	for x in range(len(trainingSet)):
		dist=carijarak(testInstance,trainingSet[x])
		#dist=cosineSimilarity(testInstance, trainingSet[x], length)	
		#print dist
		distances.append((trainingSet[x],dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors=[]
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors


def getAccuracy(testSet,predictions):
	correct=0
	for x in range(len(testSet)):
		#print "========pecah========"
		if testSet[x][-1]==predictions[x]:
			correct+=1
		#print testSet[x][-1]
		#print predictions[x]
		#print "============akhir========"
	#print correct
	return (correct/float(len(testSet)))*100.0
def splitx(testset,trainingset,dataset):
	rnd=0.67
	for x in range(len(dataset)):
		if random.random()<rnd:
			trainingset.append(dataset[x])
		else:
			testset.append(dataset[x])



def main():
	k=input("Jumlah Kelas yang Diinginkan : ")
	k=int(k)
	#print k
<<<<<<< HEAD
	dataset, centroid = loadDataset('iris.data',k)
	#######################Membuat K Means############################################
<<<<<<< HEAD

=======
	dataset=[]
	centroid=[]
	loadDataset('iris.data',k,dataset)
	#######################Membuat K Means############################################
	loadDataset2('iris.data',k,centroid)
	#printdataset(centroid)
	
>>>>>>> parent of a7fcd5b... Merge pull request #1 from DjohanP/K-Means+KNN-Enhanced
=======
#	loadDataset2('iris.data',k,centroid)
	#print 'centroid : ' + str(centroid)
	#printdataset(centroid)
	#print 'dataset =' + str(len(dataset))
>>>>>>> parent of 1f2e0ff... Centroid Masuk
	for x in range(len(dataset)):
		#print "---------mulai--------------"
		kelas=carikelas(dataset[x],k,centroid)
		dataset[x][len(dataset[x])-1]=kelas
		#print kelas
		#print "----------Akhir-------------"
<<<<<<< HEAD
	#print str(len(dataset))
	#print 'dataset =' + str(dataset)
=======
	#print len(dataset)
>>>>>>> parent of a7fcd5b... Merge pull request #1 from DjohanP/K-Means+KNN-Enhanced


	updatecentroid(dataset,k,centroid)#mengupdate centroid
	#print "==============dataset=============="
	#printdataset(dataset)
	#print "centroid"
	#printdataset(centroid)
	while True:
		cek=1#udah konfergen belum
		for x in range(len(dataset)):
			#print "---------mulai--------------"
			kelas=carikelas(dataset[x],k,centroid)
			if dataset[x][len(dataset[x])-1]!=kelas:
				cek=0
			dataset[x][len(dataset[x])-1]=kelas
			#print kelas
			#print "----------Akhir-------------"
		updatecentroid(dataset,k,centroid)#mengupdate centroid
		#printdataset(centroid)
		if cek==1:
			#print "Sudah Konfergen"
			break
		#input()
	print "===================Data Baru Setelah K Means============================"
	printdataset(dataset)
	##################################Akhir K Means########################################
	testset=[]
	trainingset=[]
	predictions=[]
	#splitx(testset,trainingset,dataset)
	#print len(testset)
	k=input("Masukkan K: ")
	k=int(k)
	fold=input("Masukkan Fold: ")
	fold=int(fold)
	sisafold=len(dataset)%fold
	n=0
	total=float(0)
	for x in range(fold):
		tambah=len(dataset)/fold
		if(x<sisafold):
			tambah=tambah+1
		for y in range(tambah):
			testset.append(dataset[n])
			#print dataset[n]
			n=n+1
			#print n

		for z in range(len(dataset)):
			if z<n-tambah:
				trainingset.append(dataset[z])
			elif z>=n:
				trainingset.append(dataset[z])
		#print "=================MUlai debug=================="
		for y in range(len(testset)):
			neighbors=getNeighbors(trainingset,testset[y],k)
			result=getResponse(neighbors)
			predictions.append(result)
			print('> predicted=' + repr(result) + ', actual=' + repr(testset[y][-1]))
		accuracy=getAccuracy(testset,predictions)
		#print accuracy
		print('Accuracy: '+repr(round(accuracy, 2)) + '%')
		#print "===================Akhir Debug==============="
		total=total+accuracy
		testset=[]
		trainingset=[]
		predictions=[]
	meanaccuracy=total/fold
	print round(meanaccuracy, 2)


	#print fold
	#for x in range(len(testset)):
	#	neighbors=getNeighbors(trainingset,testset[x],k)
	#	result=getResponse(neighbors)
	#	predictions.append(result)
	#	#print result
	#	print('> predicted=' + repr(result) + ', actual=' + repr(testset[x][-1]))

	#accuracy=getAccuracy(testset,predictions)
	#print('Accuraccy: '+repr(accuracy)+'%')
	
main()
