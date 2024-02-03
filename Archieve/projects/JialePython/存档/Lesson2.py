'''

以下内容是list
'''


# int arr[10] = {1, 2, 3, 4, 5}
# int arr2[] = {1, 2, 3, 4, 5, 6, 7, 8}

# 类型是一个列表list
arr = [1, 2, 3, 4, 4, 5.0, 1.2]
print(arr)

arr.sort()  # quicksort 快速排序
print(arr)
'''
代码追踪
Traceback (most recent call last):
  File "/home/runner/JialePython/main.py", line 8, in <module>
    arr.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
类型错误：       不  被支持     在str和float的实例之间


'''

arr.append(100)  # 添加到后面
print(arr)

# arr.clear() # 清空
'''
???? 为什么要.copy()

如果我们这样复制arr2 = arr
那么arr2就会把arr的内容超过来
arr里面储存的是指向那个列表内存的位置
所以如果我们直接抄，就把同样的地址抄给了arr2
copy by reference  传引用

arr2 = arr.copy() 其实我们做了一个深度复制
就是把arr指向的那片内存复制一遍，然后把新的内存的地址给arr2
这样arr和arr2就会指向不同的地址
'''
arr2 = arr.copy()

# f-string, formatted string, 有格式的字符串
print(f'{arr}, {arr2}')

arr[0] = 'k'

print(f'{arr}, {arr2}')

a = 5
b = a
print(f'{a} | {b}')

print(f'这个数组里有{arr.count(4)}个4')

print(f'{arr}')
arr.reverse()  # 反转
print(f'{arr}')

# index的意思序号

print(f'这个数组里第一个k在{arr.index("k")}号位置')

arr.append('k')
arr.append('k')
arr.append('k')
arr.append('k')
arr.append('k')
print(arr)

while 'k' in arr:
  arr.remove('k')
print(arr)

# 名字 年龄 电话号 地址

xuesheng = [['jige', 9, '13958666666', '1街3号'], ['gouge', 9, '13958626666' ,'1街3号'], ['yangge', 7, '12381723112', '1街3号']]

print(xuesheng[2])



'''
以下内容是字典 dictionary
'''


'''
字典是一种需要用key来查找内容的数据结构
就像你要从英语词典里查student这个单词的意思，你不会一页一页的去寻找它
你会先去看前面的索引，然后找到student这个单词在第几页，然后直接去那一页看

字典类型没有序号，字典里寻找一个物体最重要的信息是他的key
字典是key：value对子
'''

fruit_dictionary = {
  'apple': '苹果',
  'banana': '香蕉'
}

print(fruit_dictionary['apple'])

fruit_dictionary['orange'] = '橙子'
fruit_dictionary['tangerine'] = '小橘子'
fruit_dictionary['mandarin'] = '大橘子'

print(fruit_dictionary)