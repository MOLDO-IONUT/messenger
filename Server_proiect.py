#server concurent
import socket
import threading

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',1234))
s.listen(5)
print("Server deschis")
def conexiune_Client(conexiune):
    while True:
        nume = conexiune.recv(1024).decode()
        #print(nume)
        for Client in Clienti:
            Client.send(nume.encode())
 
Clienti = []
 
while True:
   client, adresa = s.accept()
   Clienti.append(client)
   print("Bun venit pe server")
   print(adresa)
   
   t= threading.Thread(target=conexiune_Client,args=(client,))
   t.start()
