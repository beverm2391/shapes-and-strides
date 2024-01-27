from typing import List

# Product of an array
def prod(arr): return (el := arr[0]) * prod(arr[1:]) if arr else 1

# Flatten an iterable into a list
def flatten(iterable: List):
    """Flattens an iterable"""
    if not getattr(iterable, '__iter__', False): return [iterable]
    return [el for sublist in iterable for el in flatten(sublist)]

# Check if all elements of an iterable are of a certain type
def recursive_checktype(obj, type):
    """Returns True if all elements of obj are of type type"""
    if not getattr(obj, '__iter__', False): return isinstance(obj, type)
    return all(recursive_checktype(o, type) for o in obj)

# Check if the shape of an iterable is uniform
def recursive_checkshape(obj):
    """Returns a shape tuple of a uniform object"""
    def _recursive_checkshape(obj):
        if not getattr(obj, '__iter__', False): return [] # if not iterable, return empty list
        return [len(obj)] + _recursive_checkshape(obj[0]) # else, return length of obj and recurse on first element
    return tuple(_recursive_checkshape(obj))