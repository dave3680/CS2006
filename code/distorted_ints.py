#!/usr/bin/env python
from distorted_int_set import IteratorOfDistortedInteger, DistortedIntSet
"""program to create and manipulate distorted integer values"""

class DistortedInt:
    """Class to hold one distorted integer"""

    def __init__(self, x, n, a):
        """new distorted int
        arguments must be integers
        n must be positive"""
        # check types of args
        if type(x) != int or type(a) != int or type(n) != int:
            raise TypeError("arguments of DistortedInt must be integers")
        # check n > 0
        if n <= 0:
            raise ValueError("n must be positive")
        # if ok, setup val, take mod n in case out of bounds
        self.x = x % n
        self.a = a % n
        self.n = n
    
    def __str__(self):
        """turn distorted int into a string
        <x mod n | a>"""
        return "<" + str(self.x) + " mod " + str(self.n) + " | " + str(self.a) + ">"
    
    def __repr__(self):
        """return representation of object
        same as to string method"""
        return str(self)

    def __mul__(self, other):
        """apply distorted multiplication
        x * y = (ax + (1 - a)y) mod n
        a and n must be same for both arguments"""
        # check a, n same
        if self.a != other.a or self.n != other.n:
            raise ValueError("a and n of both arguments must be equal")
        # new x = (ax + (1-a)y) mod n
        x = ((self.a * self.x) + ((1 - self.a) * other.x))
        return DistortedInt(x, self.n, self.a)
    
    def __eq__(self, other):
        """Check if this object is equal to another
        Compares x, a and n"""
        return self.x == other.x and self.a == other.a and self.n == other.n


def HasDistortedIdempotentProperty(n, alpha):
    """Tests if (x*x) = x for all x in Zn n > 0"""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    for x in range(n):
             xdi = DistortedInt(x, n, alpha)
             if (xdi * xdi != xdi):
                    return False
    return True

def DistortedRootsOfOne(n, alpha):
    """Calculate list of x (for mod n, and alpha) that satisfy x * x = 1
    n > 0"""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    roots = []
    e = DistortedInt(1, n, alpha) # expected
    for x in range(n):
        i = DistortedInt(x, n, alpha)
        m = i * i
        if m == e:
            roots.append(m)
    return roots
    
def IsCommutativeDistortedMultiplication(n, alpha):
    #    Tests if (x*y) = (y*x) for all x,y in Zn n > 0
    if n <= 0:
        raise ValueError("n must be greater than 0")
    for x in range(n):
        for y in range(n):
                xdi = DistortedInt(x, n, alpha)
                ydi = DistortedInt(y, n, alpha)
                if (xdi * ydi != ydi * xdi):
                    return False
    return True

def getCommutativePairs(limit=100):
    return [(n, alpha) 
            for n in range(1, (limit + 1)) 
            for alpha in range(n) 
            if IsCommutativeDistortedMultiplication(n, alpha)]

def IsAssociativeDistortedMultiplication(n, alpha):
    """Tests if (x*y)*z = x*(y*z) for all x,y,z in Zn
    n > 0"""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    for x in range(n):
        for y in range(n):
            for z in range(n):
                xdi = DistortedInt(x, n, alpha)
                ydi = DistortedInt(y, n, alpha)
                zdi = DistortedInt(z, n, alpha)
                if ((xdi * ydi) * zdi) != (xdi * (ydi * zdi)):
                    return False
    return True

def getAssociativePairs(limit=20):
    """Get all pairs of (n, alpha) that satisfy the associative law for distorted multiplication"""
    return [(n, alpha) 
            for n in range(1, (limit + 1)) 
            for alpha in range(n) 
            if IsAssociativeDistortedMultiplication(n, alpha)]

def IsQuasiDistributiveDistortedMultiplication(n, alpha):
    """Tests if (x*y)*z = (x*y)*(x*z) for all x,y,z in Zn
    n > 0"""
    if n <= 0:
        raise ValueError("n must be greater than 0")
    for x in range(n):
        for y in range(n):
            for z in range(n):
                xdi = DistortedInt(x, n, alpha)
                ydi = DistortedInt(y, n, alpha)
                zdi = DistortedInt(z, n, alpha)
                if ((xdi * ydi) * zdi) != ((xdi * ydi) * (xdi * zdi)):
                    return False
    return True

def getQuasiPairs(limit=20):
    return [(n, alpha) 
            for n in range(1, (limit + 1)) 
            for alpha in range(n) 
            if IsQuasiDistributiveDistortedMultiplication(n, alpha)]

def HasDistortedEquationProperty(n, alpha):
    """Tests if x * y = z is solvable for all x and z"""
    if n <= 0:
        raise ValueError("n must be greater than zero")
    for x in range(n):
        for z in range(n):
            # search for first y to satify relation
            found = False
            for y in range(n):
                if (DistortedInt(x, n, alpha) * DistortedInt(y, n, alpha)) == DistortedInt(z, n, alpha):
                    # y fits, no need to search further
                    found = True
                    break
            if not found:
                # this x,z break rule
                return False
    return True

def getEquationPairs(limit=20):
    """Returns all pairs of (n, alpha) 0 < n <= limit, 0 <= alpha < n, which have the equation property"""
    return [(n, alpha) 
            for n in range(1, (limit + 1)) 
            for alpha in range(n) 
            if HasDistortedEquationProperty(n, alpha)]

#All functions that follow are the same as the respective functions before however using the iterator class (in distorted_int_set.py)

def HasDistortedIdempotentPropertyIterator(n, alpha):
    for x in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
        if x * x != x:
            return False
    return True

def IsCommutativeDistortedMultiplicationIterator(n, alpha):
    for x in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
            for y in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
                if (x * y) != (y * x):
                    return False
    return True

def IsAssociativeDistortedMultiplicationIterator(n, alpha):
    for x in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
            for y in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
                    for z in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
                        if ((x * y) * z )!= ((x * (y * z))):
                            return False
    return True

def IsQuasiDistributiveDistortedMultiplicationIterator(n, alpha):
    for x in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
                for y in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
                        for z in IteratorOfDistortedInteger(DistortedIntSet(n,alpha)):
                            if ((x * y) * z )!= ((x * y) (x * z)):
                                return False
    return True