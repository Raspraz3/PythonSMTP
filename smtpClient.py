import socket

def smtp_client(port=1025, mailserver='smtp.aol.com'):
    msg = "\r\n My message.\r\n"
    endmsg = "\r\n.\r\n"


    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((mailserver, port))

    recv = clientsocket.recv(1024).decode()
    #print(recv)

    
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    #print(recv1)

    
    clientsocket.send('STARTTLS\r\n'.encode())
    recv2 = clientsocket.recv(1024).decode()
    #print(recv2)

    
    mailFromCommand = 'MAIL FROM: <raspraz2@aol.com>\r\n'
    clientsocket.send(mailFromCommand.encode())
    recv3 = clientsocket.recv(1024).decode()
    #print(recv3)

    
    rcptToCommand = 'RCPT TO: <davon.raspberry3@gmail.com>\r\n'
    clientsocket.send(rcptToCommand.encode())
    recv4 = clientsocket.recv(1024).decode()
    #print(recv4)

    
    dataCommand = 'DATA\r\n'
    clientsocket.send(dataCommand.encode())
    recv5 = clientsocket.recv(1024).decode()
    #print(recv5)

    
    clientsocket.send(msg.encode())

    
    clientsocket.send(endmsg.encode())
    recv6 = clientsocket.recv(1024).decode()
    #print(recv6)

    
    quitCommand = 'QUIT\r\n'
    clientsocket.send(quitCommand.encode())
    recv7 = clientsocket.recv(1024).decode()
    #print(recv7)

    clientsocket.close()

if __name__ == '__main__':
    smtp_client(1025, 'smtp.aol.com')
