def Fabonacci(n) :
    fab = [0]*(n+2)
    fab[0]=1
    fab[1]=1
    if n == 0:
        Result = 1
    elif n == 1:
        Result = 1
    else :
        for i in range(2,n+1):
            fab[i] = fab[i-1]+fab[i-2]
            Result = fab[i]
    return Result



N = int(input('please input the N = ' ))
print(' the #%d Fabonacci number is : %d'%(N,Fabonacci(N)))
 
 
