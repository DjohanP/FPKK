import csv
import math
import copy

def loadDataset(filename,k,dataSet=[]):
	with open(filename,'rb') as csvfile:
		lines=csv.reader(csvfile)
		dataset=list(lines)
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
	atribut=len(dataset[0])
	print atribut
	for x in range(len(dataset)):#mencari jumlah total atribut
		kls=dataset[x][atribut-1]
		for y in range(atribut-2):#ganti -1 kalau gak ada kelas
			centroid[kls-1][y]=centroid[kls-1][y]+dataset[x][y]
		centroid[kls-1][atribut-1]=centroid[kls-1][atribut-1]+1#terakhir sendiri
	for x in range(k):#mencari jumlah rata-ratanya
		for y in range(atribut-2):#ganti -1 kalau gak ada kelas
			centroid[x][y]=centroid[x][y]/centroid[x][atribut-1]


def main():
	k=input("Jumlah Kelas yang Diinginkan : ")
	k=int(k)
	#print k
	dataset=[]
	centroid=[]
	loadDataset('iris.data',k,dataset)
	loadDataset2('iris.data',k,centroid)
	#printdataset(centroid)
	
	for x in range(len(dataset)):
		#print "---------mulai--------------"
		kelas=carikelas(dataset[x],k,centroid)
		dataset[x][len(dataset[x])-1]=kelas
		#print kelas
		#print "----------Akhir-------------"
	#print len(dataset)


	updatecentroid(dataset,k,centroid)#mengupdate centroid
	#print "==============dataset=============="
	#printdataset(dataset)
	print "centroid"
	printdataset(centroid)



main()
