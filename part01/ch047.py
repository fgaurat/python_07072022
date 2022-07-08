def fib(n=2000):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n=2000):    # write Fibonacci series up to n
    """Return a Fibonacci series up to n in a list."""
    l = []
    a, b = 0, 1
    while a < n:
        l.append(a)
        a, b = b, a+b

    return l



# Now call the function we just defined:
fib(2000)
val = fib2(2000)
print(val)

print(fib)
print(fib2)

# toto = fib2

# print(toto(200))
val = fib2()
print(val)

print(50*'-')
i = 5

def f(arg=i):
    print(arg)

i = 6
f()


def f(a:int, L:list=[]):
    if L == None:
        L=[]
    L.append(a)
    return L

the_list = []
print(f("toto")) # [1]
print(f(2)) # [1,2]
print(f(3))

print(50*'-')

def f(a,b):
    print("a : "+a)
    print("b : "+b)

f(b='valb',a='vala')



print(50*'-')

def add(*params):
    print(params)
    result = 0
    for v in params:
        result+=v
    return result

l = [1,2,3,4,5]

# r = add(l)
r = add(1,2,3,4,5)
print(r) #15

print(50*'-')


def hello(sep=",",**kws):
    print(kws)
    print(kws['name'],kws['age'],sep=sep)
    # print("Hello",firstName,name)

hello(name='GAURAT',firstName = 'Fred',age=45, job="dev")


print(50*'-')

def add(*params):
    result = 0
    for v in params:
        result+=v
    return result

values = [1,2,3,4,5]
r = add(*values)# add(1,2,3,4,5])
print(r)

print(50*'-')

values = [1,2,3,4,5]
valuesx2 = []

for v in values:
    valuesx2.append(v*2)
print(valuesx2)


# def mult2 (item):
#     return item*2
# valuesx2 = list(map(mult2,values))

valuesx2 = list(map(lambda i:i*2,values))
print(valuesx2)

