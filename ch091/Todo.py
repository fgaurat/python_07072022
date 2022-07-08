

from dataclasses import dataclass


@dataclass
class Todo:

    userId:int
    title:str
    completed:bool
    id:int=0

def main():
    t = Todo(title="le titre",completed=False,userId=120)
    print(type(t))
    t.theTruc

if __name__=='__main__':
    main()