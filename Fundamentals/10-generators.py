#159.  Generators allow us to generate a sequence of values over time.
#We use a special keyword called yeild

#-General - We can also convert a range to a list : list(range(100))
#if we use range - it creates them one by one, but whenwe use list - it allocates the giant chunck of memory all at once

#list- is iterable, which means that it can iterate udner the hood.
#everything that is a generator is iterable. But everything which is iterable is not a generator.
#range - generator & iterable; list - iterable only
#difference between a generator and an iterable is the way we implement them

def generator_function(num):
    for i in range(num):
        yield i*2

g=generator_function(100)

next(g)#0
next(g)#2
next(g)#4

print(next(g))#6

#yield pauses the function and comes back to it when we do something called next. 
#if a function has a yield keyword it becomes a generator.
#yield only holds one item in memory and we used it. it holds the latest item.
#Yield keeps track of the state ( value) and it only keeeps the most recent value in memory. 

#Standard way: 
# def male_list(num):
#     result=[]
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list=make_list(100)

#once we reach the end of the range of the num array, a stop iteration error is encountered

#161______________________________________________________________
# decorator code already learned earlier
from time import time
def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000):
        i*5
#above as range is an iterator, it is only goinf to hold one value in memory at once. s

@performance
def long_time2():
    print('2')
    for i in list(range(100000)):
        i*5


long_time() # took 0.014455.. sec
long_time2() # took 0.020107.. sec
# Generators are twice fast and hence more efficient. And can be effecively used to handle large amount of data.

