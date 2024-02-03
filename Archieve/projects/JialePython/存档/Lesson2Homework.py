# 加载pandas数据库并且把它改命pd
import pandas as pd
import math

# data frame 数据框架
df = pd.read_excel('Titanic.xlsx')

b = 0
g = 0

# 'Survived'

# len() length: 长度
size = len(df['PassengerId'])

# 找到多少人活着，多少人死亡
for x in df['Survived']:
  if x == 1:
    b += 1
  else:
    g += 1

print(f'there are {b} live, {g} die')

b = g = 0

# 找到活着的人里的性别比例
for i in range(size):
  if df['Survived'][i] == 1:
    if df['Sex'][i] == 'male':
      b += 1
    else:
      g += 1

print(
    '{0:.2f}% of survivors are male, {1:.2f}% of survivors are female'.format(
        b / (b + g) * 100, g / (b + g) * 100))
'''
为什么算指数找到平方根就可以
37: 1, 2, 3, 4, *6*, 9, 12, 18, 36


'''

# 1. 死去的乘客的平均年龄

# 2. 每个舱位的乘客的存活率
#      1等舱几个人，活了几个，找到比例

# 3. 每个舱位的平均票价 （Fare）
print('--------')
b = 0
g = 0
ka = 0
ji = 0
a1 = 0
a2 = 0
a3 = 0
b1 = 0
b2 = 0 
b3 = 0
for i in range(size):
  if df['Survived'][i] == 0 and not math.isnan(df['Age'][i]):
    ka += df['Age'][i]
    ji += 1

print(f'there are {ka / ji}')
print(f'-------------')
for i in range(size):
  if df['Pclass'][i] == 1:
    a1 = a1 + 1
    if(df['Survived'][i] == 1):
       b1 = b1 + 1
  elif df['Pclass'][i] == 2:
    a2 = a2 + 1
    if(df['Survived'][i] == 1):
      b2 += 1
  elif df['Pclass'][i] == 3:
    a3 += 1
    if(df['Survived'][i] == 1):
      b3 += 1
a1 = b1 / a1 * 100
a2 = b2 / a2 * 100
a3 = b3 / a3 * 100
print(f'there are {a1}%  {a2}%  {a3}%')

# 重置a1 a2 a3 b1 b2 b3
print(f'-------------------')
ji1 = 0
ji2 = 0
for i in range(size):
  ji1 += df['Fare'][i]
  ji2 += 1
print(f'there are {ji1 /ji2}')