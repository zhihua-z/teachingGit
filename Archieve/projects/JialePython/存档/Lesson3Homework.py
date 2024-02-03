'''
chr: char
ord: order

chr -> ascii字符变成数字
ord -> ascii表里对应的数字变字符
bin() -> 把一个数字变成二进制

'''
import pandas as pd
import math
df = pd.read_excel('存档/Titanic.xlsx')
size = len(df['PassengerId'])
ka = 0
ji = 0
for i in range(size):
  if df['Survived'][i] == 0 and not math.isnan(df['Age'][i]):
    ka += df['Age'][i]
    ji += 1
print(f'age is {ka / ji} ')




print(f'--------------------')
x = 0
f = open("name.txt","r")


superhero = []

x = 0
f = open("name.txt","r")
# 把文件的内容读出来
names = f.readlines()
for name in names:
  chai = name.split(' ')
  if chai[0][0] == chai[1][0]:
    print(name)
    superhero.append(name.strip())
f.close()

print(superhero)

f = open('superhero.txt', 'w')
for hero in superhero:
  f.write(hero + '\n')
f.close()