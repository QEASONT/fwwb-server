from xmlrpc.client import ServerProxy
import uuid


def createmeeting_c():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    server = ServerProxy('http://47.98.40.28:8001')  # 初始化服务器
    if (server.checkmeeting_s(suid)):
        print("你已经组织了一场会议。")
        return 1
    else:
        meetid = server.createmeeting_s(suid)
        print("你成功创建一场会议")
        print("会议id为" + meetid)
        return 0

def joinmeeting_s():
    server = ServerProxy('http://47.98.40.28:8001')
    meetid = input("会议号")
    if server.joinmeeting_s(meetid):
        print("加入成功")
        return meetid
    else:
        print("没有这个会议")
        return 1

