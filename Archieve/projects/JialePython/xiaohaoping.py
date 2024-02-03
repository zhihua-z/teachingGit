class xiaohaoping:
  # __str__这个函数定义了，如果你要把你的Zhaoshu物体当作字符串来打的话，你应该怎样打印这个物体。
  # 其实也就是定义了这个物体到字符串的转换
  def __str__(self):
    return self.name

  def __init__(self, _name, _gongji, _hp, _mp, _tl, _ci):
    self.name = _name
    self.gongji = _gongji
    self.hp = _hp
    self.mp = _mp
    self.tl = _tl
    self.ci = _ci

  # 检查a是否满足技能消耗需求
  # 足够：返回True，不够，就返回False

  # a使用招数打到b身上
  def use(self, a, b):
    if a.ci > 0:
      print(f'{a}使用了{self.name}')
      if a.gongji != 0:
        a.gongji += self.gongji
        print(f'{a}加了{self.gongji}攻击')

      if a.hp != 0:
        a.hp += self.hp
        print(f'{a}加了{self.hp}生命')

      if a.mp != 0:
        a.mp += self.mp
        print(f'{a}加了{self.mp}法力')

      if a.tl != 0:
        a.tl += self.tl
        print(f'{a}加了{self.tl}体力')
      #专精道具：鬼符
      if self.name == "鬼符":
        print(f'{a}使用鬼符，吸取了{b}{self.tl}体力')
        b -= self.tl
        a += self.tl

      self.ci = self.ci - 1
