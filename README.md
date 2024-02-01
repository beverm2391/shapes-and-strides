# Shapes and Strides

This is a sub-project of my n-dim array library [teenyarray](https://github.com/beverm2391/teenyarray) that focuses on storing n-dimensional arrays (or Tensors) in linear, contigious memory.

Some of the refereces I'm using include
- Travis Oliphant's *[Guide to Numpy](https://web.mit.edu/dvp/Public/numpybook.pdf)*
- Alex (ajcr)'s series or blog posts, [An Illustraetd Guide To Shapes and Strides](https://ajcr.net/stride-guide-part-1/)

The goal is to build out an n-dim array class in Python and then port it over to Cpp to be integrated into teenyarray.

## TODO
- [ ] Sketch the Python API (the literal minimal implementation)
  - [ ] pick out attributes for the `tarray` API
  - [ ] pick out methods for the `tarray` API
- [ ] Implement the API in Python
  - [ ] work throguh method development
- [ ] Add Unit Tests in Python
- [ ] Start implementing in C++ and overloading with PyBind (this is when you move to the teenyarray repo)
- [ ] Iterate


## TODO OLD
- [ ] array class
  - [X] pick all attributes for the `tarray` api
    - [ ] figure out how offset works (check shapes and strides article)
  - [ ] add reshape and transpose methods (examine the numpy behavior)
  - [X] examine the numpy behavior for views (what does it return? is there a separate view object?)
  - [ ] add negative indexing, add indexing with len(indices) != len(shape) (pg 79-84)
  - [ ] write tests (compare against numpy) for ndarray class
  - [ ] figure out how the `np.array()` method works (pg 85)
  - [ ] add broadcasting (see page 30)
- [ ] finish and test the python implementation
- [ ] write a cpp implementation in this repo
- [ ] write all the cpp tests
- [ ] bind to python
- [ ] implement in the teenyarray lib
- [ ] write a blog post??