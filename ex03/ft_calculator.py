class calculator:

    """calculator"""

    def __init__(self, object) -> None:
        """initialize calculator with a iterable"""
        self.data = object

    def __add__(self, object) -> None:
        """addition"""
        self.data = [i + object for i in self.data]
        print(self.data)

    def __mul__(self, object) -> None:
        """multiplication"""
        self.data = [i * object for i in self.data]
        print(self.data)

    def __sub__(self, object) -> None:
        """subtraction"""
        self.data = [i - object for i in self.data]
        print(self.data)

    def __truediv__(self, object) -> None:
        """true division, check for zero division"""
        if (object == 0):
            print("[ERROR]: zero division")
            return
        self.data = [i / object for i in self.data]
        print(self.data)
