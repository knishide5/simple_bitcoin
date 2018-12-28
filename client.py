import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('192.168.100.222', 50030))
my_text = "Hello!"
my_socket.sendall(my_text.encode('utf-8'))
