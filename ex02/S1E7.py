from S1E9 import Character


class Baratheon(Character):

    """Representing the Baratheon family. Implements Character."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:

        """Initialize a Baratheon family member"""

        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):

    """Representing the Lannister family. Implements Character."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:

        """Initialize a Lannister family member"""

        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self) -> str:
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def create_lannister(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)
