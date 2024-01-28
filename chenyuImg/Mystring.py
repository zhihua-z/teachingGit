
# /user/chenyu/cat.webp   token: /
#             ^
def find_last_of(string, token):
  pos = -1
  
  for i in range(len(string)):
    if string[i] == token:
      pos = i
      
  return pos
      