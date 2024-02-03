from sys import implementation
from PIL import Image

def pixel_add(p, v):
  return (int(p[0] + v[0]), int(p[1] + v[1]), int(p[2] + v[2]))

def pixel_strength(p):
  return p[0] + p[1] + p[2]

def adjust_brightness(path, val):  
  img = Image.open(path)

  # print(img.getpixel((0, 0)))
  # img.putpixel((1, 0), (0, 0, 0))

  # 调整亮度就是把照片里每一个像素点的颜色变亮/暗

  for y in range(img.height):
    for x in range(img.width):
      p = img.getpixel((x, y))
      p = pixel_add(p, (val, val, val))
      img.putpixel((x, y), p)

  img.show()

'''
如果一个颜色的rgb加起来<100, 那么它就是暗的，我们就应该调整它
'''
def adjust_shadow(path, shadow_strength, val):
  img = Image.open(path)

  # print(img.getpixel((0, 0)))
  # img.putpixel((1, 0), (0, 0, 0))

  # 调整阴影就是调整照片里暗的部分

  for y in range(img.height):
    for x in range(img.width):
      p = img.getpixel((x, y))
      s = pixel_strength(p)

      if s < shadow_strength:
        newval = val * (abs(s - shadow_strength) / shadow_strength)
        p = pixel_add(p, (newval, newval, newval))

      img.putpixel((x, y), p)

  img.show()

def green(path, y1):
  img = Image.open(path)
  
  for y in range(img.height):
    for x in range(img.width):
      p = img.getpixel((x, y))
      # Check if the pixel is ot green
      newcolor = pixel_add(p, (0, y1, 0))
      
      img.putpixel((x, y), newcolor)

  img.show()

def crop(src, dest, x1, y1, x2, y2):
  img = Image.open(src)
  img_r = Image.new('RGB', (x2 - x1 + 1, y2 - y1 + 1))

  for y in range(img.height):
    for x in range(img.width):
      if x < x1 or x > x2 or y < y1 or y > y2:
        continue
      
      p = img.getpixel((x, y))
      img_r.putpixel((x - x1, y - y1), p)
  
  img.show()
  img_r.show()

  img_r.save(dest)



#adjust_shadow('star.bmp', 300, 40)


# crop('star.bmp', 'result.bmp', 157, 128, 557, 328)
green('star.bmp', 50)

# homework 1.
# write a function to adjust highlight of an image

# homework 2. 
# write a function to make the image greener
# 注意的是原本就很绿的像素点，你别调整
# 距离绿色越远的像素点，调的越多