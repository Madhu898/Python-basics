'''from typing import ItemsView
di={"madhu":"programmer",
"malli":"father of madhu",
"raji":"mother of madhu"}
print(di)
di.update({"fa":"djdj"})
d2=di
#del d2["madhu"]
print(d2)'''
di={
    1:"addition",
    2:"subtraction",
    3:'multiplication',
    4:"division ",
    5:"invalid operation"
}
print(di)
print(di[2])
print(di.keys())
d1=di.copy()
del d1[1]
print(d1)
print(di)
