"""
process : 
- pixel related operation
- image transformation


image in -> process.xxxxxxx() -> image out 

"""


from sys import implementation
from PIL import Image

from UIBase import Position


def pixel_add(p, v):
    return (int(p[0] + v[0]), int(p[1] + v[1]), int(p[2] + v[2]))

def pixel_multiply(p, v):
    return (int(p[0] * v), int(p[1] * v), int(p[2] * v))

def pixel_strength(p):
    return p[0] + p[1] + p[2]


def pixel_max_index(p):
    if p[0] > p[1] and p[0] > p[2]:
        return 0
    elif p[1] > p[0] and p[1] > p[2]:
        return 1
    else:
        return 2


def pixel_min_index(p):
    if p[0] < p[1] and p[0] < p[2]:
        return 0
    elif p[1] < p[0] and p[1] < p[2]:
        return 1
    else:
        return 2

def adjust_saturation(img, saturation):
    t_img = img.copy()
    # 调整亮度就是把照片里每一个像素点的颜色变亮/暗

    for y in range(t_img.height):
        for x in range(t_img.width):
            p = t_img.getpixel((x, y))
            
            # # calculate mean value of r g b
            # if saturation < 0 :
            #     ....
            # else:
            #     ....
            
            t_img.putpixel((x, y), p)

    return t_img
    

def adjust_brightness(img, val):
    t_img = img.copy()
    # 调整亮度就是把照片里每一个像素点的颜色变亮/暗

    for y in range(t_img.height):
        for x in range(t_img.width):
            p = t_img.getpixel((x, y))
            p = pixel_add(p, (val, val, val))
            t_img.putpixel((x, y), p)

    return t_img


def adjust_vibrance(img, val):
    t_img = img.copy()
    # 调整亮度就是把照片里每一个像素点的颜色变亮/暗

    for y in range(t_img.height):
        for x in range(t_img.width):
            p = t_img.getpixel((x, y))

            # adjust vibrance of this pixel
            # find max
            # find min

            max_i = pixel_max_index(p)
            max_v = p[max_i]

            # min_i = pixel_min_index(p)

            # vibrance default = 50
            # (25, 100, 50) -> if vibrance == 0: (100, 100, 100)
            # r: difference = -50: r 25 -> 100
            # r: difference = -25: r 25 -> 67.5
            # r: difference = 0  : r 25 -> 25
            # r: difference = x  : r 25 -> r + (max_i - r) * (-x / 50)

            # b: difference = 25 : b 50 -> b + (max_i - b) * (-25 / 50) -> 25
            # (25, 100, 50) -> if vibrance == 100: (0, 100, 3)

            r = p[0]
            g = p[1]
            b = p[2]

            diff = val - 50

            r = round(r + (max_v - r) * (-diff / 50))
            g = round(g + (max_v - g) * (-diff / 50))
            b = round(b + (max_v - b) * (-diff / 50))

            t_img.putpixel((x, y), (r, g, b))

            # vibrance = 0 means all three colours tends to be equal

            # vibrance = 100 means all three colours spread very far apart

    return t_img


"""
如果一个颜色的rgb加起来<100, 那么它就是暗的，我们就应该调整它
"""


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
    img_r = Image.new("RGB", (x2 - x1 + 1, y2 - y1 + 1))

    for y in range(img.height):
        for x in range(img.width):
            if x < x1 or x > x2 or y < y1 or y > y2:
                continue

            p = img.getpixel((x, y))
            img_r.putpixel((x - x1, y - y1), p)

    img.show()
    img_r.show()

    img_r.save(dest)

def crop_a_mask(img, pointA, pointB):
    t_img = img.copy()

    for y in range(t_img.height):
        for x in range(t_img.width):
            p = t_img.getpixel((x, y))
            
            if x < pointA.x:
                p = pixel_multiply(p, 0.3)
            
            elif y < pointA.y:
                p = pixel_multiply(p, 0.3)
            
            t_img.putpixel((x, y), p)

    return t_img

def crop_b_mask(img, pointA, pointB):
    t_img = img.copy()

    for y in range(t_img.height):
        for x in range(t_img.width):
            p = t_img.getpixel((x, y))
            
            if x > pointB.x and y >= pointA.y:
                p = pixel_multiply(p, 0.3)
            elif y > pointB.y and x >= pointA.x:
                p = pixel_multiply(p, 0.3)
            
            t_img.putpixel((x, y), p)

    return t_img