from code import flying

class Sky(flying.Flying):
    def __init__(self,x , y, image):
        super().__init__(x, y, image.width(),image.height(),image)