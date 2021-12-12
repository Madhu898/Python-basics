					'''    optimised code 
									def rotateLeft(d, arr):
									    res=arr[0:d]
									    for i in range(len(arr)-d):
										arr[i]=arr[i+d]
									    arr[-d:]=res
									    return arr
'''
'''
                                                input 1  = 
                                                              5                  =  no of elements in list
                                                              10 20 30 40 50     =  elements of list
                                                              2				           =  k times shift


                                                output 1 =
                                                              30 40 50 10 20	   =  after k times shift
'''



a=[]
n=int(input())
for i in range(n):
	ele=int(input())
	a.append(ele)
k=int(input())
for i in range(k):
	temp=a[0]
	for j in range(len(a)-1):
		a[j]=a[j+1]

	a[len(a)-1]=temp
for i in a:
	print(i,end=" ")		

