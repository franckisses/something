import tkinter
import time
import bee
from code import bullet
from code import image
from code import enemy_plane
from . import sky
from . import heroplane
from . import config


#定义需要使用到的数据
enemys = []
bullets = []
skys = []
hplane = []


#创建窗体
game_window = tkinter.Tk()
#窗口设置
game_window.title('飞机大战')
#game_window.maxsize(600, 1000)
#game_window.minsize(100, 200)
#窗口位置处理
screenwidth = game_window.winfo_screenwidth()
screenheight = game_window.winfo_screenheight()
size='%dx%d+%d+%d' % (400, 654, (screenwidth-400)/2, 20)
print(size)
game_window.geometry(size)


#获取画布
window_canvas = tkinter.Canvas(game_window)
#画布包装方式
window_canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)



#加载需要使用到的图片
sky_image, bee_image, bullet_image, bigplane_image, hero_image, hero_image1, smallplane_image = image.load_image(tkinter)
#加载状态图片
#start_image, pause_image, stop_image = image.load_status_iamge(tkinter)
#绘制模型
def draw_model(canvas, *args):
    for models in args:
        if isinstance(models,list):
            for model in models:
                canvas.create_image(model.x,model.y,anchor=tkinter.NW,image=model.image, tag=str(model))
        else:
            canvas.create_image(models.x, models.y, anchor=tkinter.NW, image=models.image, tag="HP")
# 测试绘图，界面上绘制sky，bullet，bee，plane
# bee1 = bee.Bee(0, 0, bee_image)
# bullet = bullet.Bullet(100, 100, bullet_image)
# enemys.append(bee1)
# #bullets.append(bullet)
# sky1 = sky.Sky(0, 0, sky_image)
# skys.append(sky1)
# # 绘制所有模型
# draw_model(window_canvas, skys, enemys, bullets, hplane)
# sky1 = sky.Sky(0, 0, sky_image)
# skys.append(sky1)
import random
#产生敌机
def make_plane():
    i=random.randint(0, 20)
    if i <= 1:
        return(bee.Bee( bee_image))
    else:
        return enemy_plane.EnemyPlane(smallplane_image)

# 敌机入场
flying_enemy_count=0
def enter_action():
    global flying_enemy_count
    flying_enemy_count += 1
    if flying_enemy_count %10 ==0:
        plane = make_plane()
        window_canvas.create_image(plane.x, plane.y, anchor=tkinter.NW, image=plane.image, tag=plane.tag)
        enemys.append(plane)
        # 子弹入场
        new_bull = bullet.Bullet(hplane.x+hplane.image.width()/2+1-bullet_image.width()/2, hplane.y-bullet_image.height(), bullet_image)
        window_canvas.create_image(new_bull.x, new_bull.y, anchor=tkinter.NW, image=new_bull.image, tag=new_bull.tag)
        bullets.append(new_bull)

# 敌机动
index = 0  # 辅助战机切换图片。
def step_action():
    global index
    index += 1
    for model in enemys:
        model.step(window_canvas)
        model.des()
    for bul in bullets:
        bul.step(window_canvas)
    # 战机切换图片
    window_canvas.delete(hplane.tag)
    if index%2==0:
        window_canvas.create_image(hplane.x, hplane.y, anchor=tkinter.NW, image=hero_image1, tag=hplane.tag)
    else:
        window_canvas.create_image(hplane.x, hplane.y, anchor=tkinter.NW, image=hero_image, tag=hplane.tag)

def out_of_bounds_action():
    for e in enemys:
        if e.out_of_bounds():
            window_canvas.delete(e.tag)
            enemys.remove(e)
    for b in bullets:
        if b.out_of_bounds():
            window_canvas.delete(b.tag)
            bullets.remove(b)

def game_over():
    config.GAME_STATE = config.GAME_STOP
    window_canvas.create_image(0 ,0 , anchor=tkinter.NW, image=stop_image, tag="STATE")
    for e in enemys:
        window_canvas.delete(e.tag)
    for b in bullets:
        window_canvas.delete(b.tag)
    enemys.clear()
    bullets.clear()

def bomb_action():
    # 子弹撞敌机
    for e in enemys:
        for b in bullets:
            if b.bomb(e):
                enemys.remove(e)
                window_canvas.delete(e.tag)
                bullets.remove(b)
                window_canvas.delete(b.tag)
                break
    # 敌机撞英雄机
    for e in enemys:
        if hplane.bomb(e):
            enemys.remove(e)
            window_canvas.delete(e.tag)
            game_over()
            return


def game():
    #绘制游戏背景
    window_canvas.create_image(0 ,0 , anchor=tkinter.NW, image=sky_image, tag="BACK")
    # 绘制游戏启动界面
    #window_canvas.create_image(0 ,0 , anchor=tkinter.NW, image=start_image, tag="STATE")
    global hplane
    hplane = heroplane.Heloplane(hero_image)
    # 绘制基础模型
    draw_model(window_canvas, enemys, hplane, bullets)

    #鼠标检测
    def call_back_move(event):
        print("现在的位置是", event.x, event.y)  # 按哪个键，在Shell中打印
        if config.GAME_STATE == config.GAME_RUNNING:
            hplane.x, hplane.y = event.x -0.5*hplane.image.width(), event.y-0.5*hplane.image.height()
            hplane.step(window_canvas)
    def call_back_press(event):
        if config.GAME_STATE == config.GAME_START:
            config.GAME_STATE = config.GAME_RUNNING
            window_canvas.delete("STATE")
        elif config.GAME_STATE == config.GAME_STOP:
            config.GAME_STATE = config.GAME_START
            window_canvas.create_image(0 ,0 , anchor=tkinter.NW, image=sky_image, tag="BACK")
            window_canvas.create_image(0 ,0 , anchor=tkinter.NW, image=start_image, tag="STATE")
    window_canvas.bind("<Motion>", call_back_move)
    window_canvas.bind("<Button-1>", call_back_press)
    while(True):
        if config.GAME_STATE == config.GAME_RUNNING:
            # 敌机入场enter_action
            enter_action()
            step_action()
            # 删除越界
            out_of_bounds_action()
            # 检测碰撞
            bomb_action()
        game_window.update()
        time.sleep(0.01)

if __name__ == '__main__':
    game()
    # 显示窗口
    game_window.mainloop()
