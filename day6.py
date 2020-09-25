if __name__ == '__main__':
    N = int(input())
    res=[]
    for i in range(N):
        n,*sda=input().split()
        if n=='insert':
            res.insert(int(sda[0]),int(sda[1]))
        elif n=='remove':
            res.remove(int(sda[0]))
        elif n=='append':
            res.append(int(sda[0]))
        elif n =='sort':
            res.sort()
        elif n=='reverse':
            res.reverse()
        elif n=='pop':
            res.pop(-1)
        else:
            print(res)
