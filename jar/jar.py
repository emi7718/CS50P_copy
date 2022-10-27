class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self._size = 0
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
      
    @property
    def size(self):
        return self._size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def __str__(self):
        if self.size == 0:
            return ''
        str_1 = str()
        for _ in range(self.size):
            str_1 = str_1 + '🍪'
        return str_1

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self.size = n + self.size

    def withdraw(self, n):
        if n > self.size or n > self.capacity:
            raise ValueError
        self.size = self.size - n
