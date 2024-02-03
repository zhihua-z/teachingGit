


'''
递归算法 (recursion) 最明显的特征就是有一个terminate condition，和一个call自己的过程

'''
def merge(left, right):
  result = []

  # result = [ 1, 2, 3, 4]
  # left = []
  # right = [6, 7, 8]
  while len(left) > 0 and len(right) > 0:
    if left[0] < right[0]:
      result.append(left[0])
      left = left[1:]
    else:
      result.append(right[0])
      right = right[1:]
  
  if len(left) == 0:
    result += right
  else:
    result += left
  
  return result


def merge_sort(mylist, level = 0):
  if len(mylist) <= 1:
    print(' ' * level + f'returned {mylist}')
    return mylist

  mid = len(mylist) // 2 # 1 // 2 -> 0

  left = mylist[:mid]
  right = mylist[mid:]

  print(' ' * level + f'left: {left}')
  print(' ' * level + f'right: {right}')

  leftreturn = merge_sort(left, level + 4)
  rightreturn = merge_sort(right, level + 4)

  result = merge(leftreturn, rightreturn)

  print(' ' * level + f'returned {result}')
  return result


# fastest sorting method in general sorting algorithms
# COMPLEXITY OF MERGE SORT is always O(N log N)
print(merge_sort([4, 1, 9, 2, 5, 8, 3, 6, 7]))