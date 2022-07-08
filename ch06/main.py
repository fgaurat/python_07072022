import fibo as fb
# from fibo import fib as fb,fib2,a as val_a
from fibo import fib
import sys

# fb.fib(100)


# print(50*'-')
# def fib(n):
#     print("bonjour fib",n)


def main():
    # if len(sys.argv)!=2:
    #     print('Erreur !')
    #     sys.exit(-1)

    if len(sys.argv)>1:
        print(sys.argv[1])
        value = int(sys.argv[1])
        # fib(1000)
        fb.fib(value)

        print(fb.a)
        print("main",__name__)
    else:
        print("Erreur !")

if __name__ == '__main__':
    main()