import json
import socket
import sqlite3
import threading


# Function to check if a given username and password are valid
def is_valid_login(username, password):
    conn = sqlite3.connect('a.db')
    cursor = conn.cursor()

    # Check if the provided username and password match any entry in the database
    cursor.execute('SELECT * FROM login WHERE username = ? AND password = ?', (username, password))
    result = cursor.fetchone()

    conn.close()

    return result is not None

# Function to handle client connections
def handle_client(client_socket):
    request_data = client_socket.recv(1024).decode('utf-8')
    try:
        data = json.loads(request_data)
        if 'username' not in data or 'password' not in data:
            response = {'error': 'Invalid request'}
        else:
            username = data['username']
            password = data['password']

            if is_valid_login(username, password):
                response = {'message': 'Login successful'}
            else:
                response = {'error': 'Invalid username or password'}
    except json.JSONDecodeError:
        response = {'error': 'Invalid JSON format'}

    client_socket.send(json.dumps(response).encode('utf-8'))
    client_socket.close()

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)

print('[*] Server listening on 127.0.0.1:8888')

while True:
    client, addr = server.accept()
    print('[*] Accepted connection from {}:{}'.format(addr[0], addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
