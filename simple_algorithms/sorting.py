def bubble_sort(nums):
  """
  Sorts a list of integers using bubble sort algorithm
  :param nums: 
  :return: list
  """
  n = len(nums)
  if not nums:
    return []
  for i in range(n):
    for j in range(i, n):
      if nums[i] > nums[j]:
        nums[i] = nums[i] + nums[j]
        nums[j] = nums[i] - nums[j]
        nums[i] = nums[i] - nums[j]
  return nums

def merge_sort(nums):
  """
  Sorts a list of numbers using merge sort algorithm
  :param nums: 
  :return: list
  """
  if not nums:
    return []
  if len(nums) == 1:
    return nums
  mid = len(nums) / 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  return merge(left, right)

def merge(left, right):
  """
  Helper function for merge sort; Merges two sorted lists in order
  :param left: 
  :param right: 
  :return: list
  """
  res = []
  while left and right:
    if left[0] <= right[0]:
      res.append(left.pop(0))
    else:
      res.append(right.pop(0))
  return res + left + right


def quick_sort(nums, left=None, right=None):
  """
  Sorts a list on numbers using quick sort
  :param nums: 
  :param left: 
  :param right: 
  :return: list
  """
  left = 0 if left is None else left
  right = len(nums) - 1 if right is None else right
  if left >= right:
    return nums
  pivot = nums[left + (right-left)/2]
  idx = partition(nums, left, right, pivot)
  quick_sort(nums, left, idx - 1)
  quick_sort(nums, idx, right)
  return nums


def partition(nums, left, right, pivot):
  """
  Helper function for quick sort; Partitions the numbers so that all numbers
  smaller than partition are on the left and greater on the right 
  :param nums: 
  :param left: 
  :param right: 
  :param pivot: 
  :return: int index
  """
  while left <= right:
    while nums[left] < pivot:
      left += 1
    while nums[right] > pivot:
      right -= 1
    if left <= right:
      tmp = nums[left]
      nums[left] = nums[right]
      nums[right] = tmp
      left += 1
      right -= 1
  return left








