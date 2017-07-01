import unittest
from linked_list import LinkedList
from stack import StackArray, StackLinkedList

class Test(unittest.TestCase):


  def test_linked_list(self):
    self.lnk_lst = LinkedList()
    self.lnk_lst.append(1)
    self.lnk_lst.append(2)
    self.lnk_lst.append(3)
    self.lnk_lst.delete(3)
    self.lnk_lst.prepend(4)
    self.lnk_lst.delete(2)
    self.assertEqual(self.lnk_lst.toArray(), [4, 1])

  def test_stack_array(self):
    self.stack_array = StackArray()
    self.stack_array.push(1)
    self.stack_array.push(2)
    self.stack_array.push(3)
    self.stack_array.pop()
    self.stack_array.pop()
    self.stack_array.push(2)

    self.assertEqual(self.stack_array.toArray(), [2, 1])
    self.assertEqual(self.stack_array.peek(), 2)

  def test_stack_list(self):
    self.stack_list = StackLinkedList()
    self.stack_list.push(1)
    self.stack_list.push(2)
    self.stack_list.push(3)
    self.stack_list.pop()
    self.stack_list.pop()
    self.stack_list.push(2)

    self.assertEqual(self.stack_list.toArray(), [2, 1])
    self.assertEqual(self.stack_list.peek(), 2)
