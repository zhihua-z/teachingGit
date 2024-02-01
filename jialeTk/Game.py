from Juese import Juese
from Zhaoshu import Zhaoshu
from zhuangbei import zhuangbei
import json


def find_name(biao, n):
  for z in biao:
    if z.name == n:
      return z
  return None


class Game:

  def __init__(self, juese_path, zhaoshu_path, zhuangbei_path):
    self.p_juese = juese_path
    self.p_zhaoshu = zhaoshu_path
    self.p_zhuangbei = zhuangbei_path

    self.zhuangbei = []
    self.zhaoshu = []
    self.juese = []

    self.load()

  def load(self):
    # 加载装备
    f = open(self.p_zhuangbei, 'r',encoding='utf-8')
    d = f.read().encode('utf-8')
    data = json.loads(d)  # 列表 of 一堆字典

    for di in data:
      zb = zhuangbei(di['名字'], di['攻击'], di['血量'], di['法力'], di['体力'],
                     di['防御'])
      self.zhuangbei.append(zb)

    print('加载了以下装备')
    for x in self.zhuangbei:
      print(x)

    # 加载招数
    f = open(self.p_zhaoshu,'r',encoding='utf-8')
    d = f.read()
    data = json.loads(d)  # 列表 of 一堆字典

    for di in data:
      zs = Zhaoshu(di['名字'], di['攻击'], di['消耗'], di['类型'])
      self.zhaoshu.append(zs)


    print('加载了以下招数')
    for x in self.zhaoshu:
      print(x)

    # 加载角色
    # "名字": "广陵",
    # "帮派": "逍遥派",
    # "血量": "80",
    # "法力": "0",
    # "等级": "1",
    # "体力": "40",
    # "攻击": "25",
    # "防御": "8",
    # "招数": [
    #     "召唤李逍遥",
    #     "八荒六合唯我独尊功"
    # ],
    # "装备": [
    #     "再生金良药",
    #     "萨满的珍珠法杖"
    # ]

    f = open(self.p_juese, 'r',encoding='utf-8 ')
    d = f.read()
    data = json.loads(d)  # 列表 of 一堆字典

    for di in data:
      _zhao = []
      _zhuangbei = []
      

      for zs in di['招数']:
        for zzz in self.zhaoshu:
          if zzz.name == zs:
            _zhao.append(zzz)
            break
      for zb in di['装备']:
        for zzzz in self.zhuangbei:
          if zzzz.name == zb:
            _zhuangbei.append(zzzz)
            break

      js = Juese(di['名字'], di['帮派'], di['等级'], di['血量'], di['法力'], di['体力'],
                 di['攻击'], di['防御'], _zhao, _zhuangbei)
      self.juese.append(js)

    print('加载了以下角色')
    for x in self.juese:
      print(x)

  def save(self):
    # # 储存游戏里的全部装备

    zb = []
    for z in self.zhuangbei:
      d = {
          '名字': z.name,
          '防御': z.fy,
          '攻击': z.gongji,
          '血量': z.hp,
          '法力': z.mp,
          '体力': z.tl
      }
      zb.append(d)

    t = json.dumps(zb, indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open('zhuangbei.json', 'w')
    f.write(t)
    f.close()

    # 储存游戏里的全部招数
    zs = []
    for z in self.zhaoshu:
      d = {'名字': z.name, '攻击': z.gongji, '消耗': z.xiaohao, '类型': z.leixing}
      zs.append(d)

    t = json.dumps(zs, indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open('zhaoshu.json', 'w')
    f.write(t)
    f.close()

    # 储存数据里的全部角色
    js = []
    for z in self.juese:
      d = {
          '名字': z.mingzi,
          '帮派': z.bangpai,
          '血量': z.hp,
          '法力': z.mp,
          '等级': z.lv,
          '体力': z.tl,
          '攻击': z.gj,
          '防御': z.fy,
          '招数': [z.name for z in z.zhao],
          '装备': [z.name for z in z.zhuangbei]
      }
      js.append(d)

    zb = []
    for z in self.zhaoshu:
      d = {'名字': z.name, '防御': z.fy, '攻击': z.gj, '血量': z.hp,'法力':z.mp,'体力':z.tl}
      zb.append(d)

    t = json.dumps(zs, indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open('zhaoshu.json', 'w')
    f.write(t)
    f.close()

    t = json.dumps(js, indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open('juese.json', 'w')
    f.write(t)
    f.close()


