def pretty_print(countArray):
    for i in range(len(countArray)):
        print(f'{i}\t{countArray[i]}')

def print_sorted(countArray):
    for i in range(len(countArray)):
        print(f'{i} ' * countArray[i], end='')
    print('')

inputArray = [2, 5, 3, 0, 2, 3, 0, 3]

# 6 position because max input is 5, min input is 0
countArray = [0, 0, 0, 0, 0, 0]

for e in inputArray:
    countArray[e] += 1

print(f'original array: {inputArray}')
pretty_print(countArray)
print_sorted(countArray)

# limitation 1:
# very ineffective when dealing with very large numbers, waste of memory
# can be resolved sparse array
'''
正常的array's index is 0, 1, 2, 3, 4, 5, 6, 7 ....
不正常的array index: #hashtable[0, 1, 2, 3, 4, 5, 590000000000]
or
linked list implementation of sparse array
'''

# limitation 2
# can only deal with non negative integers
# can be resolved with add a bias technique
# [-3, 5, 9, 0, 11, 5] +3=> [0, 8, 12, 3, 14, 8] -3=> [-3, 0, 5, 5, 9, 11]
