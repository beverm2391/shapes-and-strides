class Dtype:
    def __init__(self, type_, size):
        self.type_ = type_ # e.g. float32, int32, etc.
        self.size = size # size in bytes

    def __str__(self): return f"Dtype({self.type_})"