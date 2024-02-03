
originalArray = [123, 531, 82, 1, 29, 19201, 21, 442, 231, 5543, 12, 12]

#: 个位数 3 1 2 1 9 1 1 2 1 3 2 2
#: 十位数 2 3 8 0 2 0 2 4 3 3 1 1
#: 百位数 1 5 0 0 0 2 0 4 2 5 0 0
#: 千位数 0 0 0 0 0 9 0 0 0 5 0 0
#: 万位数 0 0 0 0 0 1 0 0 0 0 0 0
#: statusx x x x x x x x x x x x
#: result: 19201, 5543, 531, 442, 231, 123 82, 29, 21, 12, 12, 1

inputArray = originalArray.copy()

# 第一步，找出最大值的位数

def count_digit(N):
    if N == 0:
        return 0
    return 1 + count_digit(N // 10)


numdigits = count_digit(max(inputArray))
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
    for num in inputArray:
        countArray[num // (10 ** i) % 10].append(num)
        # [[], [21, 51, 11], [52, 2, 32], [3, 73, 103]...]
    print_sorted(countArray)
    inputArray = return_count_sorted(countArray)
    
print(f'original array is {originalArray}')
print(f'sorted array is {inputArray}')