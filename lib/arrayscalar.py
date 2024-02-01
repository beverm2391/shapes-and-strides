from typing import Union
from lib.dtype import Dtype

class ArrayScalar:
    def __init__(self, value: Union[int, float], dtype: Dtype):
        self._validate_args(value, dtype)
        self.value = value
        self.dtype = dtype

    # ! Internal methods ========================================================
    def _is_compatible(self, other): return self.dtype == other.dtype if isinstance(other, ArrayScalar) else isinstance(other, (int, float))
    def _is_valid_dtype(self, dtype): return isinstance(dtype, Dtype)
    def _cast(self, other): raise NotImplementedError # TODO implement dtype casting in the dtype class
    def _validate_args(self, value: Union[int, float], dtype: Dtype):
        if not isinstance(value, (int, float)): raise TypeError(f"ArrayScalar value must be an int or float, not {type(value)}")
        if not isinstance(dtype, Dtype): raise TypeError(f"ArrayScalar dtype must be a Dtype object, not {type(dtype)}")

    # ! Arithmetic operators ===================================================
    # TODO figure out dtype casting logic
    def __add__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot add {self.dtype} and {type(other)}")
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value + other.value, self.dtype)
        return ArrayScalar(self.value + other, self.dtype)

    def __sub__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot subtract {self.dtype} and {type(other)}")
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value - other.value, self.dtype)
        return ArrayScalar(self.value - other, self.dtype)
    
    def __mul__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot multiply {self.dtype} and {type(other)}")
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value * other.value, self.dtype)
        return ArrayScalar(self.value * other, self.dtype)
    
    def __truediv__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot divide {self.dtype} and {type(other)}")
        if other == 0: raise ZeroDivisionError
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value / other.value, self.dtype)
        return ArrayScalar(self.value / other, self.dtype)
    
    def __floordiv__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot floor divide {self.dtype} and {type(other)}")
        if other == 0: raise ZeroDivisionError
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value // other.value, self.dtype)
        return ArrayScalar(self.value // other, self.dtype)
    
    def __mod__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot mod {self.dtype} and {type(other)}")
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value % other.value, self.dtype)
        return ArrayScalar(self.value % other, self.dtype)
    
    def __pow__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot exponentiate {self.dtype} and {type(other)}")
        if isinstance(other, ArrayScalar): return ArrayScalar(self.value ** other.value, self.dtype)
        return ArrayScalar(self.value ** other, self.dtype)
    
    # ! Reverse arithmetic operators ============================================
    # ex: 3 + array_scalar(2) -> array_scalar(2) + 3
    def __radd__(self, other): return self.__add__(other)
    def __rsub__(self, other): return self.__sub__(other)
    def __rmul__(self, other): return self.__mul__(other)
    def __rtruediv__(self, other): return self.__truediv__(other)
    def __rfloordiv__(self, other): return self.__floordiv__(other)
    def __rmod__(self, other): return self.__mod__(other)
    def __rpow__(self, other): return self.__pow__(other)

    # ! Inplace arithmetic operators ============================================
    # ex: a += 3 -> a = a + 3
    def __iadd__(self, other): return self.__add__(other)
    def __isub__(self, other): return self.__sub__(other)
    def __imul__(self, other): return self.__mul__(other)
    def __itruediv__(self, other): return self.__truediv__(other)
    def __ifloordiv__(self, other): return self.__floordiv__(other)
    def __imod__(self, other): return self.__mod__(other)
    def __ipow__(self, other): return self.__pow__(other)

    # ! Unary arithmetic operators ==============================================
    def __neg__(self): return ArrayScalar(-self.value, self.dtype)
    def __pos__(self): return self
    def __abs__(self): return ArrayScalar(abs(self.value), self.dtype)

    # ! Comparison operators ===================================================
    def __eq__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot compare {self.dtype} and {type(other)}")
        return self.value == other.value if isinstance(other, ArrayScalar) else self.value == other
    
    def __ne__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot compare {self.dtype} and {type(other)}")
        return self.value != other.value if isinstance(other, ArrayScalar) else self.value != other
    
    def __lt__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot compare {self.dtype} and {type(other)}")
        return self.value < other.value if isinstance(other, ArrayScalar) else self.value < other
    
    def __le__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot compare {self.dtype} and {type(other)}")
        return self.value <= other.value if isinstance(other, ArrayScalar) else self.value <= other
    
    def __gt__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot compare {self.dtype} and {type(other)}")
        return self.value > other.value if isinstance(other, ArrayScalar) else self.value > other
    
    def __ge__(self, other):
        if not self._is_compatible(other): raise TypeError(f"Cannot compare {self.dtype} and {type(other)}")
        return self.value >= other.value if isinstance(other, ArrayScalar) else self.value >= other
    
    # ! Reverse comparison operators ============================================
    # ex: 3 < array_scalar(2) -> array_scalar(2) > 3
    def __req__(self, other): return self.__eq__(other)
    def __rne__(self, other): return self.__ne__(other)
    def __rlt__(self, other): return self.__lt__(other)
    def __rle__(self, other): return self.__le__(other)
    def __rgt__(self, other): return self.__gt__(other)
    def __rge__(self, other): return self.__ge__(other)

    # ! Utility methods =========================================================
    def to_pyscalar(self): return self.value
    def __repr__(self): return f"ArrayScalar({self.value}, {self.dtype})"

class Float32Scalar(ArrayScalar):
    def __init__(self, value):
        super().__init__(value, Dtype('float32', 4))

    def __repr__(self): return f"Float32Scalar({self.value})"

class Int32Scalar(ArrayScalar):
    def __init__(self, value):
        super().__init__(value, Dtype('int32', 4))

    def __repr__(self): return f"Int32Scalar({self.value})"