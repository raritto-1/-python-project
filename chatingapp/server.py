import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 9773))
server_socket.listen()
print('server is listening to 9773 ')



while True :
    
    client_socket, client_address = server_socket.accept()
    print(f'accept from {client_address}')
    
    msg = client_socket.recv(1024).decode('utf-8')
    if msg == 'quit':
        client_socket.close()
    else:
        print(msg)

        # response = input('message: ')
        # client_socket.send(response.encode('utf-8'))
    client_socket.close()

# client_socket.close()
