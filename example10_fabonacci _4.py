import cmath

def Fabonacci(n) :
    if n == 0:
        Result = 1
    elif n == 1:
        Result = 1
    else:
        Result = (((1 + 5 ** 0.5 ) / 2) ** (n+1) - ((1 - 5 ** 0.5 ) / 2) ** (n+1)) / 5 ** 0.5
    return Result 



N = int(input('please input the N = ' ))
print(' the #%d Fabonacci number is : %d' % (N, Fabonacci(N)))

