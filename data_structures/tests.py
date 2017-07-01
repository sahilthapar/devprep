import unittest
from linked_list import LinkedList

class Test(unittest.TestCase):
  def setUp(self):
    self.lnk_lst = LinkedList()

  def test_add(self):
    self.lnk_lst.append(1)
    self.lnk_lst.append(2)
    self.lnk_lst.append(3)
    self.lnk_lst.delete(3)
    self.lnk_lst.prepend(4)
    self.lnk_lst.delete(2)
    self.assertEqual(self.lnk_lst.toArray(), [4, 1])
