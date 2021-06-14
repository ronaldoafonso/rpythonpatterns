"""
    Singleton Design Pattern
"""

class Singleton:
    """
        A Singleton class.
        It must have only one instance of it in the system.
    """

    _singleton = None

    def __new__(cls):
        if not cls._singleton:
            cls._singleton = super().__new__(Singleton)
        return cls._singleton

    def __init__(self):
        self.value = 0

    def increment(self):
        """
            Incremente the value of singleton to 2 at maximum.
        """
        if self.value < 2:
            self.value += 1

    def decrement(self):
        """
            Decrement the value of singleton to 0 at minimum.
        """
        if self.value > 0:
            self.value -= 1
