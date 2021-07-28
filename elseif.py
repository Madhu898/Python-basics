# for if else loop
'''
 a = int(input("enter the first number "))
b = int(input("enter the second number "))
c = int(input("enter the third number "))
if a > b and a > c:
    print(a, "a is largest of three numbets ")
elif b > c and b > a:
    print(b, "is largest number ")
else:
    print(c, " is largest of three numbers ") '''
#num = int(input("enter an iteger "))
#rem = num % 10
# if rem == 0:
#    print("the number is divisible by 10 and 5")
# else:
#    print("the number is not divisible by 10 and 5")
#if the numbers are 4 and 9 the sum must be of 89 andn subtraction is of 4 and multiplication of 98
print("falsi caluulator ")
a = int(input("enter first  number\n "))
b = int(input("enter seond number\n  "))
op = input("enter arithmatic operator ( + , _ , * , \ , )\n")
if a==4 and b==9 and op=="+":
    print("the addition of two numbers is ",89)
elif a==4 and b==9 and op=="-":
    print("the subtraction  of two numbers is ",4)
elif a==4 and b==9 and op=="*":
    print("the multiplication of two numbers is ",98)   
 
elif op == "+":
    print("the addition of two numbers is\n ", a+b)
elif op == "-":
    print("the subtraction of two numbers is\n ", a-b)
elif op == "*":
    print("the multiplication of two numbers is\n ", a*b)
elif op == "/":
    print("the division of two numbers are\n ", a/b)
else:
    print("the input is invalid ")
