import traceback

from DivBy12Error import DivBy12Error


def div(a,b):

    if b==12:
        # err = DivBy12Error()
        # raise err
        raise DivBy12Error()
        
    result = a/b
    return result

def call_div(a,b):
    r=0
    print("call_div",a,b)
    try:
        r = div(a,b)
    finally:
        print("return call_div")
    return r

def main():
    try:
        a=2
        b=int(input('value : '))
        c=call_div(a,b)
        print(c)
    except ZeroDivisionError as e:
        print("ZeroDivisionError !")
        print(e)
        traceback.print_exc()
    except ValueError as e:
        print("ValueError !")
        print(e)
    
    except DivBy12Error as e:
        print("DivBy12Error !")
        print(e)

    except Exception as e:
        print("Exception !")
        print(e)
    else:
        print("pas d'erreur :)")

    print("après")
if __name__=='__main__':
    main()