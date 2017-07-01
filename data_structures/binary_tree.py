

class TreeNode():

  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None


class BinaryTree():

  def __init__(self):
    self.root = None

  def add(self, val, node=None):
    """
    Function to add a new value to the tree
    :param val: 
    :return: 
    """
    if node is None:
      node = self.root
    if self.root is None:
      self.root = TreeNode(val)
    elif val < node.value:
      if node.left is None:
        node.left = TreeNode(val)
      else:
        self.add(val, node.left)
    else:
      if node.right is None:
        node.right = TreeNode(val)
      else:
        self.add(val, node.right)

  def inorder(self, node=None):
    """
    Inorder traversal
    :return: list Inorder traversal values
    """
    if node is None:
      node = self.root
    res = []
    if node.left is not None:
      res += self.inorder(node.left)
    res += [node.value]
    if node.right is not None:
      res += self.inorder(node.right)
    return res


  def preorder(self, node=None):
    """
    Preorder traversal
    :return: list Preorder traversal values
    """
    if node is None:
      node = self.root
    res = []
    res += [node.value]
    if node.left is not None:
      res += self.preorder(node.left)
    if node.right is not None:
      res += self.preorder(node.right)
    return res

  def postorder(self, node=None):
    """
    Postorder traversal
    :return: list Postorder traversal values
    """
    if node is None:
      node = self.root
    res = []
    if node.left is not None:
      res += self.postorder(node.left)
    if node.right is not None:
      res += self.postorder(node.right)
    res += [node.value]
    return res

  def bfs(self):
    """
    BFS traversal
    :return: list BFS traversal values
    """
    if self.root is None:
      return None
    res = []
    queue = [self.root]
    while len(queue):
      node = queue.pop(0)
      if node.left is not None:
        queue.append(node.left)
      if node.right is not None:
        queue.append(node.right)
      res += [node.value]
    return res


