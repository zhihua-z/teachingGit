'''
class全局变量和属性的区别

self.abc <- 这个class object的一个属性
比如身高，必须有主体的情况下，身高才有意义，因为
身高指的是某一个人类的身高
^ 身高就是一个属性

人类数量 <- 是一个class的全局变量
人类数量必须再有人类主体的情况下才有意义吗？
如果没有人类主体的话，人类数量的值依然有意义，0
如果有三个人，人类数量就是3

'''

class Human:
  # 这是一个共享的变量
  人类数量 = 0

  def __init__(self, gao):
    self.身高 = gao
    ttt = 10
    Human.人类数量 += 1
    

r = Human(150)
r2 = Human(170)

print(r.身高)
# print(r.ttt)
print(r.人类数量)
print(Human.人类数量)
# print(Human.身高)




