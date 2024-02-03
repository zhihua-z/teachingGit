'''
怎么在python处理更加复杂的文件
很多时候文件并不是好好的放在一个表格的，他可能就是一个文本文档，但是你需要从里面提取出自己想要的信息

<_io.TextIOWrapper name='name.txt' mode='r' encoding='UTF-8'>
mode: 模式
-入
- x: create 创建 r: read 读取
- w: write 写
- a: append 把内容填到最后

open() 默认使用r

'''

f = open('name.txt', 'r')

# read() 读取整个文档，返回一个字符串
# readline() 读取下一行，你的文件读取指针每次都会停在下一行
# readlines() 读取所有行，把结果保存在一个列表上
names = f.readlines()

name = names[0].strip()

namelist = name.split(' ')

print('-'.join(namelist))
f.close()
print('\\')
'''
转义字符 \ 将一个字符在普通字符和特殊字符之间切换

abcd <- 字母

\n <- 换行
\t <- TAB
\a <- alarm

'\''



.strip() 把一个字符串前后的空白删掉（空白包括：空格，tab和换行）

.split() 分开 .split(',')用，把一个字符串分开
split也会返回列表

','.join(列表) 把列表里的东西用，连接在一起


.upper() 把所有英文字母变成大些
.lower() 把所有英文字母变成小些






'''


# f = open("name.txt","r")
# names = f.readlines()
# for i in range(len(names)):
#   names[i] = names[i].strip()
# print(names)
# f.close()


'''
List comprehension
返回 [x for x in <列表>]
'''

f = open("name.txt","r")
# names = [x.strip().split(' ')[0] + ' ' + x.strip().split(' ')[1].upper() for x in f.readlines()]
names = [x.strip().split(' ') for x in f.readlines()]
names = [x[0] + ' ' + x[1].upper() for x in names]
print(f'-----------------')


# for name in names:
#   for word in name:
#     print(word)

# print([word for name in names for word in name ])
# 可以这样写但是没必要这样写
names.append('Lisa HAINES')
print(names)

# 第一个办法
# for name in names:
#   if names.count(name) > 1:
#     print(f'{name} 重复了')

# 第二个办法
for i in range(len(names)):
  for j in range(len(names)):
    if i != j and names[i] == names[j]:
      print(f'重复 {names[i]}')



