'''
    input 1 =
                man
                nam
     output = 
                yes
'''

def sort(s):
    res=''.join(sorted(s))
    return res

s1=input()
s2=input()
s1=sort(s1)
s2=sort(s2)
if (s1==s2):
    print("yes")
else:
    print("no")
