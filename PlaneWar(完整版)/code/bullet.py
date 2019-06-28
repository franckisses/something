from code import flying
from code import config
class Bullet(flying.Flying):

    bullet_count = 0

    def __init__(self, x, y, image):
        Bullet.bullet_count += 1
        self.tag = "bullet_" + str(Bullet.bullet_count)
        super().__init__(x, y, image.width(),image.height(),image)


    def step(self, canvas):
        self.y -= 1
        canvas.move(self.tag, 0, -1)

    def pos(self):
        return self.x,self.y

    def out_of_bounds(self):
        if self.y < -self.image.height():
            return True
        else:
            return False


    def bomb(self, enemy):
        if enemy.x <= self.x <= enemy.x+enemy.image.width() and enemy.y <= self.y <=enemy.y+enemy.image.height():
            return True
        else:
            return False
    def des(self):
        pass#print("("+str(self.x)+","+str(self.y)+")")