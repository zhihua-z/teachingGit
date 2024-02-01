'''
游戏和软件的区别 - 渲染

游戏：主动渲染软件，每一秒钟游戏都会画120帧的画面。每8毫秒，游戏画一次画面。
软件：被动渲染软件，在你做某一个操作之前，它是不会渲染的，或者只是已非常低的帧率画一些简单的动画。

软件的渲染是通过事件来驱动的，比如我移动一下窗口，那么这个软件就会收到一个窗口移动事件。它就知道它应该重新画在一个新的位置上了。

'''

import tkinter as tk
import json
import mystring
from Game import Game

# Position class能够帮我们记住一个坐标，包含了（x，y）两个数字
class Position:
  
  # 初始化一个Position class
  def __init__(self, tuple_pos):
    self.x = tuple_pos[0]
    self.y = tuple_pos[1]
  
  # 当我们要打印一个Position的时候，这个函数帮我们得到一个文字来描述这个Position
  # 输入：Position class
  # 输出：'(x, y)' 这个字符串
  def __str__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
  
  # 使坐标变化
  # 输入：x的变化，y的变化
  # 导致本身坐标的更改
  def add(self, x, y): # 这里的x，是一个本地变量，是你在呼叫这个函数的时候传进来的那个数字
    self.x += x # self.x，是存在于Position这个class里的一个属性
    self.y += y
  
  # 返回一个当前Position的复制品
  # 输出：一个新的Position class 物体，拥有和当前Position一样的数值
  def copy(self):
    return Position((self.x, self.y))

class BlackButton:
  def __init__(self, t, m, c, p):
    self.text = t
    self.master = m
    self.command = c
    self.position = p
    
    self.btn = tk.Button(\
      text=self.text, \
      master=self.master, \
      command=self.command, \
      highlightbackground='#111111'
      )
    self.btn.place(x = self.position[0], y = self.position[1])
    
  def clear(self):
    self.btn.destroy()


#jinengjian
class JnButton:
  def __init__(self, t, m, c, p):
    self.text = t
    self.master = m
    self.command = c
    self.position = p
    
    self.btn = tk.Button(\
      text=self.text, \
      master=self.master, \
      command=self.command, \
      highlightbackground='#111111'
      )
    self.btn.place(x = self.position[0], y = self.position[1])
    
  def clear(self):
    self.btn.destroy()   
class JueseLabel:
  def __init__(self, juese, m, p):
    self.juese = juese
    self.master = m
    self.position = Position(p)
    self.ui_items = []
    
    self.draw()
  
  def draw(self):
    # 把之前画过的角色清掉
    self.clear()
    
    # 我们不想修改原position
    current_pos = self.position.copy()
    
    #      ----------------     画出角色的基础信息
    t = tk.Label(text=f'名字：{self.juese.mingzi}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'帮派：{self.juese.bangpai}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'血量：{self.juese.hp}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'等级：{self.juese.lv}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    #      ----------------     画出角色的招数
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'招数：', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(20, 0)
    for z in self.juese.zhao:
      current_pos.add(0, 30)
      tz = tk.Label(text=f'{z.name}', master=self.master)
      tz.place(x = current_pos.x, y = current_pos.y)
      self.register(tz)
      
      leixing_wenzi = ''
      if z.leixing == 's':
        leixing_wenzi = '生命'
      elif z.leixing == 't':
        leixing_wenzi = '体力'
      elif z.leixing == 'm':
        leixing_wenzi = '法力'
      
      current_pos.add(0, 30)
      tz = tk.Label(text=f'攻击：{z.gongji}, 消耗: {z.xiaohao}点{leixing_wenzi}', master=self.master)
      tz.place(x = current_pos.x, y = current_pos.y)
      self.register(tz)
    current_pos.add(-20, 0)
    
    
    #      ----------------     画出角色的装备
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'装备：', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(20, 0)
    for z in self.juese.zhuangbei:
      current_pos.add(0,100)
      # t: temporary
      tz = tk.Label(text=f'名字:{z.name} 防御:{z.fy}\n攻击:{z.gongji} 生命:{z.hp}\n法力:{z.mp} 体力:{z.tl}', master=self.master) 
                            
                           
                           
                            
                           
      tz.place(x = current_pos.x, y = current_pos.y)
      self.register(tz)
      
    current_pos.add(-20, 0)
    
  def register(self, item):
    self.ui_items.append(item)
  
  # 清除之前画的内容
  def clear(self):
    for z in self.ui_items:
      z.destroy()






  
'''''
class ZhuangbeiLabel:
  def __init__(self, zhuangbei, m, p):
    self.zhuangbei = zhuangbei
    self.master = m
    self.position = Position(p)
    self.ui_items = []
    
    self.draw()
  
  def draw(self):
    self.clear()
    current_pos = self.position.copy()
    print(current_pos)
    
    t = tk.Label(text=f'名字：{self.zhuangbei.mingzi}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'防御：{self.zhuangbei.fy}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'攻击：{self.zhuangbei.gongji}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'血量：{self.zhuangbei.}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)


    current_pos.add(0, 30)
    t = tk.Label(text=f'法力：{self.zhuangbei.lv}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)


    current_pos.add(0, 30)
    t = tk.Label(text=f'体力：{self.zhuangbei.lv}', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)








    
    current_pos.add(0, 30)
    t = tk.Label(text=f'招数：', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(20, 0)
    for z in self.juese.zhao:
      current_pos.add(0, 30)
      tz = tk.Label(text=f'{z.name}', master=self.master)
      tz.place(x = current_pos.x, y = current_pos.y)
      self.register(tz)
      
      leixing_wenzi = ''
      if z.leixing == 's':
        leixing_wenzi = '生命'
      elif z.leixing == 't':
        leixing_wenzi = '体力'
      elif z.leixing == 'm':
        leixing_wenzi = '法力'
      
      tz = tk.Label(text=f'攻击：{z.gongji}, 消耗: {z.xiaohao}点{leixing_wenzi}', master=self.master)
      tz.place(x = current_pos.x, y = current_pos.y)
      self.register(tz)
    current_pos.add(-20, 0)
    
    current_pos.add(0, 30)
    t = tk.Label(text=f'装备：', master=self.master)
    t.place(x = current_pos.x, y = current_pos.y)
    self.register(t)
    
    current_pos.add(20, 0)
    for z in self.juese.zhuangbei:
      current_pos.add(0, 30)
      # t: temporary
      tz = tk.Label(text=f'{z.name}, {z.fy}, {z.gongji}, {z.hp}, {z.mp}, {z.tl}', master=self.master)
      tz.place(x = current_pos.x, y = current_pos.y)
      self.register(tz)
      
    current_pos.add(-20, 0)
    
  def register(self, item):
    self.ui_items.append(item)
    
  def clear(self):
    for z in self.ui_items:
      z.destroy()
    '''













'''class JueseLabelFight
JueseLabelFight继承了JueseLabel
当一个class继承另一个class的时候，我们是在说，这个JueseLabelFight是一个特殊的
JueseLabel，
JueseLabelFight将会拥有JueseLabel的一切的变量和function，并且也会是一个特殊
版本的角色标签

JueseLabelFight是一个子类型
JueseLabel是一个父类型
'''
class JueseLabelFight(JueseLabel):
  def __init__(self, juese, m, p, mubiao, redraw_fn):
    # super()指JueseLabel
    super().__init__(juese, m, p)
    self.mubiao = mubiao
    self.redraw = redraw_fn
    
    current_pos = Position(p)
    current_pos.add(0, 350)
    t = tk.Button(text='攻击', command=self.fight)
    t.place(x = current_pos.x, y = current_pos.y)
    
    for zhao in self.juese.zhao:
      current_pos.add(0, 30)
      t = tk.Button(text=f'{zhao.name}', command=self.use_zhao)
      t.place(x = current_pos.x, y = current_pos.y)
      

  def fight(self):
    self.juese.gongji(self.mubiao)
    self.redraw()
    
  def use_zhao(self):
    pass
    
    
class App:
  # 初始化这个App所需要的变量
  def __init__(self):
    self.game = None
    self.buttons = []
    self.jueseList = []
    self.jueseFightList = []
    
  # 加载App的资源，创建UI资源
  def load(self):
    self.game = Game(zhaoshu_path='./zhaoshu.json', zhuangbei_path='./zhuangbei.json', juese_path='./juese.json')
    
    # 创建一个窗口
    self.window = tk.Tk()
    self.window.title("逍遥传")
    self.window.geometry("1000x600")
    
    # 创建主游戏渲染分区
    self.f1 = tk.Frame(width=800, height=600)
    self.f1.pack(side=tk.LEFT)
    
    
    # 创建侧面按钮分区
    self.f2 = tk.Frame(width=200, height=600, background='#111111')
    self.f2.pack(side=tk.LEFT)

    self.btnViewJuese = BlackButton('查看角色', self.f2, self.view_juese, (10, 40))
    self.AddButton(self.btnViewJuese)

    self.btnC = BlackButton('清除角色', self.f2, self.clearJuese, (10, 70))
    self.AddButton(self.btnC)
    
    self.btnFight = BlackButton('打架', self.f2, self.view_fight, (10, 100))
    self.AddButton(self.btnFight)
    
    # 听取窗口的各种事件，然后对事件做出反应
    tk.mainloop()

  def view_fight(self):
    self.clearJueseFight()
    
    j0 = JueseLabelFight(self.game.juese[0], self.f1, (10, 10), self.game.juese[1], self.view_fight)
    j1 = JueseLabelFight(self.game.juese[1], self.f1, (400, 10), self.game.juese[0], self.view_fight)
    
    self.AddJueseLabelFight(j0)
    self.AddJueseLabelFight(j1)

    
  def view_juese(self):
    # 清除列表的里面的Label的内容
    for x in self.jueseList:
      x.clear()
      
    # 清除列表
    self.jueseList.clear()
    
    # 找到游戏里所有角色，把他们显示在左侧屏幕上
    pos_x = 10
    for x in self.game.juese:
      jl = JueseLabel(x, self.f1, (pos_x, 10))
      self.AddJueseLabel(jl)
      pos_x += 300
    
    
  def AddButton(self, btn):
    self.buttons.append(btn)
    
  def AddJueseLabel(self, lbl):
    self.jueseList.append(lbl)
    
  def AddJueseLabelFight(self, lbl):
    self.jueseFightList.append(lbl)
    
  def clear(self, option = ''):
    print('============')
    if option == '':
      for x in self.buttons:
        x.clear()
      for x in self.jueseList:
        x.clear()
      for x in self.jueseFightList:
        x.clear()
    elif option == 'view_juese':
      for x in self.jueseList:
        x.clear()
    elif option == 'buttons':
      for x in self.buttons:
        x.clear()
    else:
      return
    
  def clearJuese(self):
    for x in self.jueseList:
      x.clear()
      
  def clearJueseFight(self):
    for x in self.jueseFightList:
      x.clear()




  
  
  

# 主画面

# hello = tk.Label(text=txt)
# hello.place(x=200, y=10) #place(x=200, y=400)

# button = tk.Button(text="启动游戏!", command=load)
# button.place(x=200, y = 40)

# entry = tk.Entry()
# entry.place(x=10, y = 100)

# btnClear = tk.Button(text='清除', command=clear)
# btnClear.place(x = 200, y = 100)

# txtContent = tk.Text()
# txtContent.place(x = 10, y = 150)

# btnText = tk.Button(text='干点事儿', command=ganshier)
# btnText.place(x = 10, y = 500)




# 进入tk主程序循环
# 在这个循环里，你的程序会持续监听windows事件，并且对其作出反应，比如
# 移动窗口，变大变小，重新渲染。。。。。


'''
1. 再加两个按钮，查看装备和查看技能

丰富一下查看角色，装备和技能的现实，把它们的名字，各种属性都显示出来，并且显示在合理的位置

再加两个清除按钮


2. Optional：
加一个清除主页面按钮，按下这个按钮会清除掉f1里所有的东西

'''