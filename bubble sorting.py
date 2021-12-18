'''
      input :
              a=[1200,1,5,9,7,0,68,100]              
      output:
              [0, 1, 5, 7, 9, 68, 100, 1200]


'''
os.system('cls')
def bs(a):    
    l=len(a)
    for i in range(l):
        for j in range(l-i-1):
            if a[j]>a[j+1]:
             a[j],a[j+1]=a[j+1],a[j]
    return a     
a=[1200,1,5,9,7,0,68,100]
print(bs(a))
