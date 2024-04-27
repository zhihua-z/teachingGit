class Page:
    def __init__(self, posX, posY, width, height, app):
        self.app = app
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.frame = None
        
        # 物体
        self.objects = []
        
    def setSize(self, size):
        self.width = size[0]
        self.height = size[1]
        
    def setPosition(self, pos):
        self.posX = pos[0]
        self.posY = pos[1]
        
    def register(self, object):
        self.objects.append(object)
    
    def clear(self):
        for object in self.objects:
            object.destroy()
        self.objects.clear()