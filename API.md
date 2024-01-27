# tarray API

## tarray
### Attributes
- `flags` (readonly)
  - metadata and helpful info
- `isContiguous`
  - is the array C Contiguous (not memory contiguous)
  - see the Contiguity section of the [docs](DOCS.md) for more info
- `shape`
  - tuple showing the array shape (number of elements in each dimenaion)
  - `a.shape = x` is equivalent to `a.reshape(x)`
- `strides` (readonly)
  - tuple showing how many *bytes* must be jumped in the buffer to get from one entry to the next
- `ndim` (readonly)
  - number of dimensions in the array
- `data`
  - the underlying buffer
- `size` (readonly)
  - total number of elements
- `itemsize`
  - size (in bytes) of each element 
  - default 4 (float32)
- `nbytes`
  - number of butes (itemsize * size)
- `dtype`
  - type of data
- `T`
  - transposition