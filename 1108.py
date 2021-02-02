address=input()
res=""

for x in address:
    if x=='.':
        res+='[.]'
    else:
        res+=x
print(res)