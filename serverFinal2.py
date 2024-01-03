import json
import socket
import sqlite3


def verify_user(data):
    conn = sqlite3.connect('a.db')
    cursor = conn.cursor()

    # Retrieve username and password from received JSON data
    login_data = json.loads(data)
    username = login_data.get('username')
    password = login_data.get('password')

    # Query the database for the given username and password
    cursor.execute("SELECT * FROM login WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return "Login successful! Welcome, {}".format(username)
    else:
        return "Invalid username or password"

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8888))
    server.listen(5)

    print("Server is listening...")

    while True:
        client, address = server.accept()
        print(f"Connection from {address} has been established!")

        # Receive data from the client
        data = client.recv(1024).decode('utf-8')

        if data:
            # Verify the user
            result = verify_user(data)

            # Send the verification result back to the client
            client.send(result.encode('utf-8'))

        client.close()

if __name__ == "__main__":
    start_server()
