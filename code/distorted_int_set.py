import distorted_ints
"""Program to create DistortedIntSets, abstract representations of Zn for n and alpha"""

class DistortedIntSet:
    """Abstract representation of Zn"""

    def __init__(self, n, alpha):
        """Initialise integers object
        n > 0"""
        if n <= 0:
            raise ValueError("n must be greater than zero")
        # init
        self.n = n
        self.alpha = alpha % n
    
    def __str__(self):
        """String representation of set
        <[x0, x1, ...] mod n | alpha>"""
        s = [x for x in range(self.n)]
        return "<" + str(s) + " mod " + str(self.n) + " | " + str(self.alpha) + ">"
    
    def __repr__(self):
        """Representation of set - list of DistortedInt objects"""
        return str(self.to_list())
    
    def size(self):
        """Returns the number of objects in Zn"""
        return self.n
    
    def to_list(self):
        """Returns a list of the objects in Zn"""
        return [distorted_ints.DistortedInt(x, self.n, self.alpha) for x in range(self.n)]

class IteratorOfDistortedInteger:

    """Initializes the object from the class and all the values it holds"""
    def __init__ (self, dis_ints):
        self.dis_ints = dis_ints
        self.size = self.dis_ints.size()
        self.num = 0
        self.list = []
        """adds dis_ints to the list"""
        for i in self.dis_ints.to_list():
            self.list.append(i)

    """returns slef (in practicality just iterates)"""
    def __iter__(self):
        return self

    """Continues the iteration (if maximum not reached)"""
    def __next__(self):
        if self.num == self.size:
            raise StopIteration
        self.num = self.num + 1
        return self.list[self.num - 1]
