import socket

def raw_http_get(host, port):
	request = "GET / HTTP/1.1\nHost: " + host + "\nUser-Agent:Mozilla 5.0\n\n"
	# request = raw_input(">> ")

	# Create socket & connect
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

	# send our request in the HTTP protocol
	s.send(request)

	response = s.recv(1024)

	while response:
		print response,
		response = s.recv(1024)

	s.close()	

# raw_http_get('www.google.com', 80)
raw_http_get('127.0.0.1', 50000)