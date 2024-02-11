import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# server.bind(("localhost", 9774))

client_address = ("localhost", 9773)
client_socket.connect(client_address)







msg = input ('msg:- ')
if msg == 'quit':
    client_socket.close()
else:
    print(msg)

# response = input('message: ')
    # client.send(response.encode('utf-8'))
client_socket.sendall(msg.encode('utf-8'))
client_socket.close()

# client.close()
