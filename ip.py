import socket
hostn=socket.gethostname()
IPad= socket.gethostbyname(hostn)
print("IP ADDRESS IS:"+ IPad)
