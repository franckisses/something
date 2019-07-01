# -*-coding: utf-8 -*-
from wxpy import *
from PIL import Image
import os
import math


def create_filepath():
	avatar_dir = os.getcwd() + '\\wechat\\'
	if not os.path.exists(avatar_dir):
		os.mkdir(avatar_dir)
	return avatar_dir


#保存好友头像
def save_avator(avatar_dir):
	#初始机器人，扫码登录
	bot = Bot()
	firends = bot.friends(update=True)
	num = 0
	for firend in firends:
		firend.get_avatar(avatar_dir + '\\' + str(num)+ '.jpg')
		print('好友昵称：%s'%firend.nick_name)
		num += 1

#拼接头像
def joint_avatar(path):
	# 获取文件内的头像个数
	length = len(os.listdir(path))
	image_size = 2560
	# 设置每个头像的大小
	each_size = math.ceil(2560 / math.floor(math.sqrt(length)))
	x_lines = math.ceil(math.sqrt(length))
	y_lines = math.ceil(math.sqrt(length))
	image = Image.new('RGB',(each_size * x_lines, each_size * y_lines))
	x = 0
	y = 0
	for (root,dirs,files) in os.walk(path):
		for pic_name in files:
			try:
				with Image.open(path+pic_name) as img:
					image.paste(img,(x * each_size,y*each_size))
					x += 1
					if x == x_lines:
						x =0
						y +=1
			except IOError:
				print('头像读取失败！')
	img = image.save(os.getcwd() + '/wechat.png')
	print('微信好友头像拼接完成')

if __name__ == '__main__':
	avatar_dir = create_filepath()
	save_avator(avatar_dir)
	joint_avatar(avatar_dir)