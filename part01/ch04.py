# val_a = int(input('Valeur de a : '))


# if val_a % 2 ==0:
#     print("pair")
# elif val_a % 3 ==0:
#     print("divisible par 3")
# else:
#     print("else")

print(50*'-')

l = ['val1','val2','val3','val4',"toto"]

for elem in l:
    print(elem+" "+str(len(elem)))


for i in range(len(l)):
    print(str(i)+" "+l[i])


print(list(range(5)))

r = list(range(12,25,2))
print(r)



somme = 0
values = [1,5,8,9,12,78]


for v in values:
    # somme= somme+v
    somme+= v

print(somme)

somme = sum(values)
print(somme)
print(50*'-')

values = [1,5,8,9,12,78]

found = False
for v in values:
    print(v)
    if v == 28:
        found = True
        break

if found:
    print("valeur trouvée")
else:
    print("valeur non trouvée")


for v in values:
    print(v)
    if v == 28:
        print("valeur trouvée")
        break
else:
    print("valeur non trouvée")


b = 3
if b ==3:
    pass