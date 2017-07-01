from node import Node

class QueueArray():

  def __init__(self):
    self.lst = []

  def enqueue(self, value):
    """
    Add an element to the end of the queue
    :param value: int
    :return: 
    """
    self.lst.append(value)

  def dequeue(self):
    """
    Remove an element from the start of the queue and return it
    :return: int
    """
    return None if self.isEmpty() else self.lst.pop(0)


  def peek(self):
    """
    Look at the element at the start of the queue
    :return: int
    """
    return None if self.isEmpty() else self.lst[0]

  def isEmpty(self):
    """
    Check if queue is empty
    :return: bool
    """
    return not self.lst

  def toArray(self):
    """
    Helper function to convert queue to array
    :return: 
    """
    return self.lst


class QueueLinkedList():

  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, value):
    """
    Add an element to the end of the queue
    :param value: int
    :return: 
    """
    newNode = Node(value)
    if self.tail is not None:
      self.tail.next = newNode
    self.tail = newNode
    if self.isEmpty():
      self.head = newNode

  def dequeue(self):
    """
    Remove an element from the start of the queue and return it
    :return: int
    """
    if self.isEmpty():
      return None
    dequeue_value = self.head.value
    self.head = self.head.next
    return dequeue_value


  def peek(self):
    """
    Look at the element at the start of the queue
    :return: int
    """
    return None if self.isEmpty() else self.head.value

  def isEmpty(self):
    """
    Check if queue is empty
    :return: bool
    """
    return self.head is None

  def toArray(self):
    """
    Helper function to convert queue to array
    :return: 
    """
    current = self.head
    lst = []
    while current is not None:
      lst.append(current.value)
      current = current.next
    return lst
