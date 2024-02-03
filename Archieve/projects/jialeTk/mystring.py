
# 如果返回-1，就是找不到
# 否则就是找到了，并且是最后一次出现的位置
def find_last(string, chr):
  pos = -1
  
  for i in range(len(string)):
        if string[i] == chr:
            pos = i
            
  return pos


# 如果返回-1，就是找不到
# 否则就是找到了，并且是第一次出现的位置
def find_first(string, chr):
  pos = -1
  
  for i in range(len(string)):
        if string[i] == chr:
            pos = i
            break
            
  return pos




