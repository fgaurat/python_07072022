import json



def main():
    data = [
        {
            "userId": 1,
            "id": 1,
            "title": 'delectus "aut" autem',
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

    with open('todos.json','w') as f:
        json.dump(data,f)

    with open('todos.json','r') as f:
        todos = json.load(f)

        print(todos[0]['title'])
        if todos[0]['completed'] : 
            print('ok',todos[0]['completed'])
        else:
            print('ko',todos[0]['completed'])


    a = 2
    print(type(a))


if __name__=='__main__':
    main()