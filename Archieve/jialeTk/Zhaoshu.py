class Zhaoshu:

  # __str__这个函数定义了，如果你要把你的Zhaoshu物体当作字符串来打的话，你应该怎样打印这个物体。
  # 其实也就是定义了这个物体到字符串的转换
  def __str__(self):
    return self.name

  def __init__(self, _name, _gongji, _xiaohao, _leixing):
    self.name = _name
    self.gongji = int(_gongji)
    self.xiaohao = int(_xiaohao)
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
    #       ---------------        特殊效果检查
    if self.name == '八荒六合唯我独尊功':
      print(f'{a.mingzi}:我要变强啦，哈哈哈，渣滓们，感受我的怒火吧,哈哈哈哈')
      a.lv += 100
      a.hp -= self.xiaohao
      print(f'{a.mingzi}使用禁术{self.name}，遭到反噬，扣了{self.xiaohao}生命,还剩{a.hp}点血')

    #       ---------------        计算伤害数值
    # 招数攻击的最终树枝=招数的攻击力
    # max：最大，会返回后面两个值中比较大的一个数字
    gongjizhi = max(self.gongji, 0)
    
    
    
    
    
    #       ---------------        应用伤害到对手身上
    print(f'{b.mingzi}被{a.mingzi}用{self.name}打了一下')
    print(f'{self.name}打出了{gongjizhi}点伤害')

    if gongjizhi > 0:
      b.hp -= gongjizhi
      b.hp = max(b.hp, 0)
      #print(mubiao.mingzi, '被', self.mingzi, '打了一下，扣了', self.gj, '点血量。')
      #print(mubiao.mingzi, '还剩', mubiao.hp, '点血')
      # f-string, f字符串，f：format，有格式的字符串
    print(f'{b.mingzi}还剩{b.hp}点血')
    
    
    
    
    
    #       ---------------        更新对手状态 & 说废话
    b.gengxin_zhuangtai()
    b.shuofeihua(gongjizhi)
    b.print_zhuangtai()  # 这是一个没有用的指令，意思是啥也不干
