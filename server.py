# _*_ coding:utf-8 _*_

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import os


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass
# 调用函数1
def respon_string(str):
    return "明天中午咱们去看排球学妹，%s给我冲！" % str
# 调用函数2
def add(x, y):
    return x + y
def createuser_s(username, password):
    try:
        f = open('userlist.txt', 'a')  #创建新的用户
        f.write('\n' + username)
        f.write('*')
        f.write(password)
        f.close()
        return 0
    except:
        return 1  
def checkusername_s(username):
    f = open('userlist.txt', 'r')  #打开已存在用户的文件，假设文件已经存在
    name = f.readlines()
    for line in name:
        if (username == line.split('*')[0]):
            return True
    return False
def checkblack_s(username):
    f2 = open('blocklist.txt', 'r')
    block_name = f2.readlines()
    f2.close()
    for line in block_name:  #检查用户名是否被锁定，锁定则返回主菜单
        if username == line.strip('\n'):
            return 1
    return 0
def movetoblack_s(username):
    try:
        f3 = open('blocklist.txt', 'a')
        f3.write('\n' + username)
        f3.close()
        return 0
    except:
        return 1
#锁定 error2 
#登陆成功 0 
def login_s(username,password):  #登入函数，输入密码错误三次则锁定用户

    f = open('userlist.txt', 'r')
    info = f.readlines()
    f.close()
    for line in info:
        if (username == line.split('*')[0]
                and password == line.split('*')[1].strip('\n')):
            return 0
    return 1
def checkmeeting_s(suid):
    if os.path.exists(suid[0:5]):
        return True
    else:
        return False
def createmeeting_s(suid):
    file_path  = os.path.dirname(__file__)
    os.mkdir(file_path+'/'+suid[0:5])
    return suid[0:5]
def joinmeeting_s(meetid):
    if os.path.exists(meetid):
        return True
    else:
        return False
def link_s(suid, prediction_postprocessed):
    if joinmeeting_s(suid):
        
    

if __name__ == '__main__':
    server = ThreadXMLRPCServer(('127.0.0.1', 8000))  # 初始化
    server.register_function(respon_string, "get_string")  
    server.register_function(add, 'add')  
    server.register_function(createuser_s, 'createuser_s')  
    server.register_function(checkusername_s, 'checkusername_s')  
    server.register_function(checkblack_s, 'checkblack_s')  
    server.register_function(movetoblack_s, 'movetoblack_s')  
    server.register_function(login_s, 'login_s')  
    server.register_function(createmeeting_s, 'createmeeting_s')  

    print("Listening for Client")
    server.serve_forever()  # 保持等待调用状态


