from pprint import pprint

def main():

    data =[]

    with open('todos.csv','r') as f:
        lines = f.readlines()
        keys = lines[0].strip().split(';')

        lines = lines[1:]
        
        
        for line in lines:
            line = line.strip().split(';')
            value = zip(keys,line)
            dico = dict(value)
            data.append(dico)

    pprint(data)



def main_write_csv():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": "delectus aut autem",
            "completed": False
        },
        {
            "userId": 1,
            "id": 2,
            "title": "quis ut nam facilis et officia qui",
            "completed": False
        },
        {
            "userId": 1,
            "id": 3,
            "title": "fugiat veniam minus",
            "completed": False
        },
        {
            "userId": 1,
            "id": 4,
            "title": "et porro tempora",
            "completed": True
        },
        {
            "userId": 1,
            "id": 5,
            "title": "laboriosam mollitia et enim quasi adipisci quia provident illum",
            "completed": False
        }
    ]

    with open('todos.csv','w') as f:
        print(*data[0].keys(),sep=";",file=f)
        for todo in data:
            print(*todo.values(),sep=";",file=f)


    with open('todos.csv','w') as f:
        list_header = data[0].keys()
        header = ";".join(list_header)
        print(header,file=f)

        for todo in data:
            values = [str(i) for i in todo.values()]
            line = ";".join(values)
            print(line,file=f)



def writefile():
    with open('monfichier.txt','w') as f:
        for i in range(10):
            print(f'This is a test {i:02d}',file=f)


def readfile():
    # with open('monfichier.txt','r') as f: => lecture par défaut
    # with open('monfichier.txt') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line.strip())
    with open('monfichier.txt') as f:
        for line in f:
            print(line.strip())
        

if __name__ == '__main__':
    main()
    # writefile()
    # readfile()





