#_*_coding:utf-8_*_

class Flying(object):
    '''
        能飞行/移动的父类(拥有所有会动的物种特点)
        包括：左上角x、y坐标。width、height坐标。image
    '''
    def __init__(self, x, y, width,height,image):
        '''
        :param x: 左上角x坐标
        :param y: 左上角y坐标
        :param width: 图片宽度
        :param height: 图片高度
        :param image: 图片
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image


    def pos(self):
        return self.x,self.y


    def des(self):
        pass# print("("+str(self.x)+","+str(self.y)+")")


