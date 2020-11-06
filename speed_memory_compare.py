######################################################################
import datetime
import numpy as np
from memory_profiler import profile


@profile
def measure_memory(a, fun):
    '''Profiles memroy of single function applied to a.
    '''
    fun(a)
        
def compare_memory(a, functions):
    '''Prints memory use of various functions applied to a.
    
    Parameters
    ----------
    a : object
        Ojbect for the function(s) to be applied to.
    
    functions : list 
        List of functions to apply to a.
        
    Returns
    -------
    None
    
    References
    ----------
    https://coderzcolumn.com/tutorials/python/how-to-profile-memory-usage-in-python-using-memory-profiler
    '''
    for fun in functions:
        print('MEMORY USE OF ', fun)
        measure_memory(a, fun)
        
def compare_speed(a, functions):
    '''Prints duration of various functions applied to a.
    
    Parameters
    ----------
    a : object
        Ojbect for the function(s) to be applied to.
    
    functions : list 
        List of functions to apply to a.
        
    Returns
    -------
    None
    '''
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
    
