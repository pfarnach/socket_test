import socket

HOST = '0.0.0.0'
PORT = 50000

def server():
	'''Super simple network server'''

	print "Starting network server on:", socket.gethostname()

	# read at most this many bytes from the socket
	bufferSize = 4 * 1024

	# create server socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((HOST, PORT))

	# Connection backlog
	s.listen(5)

	# wait for and accept incoming connections, read the data, generate
	# and return a response, then go back to waiting
	while True:
		client, address = s.accept()

		data = client.recv(bufferSize)
		print "received from:", client, address
		print data

		send_output(client, data)
		client.close()

def send_output(client_socket, in_data):
	# client_socket.send('You sent %d' % (len(in_data),))
	client_socket.send('HTTP/1.1 200 OK\r\n')
	client_socket.send('Content-type: text/html\r\n\r\n')
	client_socket.send('<h1>Hey there!</h1><p style="color:blue">This is Pat\'s server</p>')


server()