arr = [5, 1, -1, 6, 9, 3, 7, 19, 22, 4, 0]
arr2 = [-1, 0, 1, 3, 4, 5, 6, 7, 9, 19, 22]

dict = {
  1: 1,
  2: 1,
  5: 1,
  6: 1,
  100: 1,
  1000: 1
}

'''
arr = [5, 4, 3, 2, 1]
4, 3, 2, 1, 5
3, 2, 1, 4, 5
2, 1, 3, 4, 5
1, 2, 3, 4, 5

'''

result = arr.copy()

def swap(list, a, b):
  t = list[a]
  list[a] = list[b]
  list[b] = t

'''
最差运行时间: N^2
最佳运行时间: N

时间复杂度一般取最坏情况： O(N^2)
'''
def bubble_sort(mylist):
  result = mylist.copy()
  sorted = False

  while not sorted:
    sorted = True
    for j in range(len(result) - 1):
      if result[j] > result[j + 1]:
        swap(result, j, j + 1)
        sorted = False
    if sorted:
      break

  return result

'''
最佳：1
最差：N

O(N)
'''

def linear_search(list, num):
  for x in list:
    if x == num:
      return True
  return False
#print(bubble_sort(arr))
#print(linear_search(arr, 100))






'''

最佳：1
最差：log N

O(log N)

'''
def binary_search(sortedlist, num):
  left = 0
  right = len(sortedlist) - 1

  while left < right:
    m = (left + right) // 2

    if sortedlist[m] == num:
      return True
    elif sortedlist[m] < num:
      left = m + 1
    else:
      right = m - 1

  return False





'''
最佳时间：1
最差时间：1

哈希表搜索

O(1)
'''
def hashtable_search(hashtable, num):
  return num in hashtable



print(10 in dict)
print('----------')

print(linear_search(arr, 19))
print(binary_search(arr2, 19))
print(hashtable_search(dict, 10))


'''
对于这个列表里每个东西，我会从头到尾一个一个看
如果其中某一个元素是我要找的东西，返回True
如果找了所有的都找不到，返回False
'''
arr = [1, 2, 3, 4, 5, 6]
if 5 in arr:
  print(True)


'''
如果我要在第m个位置放一个a

1. 扩大数组的个数by 1
2. 把原来123的位置不懂，把456的位置往后移
3. 最后把7放到中间

扩大数组的个数by 1
m前面的位置不动
m和m后面的数字往后移动1格
最后把a放在m位置

1 2 3 7 4 5 6
     g
'''
def insert(arr, m, num):
  arr.append(0)
  for i in range(len(arr) - 1, m, -1):
    arr[i] = arr[i - 1]
  arr[m] = num

'''
slicing; 列表分割
arr[1:5:3] -> 从1开始，到5结束，每次+3
arr[:5] -> 从0开始，到5结束
arr[5:] -> 从5开始，到最后
arr[::1] -> 从0开始，到最后，每次+1
arr[::-1] -> 从最后面开始，到最前面，每次-1
'''
def insert2(arr, m, num):
  return arr[:m] + [num] + arr[m:]



arr2 = [1, 2, 3, 4, 5, 6]
print(arr2[:5])

arr2 = insert2(arr2, 3, 7)
print(arr2)

'''
对列表实现以下几个函数，并且测试它们

1. 列表删除
remove(arr, 2) -> 删除arr里第一个出现的2

2. 列表完全删除
removeall(arr, 2) -> 删除arr里所有的2

3. 列表替换
replace(arr, 2, 6) -> 把列表里全部的2变成6

要求是每个函数前面，
'''
print("------------------")
#我打算先读取一遍列表，先输入查找要求为x。如果有x,删掉并结束。
arr = [5, 1,2,2, -1, 6, 9, 3, 7, 19, 22, 4, 0]
def remove(arr, x):
  arr.remove(x)
remove(arr, 2)
print(arr)
print("----------------")
#我打算先读取一遍列表，先输入查找要求为x，在设置条件while循环（只要有x）就删掉
arr = [5, 1,2,2, -1, 6, 9, 3, 7, 19, 22, 4, 0]
def removeall(arr, x):
  while x in arr:
    arr.remove(x)
removeall(arr, 2)
print(arr)
print("----------------")
#我打算先读取一遍列表，先输入查找要求为x，替换目标为Y。如果a[I] ==x，就替换
print(arr)
def replace(arr, x,y):
  for i in range (len(arr)):
    if(arr[i]==x):
      arr[i]=y
replace(arr, 2,6)
print(arr)

