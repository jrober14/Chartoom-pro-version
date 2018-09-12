import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 50000))
s.listen(1)
conn, addr = s.accept()
print(1)
print(conn)
print(2)
print(addr)
print(3)
while True:
    data = conn.recv(1024)


    print(data)
    data = input(": ")
    conn.send(data.encode())

conn.close()

# socket.gethostbyname_ex(socket.gethostname())[-1]
