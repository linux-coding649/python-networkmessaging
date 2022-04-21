import socket

from time import sleep

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
serversocket.bind(("0.0.0.0", 2022))
serversocket.listen(5)

while True:
    conn, addr = serversocket.accept()
    strsend1 = "Welcome to this Message Portal!\n"
    conn.send(strsend1.encode())
    strsend2 = "Be careful what you send, because this socket is unencrypted.\n"
    conn.send(strsend2.encode())
    strsend3 = "(One Line) Message: "
    conn.send(strsend3.encode())
    mssge = conn.recv(1024).decode()
    mssge = mssge.strip("\n")
    straddr = str(addr)
    mfile = open('messages.in.py.txt', 'a')
    mfile.write(straddr+",  "+mssge+"\n")
    mfile.close()
    strsend5 = "Message Sent.\n"
    conn.send(strsend5.encode())
    conn.close()


