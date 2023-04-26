from tcp_socket_handler import TcpClientSocketHandler
import configs

"""
        client_method

        Start interaction with server on a socket connection and
        keeps exchanging messages until 'exit' is provided.
"""


def client_method():
    print('<-----DEFINE HOST ADDRESS/PORT----->')
    host_port = input(f'Host/IP Port [Default: {configs.default_client_host} {configs.default_client_port}]: ')
    if not host_port == '':
        host = host_port.split(' ')[0]
        port = host_port.split(' ')[1]
    else:
        host = configs.default_client_host
        port = configs.default_client_port

    print(host)

    client_handler = TcpClientSocketHandler(host, port)
    client_handler.connect()

    while True:
        msg = input('Message to send...: ')
        if msg.strip().lower() == 'exit':
            break

        server_response = client_handler.send_message(msg)
        client_handler.show_server_response(server_response)

    client_handler.close_socket()


if __name__ == '__main__':
    client_method()
