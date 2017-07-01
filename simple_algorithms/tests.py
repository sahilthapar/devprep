import unittest
from recursion import fib_rec, fib_memo
from misc import reverse, largest_number, check_cycle, bin_search
from data_structures.node import Node
from data_structures.linked_list import LinkedList
from sorting import bubble_sort, merge_sort

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

  def test_reverse(self):
    self.assertEqual(reverse([1, 2, 3, 4]), [4, 3, 2, 1])
    self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])

  def test_largest_number(self):
    self.assertEqual(largest_number([1, 34, 3, 98, 9, 76, 45, 4]), 998764543431)
    self.assertEqual(largest_number([54, 546, 548, 60]), 6054854654)

  def test_bin_search(self):
    self.assertEqual(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7), 7)
    self.assertEqual(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1), 1)
    self.assertEqual(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 12), -1)

  def test_cycle_list(self):
    # With cycle
    n1 = Node(1)
    n2 = Node(2)
    n1.next = n2

    n3 = Node(3)
    n2.next = n3

    n4 = Node(4)
    n3.next = n4

    n5 = Node(5)
    n4.next = n5

    n6 = Node(6)
    n5.next = n6

    n6.next = n3

    self.assertEqual(check_cycle(n1), True)

    # Without cycle
    lst = LinkedList()
    map(lst.append, [1,2,3,4,5,6])

    self.assertEqual(check_cycle(lst.head), False)

  def test_bubble_sort(self):

    nums = [1, 0, -1, 3, 99, 0, 120, -120, 3, 4]
    sorted_nums = [-120, -1, 0, 0, 1, 3, 3, 4, 99, 120]

    self.assertEqual(bubble_sort(nums), sorted_nums)
    self.assertEqual(bubble_sort([]), [])
    self.assertEqual(bubble_sort([0]), [0])

  def test_merge_sort(self):

    nums = [1, 0, -1, 3, 99, 0, 120, -120, 3, 4]
    sorted_nums = [-120, -1, 0, 0, 1, 3, 3, 4, 99, 120]

    self.assertEqual(merge_sort(nums), sorted_nums)
    self.assertEqual(merge_sort([]), [])
    self.assertEqual(merge_sort([0]), [0])


