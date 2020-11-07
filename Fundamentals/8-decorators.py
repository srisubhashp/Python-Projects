#decorators - 19-Oct-2020

def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('***********')
    return wrap_func

#Declarators can be used just above as a word, when defining our functions, as in the example below : 
@my_decorator
def hello():
    print('Hellooo')

@my_decorator
def bye():
    print('See ya later')

hello()
#*********
#Hellooo
#*********

bye() #similar output as hello function, with just the string displayed is different

#Using a decorator, the decorator function wraps the original function and adds additional functionality (enhances it). 
#-----------------------------------------------------------------------

#Another form of wrapping functions with decorators:

hello2=my_decorator(hello)

hello2() #it prints the starts followed by the Hellooo and the last line contains stars again.
my_decorator(hello)()# another form of wrapping that is temporary. 

#151____________________________________________________________________________________
# If we need to take in arguments we need to pass them everywhere.

def my_Decorator(func):
    def wrap_func(x,y):
        print('********')
        func(x,y)
        print('***********')
    return wrap_func

hello2=my_decorator(hello)
hello2('HI','bye')

# *args takes all the positional arguments, and **kwargs which takes all the keyword arguments. 

# We use (*args) in the function to unpack all the positional arguments. & (**kwargs) to unpack all the positional arguments. This
# ITs called decorator. Bcz it has the famous decorator pattern in programming and provides flexibility. 

# Regarding the below code, you do not need to change the function if the number of arguments vary each time.
def my_Decorator(func):
    def wrap_func(*args, **kwargs):
        print('********')
        func(*args, **kwargs)
        print('***********')
    return wrap_func

@my_Decorator
def hello(greeting,emoji=':('):
    print(greeting,emoji)

#152____________________________________________________________________________________

#Decorators can be used for testing the time consumed by the functions in
# We are importing the time module into this snippet
from time import time
def performance(fn):
    def wrapper(*args, **kwargs):
        t1=time()
        result=fn(*args, **kwargs)
        t2=time()
        print(f' took {t2-t1} seconds.')


@performance# as now this decorator can be used to measure the time consumption of any function
def long_time():
    for i in range(100000000):
        i*5
