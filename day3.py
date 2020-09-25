def merge_the_tools(string, k):
    # your code goes here
    lines=int(len(string)/k)
    line=0
    part=''
    listo=[]
    for i in range(len(string)):
        if int(i/k) >line:
            line+=1
            listo.append(part)
            part=string[i]
        else:
            part+=string[i]
    listo.append(part)
    for i in listo:
        res=''
        for k in i:
            if not k in res:
                res+=k
        print(res)


merge_the_tools(input(),int(input()))