# Count primes

class Solution(object):
  def countPrimes(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
      return 0
  primes = [True] * n
  primes[0] = primes[1] = False
  for i in range(2, int(n ** 0.5) + 1):
    if primes[i]:
      primes[i * i:n:i] = [False] * len(primes[i * i: n: i])
  return sum(primes)


# Valid Parenthesis

class Solution(object):
  def top(self, stack):
    if len(stack) == 0:
      return None
    else:
      return stack[-1]

  def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []
    if (len(s) % 2 == 1):
      return False

    for c in s:
      if self.top(stack) == matching.get(c, "0"):
        stack.pop()
      else:
        stack.append(c)
    return True if len(stack) == 0 else False


# Find all anagrams of substring in a string
## Sliding window
class Solution(object):
  def findAnagrams(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    p_map = collections.Counter(p)
    window_map = collections.Counter(s[:len(p)])
    lst_idx = [0] if p_map == window_map else []
    idx = 0

    for c in s[len(p):]:
      cur_c_count = window_map.get(s[idx])
      if cur_c_count == 1:
        window_map.pop(s[idx])
      else:
        window_map[s[idx]] = cur_c_count - 1
      window_map[c] = window_map.get(c, 0) + 1
      if p_map == window_map:
        lst_idx.append(idx + 1)
      idx += 1
    return lst_idx


# Find first unique character in a string

class Solution(object):
  def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    char_count = collections.Counter(s)
    for i in range(len(s)):
      if char_count[s[i]] == 1:
        return i
    return -1

# Lowest common ancestor

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p, q):
      return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    if left is None:
      return right
    if right is None:
      return left
    else:
      return root

# Two sum
class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    required = {}
    for i in range(len(numbers)):
      if numbers[i] in required:
        return [required[numbers[i]] + 1, i + 1]
      else:
        required[target - numbers[i]] = i

# Two sum - array is sorted

class Solution(object):
  def twoSum(self, numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    high = len(numbers)
    low = 0

    while low < high:
      sum_numbers = numbers[low] + numbers[high]
      if sum_numbers == target:
        return [low, high]
      elif sum_numbers < target:
        low += 1
      else:
        high -= 1

# Product except self
