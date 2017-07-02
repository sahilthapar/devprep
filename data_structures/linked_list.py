from node import Node


class LinkedList():

  def __init__(self):
    self.head = None

  def append(self, value):
    """
    Adds a new value to the linked list and returns the head
    :param value: 
    :return: head
    """
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
      return
    cur = self.head
    while cur.next is not None:
      cur = cur.next

    cur.next = newNode

  def prepend(self, value):
    """
    Prepend a value to the linked list and return the head
    :param value: 
    :return: 
    """
    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode

  def delete(self, value):
    """
    Deletes a value from a linked list and returns head
    :param value: 
    :return: 
    """
    if self.head is None:
      return
    if self.head.value == value:
      self.head = self.head.next
      return
    current = self.head
    while current.next is not None:
      if current.next.value == value:
        current.next = current.next.next
        return
      current = current.next

  def reverse(self):
    """
    Reverses the list in place
    O(n), extra space O(1)
    :return: 
    """
    prev = None
    cur = self.head
    while cur:
      next = cur.next
      cur.next = prev
      prev = cur
      cur = next
    self.head = prev


  def toArray(self):
    """
    Helper function to convert linked list to array
    :return: lst
    """
    current = self.head
    lst = []
    while current is not None:
      lst.append(current.value)
      current = current.next
    return lst



