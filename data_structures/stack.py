from node import Node

class StackArray():
  """
  Stack implementation using Array (Python list)
  """

  def __init__(self):
    self.lst = []

  def push(self, value):
    """
    Pushes a value to the top of the stack
    :param value: 
    :return: 
    """
    self.lst.append(value)
    return

  def peek(self):
    """
    Get the value at the top of the stack
    :return: int:
    """
    return None if self.isEmpty() else self.lst[-1]

  def pop(self):
    """
    Deletes the value at the top of the stack, and returns it
    :return: int
    """
    return None if self.isEmpty() else self.lst.pop()

  def isEmpty(self):
    """
    Checks if stack is empty
    :return: bool
    """
    return len(self.lst) == 0

  def toArray(self):
    """
    Helper function to convert stack to array
    :return: 
    """
    return self.lst[::-1]


class StackLinkedList():

  """
  Stack implementation using LinkedList
  """

  def __init__(self):
    self.top = None

  def push(self, value):
    """
    Pushes a value to the top of the stack
    :param value: 
    :return: 
    """
    newNode = Node(value)
    if not self.isEmpty():
      newNode.next = self.top
    self.top = newNode
    return

  def peek(self):
    """
    Get the value at the top of the stack
    :return: int:
    """
    return self.top.value

  def pop(self):
    """
    Deletes the value at the top of the stack, and returns it
    :return: int
    """
    if self.isEmpty():
      return None
    pop_val = self.top.value
    self.top = self.top.next
    return pop_val

  def isEmpty(self):
    """
    Checks if stack is empty
    :return: bool
    """
    return self.top is None

  def toArray(self):
    """
    Helper function to convert stack to array
    :return: 
    """
    current = self.top
    lst = []
    while current is not None:
      lst.append(current.value)
      current = current.next
    return lst
