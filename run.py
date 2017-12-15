import csv
import math
centroid=[]

def loadDataset(filename,dataSet=[]):
	with open(filename,'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
		for x in range(len(dataset)):
			for y in range(len(dataset[x])-1):#kalau gakada kelasnya seperti Iris-virginica hapus -1nya
				dataset[x][y]=float(dataset[x][y])
			dataset[x].append(0)#buat kelas baru
			dataSet.append(dataset[x])
			
def buatrandom(dataset,k):
	banyak = len(dataset)/k
	mulai=0
	#print banyak
	for x in range(k):
		if x==k-1:
			centroid.append(dataset[len(dataset)-1])
		else:
			centroid.append(dataset[mulai])
		mulai=mulai+banyak

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

def carikelas(dataset,k):
	terpendek=9223372036854775807
	kelas=0
	for y in range(k):
		a=carijarak(dataset,centroid[y])
		#print a
		if a<terpendek:
			terpendek=a
			kelas=y+1
			#print a
	print "kelas"
	return kelas

def printdataset(dataset):
	for x in range(len(dataset)):
		print dataset[x]

def main():
	k=input("Jumlah Kelas yang Diinginkan : ")
	k=int(k)
	#print k
	dataset=[]
	loadDataset('iris.data',dataset)
	#printdataset(dataset)
	buatrandom(dataset,k)
	#printdataset(centroid)
	
	for x in range(len(dataset)):
		print "---------mulai--------------"
		kelas=carikelas(dataset[x],k)
		dataset[x][len(dataset[x])-1]=kelas
		#print kelas
		print "----------Akhir-------------"
	printdataset(dataset)
	#print centroid
	#print k
	#print dataset
	#print dataset[0]
	#print len(dataset[0])



main()
