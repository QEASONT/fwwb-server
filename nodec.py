from xmlrpc.client import ServerProxy

filename = 'file.txt'  # 请求的资源文件名称

url1 = 'http://127.0.0.1:7777'  # 请求的服务器URL
peer1 = ServerProxy(url1)  # 创建服务器代理对象
print(peer1.query(filename))  # 调用服务器的接收请求方法

url2 = 'http://127.0.0.1:6666'
peer2 = ServerProxy(url2)
print(peer2.query(filename))

peer1.hello(url2)  # 添加其它节点到peer1的已知节点
print(peer1.query(filename))

peer1.fetch(filename, '123456')  # 下载文件
