import socket
#q = "hi"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 50000))
s.listen(1)
conn, addr = s.accept()
#print(1)
#print(conn)
#print(2)
#print(addr)
#print(3)
while True:
    try:
        data = conn.recv(1024)
        rec = repr(data)
        #print(rec)
        #print(1)
        #print(data)
        #print(2)
        print("The Message Recived is " + rec[2:-1])
        #print(3)
        data = input("What Message Would You like to send?: ")
        conn.send(data.encode())
    except:
        conn.shutdown(1)
        conn.close()
        print("There was an error!")
        exit()

# socket.gethostbyname_ex(socket.gethostname())[-1]
