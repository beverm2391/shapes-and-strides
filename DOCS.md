# Documentation

## Contiguity

In NumPy, whether an array is contiguous or not depends on how its elements are laid out in memory. Two key types of contiguity are often discussed: C-contiguous (row-major order) and F-contiguous (column-major order). Understanding this requires a bit of insight into how multi-dimensional arrays are stored in memory, which is essentially a linear, one-dimensional block of memory.

1. **C-Contiguous (Row-Major Order)**: An array is C-contiguous if consecutive elements of the rows of the array are contiguous in memory. In this layout, the last dimension is "raveled" or laid out first. This is the default order in NumPy and is similar to the way arrays are stored in C/C++. For example, in a 2D array, elements of each row are stored in contiguous memory locations.

2. **F-Contiguous (Column-Major Order)**: An array is F-contiguous if consecutive elements of the columns are contiguous in memory. Here, the first dimension is laid out in the memory first. This layout is similar to the way arrays are stored in Fortran. In a 2D array, elements of each column are stored in contiguous memory locations.

3. **Strides**: The concept of strides is crucial in understanding contiguity. Strides are a tuple of bytes to step in each dimension when traversing an array. A NumPy array is contiguous when the strides for each dimension are such that the elements of the array are laid out sequentially in memory without any gaps. In a C-contiguous array, the stride for the last dimension is typically equal to the size of the array element, while in an F-contiguous array, the stride for the first dimension is equal to the size of the array element.

4. **Non-Contiguous Arrays**: An array is non-contiguous if it doesn't meet the criteria for being C-contiguous or F-contiguous. This can happen in several ways:
   - **Slicing**: Creating a slice of an array can result in a non-contiguous array. For example, taking every other element of an array creates a gap between elements in memory.
   - **Reshaping**: Reshaping an array can also lead to non-contiguity, especially if the order of the elements is changed in a way that they are no longer sequentially stored in memory.
   - **Views and Copies**: Creating views (which share the same data buffer as the original array) can lead to non-contiguous arrays. On the other hand, creating a copy (which creates a new data buffer) of a non-contiguous array can make it contiguous again.

5. **Contiguity and Performance**: Contiguous arrays often allow for more efficient computation as they enable better use of CPU cache and memory bandwidth. Operations on non-contiguous arrays might be less efficient due to the overhead of jumping around in memory.

The `flags` attribute of a NumPy array can be used to check if an array is contiguous in memory. (use this for testing)