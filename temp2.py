def mul(a):
    def helper(b):
        return a * b
    return helper

def first_test():    print("Test function 1") #тут и так понятно
def second_test():    print("Test function 2")
def decore(fn): #внутрь кинули функцию
    def wrap():
        print("start")
        fn()
        print("stop")
    return wrap #ебаный мэджик
first_wrapped = decore(first_test)
first=first_wrapped
first()