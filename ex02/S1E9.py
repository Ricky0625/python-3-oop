from abc import ABC, abstractmethod


class Character(ABC):

    """Abstract base class that defines the interface for Characters.
    Attributes:
        first_name: first name
        is_alive: a boolean value, the state of the character
    """

    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True) -> None:

        """Constructor of Character.
        Initialize the data member of the class"""

        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:

        """Kill the character"""

        self.is_alive = False


class Stark(Character):

    """Implementation of the abstract class"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:

        """Initialize Stark"""

        super().__init__(first_name, is_alive)
