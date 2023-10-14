import socket
import ssl
import smtplib

# Define the sender and recipient email address
sender_email = "raspraz2@aol.com"
recipient_email = "Davon.raspberry3@gmail.com"


def smtp_client(port, mailserver):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Define the email message
    subject = "Subject: Your Subject Here\r\n"
    message = "Your message goes here."

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope



    # Fill in start
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((mailserver, port))

    # Recieve the server's response
    recv = clientsocket.recv(1024).decode()
    #print(recv)
    # Fill end

    if recv[:3] != '220':
       #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientsocket.send(heloCommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    print(recv1)
    #
    if recv1[:3] != '250':
       #print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    sender_email = "raspraz2@aol.com"
    recipient_email = "Davon.raspberry3@gmail.com"
    app_password = 'bspu rgte ttfu hqwr'

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP("smtp.aol.com", 1025) as server:
            server.ehlo()  # Identify yourself to the SMTP server
            server.starttls(context=context)  # Upgrade the connection to secure (TLS)

            # Replace 'your_email@gmail.com' and 'your_password' with your Gmail credentials
            server.login(Raspraz2@aol.com, BBBBBBBDAAAAAA1)

            mailFromCommand = f"MAIL FROM: {Raspraz2@aol.com}\r\n"

            # Get the server response
            response = server.sendmail(sender_email, recipient_email, mailFromCommand)
            #print("Email sent successfully")
            #print(f"Server Response:{response}")

    except smtplib.SMTPException as e:
        # Handle SMTP exceptions, if any
        #print(f"SMTP Exception: {e}")
    except Exception as e:
        #print(f"An error occurred: {e}")


    # Send DATA command and handle server response.
    # Fill in start
    # Send the DATA command
    data_command = "DATA\r\n"
    clientsocket.send(data_command.encode())
    recv_data = clientsocket.recv(1024).decode()
    #print(recv_data)
    # Fill in end

    # End the email message
    end_message = "\r\n.\r\n"
    clientsocket.send(end_message.encode())
    recv_data = clientsocket.recv(1024).decode()
    #print(recv_data)

    # Send the QUIT command
    quit_command = "QUIT\r\n"
    clientsocket.send(quit_command.encode())
    recv_data = clientsocket.recv(1024).decode()
    #print(recv_data)

    # Close the socket
    clientsocket.close()
    # Fill in end

    clientsocket.close()


if __name__ == '__main__':
    # Define the SMTP server's hostname and port
    smtp_server = "smtp.aol.com"
    smtp_port = 1025

    smtp_client(smtp_port, smtp_server)