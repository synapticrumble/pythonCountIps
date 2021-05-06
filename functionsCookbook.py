import html
import time
from functools import wraps
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    '''
    For finding a date for the last occurence of a way of the week
    Last Friday for example!
    '''
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


    


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result
    return wrapper

#using the wrapper fucnction built above

@timethis
def countdownUsingDecorator(n):
    '''
    Counts down using decorator
    '''
    while n>0:
        n -= 1



def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

def avg(first, *rest):
    return (first + sum(rest))/(1 + len(rest))


def anyargs(*args, **kwargs):
    # to accept both positional (set form), and keyword-only (dictionary form) arguments

    print(args)
    print(kwargs)

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


def add(x:int, y:int) -> int:
    return x + y

# -------------------------------------------------------------------
items = ['a', 'b', 'c']
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)

for idx, val in enumerate(items):
    print(idx, val)

for idx, val in enumerate(items, 1):
    print(idx, val)
    

# iterating over multiple lists

xpts = [2,3,4,5,6,7]
ypts =[101,102,103,104,105,106]
for x,y in zip(xpts, ypts):
    print(x,y)

# also making dictionary out of two list is easy: 
# use dict(zip(list1, list2)) 

print(dict(zip(xpts, ypts)))

headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]

s = dict(zip(headers, values))
print(s)

# Also, displaying items and values in different way

for name, val in zip(headers, values):
    print(name, '=', val)


# --------------------------------------------------------------------

print (avg(1,2))

print (avg(2,3,4,8))
print("---------------------")

make_element('item', 'Albatross', size='large', quantity=6)
make_element('p', '<spam>')

anyargs('item', 'Albatross', size='large', quantity=6)

anyargs('alibaba', 'amazon', 'azure', 'digitalocean', cloudVendors=4)
print("---------------------")

print("------------using minimum function -----------")

print(minimum(1,5,2,-5,10))
print(minimum(1,5,2,-5, 10, clip=-2))
print(minimum(34,45,23,678,123, 2,22, 15, clip=16))

print(help(add))

print(add(3,4))


print("---------------decorator functions--------------")

countdownUsingDecorator(1000000)
#countdownUsingDecorator(100000000)

print("---------------finding a day of the week--------------")

print('Todays date is: ', datetime.today())
print('last Monday was on date: ', get_previous_byday('Monday'))
print('last Tuesday was on date: ',get_previous_byday('Tuesday'))
print('last Friday was on date: ',get_previous_byday('Friday'))


print("---------------THE END---------------")





