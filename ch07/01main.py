def main():
    name = "MARTIN"
    age = 45

    # s = "name : "+name+" age : "+str(age)
    s = f"name : {name} age : {age}"

    print(s)

    a = 2
    b = 3
    c = a/b
    # s = f"{a=}/{b=} = {c*100=:.2f}%"
    s = f"{a=}/{b=} = {c=:.2%}"

    print(s)

    s = "name : {} age : {}".format(name,age)
    s = "age : {1} name : {0} ".format(name,age)
    print(s)
    s = "{}/{} = {:.2%}".format(a,b,c)
    print(s)

    s = "name : {name} age : {age}".format(name=name,age=age)
    print(s)

    l = ["MARTIN",45]
    # s = "name : {} age : {}".format("MARTIN",45)
    s = "name : {} age : {}".format(*l)
    print(s)
    l = {"name":"MARTIN","age":45}
    s = "name : {name} age : {age}".format(**l)
    print(s)


    for i in range(20):
        print("{:>9}toto".format(i))


if __name__=='__main__':
    main()