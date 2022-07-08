# Fibonacci numbers module


a=2
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result





def main():
    fib(100)
    print(fib2(200))

    print("fibo",__name__)

if __name__=='__main__':
    main()