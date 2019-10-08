#监测端口是否正常
import socket


while True:
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect(('172.20.66.43',8066))
        #print("server port connect OK! ")
    except Exception:
        print("server port not connect!")
        sk.close()
