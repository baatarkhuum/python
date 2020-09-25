if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr.sort()
    for i in range(1,len(arr)+1):
        if arr[-i] < arr[-1]:
            print(arr[-i])
            break
    
    

