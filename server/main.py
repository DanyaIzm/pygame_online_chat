import socket
import time
import json


def get_jsonified_message(message: bytes):
    try:
        return json.loads(message.decode())
    except:
        return None


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

                user_alredy_exists = False
                for user in client_sockets:
                    if user[0] == username:
                        user_alredy_exists = True
                        break
                
                if user_alredy_exists:
                    # if user tries to connect under already used username, we close connection and pass the cycle
                    cant_connect_message = {
                        'method': 'MESSAGE',
                        'username': None,
                        'message': 'Вы не можете присоединиться к серверу с таким именем'
                    }
                    connection.sendall(json.dumps(cant_connect_message).encode())
                    connection.close()
                    continue

                client_sockets.append([username, connection])

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
                    data = get_jsonified_message(data)
                    if not data or data.get('method') == 'QUIT':
                        # if client is disconnected or wants to disconnect - close socket and remove him from sockets
                        client_sockets.remove(user)
                        print(f'[EVENT] Disconnected: {user[0]}')
                        cur_socket.close()

                        disconnected_message = {
                            'method': 'QUIT',
                            'username': user[0],
                        }

                        for receiver_user in client_sockets:
                            # send "user diconnected" message to all users
                            receiver_user[1].sendall(json.dumps(disconnected_message).encode())
                    elif data.get('method') == 'MESSAGE':
                        for receiver_user in client_sockets:
                            # send message to all users
                            receiver_user[1].sendall(json.dumps(data).encode())
                    elif data.get('method') == 'USERS':
                        users_message = {
                            'method': 'USERS',
                            'username': user[0],
                            'message': [u[0] for u in client_sockets]
                        }
                        cur_socket.sendall(json.dumps(users_message).encode())
                except:
                    pass

            time.sleep(0.2)

    except KeyboardInterrupt:
        print('[EVENT] Keyboard interrupt')
    finally:
        for cur_socket in client_sockets:
            cur_socket[1].close()
        server_socket.close()
        print('[EXIT] Successfully exited')


if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 25560
    
    run_server(HOST, PORT)
