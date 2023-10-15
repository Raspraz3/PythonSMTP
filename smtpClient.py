import socket
def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    #Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    server_hostname = "smtp.gmail.com"
    server_port = 1025
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print("Connection to mail server established")

    try:
        clientsocket.connect((server_hostname, server_port))
        #print("Connected to the mail server")
    except ConnectionRefusedError:
    #print("Connection NOT established")
    except Exception as e:
        #print(f"An error occurred: {str(e)}")
        return
    recv = clientsocket.recv(1024).decode()
    # Fill in end

    #print(recv)="You can use these print statement to validate return codes from the server."
    if recv[:3] != '220':
    #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    #print(recv1)
    if recv1[:3] != '250':
    #print('250 reply not received from the server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: <raspraz2@gmail.com>\r\n'
    clientsocket.send(mailFromCommand.encode())
    recv2 = clientsocket.recv(1024).decode()
    #print(recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO: <davon.raspberry3@example.com>\r\n'
    clientsocket.send(rcptToCommand.encode())
    recv3 = clientsocket.recv(1024).decode()
    #print(recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientsocket.send(dataCommand.encode())
    recv4 = clientsocket.recv(1024).decode()
    #print(recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    clientsocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientsocket.send(endmsg.encode())
    recv5 = clientsocket.recv(1024).decode()
    #print(recv5)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientsocket.send(quitCommand.encode())
    recv6 = clientsocket.recv(1024).decode()
    #print(recv6)
    # Fill in end

    clientsocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')