from code import flying
class Heloplane(flying.Flying):
    def __init__(self, image):
        self.x = self.ox = 180
        self.y = self.oy = 400
        self.tag = "HP"
        super().__init__(self.x, self.y, image.width(), image.height(), image)
    def step(self, canvas):
        # 计算战机移动的方向和距离
        canvas.move("HP", self.x - self.ox, self.y - self.oy)
        self.ox = self.x
        self.oy = self.y

    def bomb(self, enemy):
        if self.x <= enemy.x <= self.x+self.image.width() and self.y <= enemy.y <=self.y+self.image.height():
            return True
        else:
            return False