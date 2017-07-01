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
