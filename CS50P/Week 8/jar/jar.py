class Jar:
    def __init__(self, capacity=12):

        if type(capacity) != int:
            raise ValueError("Define Capacity")
        if capacity < 0:
            raise ValueError("Define Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self._size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


