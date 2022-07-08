import sqlite3

from Todo import Todo

class TodoDAO:

    def __init__(self,db_file_name) -> None:
        self._con = sqlite3.connect(db_file_name)

    def save(self,todo:Todo):
        cur = self._con.cursor()
        sql =f"INSERT INTO todos(user_id,title,completed) VALUES ({todo.userId},'{todo.title}',{int(todo.completed)})"
        cur.execute(sql)
        self._con.commit()

    def findAll(self):
        cur = self._con.cursor()
        # all=[]
        sql = "SELECT * FROM todos"
        for id,title,userId,completed in cur.execute(sql):
            todo = Todo(id=id,userId=userId,completed=bool(completed),title=title)
            # all.append(todo)
            yield todo
        
        # return all

    def __del__(self):
        self._con.close()
        