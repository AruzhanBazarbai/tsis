arr=input().split()
cnt=0


for i in range (0,len(arr)):
    b=arr[i]
    x=i
    for j in range (x+1,len(arr)):
        if b==arr[j] and x<j:
            cnt+=1

print(cnt)
   

