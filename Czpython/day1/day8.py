#import sys  #模块
 #print(sys.path)  #打印环境变量
# #print(sys.argv) #打印文件的相对目录
#import os
#os.system("dir")#打印文件所在目录的地址
#cmd_res = os.popen("dir")#将文件所在目录的地址存下来
#print(cmd_res.read())#打印文件所在目录的地址
#os.mkdir("new_dir")#创建一个新的目录
msg = "我爱北京天安门"
print(msg)
print(msg.encode("utf-8"))#字符串编码成二进制的形式
print(msg.encode("utf-8").decode("utf-8"))#字符串编码成二进制的形式又解码为字符串