print("guess the number between (1 to 100) in the guessing game")
n=36
i=1
flag=0
while i<=9 :
    print("chances remaining ",10-i)
    i=i+1
    num=int(input("guess the number\n"))
    if num==n:
        print("wowwww :) you guessed it champ")
        flag=1
        break
    elif num<n:
        print("the number is little more :)\n ")
    elif num>n:
        print("the number is little less  :)\n ")
        
if flag==0:
    print("sorry you lost the game :( try again ")