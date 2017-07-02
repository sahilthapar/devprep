# Reverse a list in place

def reverse(l):
  for i in range(0, len(l)/2):
    cur = l[i]
    l[i] = l[-(i+1)]
    l[-(i+1)] = cur
  return l

# Given a list of numbers create the largest number

def largest_number(nums):
  sorted_nums = sorted(nums, cmp=lambda a, b: -1 if str(b)+str(a) < str(a)+str(b) else 1)
  return int(''.join(map(str, sorted_nums)))


# Check if a linkedlist has a cycle

def check_cycle(head):
  if head is None or head.next is None:
    return None
  ta = head
  tb = head.next

  while ta is not None and tb is not None and tb.next is not None:
    if ta == tb:
      return True
    ta = ta.next
    tb = tb.next.next

  return False

# Binary search

def bin_search(nums, n, low=None, high=None):
  # Find mid
  if low is None:
    low = 0
  if high is None:
    high = len(nums)
  mid = low + (high - low) / 2
  while low < high:
    # If n is at mid, return mid
    if nums[mid] == n:
      return mid + 1
    # If n < nums[mid], search in smaller half
    elif n < nums[mid]:
      return bin_search(nums, n, low, mid)
    # If n > nums[mid], search in upper half
    elif n > nums[mid]:
      return bin_search(nums, n, mid + 1, high)
  return -1


def is_unique_chars(s):
  """
  Checks if all characters in a string are unique
  Space complexity: Additional O(n)
  Time complexity: O(n)
  :param s: 
  :return: 
  """
  char_set = set()
  for c in s:
    if c in char_set:
      return False
    char_set.add(c)
  return True

def deduplicate(s):
  """
  Removes duplicate characters from a string
  Time complexity: O(n)
  Space complexity: Additional O(n)
  :param s: 
  :return:
  """
  char_set = set()
  rslt = []
  for c in s:
    if c not in char_set:
      rslt.append(c)
      char_set.add(c)
  return ''.join(rslt)


def reverse_string(s):
  """
  Reverse a given string
  :type s: str
  :rtype: str
  """
  n = len(s)
  if n <= 1:
    return s
  return reverse_string(s[n / 2:]) + reverse_string(s[:n / 2])

  # Can also use
  # return s[::-1]
