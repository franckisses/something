from code import flying
import random
from code import config
import time
class EnemyPlane(flying.Flying):
    STEP = 3
    plane_count = 0


    def __init__(self,image=None):
        EnemyPlane.plane_count+=1
        self.y = 0 - image.height()
        self.x = random.randint(0, config.WINDOW_WIDTH - image.width())
        self.tag = "enemy_plane_" + str(EnemyPlane.plane_count)
        super().__init__(self.x, self.y, image.width(),image.height(),image)

    def step(self, canvas):
        self.y += 1
        canvas.move(self.tag, 0, 1)

    def pos(self):
        return self.x, self.y

    def out_of_bounds(self):
        if self.y > config.WINDOW_HEIGHT:
            return True
        else:
            return False

    def des(self):
        pass#print("("+str(self.x)+","+str(self.y)+")")