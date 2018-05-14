#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 11:36:37 2018

@author: airos

Notes taken and tips collected from Next Day Video channel on Youtube
speaker: Raymond Hettinger
https://www.youtube.com/watch?v=OSGv2VnC0go&t=1757s&list=PLFr_FlT2oMcskeTNjo3gHq5fdbXbPrsdw&index=2

General notes:
    * iterate wherever possible
    * make things iterable (compatible w Python toolkit)
    * be very comfortable with dictionaries (i.e. using keys, sorting with keys)
    * avoid indexing (i.e. use enumerate, iter, iteritems, zip etc.)
    * don't copy like crazy (slows code)
    * make code understandable (w tuple unpacking vs indexing, printing labeled tuples, etc.
"""

######################################
#Looping over a range of numbers

#1)
#takes up memory
for i in [0,1,2,3,4,5]:
    print(i**2)

#2)
#(pre Python3, range created a list and loaded whole list in memory; Python3+: xrange --> range)
for i in range(6):
    print(i**2)

#3)
#iterates over each item; does not load whole list in memory
#for i in xrange(6):
#    print(i**2)
    
######################################
#Looping over a collection and indicies
colors = ['red','green','blue','yellow']

#1) loads whole list in memory
for i in range(len(colors)):
    print(i, '-->', colors[i])
    
#2) iterates; lower memory cost
for i, color in enumerate(colors):
    print(i,'-->', colors[i])
    
######################################
#Looping over two collections

names = ['raymond','rachel','matthew']
colors = ['red','green','blue','yellow']

#1)
n = min(len(names), len(colors))
for i in range(n):
    print(names[i],'-->',colors[i])
   
#2) (pre Python3: zip loaded 3 lists in memory; post Python3: izip --> zip)
for name, color in zip(names,colors):
    print(name,'-->',color)
    
#3) izip (now zip) iterates, saving memory
#for name, color in izip(names,colors):
#    print(name,'-->',color)
    
######################################
#Custom sort order
colors = ['red','green','blue','yellow']
 
#1) don't need to do this...   
def compare_length(c1,c2):
    if len(c1) < len(c2):return(-1)
    if len(c1) > len(c2): return 1
    return 0

#2) super easy:
print(sorted(colors, key=len))

######################################
#Call a function until sentinel value
#minute: 13:48

blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

from functools import partial
    
#iter takes a function w no arguments
#partial reduces the arguments to 0 (in this specific case)
blocks = []
for block in iter(partial(f.read,32), ''):
    blocks.append(block)
    
#another example:
#from Stackoverflow (https://stackoverflow.com/questions/15331726/how-does-the-functools-partial-work-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
def fnx(a,b,c):
    return a+b+c

fnx(3,4,5)
#with a partial function
pfnx = partial(fnx,a=12)
pfnx(b=4,c=5)

#real world examples:
#http://chriskiehl.com/article/Cleaner-coding-through-partially-applied-functions/
##i.e. creating 2 versions of a function by using partial to define one of the function's several arguments as x for the first 'new' function and as y for the second 'new' function 



######################################
#Distinguishing multiple exit points in loops

def find(seq,target):
    found = False
    for i, value in enumerate(seq):
        if value == tgt:
            found = True
            break
    if not found:
        return -1
    return i

#can use 'else' with for! If the value wasn't found in all the examples...
def find(seq, target):
    for i, value in enumerate(seq):
        if value == tgt:
            break
    else:
        return -1
    return i

######################################
#DICTIONARY SKILLS
#--------------------------#

#Looping over dictionary keys

d = {'matthew':'blue', 'rachel':'green','raymond':'red'}

#cannot mutate while iterating (or shouldn't)
for k in d:
    print(k)
    
#if you want to mutate:
#basically makes a copy of keys
for k in d.keys():
    if k.startswith('r'):
        del d[k]
        
d = {k: d[k] for k in d if not k.startswith('r')}
    
    
#####################################
#Looping over a dictionary keys and values

for k in d:
    print(k, '-->', d[k])

#uses up memory
for k, v in d.items():
    print(k, '-->', v)
    
#iterate!!
for k, v in d.iteritems():
    print(k, '-->', v)
    
#####################################
#Construct a dictionary from pairs
    
names = ['raymond','rachel','matthew']
colors = ['red','green','blue','yellow']

#was izip now zip
d = dict(zip(names,colors))

d = dict(enumerate(names))


#####################################
#Counting with dictionaries

colors = ['red','green','red','blue','green','red']

#enter a key in the dictionary so it doesn't fail
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1

#use core dictionary api:
d = {}
for color in colors:
    d[color] = d.get(color,0) +1
    
#more modern (but not for beginners)
#know about dictionary vs defaultdict
#know about factory functions
#int can be called w no arguments
#and object returned needs to be converted to a regular dictionary
from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1

from collections import defaultdict
 

#####################################
#Grouping with dictionaries -- Part 1

names = ['raymond','rachel','matthew']
names2 = ['roger','betty','melissa','judith','charlie']
names3 = [*names,*names2]
names3
#25:30

#group by length
d = {}
for name in names3:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
  
#group by first letter
x =  {}
for name in names3:
    key = name[0]
    if key not in x:
        x[key] = []
    x[key].append(name)
    
#group by last letter
y = {}
for name in names3:
    key = name[-1]
    if key not in y:
        y[key] = []
    y[key].append(name)
    
w = {}
for name in names3:
    key = name[0]=='m'
    if key not in w:
        w[key] = []
    w[key].append(name)

v = {}
for name in names3:
    key = 'tt' in name
    if key not in v:
        v[key] = []
    v[key].append(name)
    
    
#better way:
    #setdefault
d = {}
for name in names3:
    key = len(name)
    d.setdefault(key,[]).append(name)
    
x = {}
for name in names3:
    key = name[0]
    x.setdefault(key,[]).append(name)
    
#modern version of setdefault:
d = defaultdict(list)
for name in names3:
    key = len(name)
    d[key].append(name)
    
    
#####################################
#Is a dictionary popitem() atomic?
#time 28:00
    
d = {'mathew':'blue', 'rachel':'green','raymond':'red'}

while d:
    key,value = d.popitem()
    print(key, '-->', value)
    


#####################################
#Linking dictionaries
    
defaults = {'colors':'red','user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k,v in vars(namespace).items()if v}

import os
#copying code slows code...
d = defaults.copy()
#environment takes priority over the defaults
d.update(os.environ)
#the commandline takes priority over the environment
d.update(command_line_args)
    
#config parser is no longer slow because of this:
d = ChainMap(command_line_args, os.environ, defaults)




#####################################
#IMPROVING CLARITY

#positional arguments and indicies are nice
#keyword names are better
#the first way is convenient for the computer
#the second corresponds to how human's think



#####################################
#Clarify function calls with keyword arguments
def twitter_search(twitter_name,retweets,numtweets,popular):
    pass

twitter_search('@obama',False,20,True)

twitter_search('@obama',retweets=False,numtweets=20,popular=True)




#####################################
#Clarify multiple return values with names tuples
doctest.testmod()
(0,4)

doctest.testmod()
TestResults(failed=0,attempted=4)
from collections import namedtuple
TestResults = namedtuple('TestResults',['failed','attempted'])



#####################################
#Unpacking sequences
p = 'Rayond','Hettinger',0x30,'python@example.com'

#in most other languages:
fname=p[0]
lname=p[1]
age=p[2]
email=p[3]


#better for python:
fname,lname,age,email = p


#####################################
#Updating multiple state variables

def fibonacci(n):
    x=0
    y=1
    for i in range(n):
        print(x)
        t=y
        y=x+y
        x=t

#doesn't have order risk
#fast
#higher order
def fibonacci(n):
    x,y = 0,1
    for i in range(n):
        x,y = y, x+y


#####################################
#TUPLE PACKING AND UNPACKING

#Don't under-estimate the advantages of updating state variables at the same time
        # it eliminates an entire class off errors due to out-of-order updates
#it allows high level thinking: "chunking"
    
#example of planetary rotation:

tmp_x = x+dx*t
tmp_y = y+dy*t
tmp_dx = influence(m,x,y,dx,dy,partial='x')
tmp_dy = influence(m,x,y,dx,dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy

#better way in python:
x,y,dx,dy = (x+dx*t, y+dy*t, influence(m,x,y,dx,dy,partial='x'), influence(m,x,y,dx,dy,partial='y'))

#####################################
#EFFICIENCY
#An optimization fundamental rule
#don't cause data to move around unnecessarily
#it takes only a little care to avoid O(n**2) behavior instead of linear behavior


#####################################
#Concatenating strings

#quadratic behavior.. don't do this
s = names3[0]
for name in names3[1:]:
    s += ', ' +name
print(s)

#instead:
print(', '.join(names))


#####################################
#Updating sequences

#this can slow code...
#wrong data structure
del names3[0]
names.pop(0)
names.insert(0,'mark')

#correct data structure:
from collections import deque
names3 = deque(['raymond','rachel','matthew','roger','betty','melissa','judith','charlie'])

del names[0]
names.popleft()
names.appendleft('mark')




#####################################
#Decorators and Context Managers
#time 39:26
#Helps separate business logic from administration logic
#clean, beautiful tools for factoring code and improving code reuse
#good naming is essential
#remember the spiderman rule: with great power, comes great respsonsibility

#cache old lookups.. mixes logic
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url.read())
    saved[url] = page
    return page

#fix:
@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc


#####################################
#Factor-out temporary contexts
    
#old way:
old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
setcontext(old_context)

#new
#reusable logic
with localconteext(Context(prec=50)):
    print(Decimal(355)/Decimal(113))
    
    
#####################################
#How to open and close files
    
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()


#new (sets up the finally for you)
with open('data.txt') as f:
    data = f.read()
    
    
    
#####################################
#How to use locks

#make a lock
lock = threading.Lock()

#old way:
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally lock.release()


#new way: (releases lock for you)
with lock:
    print('Critical section 1')
    print('Critical section 2')
    
    
#####################################
#Factoring out temporary contexts

#to remove a file if it exists
    #but will get an error if it doesn't exist
try:
    os.remove('somefile.tmp')
except OSError:
    pass
    
#better way
with ignored(OSError):
    os.remove('somefile.tmp')
    
    
#Context manager: ignored()
    
@contextmanager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass
    
#####################################
#Factor-out temporary contexts
        
with open('help.txt','w') as f:
    oldstdout = sys.stdout
    sys.stdout = f
    try:
        help(pow)
    finally:
        sys.stdout = oldstoud
        
#better way:
with open('help.txt','w') as f:
    with redirect_stdout(f):
        help(pow)
        
#context manager: redirect_stdout()
@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fieldobj
    finally:
        sys.stdout = oldsdout


#####################################
#CONCISE EXPRESSIVE ONE-LINERS
#Two conflicting rules
#1) don't put too much on one line
#2) don't break atoms of thought into subatomic particles
        
#Raymond's rule::
#one logical line of code equals one sentence in English
        
        
#####################################
#List Comprehensions and Generator Expressions
        
#old way
result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print(sum((result))
    
#better
print(sum([i**2 for i in range(10))])

#even better (generator - saves more memory)
print(sum(i**2 for i in range(10)))
