import requests

from pprint import pprint

from Todo import Todo
from TodoDAO import TodoDAO

def main():
    url = "https://jsonplaceholder.typicode.com/todos"
    r = requests.get(url)
    data = r.json()
    dao = TodoDAO('todos_db.db')
    # for todo in data:
    #     t = Todo(**todo)
    #     dao.save(t)
    #     print(t)

    for todo in dao.findAll():
        print(todo)

if __name__=='__main__':
    main()