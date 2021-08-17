l=[3,1,7,8,9,0,3]#it can be mutable
print(f"the intial list is :{l}")
l=list(filter(lambda a:a%3==0,l))#it will filters the values according to the condition or given function
print(f"the filteres list according to the condition (or) function are : {l}")
l.sort()#it will sort the list in ascending order 
print(f"the sorted list is :{l}")
l=list(map(lambda a:a*a,l))#it will change the  entire values according to the given condition (or) given function
print(f"the mapped list is : {l}")
t=(1,9,12,3,0,4,5)#it is not mutable i.e not changeble 
print(f"the intial tuple is :{t}")
#t.sort()
#print(f"the sorted tuple is :{t}")
t=list(map(lambda  a:a+3,t))
print(f"the mapped items in tuple are : {t}")




