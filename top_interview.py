# Single number

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common()[-1][0]

#Another solution for single number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)

#Max depth
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
        return 1 + max(leftDepth, rightDepth)

# Minimum stack implementation


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        m = self.getMin()
        if m is None or x < m:
            m = x
        self.stack.append((x, m))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]


    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]

# Majority element
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

# Find duplicates

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return not(len(collections.Counter(nums)) == len(nums))


# Happy numbers

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum([int(c) ** 2 for c in str(n)])
        return True

# FizzBuzz

class Solution(object):
    def toPrint(self, i):
        mul_3 = ((i % 3) == 0)
        mul_5 = ((i % 5) == 0)
        mul_both = mul_3 and mul_5
        if mul_both:
            return "FizzBuzz"
        if mul_3:
            return "Fizz"
        if mul_5:
            return "Buzz"
        return str(i)

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return map(self.toPrint, range(1, n+1))
