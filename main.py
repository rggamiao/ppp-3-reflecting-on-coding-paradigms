## This function will flatten and sort an array of integers in ascending order which is part of the FO paradigm ##

def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)


## = questions
# = answers


## QUESTIONS ##
## 1. How does this solution ensure data immutability? ##

# The immutability is attained through 'arr' as it creates a new list. It returns a sorted list after. #


## 2. Is this solution a pure function? Why or why not? ##

# Yes, it produces the same output for the same input. It doesn't modify anything else.

## 3. Is this solution a higher order function? Why or why not? ##

# This is not a higher order function. Higher order functions require more than one function as an argument. This only accepts arrays.

## 4. Would it have been easier to solve this problem using a different programming style? ##

# I'm still inexperienced with this paradigm so using loops would have been easier. 

## 5. Why in particular is functional programing a helpful paradigm when solving this problem? ##

# The code is more concise and easier to read for the viewer, especially when there's a lot of data to flatten and sort. 