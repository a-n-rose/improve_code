# Improving-Code

* Notes on helpful tools to improve my code
- see pythonic_vs_unpythonic.py

* Functions helpful for making code more efficient
- see speed_memory_compare.py

## Compare speed and memory

To see how one or more functions perform as it pertains to speed and memory you first need to install memory_profiler via 'pip install memory_profiler'.

The speed and memory comparison functions can be applied so:

In file 'example.py':
```
import datetime
import numpy as np
from memory_profiler import profile


@profile
def measure_memory(a, fun):
    fun(a)
        
def compare_memory(a, functions):
    for fun in functions:
        print('MEMORY USE OF ', fun)
        measure_memory(a, fun)
        
def compare_time(a, functions):
    for fun in functions:
        start = datetime.datetime.now()
        fun(a)
        end = datetime.datetime.now()
        print()
        print('SPEED OF ', fun)
        print(end-start)
        print()
        

if __name__=='__main__':
    # example:
    def flip_array_np(a):
        return(np.concatenate((a, np.flip(a[:-1]))))

    def flip_array(a):
        return(np.concatenate((a, a[:-1][::-1])))
    
    y = np.arange(1_000)
    funs = [flip_array_np, flip_array]
    compare_memory(y, funs)
    compare_speed(y, funs)
    
```

And then type this into your console:
```
$ python3 -m memory_profiler example.py
```

You will get this printed on your screen:

```
MEMORY USE OF  <function flip_array_np at 0x7f8f318270d0>
Filename: speed_memory_compare.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     7     51.8 MiB     51.8 MiB           1   @profile
     8                                         def measure_memory(a, fun):
     9                                             '''Profiles memroy of single function applied to a.
    10                                             '''
    11     51.8 MiB      0.0 MiB           1       fun(a)


MEMORY USE OF  <function flip_array at 0x7f8f31827160>
Filename: speed_memory_compare.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     7     51.8 MiB     51.8 MiB           1   @profile
     8                                         def measure_memory(a, fun):
     9                                             '''Profiles memroy of single function applied to a.
    10                                             '''
    11     51.8 MiB      0.0 MiB           1       fun(a)



SPEED OF  <function flip_array_np at 0x7f8f318270d0>
0:00:00.000014


SPEED OF  <function flip_array at 0x7f8f31827160>
0:00:00.000006
```
