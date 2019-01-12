

def main():
    num = 12
    print(fibonacci(num))
    print(fibonacci2(num))
    fibo_minus2 = 0
    fibo_minus1 = 1
    fibo = 0

def fibonacci2(n):
    if n==0:
        return 0 #F0
    elif n==1:
        return 1 #F1
    else:
        fibo_minus1 = 1 #Fn-1
        fibo_minus2 = 0 #Fn-2
        for i in range(2,n):
            fibo = fibo_minus1 + fibo_minus2 #Fn = Fn-1 + Fn-2
            #値を更新
            fibo_minus2 = fibo_minus1
            fibo_minus1 = fibo
        return fibo

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci_sub2(n-2, 1, 0)

def fibonacci_sub(n, last1, last2):
    if n == 0:
        return last1
    else:
        return fibonacci_sub(n-1, last1+last2, last1)

def fibonacci_sub2(n, fibo_minus1, fibo_minus2):
    return fibo_minus1 if n==0 else fibonacci_sub2(n-1, fibo_minus1+fibo_minus2, fibo_minus1)

if __name__ == '__main__':
    main()
