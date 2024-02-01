class zhuangbei:
  # __str__这个函数定义了，如果你要把你的Zhaoshu物体当作字符串来打的话，你应该怎样打印这个物体。
  # 其实也就是定义了这个物体到字符串的转换
  def __str__(self):
    return self.name

  def __init__(self, _name, _gongji, _hp, _mp, _tl, _fy):
    self.name = _name
    self.fy = int(_fy)
    self.gongji = int(_gongji)
    self.hp = int(_hp)
    self.mp = int(_mp)
    self.tl = int(_tl)

  # 检查a是否满足技能消耗需求
  # 足够：返回True，不够，就返回False

  # a使用招数打到b身上
  def use(self, a):
    if a.fy > 0:
      print(f'{a}装备了{self.name}')
      a.fy += self.fy
      print(f'{a}加了{self.fy}防御')

    if a.gongji > 0:
      print(f'{a}装备了{self.name}')
      a.gongji += self.gongji
      print(f'{a}加了{self.gongji}攻击')

    if a.hp > 0:
      print(f'{a}装备了{self.name}')
      a.hp += self.hp
      print(f'{a}加了{self.hp}生命')

    if a.mp > 0:
      print(f'{a}装备了{self.name}')
      a.mp += self.mp
      print(f'{a}加了{self.mp}法力')

    if a.tl > 0:
      print(f'{a}装备了{self.name}')
      a.tl += self.tl
      print(f'{a}加了{self.tl}体力')
