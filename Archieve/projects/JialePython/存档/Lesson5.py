'''
我需要你创建几个新的变量，保存一个学生的名字，年龄和电话

下列方式储存大量的信息非常的困难

'''
# name = 'jiale'
# age = 10
# phone = 9182973102

# name2 = 'jiajia'
# age = 8
# phone = 18273917291

# names = ['jiale', 'jiajia']
# ages = [10, 8]
# phones = [9182973102, 18273917291]

# def print_mingzi(names, i):
#   print(names[i])

# def print_info(names, ages, phones, i):
#   print('名字:', names[i])
#   print('年龄:', ages[i])
#   print('手机:', phones[i])

# print_mingzi(names, 0)
# print_mingzi(names, 1)

# print_info(names, ages, phones, 1)
'''
我们需要有一个方式来储存大量的数据，并且能够管理很多的函数

jiale = Ren('jiale', 10, 109230182091)

ren_liebiao = [jiale, jiajia.....]

jiale.print_mingzi()

今天我们要学习class，class除了班级的意思，它还有一个意义：类型，类别

我们可以通过python的class来创建我们自己的类型，我们学过的一些类型包括整数，浮点数，字符串，布尔值，None，这些类型叫做原始类型。我们也可以通过class来制作我们自己的类型。

这样的类型叫做用户自定义类型

这样的编程理念叫面向对象编程，OOP，object oriented programming
在这个理念下，世界上一切的物体都可以被我们抽象化，用一些class来模拟，描述出来。

面向对象编程有三大概念：
1. Encapsulation，封装
  我们把函数，变量和信息封装在一个class里面

2. Inheritance，继承
  在创建了一些类型以后，我们可以创建一些新的类型来继承已有类型的一切内容

  class 形状 （面积）
    - 三角形
    - 圆形
    - 正方形
    - 长方形

3. Polymorphism，多变
  class 四边形 （def area）
  - 正方形（def area）
  - 平行四边形
  - 长方形（def area）
  - 棱形

'''


class Human:

  # init: initialize 初始化
  # 每次我们创建一个新的这个类型的变量的时候，都会呼叫这个初始化函数
  # self: jiale = Human() 当你创建一个叫jiale的变量的时候，self就等于jiale
  # 下一次当你用jiajia = Human() 创建一个叫jiajia的变量的时候，self就等于jiajia
  def __init__(self, _mingzi, _age, _phone):
    self.mingzi = _mingzi
    self.age = _age
    self.phone = _phone

  def print_info(self):
    print('!我的名字', self.mingzi)
    print('!我的年龄', self.age)
    print('!我的手机', self.phone)

  def grow(self):
    self.age = self.age + 1


jiale = Human('jiale', 10, '109237801928')
jiajia = Human('jiajia', 8, '192739817292')

jiale.print_info()
jiajia.print_info()

jiajia.grow()

jiale.print_info()
jiajia.print_info()

# 当你这样写的时候，这个叫mingzi的变量就会被绑定在jiale的范围里。
# jiale.mingzi = 'jiale'
# print(jiale.mingzi)
# print(mingzi)

# a = 5
# b = 1.0

# a = int(5)
# b = float(1.0)

'''
我们会模拟制作这样的文字游戏，你需要定义一些角色类型，招数类型
每一个角色都有一些基础的属性：
帮派
生命值
法力
体力
攻击力
防御力
招数 ： 列表


每一个招数都有一些以下属性：
招数的名字
攻击力
消耗
消耗类型（法力/生命/体力）

普通攻击的最终数值=攻击力 * (1 + 自己的等级*2%) - 目标的防御力 * (60% + 目标的等级*2%)

招数攻击的最终树枝=招数的攻击力

'''

import random


class Zhaoshu:

  def __init__(self, _name, _gongji, _xiaohao, _leixing):
    self.name = _name
    self.gongji = _gongji
    self.xiaohao = _xiaohao
    self.leixing = _leixing  # 'f', 's', 't'

  # 检查a是否满足技能消耗需求
  # 足够：返回True，不够，就返回False
  def check(self, a):
    if self.leixing == 's' and a.hp > self.xiaohao:
      return True
    elif self.leixing == 't' and a.tl > self.xiaohao:
      return True
    elif self.leixing == 'f' and a.mp > self.xiaohao:
      return True

    return False

  # a使用招数打到b身上
  def use(self, a, b):
    if self.name == '八荒六合唯我独尊功':
      print(f'{a.mingzi}:我要变强啦，哈哈哈，渣滓们，感受我的怒火吧,哈哈哈哈')
      a.lv += 100
      a.hp -= self.xiaohao
      print(f'{a.mingzi}使用禁术{self.name}，遭到反噬，扣了{self.xiaohao}生命,还剩{a.hp}点血')

    print(f'{b.mingzi}被{a.mingzi}用{self.name}打了一下')
    # 招数攻击的最终树枝=招数的攻击力
    # max：最大，会返回后面两个值中比较大的一个数字
    gongjizhi = max(self.gongji, 0)
    print(f'{self.name}打出了{gongjizhi}点伤害')

    if gongjizhi > 0:
      b.hp -= gongjizhi
      b.hp = max(b.hp, 0)
      #print(mubiao.mingzi, '被', self.mingzi, '打了一下，扣了', self.gj, '点血量。')
      #print(mubiao.mingzi, '还剩', mubiao.hp, '点血')
      # f-string, f字符串，f：format，有格式的字符串
    print(f'{b.mingzi}还剩{b.hp}点血')
    b.gengxin_zhuangtai()
    b.shuofeihua(gongjizhi)
    b.print_zhuangtai()  # 这是一个没有用的指令，意思是啥也不干


class Juese:

  # _zhao=[] 是一个默认参数，如果你不提供这个参数的输入的话，它就会使用默认值
  def __init__(self, _mz, _bangpai, _lv, _hp, _mp, _tl, _gj, _fy, _zhao=[]):
    self.mingzi = _mz
    self.bangpai = _bangpai
    self.hp = _hp
    self.mp = _mp
    self.lv = _lv
    self.tl = _tl
    self.gj = _gj
    self.fy = _fy
    self.zhao = _zhao

    self.huozhe = True
    self.chushi_hp = _hp

  def gongji(self, mubiao):
    if self.jiancha_zhuangtai() == False:
      print(f'{self.mingzi}已经死了，无法攻击')
      return
    # 攻击之前检查一下目标状态，确认是否要继续攻击
    if mubiao.jiancha_zhuangtai() == False:
      print(f'{mubiao.mingzi}已经死了，无法攻击')
      return

    print(f'{mubiao.mingzi}被{self.mingzi}打了一下')
    # 普通攻击的最终数值=攻击力 * (1 + 自己的等级*2%) - 目标的防御力 * (60% + 目标的等级*2%)
    #                 ^A                          ^B
    # 最后的攻击力=A-B
    a = self.gj * (1 + self.lv * 0.02)
    b = mubiao.fy * (0.6 + mubiao.lv * 0.02)
    gongjizhi = a - b

    # max：最大，会返回后面两个值中比较大的一个数字
    gongjizhi = max(gongjizhi, 0)
    print(f'此次攻击打出了{gongjizhi}点伤害')

    if gongjizhi > 0:
      mubiao.hp -= gongjizhi
      mubiao.hp = max(mubiao.hp, 0)
    #print(mubiao.mingzi, '被', self.mingzi, '打了一下，扣了', self.gj, '点血量。')
    #print(mubiao.mingzi, '还剩', mubiao.hp, '点血')
    # f-string, f字符串，f：format，有格式的字符串
    print(f'{mubiao.mingzi}还剩{mubiao.hp}点血')
    mubiao.gengxin_zhuangtai()
    mubiao.shuofeihua(gongjizhi)
    mubiao.print_zhuangtai()

  def fangzhaoshu(self, mubiao):
    # 如果我有招数的话，我就使用列表里第一个招数
    # 如果我没有招数，我就转成使用普通攻击

    if (len(self.zhao) == 0):
      self.gongji(mubiao)
    else:
      '''
      计划：
        先检查招数消耗类型，
        然后检查这个类型下你的法力/生命/体力的余额：
          如果够：
            减去消耗
            就使用招数
          如果不够：
            就使用普通攻击
      '''
      c = random.random()
      z = None  # None 没有 , 空值
      # 10% 概率
      if c < 0.10:
        z = self.zhao[1]
      else:
        z = self.zhao[0]

      # 如果够的话，再用这个招数
      if z.check(self):
        z.use(self, mubiao)
      else:
        print(f'{self.mingzi}不够技能消耗，打不出{z.name}，使用普通攻击')
        self.gongji(mubiao)

  def shuofeihua(self, gongjizhi):
    if self.huozhe == False:
      print(f'{self.mingzi}口吐鲜血，说我还会再回来的。。。')
    elif gongjizhi > 10:
      print(f'{self.mingzi}: 啊，好疼')
    elif gongjizhi > 0:
      print(f'{self.mingzi}: 行不行啊，小狗')
    else:
      print(f'{self.mingzi}大喊一声：哈哈哈没破防')

  def print_zhuangtai(self):
    '''
    打印出我的血条，血条一共10格，每拥有10%血量就+1格
    hp: 12, chushi_hp: 80
    #_________
    12 / 80 = 0.15
    0.15 * 10 = 1.25
    int(1.25) -> 1
    打印1个#，(10-1)_

    hp: 50, chushi_hp: 80
    ######____

    50 / 80 = 0.625
    0.625 * 10 = 6.25
    int(6.25) -> 6
    打印6个#，(10-6)_

    '''
    a = int(self.hp / self.chushi_hp * 30)
    b = 30 - a
    xuetiao = '#' * a + '_' * b
    print(f'{self.mingzi}: {xuetiao}')
    print('')

  def gengxin_zhuangtai(self):
    if self.hp <= 0:
      self.hp = 0
      self.huozhe = False
      print(f'{self.mingzi}被打死了。。。')

  def jiancha_zhuangtai(self):
    if self.huozhe == False:
      return False

    return True


bhlhwwdzgong = Zhaoshu('八荒六合唯我独尊功', 30, 20, 's')
zhlxy = Zhaoshu('召唤李逍遥', 90, 70, 's')
dajingangzhang = Zhaoshu('大金刚掌', 20, 20, 't')

guangling = Juese('广陵', '逍遥派', 1, 80, 0, 40, 25, 8, [zhlxy, bhlhwwdzgong])
xuanzang = Juese('玄奘', '少林寺', 1, 100, 0, 40, 20, 15, [dajingangzhang])

while xuanzang.huozhe and guangling.huozhe:
  xuanzang.fangzhaoshu(guangling)
  guangling.fangzhaoshu(xuanzang)

print('游戏结束')
if xuanzang.huozhe:
  print(f'{xuanzang.mingzi}赢了')
if guangling.huozhe:
  print(f'{guangling.mingzi}赢了')
'''
作业1:
定义一个新招数叫召唤李逍遥
给广陵加两个招数，八荒六合唯我独尊功(90%)，召唤李逍遥(10%)
在两个人身上测试新招数

你写完作业1，记得把内容备份一下

作业2（可选）:
写一个新的class：装备
装备可以增强角色的一个属性，比如攻击，或者防御
 leixing: 'h' : 生命
          'm' : 法力
          'f' : 防御
 mingzi: ...
 shuzhi: 50

角色除了招数列表以外，还应该有一个装备列表，并且这个装备要参与到计算公式中


普通攻击的最终数值=攻击力 * (1 + 自己的等级*2%) - 目标的防御力 * (60% + 目标的等级*2%) - 目标装备的防御力 + 自己装备的攻击力

招数攻击的最终数值 = 招数的攻击力 - 目标装备的防御力 + 自己装备的攻击力

'''