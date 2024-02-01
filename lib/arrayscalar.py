from lib.dtype import Dtype

class ArrayScalar:
    def __init__(self, value, dtype):
        self.value = value
        self.dtype = dtype

    def __repr__(self): return f"ArrayScalar({self.value}, {self.dtype})"

class Float32Scalar(ArrayScalar):
    def __init__(self, value):
        super().__init__(value, Dtype('float32', 4))

    def __repr__(self): return f"Float32Scalar({self.value})"

class Int32Scalar(ArrayScalar):
    def __init__(self, value):
        super().__init__(value, Dtype('int32', 4))

    def __repr__(self): return f"Int32Scalar({self.value})"