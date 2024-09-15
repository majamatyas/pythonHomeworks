
#Exercise 12.1

import unittest
import math
from homework6 import Vector

class TestVector(unittest.TestCase):
    
    def setUp(self):
        self.v = Vector(2, 4, 6)
        self.w = Vector(1, 3, 5)
        self.u = Vector(1, 2, 3)
    
    def test_equality(self):
        v2 = Vector(2, 4, 6)
        self.assertEqual(self.v, v2)  
        self.assertNotEqual(self.v, self.w)  
    
    def test_addition(self):
        self.assertEqual(self.v + self.w, Vector(3, 7, 11))  
    
    def test_subtraction(self):
        self.assertEqual(self.v - self.w, Vector(1, 1, 1))  
    
    def test_dot_product(self):
        self.assertEqual(self.v * self.w, 44)  
    
    def test_cross_product(self):
        self.assertEqual(self.v.cross(self.w), Vector(2, -4, 2))  
    
    def test_length(self):
        self.assertAlmostEqual(self.v.length(), math.sqrt(56))  
    
    def test_hash(self):
        self.assertEqual(len(set([self.v, self.v, self.w])), 2)  
    
    def test_repr(self):
        self.assertEqual(repr(self.v), "Vector(2, 4, 6)")  


if __name__ == "__main__":
    unittest.main()

