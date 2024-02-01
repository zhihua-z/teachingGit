# actually it is character
import random

class Juese:

  def __str__(self):
    return f'''
    角色名字：{self.mingzi}
    角色帮派：{self.bangpai}
    等级：{self.lv}
    血量：{self.hp}
    法力{self.mp}
    体力：{self.tl}
    攻击：{self.gj}
    防御：{self.fy}
    招数：{[z.name for z in self.zhao]}
    装备：{[c.name for c in self.zhuangbei]}
    '''

  # _zhao=[] 是一个默认参数，如果你不提供这个参数的输入的话，它就会使用默认值
  def __init__(self,
               _mz,
               _bangpai,
               _lv,
               _hp,
               _mp,
               _tl,
               _gj,
               _fy,
               _zhao=[],
               _zhuangbei=[]):
    self.mingzi = _mz
    self.bangpai = _bangpai
    self.hp = int(_hp)
    self.mp = int(_mp)
    self.lv = int(_lv)
    self.tl = int(_tl)
    self.gj = int(_gj)
    self.fy = int(_fy)
    self.zhao = _zhao
    self.zhuangbei = _zhuangbei

    self.huozhe = True
    self.chushi_hp = self.hp

  def gongji(self, mubiao):
    
    #        -------------   检查双方的状态
    
    if self.jiancha_zhuangtai() == False:
      print(f'{self.mingzi}已经死了，无法攻击')
      return
    # 攻击之前检查一下目标状态，确认是否要继续攻击
    if mubiao.jiancha_zhuangtai() == False:
      print(f'{mubiao.mingzi}已经死了，无法攻击')
      return

    
    
    #        -------------   计算出本次攻击的数值
    # 普通攻击的最终数值=攻击力 * (1 + 自己的等级*2%) - 目标的防御力 * (60% + 目标的等级*2%)
    #                 ^A                          ^B
    # 最后的攻击力=A-B
    #print('-------------')
    # type() 会打印出一个变量的数据类型
    #print(type(self.gj))
    #print(self.gj)
    a = self.gj * (1 + self.lv * 0.02)
    b = mubiao.fy * (0.6 + mubiao.lv * 0.02)
    gongjizhi = a - b

    # max：最大，会返回后面两个值中比较大的一个数字
    gongjizhi = max(gongjizhi, 0)
    
    
    
    #        -------------   打它
    print(f'{mubiao.mingzi}被{self.mingzi}打了一下')
    print(f'此次攻击打出了{gongjizhi}点伤害')

    # 扣对方的生命
    if gongjizhi > 0:
      mubiao.hp -= gongjizhi
      mubiao.hp = max(mubiao.hp, 0)
    #print(mubiao.mingzi, '被', self.mingzi, '打了一下，扣了', self.gj, '点血量。')
    #print(mubiao.mingzi, '还剩', mubiao.hp, '点血')
    # f-string, f字符串，f：format，有格式的字符串
    print(f'{mubiao.mingzi}还剩{mubiao.hp}点血')
    
    
    
    
    #        -------------   检查状态，处理后事
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
