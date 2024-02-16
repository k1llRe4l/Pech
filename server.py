import socket

import socket, cv2, pickle, struct, imutils


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(f'HOST IP: {host_ip}')
