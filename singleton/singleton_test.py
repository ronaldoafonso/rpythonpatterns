"""
    Tests for Singleton Design Pattern
"""

from singleton import Singleton


def test_singleton():
    """ Test a single singleton. """

    _singleton1 = Singleton()
    assert isinstance(_singleton1, Singleton)

def test_singleton_returning_always_the_same_instance():
    """ Test if the same stance will always be returned. """

    _singleton1 = Singleton()
    for _ in range(10):
        assert _singleton1 is Singleton()

def test_singleton_increment_and_decrement():
    """
        Test if the value inside the single will be the only one
        incremented or decremented.
    """

    base_singleton = Singleton()
    _singleton1 = Singleton()
    _singleton2 = Singleton()

    tests = [
        (_singleton1.increment, 1),
        (_singleton2.increment, 2),
        (_singleton1.decrement, 1),
        (_singleton2.decrement, 0),
        (_singleton1.decrement, 0),
        (_singleton2.increment, 1),
        (_singleton1.increment, 2),
        (_singleton2.increment, 2)
    ]

    for operation, value in tests:
        operation()
        assert base_singleton.value == value
