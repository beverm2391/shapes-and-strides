from typing import Callable

class Tfunc:
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, *args, **kwargs):
        # heres the logic to apply the function elementwise
        # This should include handling broadcasting and applying the operation.
        # For simplicity, let's assume args are Teenyarray objects.
        result = ...
        return result