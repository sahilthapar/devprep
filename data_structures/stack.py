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
    return len(self.lst) == 0

  def toArray(self):
    return self.lst
