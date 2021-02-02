arr=input().split()

a=[]
x=0
a.append(x)

for i in range(len(arr)):
    x+=int(arr[i])
    a.append(x)

maxi=-101

for i in range(len(a)):
    if maxi<a[i]:
        maxi=a[i]
print(maxi)
