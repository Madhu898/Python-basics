n1=int(input("enter number1 whose LCM is to be known "))
n2=int(input("enter numbers2 whose LCM is to be known "))
n3=int(input("enter number3 whose LCM is to be known "))

t=max(n1,n2,n3)
print("the largest of three numbers is ",t)
lcm=0
while (1):
    if(t%n1==0 and t%n2==0 and t%n3==0):
        lcm=t
        break
    t=t+1
print("the LCM of (",n1,n2,n3,") is ",lcm)
t1=min(n1,n2,n3)
gcd=0
while(1):
    if(n1%t1==0 and n2%t1==0 and n3%t1==0):
        gcd=t1
        break
    t1=t1-1
print("the gcd of (",n1,n2,n3,") is ",gcd)



    
