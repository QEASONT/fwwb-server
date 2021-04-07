from xmlrpc.server import SimpleXMLRPCServer  # 用于创建服务器
from xmlrpc.client import ServerProxy  # 用于向其它节点发出请求
from urllib.parse import urlparse  # 用于URL解析
from os.path import join, isfile  # 用于路径处理和文件查询

MAX_HISTORY_LENGTH = 6  # 访问链最大长度
OK = 1  # 查询状态：正常
FAIL = 2  # 查询状态：无效
EMPTY = ''  # 空数据


def get_port(url):  # 定义获取端口号的函数
    result = urlparse(url)[1]  # 解析并获取URL中的[域名:端口号]
    port = result.split(':')[-1]  # 获取以":"进行分割后的最后一组
    return int(port)  # 转换为整数后返回


class Node:
    def __init__(self, url, dir_name, secret):
        self.url = url
        self.dirname = dir_name
        self.secret = secret
        self.known = set()

    def _start(self):  # 定义启动服务器的方法
        server = SimpleXMLRPCServer(('', get_port(self.url)), logRequests=False)
        server.register_instance(self)  # 注册类的示例到服务器对象
        server.serve_forever()

    def _handle(self, filename):  # 定义处理请求的方法
        file_path = join(self.dirname, filename)  # 获取请求路径
        if not isfile(file_path):  # 如果路径不是一个文件
            return FAIL, EMPTY  # 返回无效状态和空数据
        return OK, open(file_path).read()  # 返回正常状态和读取的文件数据

    def _broadcast(self, filename, history):  # 定义广播的方法
        for other in self.known.copy():  # 遍历已知节点
            if other in history:  # 如果已知节点存在于历史记录
                continue  # 继续下一个已知节点信息
            try:
                server = ServerProxy(other)  # 访问非历史记录中的已知节点
                state, data = server.query(filename, history)  # 向已知节点发出请求
                if state == OK:  # 如果状态为正常
                    return OK, data  # 返回有效状态和数据
            except OSError:
                self.known.remove(other)  # 如果发生异常从已知节点中移除节点
        return FAIL, EMPTY  # 返回无效状态和空数据

    def query(self, filename, history=[]):  # 定义接收请求的方法
        state, data = self._handle(filename)  # 获取处理请求的结果
        if state == OK:  # 如果是正常状态
            return state, data  # 返回状态和数据
        else:  # 否则
            history.append(self.url)  # 历史记录添加已请求过的节点
            if len(history) >= MAX_HISTORY_LENGTH:  # 如果历史请求超过6次
                return FAIL, EMPTY  # 返回无效状态和空数据
            return self._broadcast(filename, history)  # 返回广播结果

    def hello(self, other):  # 定义向添加其它节点到已知节点的方法
        self.known.add(other)  # 添加其它节点到已知节点
        return OK  # 返回值是必须的

    def fetch(self, filename, secrt):  # 定义下载的方法
        if secrt != self.secret:  # 如果密钥不匹配
            return FAIL, EMPTY  # 返回无效状态和空数据
        state, data = self.query(filename)  # 处理请求获取文件状态与与数据
        if state == OK:  # 如果返回正常的状态
            with open(join(self.dirname, filename), 'w') as file:  # 写入模式打开文件
                file.write(data)  # 将获取到的数据写入文件
            return OK  # 返回值是必须的
        else:
            return FAIL  # 返回值是必须的


if __name__ == '__main__':
    url = 'http://127.0.0.1:6666'
    directory = 'NodeFiles01'
    secret = '123456'
    node = Node(url, directory, secret)
    node._start()
