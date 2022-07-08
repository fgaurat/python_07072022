ma_chaine = 'Il m\'a dit : "Il fait beau"'
print(ma_chaine)

# p = "c:\\name\\truc"
p = r"c:\name\truc"
print(p)

hello = "Bonjour\n"
hello+= "Fred"

hello = """Bonjour
Fred
ligne suivante
"""
print(hello)
print(50*'-')

w = 'Python'
w2 = 'Python'
print(w)
print(w[3])
print(len(w))

print(w[len(w)-1])
print(w[-1])
print(w[:])
print(id(w))
print(id(w2))
a=1 
b=1 
print(id(a))
print(id(b))
print(50*'-')

squares = [1, 4, 9, 16, 25]
squares2 = squares[:]
squares[0] = 1000

print(squares)
print(squares2)


sq1 = [
    [10,20],
    [30,40],
    [50,60],
]
print(sq1[1][1])
sq2 = sq1[:]
sq1[1][1] = 4000
print(sq2)
sq2.append("toto")
sq2.append([70,80])
print(sq2)

print(50*'-')
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b