'''       processor.py  图像引擎
process : 处理    

'''

from PIL import Image

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