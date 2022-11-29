class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ create new Serial variable named num """
        self.start = self.next = start

    def __repr__(self):
        return f'<SerialGenerator num = {self.start}>'

    def generate(self):
        """ increment num by one, then returns num value - 1 """
        self.next += 1
        return self.next - 1

    def reset(self):
        """ resets num value to original 100 value """
        self.next = self.start
