from S1E7 import Baratheon, Lannister


# constructor of `Baratheon` will be called by default
class King(Baratheon, Lannister):

    """A hybrid monster."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:

        """Initialize a king"""

        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes_color: str):

        """Set king's eye color"""

        self.eyes = eyes_color

    def set_hairs(self, hair_color: str):

        """Set king's hair color"""

        self.hairs = hair_color

    def get_eyes(self) -> str:

        """Get king's eye color"""

        return self.eyes

    def get_hairs(self) -> str:

        """Get king's hair color"""

        return self.hairs
