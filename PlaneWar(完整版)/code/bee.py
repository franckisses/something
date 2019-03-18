from code import flying
import random
from code import config

import time
class Bee(flying.Flying):
    '''
        蜜蜂类
    '''
    STEP = 3
    bee_count = 0 #蜜蜂计数


    def __init__(self,image=None):
        Bee.bee_count+=1
        self.y = 0 - image.height()
        self.x = random.randint(0,config.WINDOW_WIDTH - image.width())
        self.tag = "bee_" + str(Bee.bee_count)
        self.direct = True#飞机飞行方向，默认为True，向右
        super().__init__(self.x, self.y, image.width(),image.height(),image)

    def step(self, canvas):
        if self.x >= config.WINDOW_WIDTH - self.image.width():
            self.direct = False
        elif self.x <= 0:
            self.direct = True
        self.y += 1
        if self.direct:
            self.x += 1
            canvas.move(self.tag, 1, 1)
        else:
            self.x -= 1
            canvas.move(self.tag, -1, 1)

    def out_of_bounds(self):
        if self.y > config.WINDOW_HEIGHT:
            return True
        else:
            return False
