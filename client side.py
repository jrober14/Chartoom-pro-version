import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('Name of computer to connect', 50000))
m = "HI"
while True:
    print(1)
    s.send(m.encode())
    data = s.recv(1024)
    print('Received', repr(data))
    m = input(": ")
    
    
# socket.gethostbyname_ex(socket.gethostname())[-1]
