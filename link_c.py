from xmlrpc.client import ServerProxy
import uuid
import socket
import tkinter
import tkinter.messagebox
import threading
import json
import tkinter.filedialog
from tkinter.scrolledtext import ScrolledText
import wx
import telnetlib
from time import sleep
import _thread as thread
import pyautogui
import time
# import functin_real
# import SwitchState


def login(username):
    # 登录处理
    try:
        con.open('47.98.40.28', port=8000, timeout=10)
        response = con.read_some()
        if response != '连接成功'.encode('utf-8'):
            print('Error'+'连接失败!')
            return
        con.write(('login ' + username + '\n').encode("utf-8"))
        response = con.read_some()
        if response == '用户名为空'.encode('utf-8'):
            print('Error'+'用户名为空!')
        elif response == '用户名已存在':
            print('Error'+ '用户名已存在!')
    except Exception:
        pass




def send(prediction,username):
    con = telnetlib.Telnet()
    con.open('47.98.40.28', port=8000, timeout=10)
    response = con.read_some()
    if response != '连接成功'.encode('utf-8'):
        print('Error'+'连接失败!')
        return
    con.write(('login ' + username + '\n').encode("utf-8"))
    response = con.read_some()
    if response == '用户名为空'.encode('utf-8'):
        print('Error'+'用户名为空!')
    elif response == '用户名已存在':
        print('Error'+ '用户名已存在!')
    # 发送消息
    message = prediction
    #这里的'say '不可随意变动，为呼应server.py中命令处理类定义的handle(),实现文字聊天协议而存在
    con.write(('say ' + message + '\n').encode("utf-8"))


def receive(username):
    con = telnetlib.Telnet()
    con.open('47.98.40.28', port=8000, timeout=10)
    response = con.read_some()
    if response != '连接成功'.encode('utf-8'):
        print('Error'+'连接失败!')
        return
    con.write(('login ' + username + '\n').encode("utf-8"))
    response = con.read_some()
    if response == '用户名为空'.encode('utf-8'):
        print('Error'+'用户名为空!')
    elif response == '用户名已存在':
        print('Error'+ '用户名已存在!')
    # 接受服务器的消息
    swi = {
            "Calling someone closer": 0,
            "Covering ears": 0,
            "Covering eyes": 0,
            "Nodding": 0,
            "Pointing left": 0,
            "Pointing right": 0,
            "Pointing to the camera": 0,
            "Putting finger to mouth": 0,
            "Scratching": 0,
            "Shaking head": 0,
            "Swiping down (with two hands)": 0,
            "Swiping left": 0,
            "Swiping right": 0,
            "Swiping up": 0,
            "Swiping up (with two hands)": 0,
            "Thumb down": 0,
            "Thumb up": 0,
            "Waving": 0,
            "Zooming in": 0,
            "Zooming out": 0
        }

    action = [            
        "Calling someone closer",
        "Covering ears",
        "Covering eyes",
        "Nodding",
        "Pointing left",
        "Pointing right",
        "Pointing to the camera",
        "Putting finger to mouth",
        "Scratching",
        "Shaking head",
        "Swiping down (with two hands)",
        "Swiping left",
        "Swiping right",
        "Swiping up",
        "Swiping up (with two hands)",
        "Thumb down",
        "Thumb up",
        "Waving",
        "Zooming in",
        "Zooming out"]

     while True:
        sleep(0.6)
    #在I/O中读取数据，存在result变量中

        result = con.read_very_eager().decode('utf-8')
        result1 = list(result.split('\n'))
        try:
            result1 = result1.split(": ")
            ac = result1[1]
            if ac in action and :
                print(ac)
                prediction = ac
                mode = SwitchState.switchSt()
                print(mode)
                functin_real.pris(prediction,swi,mode)
        except:
            print("cuola")
            pass



# def link_c(uuid,prediction):
#     uid = str(uuid.uuid4())
#     suid = ''.join(uid.split('-'))
#     server = ServerProxy('http://47.98.40.28:8001')  # 初始化服务器
#     server.link_s(suid[0:5])

# def send(prediction):
#     message = prediction + '~' + user
# 	s.send(message.encode())
# 	INPUT.set('')

# def receive():
# 	global uses
# 	while True:
# 		data = s.recv(1024)
# 		data = data.decode()
# 		print(data)
# 		try:

# 		except:
# 			data = data.split('~')
# 			message = data[0]
# 			userName = data[1]
# 			message = '\n' + message
# 		    if userName == user:
#                 print(message)


# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((47.98.40.28, 8001))
# if user:
#     s.send(user.encode())  # 发送用户名
# else:
#     s.send('用户名不存在'.encode())
#     user = IP + ':' + PORT
# send(prediction.encode())