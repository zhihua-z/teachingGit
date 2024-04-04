class Page:
    def __init__(self, posX, posY, width, height, app):
        self.app = app
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.frame = None