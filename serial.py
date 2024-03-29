"""Python serial number generator."""

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
    def __init__(self, start=0):
        self.start = start
        self.new = start
    
    def __repr__(self):
        return f"<Serial Generator: Start = {self.start}>"
    
    def generate(self):
        """Returns new serial number"""
        self.new += 1
        return self.new - 1
    
    def reset(self):
        """Resets serial number to original value"""
        self.new = self.start
        return self.new

