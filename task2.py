def accessible(data,data1):
	a=0
	for line in data1:
		if line[10]=="ARTERIAL":
			#print(True)
			objectid=line[0]
			#print(objectid)
			for line1 in data:
				if line1[2]==objectid:
					print(True)
					if line1[7]=="Accessible":
						 a=a+1
	return a



data1=[]
data=[]
#opening first file
fout1=open("Bus_Stops.csv")
for line in fout1:
        line=line.split(",")
        data.append(line)
#print(data)
#opening second file
fout2=open("Street_Centrelines.csv")
for line in fout2:
	line=line.split(",")
	data1.append(line)
#print(data1)


print(accessible(data,data1))
