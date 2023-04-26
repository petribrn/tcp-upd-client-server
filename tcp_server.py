from socket_handler import ServerSocketHandler
import configs


"""
        server_method

        Handle first message received from client on a socket connection and
        answer it sending another one back.
        Keeps this behavior for every message sent by client.
"""
def server_method():
    print('<-----DEFINE HOST ADDRESS/PORT----->')
    host_port = input(f'Host/IP Port [Default: {configs.default_server_host} {configs.default_server_port}]: ')
    host = host_port.split(' ')[0] if host_port else ''
    port = host_port.split(' ')[1] if host_port else ''

    server_handler = ServerSocketHandler(host, port)
    connection, address = server_handler.connect_server()

    message_counter = 0
    while True:
        data = connection.recv(1024).decode()
        if not data:
            break

        server_handler.show_client_message(data, address)
        connection.send(f'[{message_counter}] OK ::: {data}'.encode())
        message_counter += 1

    connection.close()


if __name__ == '__main__':
    server_method()