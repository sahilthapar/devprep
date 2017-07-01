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