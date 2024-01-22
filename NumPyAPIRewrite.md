# API

## tarray
### Attributes
- `flags` (readonly) (see pg 47)
  - C_CONTIGUOUS (C)
  - F_CONTIGUOUS (F)
  - OWNDATA (O)
  - WRITEABLE (W)
  - ...
- `shape`
  - tuple showing the array shape (number of elements in each dimension)
  - setting this attribute reshapes the array
  - `a.shape = x` is equivalent to `a.reshape(x)`
    - `a.reshape` can be used on non-single-segment arrays
  - setting shape to () for a 1-element array will turn self into a 0-dimensional array. Most other ops will return an array scalar
- `strides` 
  - tuple showing how many *bytes* must be jumped in the buffer to get from one entry to the next
  - setting this to another tuple will change the way memory is viewed
  - cannot be set to a tuple that accesses unavailible memory (bounded) (raises ValueError)
- `ndim` (readonly)
  - number of dimensions in the array (len(shape) and len(strides) tuples)
- `data`
  - the buffer that loosely wraps the array data (only for single-segment arrays)
  - if not single-segment, an AttributeError is raises
- `size` (readonly)
  - total number of *elements*
- `itemsize`
  - size (in bytes) of each element (fp64 would have an itemzise of 8)
- `nbytes`
  - total number of bytes (self.itemsize * self.size)
- `base`
  - object the array is using for the buffer
  - if the array is not using its own memory this returns the object whose memory the array is referencing
- `dtype`
  - data type object
    - a data-type object that fully describes each item of the array
- `flat`
  - one dimensional indexable iterator object that acts somewhat like a 1-D array
- `T`
  - equivalent of `self.transpose()`
  - for `self.ndim < 2` returns a view of self
### Methods (pg ?)
- `tolist()`
  - contets of self in a nested list
- `astype({None})`
  - force conversion to the dtype provideed as argument
    - if `None` provided as argument, return copy ofg the array
- `copy()`
  - return a single-segment, aligned copy of the array. dtype is preserved
- `view()`
  - returns a *new array* using the *same memory* as self.
- `fill()`
  - fill an array with a scalar value
Shape Maniupulation
- `reshape(newshape, order='C')`
  - return an array that uses the same data but the new shape
  - numel for new shape must match numel of array
  - *If one of the elements of the new shape tuple is -1, then that dimension will be determined such that the overall number of items in the array stays constant. (pg 59)*
  - If possible the new array will *reference* the data of the old one. If the data needs to be moved then the new array will contain a copy of the data.
- `resize(newshape, refcheck=1, order='C')`
  - resize an array in place
  - only a single segment array can be resized
- `transpose(<None>)`
  - Return an array *view* with the shape transposed according to the argument. An argument of None is equivalent to `range(self.ndim)[::-1]`. The argument can either be a tuple of multiple integer args. This method returns a *new array with permuted shape and strides attribute using the same data as self*.
- `swapaxes(axis1, axis2)`
  - return an array *view* with `axis1` and `axis2` swapped. Special case of the `transpose` method with the arg equal to `arg=range(selff.ndim); arg[axis1], arg[axis2] = arg[axis2], arg[axis1]`
- `flatten()`
  - returns a new 1-D array with dat copied from self
- `ravel()`
  - return a 1-D version of self. If single segment, the new array references self else its copied
Item Selection and Manipulation (pg 61-)
> For array methods that take an axis keyword, it defaults to None. If axis is None, the the array is treated as a 1-D array. Any other value represents the dimension along which the operation should proceed.
- `repeat(repeats=, axis=None)`
  - copy elements of self **repeats** times. repeats arg must be a sequence of len `self.shape[axis]` of a scalr
Array Calculation (pg 65-)
- `min(axis=None, out=None)`
  - return the smallest value of self
- `clip(min=,max=, out=None)`
  - return a new array where any element in self is less than min is set to min and any element less thatn max is set to max
- `sum(axis=None, dtype=None, out=None)`
  - return the sum $\sum^{N-1}_{i=0}self[;,\ldots,:,i]$ where $:,\ldots,: = axis$
- `cumsum(axis=Nonem dtype=None, out=None)`
  - return the cumulative sum
- `mean(axis=None, dtype=None, out=None)`
- `var(axis=None, dtype=None, out=None)`
  - return variance of the data
- `std(axis=None, dtype=None, out=None)`
  - standard deviation
- `prod(axis=None, dtype=None, out=None)`
  - product
- `cumprod(axis=None, dtype=None, out=None)`
  - cumuulative product
- `all(axis=None, out=None)`
  - returns `True` if all entires along axis evaluate `True` else returns `False`
- `any(axis=None, out=None)`
  - returns `True` if any entires along axis evaluate `True` else returns `False`
Array Special Methods (not mean to be called by user, used by Python)
- `__copy__()`
  - shallow copy
- `__deepcopy__()`
  - deep copy
- `__reduce__() and __setstate__()`
  - allow for pickling
Basic Customization
- `__new__(subtype, shape=, dtype=long_, buffer=None, offset=0, strides=None, order=None)`
  - Creates a new `tarray`. Typically only uses in the `__new__` method of a subclass. Called to construct a new array whenever `a=tarray(...)`
  - Two methods or array creation include:
    - a single-segment array of the specified shape and dtype from *newly allocated memory*
      - uses shape, stype, stirdes, and order arguments, others are ignored
      - if strides is given, it speciies the new strides of the array (order is ignored)
        - bounds checked
  - an array of the shape and dtype using the provided object, buffer
  - `tarray` uses the default no-op `__init__` because `__new__` creates the array
comparison magic methods
...
- `__str__()`
- `__repr__()`
  - last axis is printed l to r
  - next-to last is printed top to bottom
  - remaining axes are printed top to bottom with separators
- `__nonzero__()`
  - truth value testing for the array is a whole. raises an error is numel > 1 (use any() and all()). if numel = 0 returns False, if numel = 1 returns True
- `__len__()`
  - returns `self.shape[0]`
- `__getitem__(key)`
  - standard and extended indexing abilities
- `__setitem()__`
  - set item
    - called when evaluating `self[key]=value`
- `__getslicce()__(key, value)`
  - used to evaluate `self.__getitem__(slice(i,j))`, `self[i:j]`
- `__contains__(item)`
  - called for `item in self`. returns `(self==item).any()`
Basis ops
- add, sub, mul, div, truediv, floordiv, mod, divmod, pow, lshift, rshift, and, or, xor
- implemented element by element for same shape or broadcastable
In place
- iadd, isub, imul, idiv, itruediv, ifloordiv, imod, ipow, ilshift, irshift, iand, ixor, ior
Unary
- neg, pos, abs, invert
  - via ufuncs except for pos
- complex, int, long, float, odc, hex
Array indexing