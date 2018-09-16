import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('Put IP Here', 50000))
m = "HI"
while True:
    try:
        #print(1)
        s.send(m.encode())
        data = s.recv(1024)
        reci = repr(data)
        #print(reci)
        print("The Message Recived is " + rec[2:-1])
        m = input("What Message Would You like to send?: ")
    except:
        s.shutdown(1)
        s.close()
        print("Quiting")
        exit()
    
# socket.gethostbyname_ex(socket.gethostname())[-1]
