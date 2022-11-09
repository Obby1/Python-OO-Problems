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
        """make a new generator starting at 0"""
        self.start = self.next = start
    
    def __repr__(self):
        return f"Creates a new serial number starting at {self.start} and incrementing by 1 on each generate"

    def generate(self):
        """generate the next sequence of serial number (start +1)"""
        self.next +=1
        return self.next -1

    def reset(self):
        """return serial number back to starting number declared at initialization"""
        self.next = self.start
        
       



