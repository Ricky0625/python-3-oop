class calculator:

    """calculator, a static class. still can instantiate
    but not necessary"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """dot product"""
        res = sum(a * b for a, b in zip(V1, V2))
        print(f"Dot product is: {res}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """add two vector"""
        res = [float(a + b) for a, b in zip(V1, V2)]
        print(f"Add Vector is: {res}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """subtract two vector"""
        res = [float(a - b) for a, b in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
