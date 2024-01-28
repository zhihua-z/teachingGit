from PIL import Image

def pixel_add(p, v):
   return (p[0] + v[0], p[1] + v[1], p[2] + v[2])

def pixel_strength(p):
   return p[0] + p[1] + p[2]

def pixel_multiply(p, f):
    return (int(p[0] * f), int(p[1] * f), int(p[2] * f))

def show_image(path):
    img = Image.open(path)
    img.show()

    return img

def adjust_brightness(img, val):
  t_img = img.copy()
  for yi in range(t_img.height):
      for xi in range(t_img.width):
          p = t_img.getpixel((xi, yi))

          p = pixel_add(p, (val, val, val))

          t_img.putpixel((xi, yi), p)

  return t_img

def crop(path, x1, y1, x2, y2, result_path):
  img = Image.open(path)
  img_result = Image.new(mode = 'RGB', size = (x2 - x1, y2 - y1))

  # 1. shift x1, y1 to be my new (0, 0) position
  for yi in range(y1, y2):
     for xi in range(x1, x2):
        p = img.getpixel((xi, yi))
        img_result.putpixel((xi - x1, yi - y1), p)
        
  img_result.show()
  return img


def inverse_crop(path, x1, y1, x2, y2, result_path):
    img = Image.open(path)
    
    for yi in range(y1, y2):
        for xi in range(x1, x2):
            img.putpixel((xi, yi), (0, 0, 0))  # Set pixel to black

    img.save(result_path)
    img.show()
    return img

def adjust_shadow(path, val):
  img = Image.open(path)

  for yi in range(img.height):
    for xi in range(img.width):
      p = img.getpixel((xi, yi))
      s = pixel_strength(p)

      # (50, 25, 24) (50, 25, 25)
      # (100, 75, 74) (50, 25, 25)
      if s < 100:
        newval = int(val * (abs(s - 100) / 100))
        p = pixel_add(p, (newval, newval, newval))
  
      img.putpixel((xi, yi), p)
  
  img.show()
  return img

def adjust_hightlight(path, val):
  img = Image.open(path)

  for yi in range(img.height):
    for xi in range(img.width):
      p = img.getpixel((xi, yi))
      s = pixel_strength(p)

      # (50, 25, 24) (50, 25, 25)
      # (100, 75, 74) (50, 25, 25)
      if s > 100:
        newval = int(val * (abs(s - 100) / 100))
        p = pixel_add(p, (newval, newval, newval))
  
      img.putpixel((xi, yi), p)
  
  img.show()
  return img

def extract_channel(img, channel):
    img_t = Image.new('RGB', (img.width, img.height))
    
    for yi in range(img.height):
      for xi in range(img.width):
          p = img.getpixel((xi, yi))
          val = (0, 0, 0)
          if channel == 'r':
             val = (p[0], 0, 0)
          elif channel == 'g':
             val = (0, p[1], 0)
          elif channel == 'b':
             val = (0, 0, p[2])
          elif channel == 'rgb':
             val = p

          img_t.putpixel((xi, yi), val)
      
    return img_t

def crop_line(img, mode, val, color, pt):
    img_t = img.copy()
    
    for yi in range(img.height):
        for xi in range(img.width):
            p = img_t.getpixel((xi, yi)) # color of the current pixel
            if mode == 'h':
                if yi == val:
                    img_t.putpixel((xi, yi), color)
                if (yi < val and pt == 'A') or (yi > val and pt == 'B'):
                    img_t.putpixel((xi, yi), pixel_multiply(p, 0.3))
            elif mode == 'v':
                if xi == val:
                    img_t.putpixel((xi, yi), color)
                if (xi < val and pt == 'A') or (xi > val and pt == 'B'):
                    img_t.putpixel((xi, yi), pixel_multiply(p, 0.3))
      
    return img_t

# white: keep
# black: discard
def create_crop_layer(img, mode, val, pt, newLayer):
    img_t = None
    if newLayer:
        img_t = Image.new(mode = 'RGB', size = (img.width, img.height), color=(255, 255, 255))
    else:
        img_t = img
        
    for yi in range(img_t.height):
        for xi in range(img_t.width):
            if mode == 'h':
                if (yi < val and pt == 'A') or (yi > val and pt == 'B'):
                    img_t.putpixel((xi, yi), (0, 0, 0))
            elif mode == 'v':
                if (xi < val and pt == 'A') or (xi > val and pt == 'B'):
                    img_t.putpixel((xi, yi), (0, 0, 0))
                    
    return img_t

# 渲染出当前照片和crop layer
def render_crop(img, cropimg):
    img_t = img.copy()
    for yi in range(img_t.height):
        for xi in range(img_t.width):
            p1 = img_t.getpixel((xi, yi))
            p = cropimg.getpixel((xi, yi))
            if p != (255, 255, 255):
                img_t.putpixel((xi, yi), pixel_multiply(p1, 0.3))
                    
    return img_t

# 把crop a layer 和crop b layer 融合起来
def merge_crop(imgA, imgB):
    # 把img A 抄成 img_t
    img_t = imgA.copy()
    for yi in range(img_t.height):
        for xi in range(img_t.width):
            p2 = imgB.getpixel((xi, yi))
            if p2 == (0, 0, 0):
                img_t.putpixel((xi, yi), p2)
                # 把img B的内容抄去img t
                    
    return img_t
  
def crop_image(img, Apos, Bpos):
    # 1. 当你看到一个白色像素点的时候，记下当前 x1
    # 2. 然这一条白色像素点结束的时候，记下当前 x2
    # 3. width = x2 - x1 + 1
    
    img_t = Image.new(mode = 'RGB', size = (Bpos[0] - Apos[0] + 1, Bpos[1] - Apos[1] + 1), color=(255, 255, 255))
    start_x = Apos[0]
    start_y = Apos[1]
    
    for yi in range(Apos[1], Bpos[1] + 1):
      for xi in range(Apos[0], Bpos[0] + 1):
        p = img.getpixel((xi, yi))
        img_t.putpixel((xi - start_x, yi - start_y), p)
        
    return img_t
    
