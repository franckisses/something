print("welcome back to this app")
while True:
    userinfo ={}
    print("1.注册")
    print("2.登录")
    choice = int(input("请输入选择："))
    if choice is 1:
        print("欢迎注册，请输入：")
        name = input("请输入您的用户名")
        password = input("请输入您的密码")
        userinfo['name']= name
        userinfo['password']= password
        print(userinfo)
    elif choice is 2:
        print("欢迎回来，请登录。")
        print(userinfo)
        name = input("请输入您的用户名")
        password = input("请输入您的密码")
        print("welcome back")
    else:
        print("please try again")
