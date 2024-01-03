import json
import socket
import sys


def login():
    # Create a socket to connect to the server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8888))

    # Get username and password from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python gptclient.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    # Prepare the data as a dictionary
    login_data = {'username': username, 'password': password}

    # Convert the dictionary to a JSON string
    json_data = json.dumps(login_data)

    # Send the JSON data to the server
    client.send(json_data.encode('utf-8'))

    # Receive and print the server's response
    response_data = client.recv(1024).decode('utf-8')
    print(response_data)

    # Close the connection
    client.close()

login()

