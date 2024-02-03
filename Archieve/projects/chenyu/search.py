from operator import truediv



def linear_search():

  arr = []
  with open('sorted_random_ints.txt') as f:
    data = f.readlines()
    for elem in data:
        arr.append(int(elem))

  print(arr)
  operation_count = 0
  target = 981944
  found = False

  # O(N)
  # Linear search
  # best case:  1
  # worst case: N


  for x in arr:
      operation_count += 1
      if x == target:
          found = True
          break

  if found:
    print(f'found in {operation_count} steps')
  else:
    print(f'not found after {operation_count} steps')

def binary_search():
  # O(log N)
  # Binary Search

  # 先排序，再找
  arr = []
  with open('sorted_random_ints.txt') as f:
    data = f.readlines()
    for elem in data:
        arr.append(int(elem))

  operation_count = 0
  target = 981944
  found = False

  left = 0
  right = len(arr)

  m = (left + right) // 2
  found = False

  while not found:
    print(left, right)
    m = (left + right) // 2
    
    operation_count += 1

    if right <= left:
      break
    elif arr[m] == target:
      found = True
      break
    elif arr[m] < target:
      left = m + 1
    else:
      right = m - 1

  if found:
    print(f'found in {operation_count} steps')
  else:
    print(f'not found after {operation_count} steps')

'''
if you put all the numbers start with 1 in a chunk
all numbers start with 2 in a chunk

if you want to find 2132
you can call it B_list

you can also save them into 100 different files

'''

def b_list_search():
  pass



binary_search()