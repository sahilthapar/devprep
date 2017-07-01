import unittest
from recursion import fib_rec, fib_memo

class Test(unittest.TestCase):

  def test_fib_rec(self):

    self.assertEqual(fib_rec(-1), 0)
    self.assertEqual(fib_rec(0), 0)
    self.assertEqual(fib_rec(1), 1)
    self.assertEqual(fib_rec(2), 1)
    self.assertEqual(fib_rec(3), 2)
    self.assertEqual(fib_rec(4), 3)
    self.assertEqual(fib_rec(5), 5)
    self.assertEqual(fib_rec(6), 8)
    self.assertEqual(fib_rec(7), 13)

  def test_fib_memo(self):

    self.assertEqual(fib_memo(-1), 0)
    self.assertEqual(fib_memo(0), 0)
    self.assertEqual(fib_memo(1), 1)
    self.assertEqual(fib_memo(2), 1)
    self.assertEqual(fib_memo(3), 2)
    self.assertEqual(fib_memo(4), 3)
    self.assertEqual(fib_memo(5), 5)
    self.assertEqual(fib_memo(6), 8)
    self.assertEqual(fib_memo(7), 13)