#!/usr/bin/env python
# coding: utf-8

# ### Map

# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given sequence (list, tuple etc.)
# 
# `map(function, sequence)`
# ```
# Parameters:
#     function:  It is a function to which map passes each element of given iterable.
#     sequence:  It is a iterable which is to be mapped, it can be sets, lists, tuples, or containers of any iterators.
# Returns:
#     returns an iterator after applying the given function to each item of a given sequence.
# ```

# In[15]:


# function to add
def addition(n):
    """
    Add number with itself.
    """
    return n + n
  
# sequence
numbers = (1, 2, 3, 4)

# We double all numbers using map()
result = map(addition, numbers)

# result
print(list(result))


# ### Filter
# 

# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.
# 
# `
# filter(function, sequence)
# `
# ```
# Parameters:
#     function: function that tests if each element of a 
#             sequence true or not.
#     sequence: sequence which needs to be filtered, it can 
#             be sets, lists, tuples, or containers of any iterators.
# Returns:
#     returns an iterator that is already filtered.
# ```

# In[14]:


# function that filters vowels
def is_vowel(variable):
    """
    Check if varaible is vowel or not
    """
    letters = ['a', 'e', 'i', 'o', 'u']
    
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(is_vowel, sequence)

print('The filtered letters are:')
print(list(filtered))


# ### Lambda Functions 

# A lambda function is just like any normal python function, except that it has no name when defining it, and it is contained in one line of code.
# 
# ``` lambda argument(s): expression ```

# In[2]:


#Normal python function
def square(x):
    """
    Function to computer square of a given value
    """
    return x**2


#Lambda function
square = lambda x: x**2


# #### Why use lambda function?
# * It can be used to declare small anonimus functions.
# * Faster executaion (minor).
# * Better code readibility.
# 

# In[ ]:




