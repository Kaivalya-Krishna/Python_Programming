a=('A', 'B', 'C')
k= input("Enter the desired value - ")
j=0
for i in a:
    if (i==k):
        j=j+1
if (j>0):
    print (k, "exists")
else:
    print (k, "do not exist")