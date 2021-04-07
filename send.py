import paramiko
# 定义一个类，表示一台远端linux主机
class Linux(object):
    # 通过IP, 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        # transport和chanel
        self.t = ''
        self.chan = ''
        # 链接失败的重试次数
        self.try_times = 3
 
    # 调用该方法连接远程主机
    def connect(self):
         pass
 
    # 断开连接
    def close(self):
        pass
 
    # 发送要执行的命令
    def send(self, cmd):
        pass
 
    # get单个文件
    def sftp_get(self, remotefile, localfile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.get(remotefile, localfile)
        t.close()
 
    # put单个文件
    def sftp_put(self, localfile, remotefile):
        t = paramiko.Transport(sock=(self.ip, 22))
        t.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(localfile, remotefile)
        t.close()

if __name__ == '__main__':
    remotefile = r'/sense/p2ps.py/'
    localfile = r'p2ps.py'
 
    host = Linux('47.98.40.28', 'root', 'Qiantang2001007')
 
    # 将远端的xxoo.txt get到本地，并保存为ooxx.txt
    host.sftp_put(localfile, remotefile)
 
    # # 将本地的xxoo.txt put到远端，并保持为xxoo.txt
    # host.sftp_put(localfile, remotefile)