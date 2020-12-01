

def lookingForNumbersThatSumTo(data,start,number,nnumber):
	ret=[]
	for i in range(start,len(data)):
		if(nnumber==1):
			if(data[i]==number):
				return [i]
		else:
			rem=number-data[i]
			if(rem<0):
				continue
			n=lookingForNumbersThatSumTo(data,i+1,rem,nnumber-1)
			if(n!=None):
				ret.append(i)
				ret+=n
				return ret
	return None
			

def readInputFile(path):
	f=open(path,"r")
	data=[]
	for l in f:
		data.append(int(l))
	return data


if __name__=="__main__":
	data=readInputFile("input")
	lend=len(data)
	for n in range(2,7):
		res=lookingForNumbersThatSumTo(data,0,2020,n)
		if(res==None):
			print "{0} No solution could be found".format(n)
			continue
		total=0
		for i in res:
			total+=data[i]
		if(total!=2020):
			print "Sum does not equal to 2020 {}".format(total)
		mul=1
		for i in res:
			mul*=data[i]
		print "{0} {1}".format(n,mul)

