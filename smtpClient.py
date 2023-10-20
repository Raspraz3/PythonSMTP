import socket

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientsocket.connect((mailserver, port))  # Use mailserver and port from the function arguments
    except ConnectionRefusedError:
        print("Connection NOT established")
        return
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return

    recv = clientsocket.recv(1024).decode()

    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    print(recv1)

    if recv1[:3] != '250':
        print('250 reply not received from the server.')

    # Send MAIL FROM command and handle server response.
    mailFromCommand = 'MAIL FROM: <raspraz2@gmail.com>\r\n'
    clientsocket.send(mailFromCommand.encode())
    recv2 = clientsocket.recv(1024).decode()
    print(recv2)

    # Send RCPT TO command and handle server response.
    rcptToCommand = 'RCPT TO: <davon.raspberry3@example.com>\r\n'
    clientsocket.send(rcptToCommand.encode())
    recv3 = clientsocket.recv(1024).decode()
    print(recv3)

    # Send DATA command and handle server response.
    dataCommand = 'DATA\r\n'
    clientsocket.send(dataCommand.encode())
    recv4 = clientsocket.recv(1024).decode()
    print(recv4)

    # Send message data.
    clientsocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientsocket.send(endmsg.encode())
    recv5 = clientsocket.recv(1024).decode()
    print(recv5)

    # Send QUIT command and handle server response.
    quitCommand = 'QUIT\r\n'
    clientsocket.send(quitCommand.encode())
    recv6 = clientsocket.recv(1024).decode()
    print(recv6)

    clientsocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
