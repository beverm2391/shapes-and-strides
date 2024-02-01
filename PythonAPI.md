# Minimmal Python API Sketch

## Design Philosiphy
- Keep it minimul but functional
- Focus on performance critical features
- prioritize ease of use and clear API design

## tarray
The core n-dimensional array class. (teenyarray)
### Attributes
- `shape`
  - dimensions of the array
- `strides`
  - steps in bytes to access elements on each dimension
- `data`
  - pointer or reference to the array's data
- `dtype`
  - data type of the elements
  - start with `fp32`
### Methods
- Initialization
  - construtor
  - argument validation?
- Indexing and Slicing
  - access and modify elements of subbarays
- Basic Operations
- Broadcasting Rules
- Convesion Methods
- Reshape
  - change the shape of the array without changing the data
- Transpose
  - permute the dimensions of the array

## ArrayScalar
- interaction with python scalars
- arithmetic and comparison operators
- type compatibility (with corresponding `Dtype`)

## Dtype
- type info
- compatibility checks

## Tfunc
- function registration (decorators?)
- Broadcasting and Element Wise Operations
- Integration with `Tarray`

## Advanced Functionality
- should i add broadcasting??
- mathmatecal operations
  - UOPS
  - BOPS
  - reduction/aggregation ops (sum, mean, min, max, etc.)
  - others?
- linear algebra
  - dot product
  - matmul

## Utility Methods
- copy
- view
- conversion to other datatypes (like lists)

## Performance Considerations
- efficent memory layout and access patterns
- handling of contiguous and non-contiguous data

## Testing
- write unit tests in pytest or unittest