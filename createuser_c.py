from xmlrpc.client import ServerProxy


def createuser_c():
    server = ServerProxy('http://47.98.40.28:8001')  # 初始化服务器
    username = ""
    username = input('username')
    while (server.checkusername_s(username)):
        print('用户名已经存在')
        username = input('username:')
    password = input('password: ')
    if (server.createuser_s(username, password) == 0):
        print("注册成功")
        return 0
    else:
        print("注册失败")
        return 1


def login_c():
    server = ServerProxy('http://47.98.40.28:8001')  # 初始化服务器
    user = None
    count = 0
    while count < 4:
        username = input('username:')
        if user == None:  #user没有使用过，则直接赋予输入的用户名
            user = username
        elif user != username:  #如果下一次输入的用户名不一样，则记录上一次的用户名，同时计数清零
            user = username
            count = 0
        if server.checkblack_s(user) == 1:
            print("用户在黑名单中，请联系管理员")
            return 2
        password = input('password:')
        if server.login_s(user,password)==1:
            print("密码错误")
            count +=1
        else:
            print("登陆成功")
            return 0
    if count == 3:
        if server.movetoblack_s(user)==0:
            print("错误次数过多，拉入黑名单")
            return 1


