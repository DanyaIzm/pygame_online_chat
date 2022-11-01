import socket
import time
import json


def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)
    server_socket.setblocking(False)

    client_sockets = []

    try:
        while True:
            try:
                # try to get new incoming connection
                connection, address = server_socket.accept()

                server_socket.setblocking(True)
                username = connection.recv(1024).decode()
                server_socket.setblocking(False)

                connection.setblocking(False)

                client_sockets.append([username, connection])
                print(f'[EVENT] Connected: {username}')

                connected_message = {
                            'method': 'CONNECT',
                            'username': username,
                        }

                for receiver_user in client_sockets:
                    # send "user diconnected" message to all users
                    receiver_user[1].sendall(json.dumps(connected_message).encode())
            except:
                pass

            for user in client_sockets:
                # for every client check if they send something
                try:
                    cur_socket = user[1]
                    data = cur_socket.recv(1024)
                    data = json.loads(data.decode())
                    if not data or data.get('method') == 'QUIT':
                        # if client is disconnected or wants to disconnect - close socket and remove him from sockets
                        cur_socket.close()
                        print(f'[EVENT] Disconnected: {user[0]}')
                        client_sockets.remove(user)

                        disconnected_message = {
                            'method': 'QUIT',
                            'username': user[0],
                        }

                        for receiver_user in client_sockets:
                            # send "user diconnected" message to all users
                            receiver_user[1].sendall(json.dumps(disconnected_message).encode())
                    else:
                        for receiver_user in client_sockets:
                            # send message to all users
                            receiver_user[1].sendall(json.dumps(data).encode())
                except:
                    pass

            time.sleep(0.2)

    except KeyboardInterrupt:
        print('[EVENT] Keyboard interrupt')
    finally:
        for cur_socket in client_sockets:
            cur_socket.close()
        server_socket.close()
        print('[EXIT] Successfully exited')


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 25560
    
    run_server(HOST, PORT)
