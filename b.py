from socket import *

#创建udp套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)

#绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
binAddr = ("",7788) #ip地址和端口号，ip地址一般不用写，表示本机的任何一个ip
udpSocket.bind(binAddr)

#等待接收对方发送的数据
recvData = udpSocket.recvfrom(1024) #1024表示本次接收的最大字节数

#显示接收到的数据
print(recvData)

#关闭套接字
udpSocket.close()