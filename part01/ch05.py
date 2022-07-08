from collections import deque


values = [1,2,3,4,5]

print(values)
l = values.pop()
print(l)
print(values)
values.insert(0,0)
print(values)
first = values.pop(0)
print("first",first)
print("values",values)

d = deque(values)
print(d)
d.appendleft(1000)
print(d)
first = d.popleft()
print("first",first)
print("values",values)
print(50*'-')
values = [1,2,3,4,5]

valuesx2  = []
for v in values:
    valuesx2.append(v*2)

valuesx2  = [v*2 for v in values]


s = "   toto   "
print(s.strip())

values = ["   value1  ","value2   ","   value3"]


clean_values=[]
for v in values:
    clean_values.append(v.strip())
print(clean_values)

# clean_values = ["value1","value2","value3"]
clean_values=[v.strip() for v in values]
print(clean_values)



labels = ['name','firstname','job']
values = ['GAURAT','Fred','dev']

r = list(zip(labels,values))
print(r)


a = 2 
print(a)
print(50*'-')


t = 1,2,3,5
print(t)

for i in t:
    print(i)


# t[0] = 10

a,b=0,1
c = 0,1
del a

print(b)

def the_function():

    return "toto","titi"

s1,s2 = the_function()


a,b,*c = 0,1,2,5,4589

print(a)
print(b)
print(c)
s = 1,
print(s)



values = [1,5,8,9,12,78]


for i,v in enumerate(values):
    print(i,v)


print(50*'-')
s = {1,5,6,5,15,5,7,5}
print(len(s))
print(s)


values = ["value 01","value 01","value 04","value 01","value 05","value 03","value 01"]
dedup = sorted(list(set(values)))

print(dedup)


d = {'name':'GAURAT','firstName' : 'Fred'}


print(d['name'])

d['jobs'] = ["dev"]
print(d)
d['jobs'].append("datascientist")
print(d)

for key,value in d.items():
    print(key,value)