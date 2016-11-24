import math
import random

def split_fun(x,n):
    return (x[0:n],x[n:len(x)])

def karatsuba(x,y):

    x = str(x)
    y = str(y)
    N = max(len(x),len(y))
    x = x.rjust(N,'0')
    y = y.rjust(N,'0')

    if N==1:
        return int(x)*int(y)

    split_len = math.ceil(N/2)

    x_split = split_fun(x, split_len)
    y_split = split_fun(y, split_len)

    A = karatsuba(x_split[0],y_split[0])
    B = karatsuba(x_split[1],y_split[1])
    C = karatsuba(int(x_split[0])+int(x_split[1]),
                  int(y_split[0])+int(y_split[1]))
    K = C-A-B

    num_out = int(A)*(10**((N-split_len)*2))+int(K)*(10**(N-split_len))+int(B)

    return num_out


def tester(N,n):
    test_res = []
    for i in range(N):

        num1 = math.ceil(random.random() * 10 ** n)
        num2 = math.ceil(random.random() * 10 ** n)
        test_res.append(karatsuba(num1,num2) == num1*num2)
    return all(test_res)


print(karatsuba(3141592653589793238462643383279502884197169399375105820974944592,
          2718281828459045235360287471352662497757247093699959574966967627))
