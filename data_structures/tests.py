import unittest
from linked_list import LinkedList
from stack import StackArray, StackLinkedList
from queue import QueueArray, QueueLinkedList
from binary_tree import BinaryTree


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

  def test_queue_array(self):
    self.queue_array = QueueArray()
    self.queue_array.enqueue(1)
    self.queue_array.enqueue(2)
    self.queue_array.enqueue(3)
    self.queue_array.dequeue()
    self.queue_array.dequeue()
    self.queue_array.enqueue(2)

    self.assertEqual(self.queue_array.toArray(), [3, 2])
    self.assertEqual(self.queue_array.peek(), 3)

  def test_queue_list(self):
    self.queue_list = QueueLinkedList()
    self.queue_list.enqueue(1)
    self.queue_list.enqueue(2)
    self.queue_list.enqueue(3)
    self.queue_list.dequeue()
    self.queue_list.dequeue()
    self.queue_list.enqueue(2)

    self.assertEqual(self.queue_list.toArray(), [3, 2])
    self.assertEqual(self.queue_list.peek(), 3)

  def test_binary_tree(self):
    self.binary_tree = BinaryTree()
    self.binary_tree.add(10)
    self.binary_tree.add(4)
    self.binary_tree.add(15)
    self.binary_tree.add(1)
    self.binary_tree.add(12)
    self.binary_tree.add(19)
    self.binary_tree.add(3)
    self.binary_tree.add(8)
    self.assertEqual(self.binary_tree.inorder(), [1, 3, 4, 8, 10, 12, 15, 19])
    self.assertEqual(self.binary_tree.preorder(), [10, 4, 1, 3, 8, 15, 12, 19])
    self.assertEqual(self.binary_tree.postorder(), [3, 1, 8, 4, 12, 19, 15, 10])
    self.assertEqual(self.binary_tree.bfs(), [10, 4, 15, 1, 8, 12, 19, 3])
