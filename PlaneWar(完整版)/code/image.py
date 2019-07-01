# 图片名称
background, bee, bullet, bigplane, hero, hero1,  smallplane \
    = \
    ('background', 'bee', 'bullet', 'bigplane',  'hero', 'hero0', 'smallplane')

start, pause, stop = "../image/start.png", "../image/pause.png", "../image/stop.png"
# 图片目录相对位置
path = '../image/'
# 图片前缀
suffix = '.gif'
# 图片后缀
prefix = ''


# 采用tkinter加载图片
def get_image(tkinter, image_name):
    return tkinter.PhotoImage(file=path + prefix +image_name + suffix)

#
# 图片对象获取
def load_image(tkinter):
    return (get_image(tkinter, background),
            get_image(tkinter, bee),
            get_image(tkinter, bullet),
            get_image(tkinter, bigplane),
            get_image(tkinter, hero),
            get_image(tkinter, hero1),
            get_image(tkinter, smallplane)
            )
def load_status_iamge(tkinter):
    return (
        tkinter.PhotoImage(file=start),
        tkinter.PhotoImage(file=pause),
        tkinter.PhotoImage(file=stop)
    )

if __name__ == '__main__':
    #print(image_path(bullet))
    print(round(0.05, 1))













