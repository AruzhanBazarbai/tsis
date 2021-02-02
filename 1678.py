command=input()

cnt=""
res=""

for x in command:
    cnt+=x
    if cnt=='G':
        res+='G'
        cnt=""
    elif cnt=="()":
        res+='o'
        cnt=""
    elif cnt=="(al)":
        res+='al'
        cnt=""
print(res)


