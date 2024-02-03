import random

def gen_random():
  with open('random_ints.txt', 'w') as f: # context manager, it helps you to close the file automatically
    count = 0
    numbers = []
    while count < 10000:
      num = random.randint(0, 1000000)
      if num not in numbers:
        numbers.append(num)
        count += 1

    for x in numbers:
      f.write(str(x) + '\n')

def sort_numbers():
  with open('random_ints.txt', 'r') as f:
    arr = []
    data = f.readlines()
    for elem in data:
      arr.append(int(elem))

  # 第一步，找出最大值的位数
  def count_digit(N):
      if N == 0:
          return 0
      return 1 + count_digit(N // 10)


  numdigits = count_digit(max(arr))
  print(f'max number has {numdigits} digits')

  def print_sorted(countArray):
      # for x in countArray:
      #     for e in x:
      #         print(f'{e} ', end = '')

      # print('')
      print(' '.join([str(e) for items in countArray for e in items]))

  def return_count_sorted(countArray):
      # result = []
      # for x in countArray:
      #     for e in x:
      #         result.append(e)
      # return result
      return [e for items in countArray for e in items]

  # [[2, 3, 103], [11,], [21], [32], [], [51, 52], [], [73]..]
  # ge [21, 51, 11, 52, 2, 32, 3, 73, 103...]
  # shi [2, 3, 103, 11, 21, 32, 51, 52, 73]

  # bai [[2, 3, 11, 21, 32, 51, 52, 73], [103]]
  # bai [2, 3, 11, 21, 32, 51, 52, 73, 103]

  for i in range(numdigits):
      # 根据第i位来排
      
      # 准备10个位置给不同的数字用
      countArray = []
      for k in range(10):
          countArray.append([])

      12345 % 10

      #countArray = [[]] * 10 # will create 10 shared memory list
      for num in arr:
          countArray[num // (10 ** i) % 10].append(num)
          # [[], [21, 51, 11], [52, 2, 32], [3, 73, 103]...]
      print_sorted(countArray)
      arr = return_count_sorted(countArray)
    
  # arr is sorted
  with open('sorted_random_ints.txt', 'w') as f:
    for x in arr:
       f.write(str(x) + '\n')

sort_numbers()