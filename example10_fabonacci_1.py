def Fabonacci(n) :
    if n == 0:
        Result = 1
    elif n == 1:
        Result = 1
    else:
        Result = Fabonacci(n - 1) + Fabonacci(n - 2)
    return Result


N = int(input('please input the N = ' ))
print(' the #%d Fabonacci number is : %d'%(N,Fabonacci(N)))
 
 
