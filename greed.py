
event=[[1,3,0,5,3,5,6,8,8,2,12],[4,5,6,7,9,9,10,11,12,14,16]]
start=event[0]
finish=event[1]

n=len(start)
k=0
#for iterative 
def greedy_activity_selector(start,finish):
	A=[1]
	k=1
	for m in range(2,n):
		if start[m]>=finish[k]:
			A.append(m+1)
			k=m
	# print (A)
	return A

print(greedy_activity_selector(start,finish))

# for recursion 
def recursive_acti_sel(start,finish,k,n):
	A=[1]
	m=k+1
	while m <n and start[m]<finish[k] and k>0:		#find first activity in start to finish
		m=m+1
	if m<=n:
		A.append(recursive_acti_sel(start,finish,m,n))
		return "True"
	else: 
		return "False"
print(recursive_acti_sel(start,finish,1,n))

