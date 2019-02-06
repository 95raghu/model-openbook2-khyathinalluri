t=[]
def opening_file(filename):
	fout=open(filename)
	for line in fout:
		f=tuple()
		line=line.split(",")
		#print(line)
		str_name=line[2]
		full_name=line[4]
		from_str=line[6]
		to_str=line[7]
		f=(str_name,full_name,from_str,to_str)
		t.append(f)
	return t
print(opening_file("Street_Centrelines.csv"))
