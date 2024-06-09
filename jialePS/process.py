'''       processor.py  图像引擎
process : 处理    

'''

from PIL import Image



#输入：一个数字
#输出：1个数字
#功能：限制在0~255之间
def clamp(r):
    r=255 if r>255 else r
    r=0 if r<0 else r

    return r






# 合成，编成
# 输入：图片列表
# 输出：一张图片
def compose(imgs, width, height):
    
    img = Image.new('RGBA', (width, height), (255, 255, 255, 255))
    
    
    for ti in imgs:
        size = ti.size
        
        for y in range(height):
            if y >= size[1]:
                break
            
            for x in range(width):
                if x >= size[0]:
                    break
                # 提取像素颜色
                pixel = ti.getpixel((x, y))
                
                # 把提取出来的颜色放到img里
                img.putpixel((x, y), pixel)
    
    return img


#输入一张照片，多少亮度
#输出一张照片
#这个函数会调整照片里的每一个像素点的颜色来调整亮度
def liangdu(img, ld):
    for y in range(img.height):
    
        for x in range(img.width):
            if img.mode =='RGB':
                # 提取像素颜色
                r, g, b = img.getpixel((x, y))

                r = clamp(r+ld)
                g = clamp(g+ld)
                b = clamp(b+ld)
                a = 255
                # 把提取出来的颜色放到img里
                img.putpixel((x, y), (r,g,b,a))
            elif img.mode =='RGBA':
                # 提取像素颜色
                r, g, b, a = img.getpixel((x, y))

                r = clamp(r+ld)
                g = clamp(g+ld)
                b = clamp(b+ld)
                # 把提取出来的颜色放到img里
                img.putpixel((x, y), (r,g,b,a))

    return img

def baohedu(img, bh):
        
    for y in range(img.height):
        for x in range(img.width):
            if img.mode =='RGB':
                r, g, b = img.getpixel((x, y))
                
                pingjunzhi = (r + g + b) / 3
                
                newr = int(clamp(r + (r - pingjunzhi) * bh))
                newg = int(clamp(g + (g - pingjunzhi) * bh))
                newb = int(clamp(b + (b - pingjunzhi) * bh))
                newa = 255
            
                img.putpixel((x, y),(newr, newg, newb,newa))
            elif img.mode =='RGBA':
                r, g, b ,a= img.getpixel((x, y))
                
                pingjunzhi = (r + g + b) / 3
                
                newr = int(clamp(r + (r - pingjunzhi) * bh))
                newg = int(clamp(g + (g - pingjunzhi) * bh))
                newb = int(clamp(b + (b - pingjunzhi) * bh))
                newa = int(a)
            
                img.putpixel((x, y),(newr, newg, newb,newa))            
    
    return img


def fn调整透明度(img, 透明度):
    if img.mode =='RGBA':
        for y in range(img.height):
            for x in range(img.width):

                r,g,b,a = img.getpixel((x, y))

                a = int(a * 透明度)
                img.putpixel((x, y),(r, g, b, a))
    elif img.mode =='RGB':
        for y in range(img.height):
            for x in range(img.width):

                r,g,b = img.getpixel((x, y))

                a = 255
                img.putpixel((x, y),(r, g, b,a))       
    
    return img

def qiutian_lvjing(img, bh):
    
    newPixels = []
    
    for y in range(img.height):
        for x in range(img.width):
            r, g, b= img.getpixel((x, y))
            
            pingjunzhi = (r + g + b) / 3
            
            newr = int(clamp(r + (r - pingjunzhi) * bh))
            newg = int(clamp(g + (g - pingjunzhi) / bh))
            newb = int(clamp(b + (b - pingjunzhi) * bh))


        
            newPixels.append((newr, newg, newb))
    
    image = Image.new(img.mode, img.size)  
    image.putdata(newPixels)  

    return image