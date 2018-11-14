import numpy as np

def Fabonacci(n):
    A = np.mat('1 1;1 0')
    I= np.mat('1 0;0 1')
    if n == 0:
        Result = 1
    else:
        for i in range(1, n+1):
            I = I * A
        Result = I[0, 0]
    return Result


N = int(input('please input the N = '))
print(' the #%d Fabonacci number is : %d' % (N, Fabonacci(N)))
