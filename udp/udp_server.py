from udp_socket_handler import UdpServerSocketHandler
import configs


def server_method():
    print('<-----DEFINE HOST ADDRESS/PORT----->')
    host_port = input(f'Host/IP Port [Default: {configs.default_server_host} {configs.default_server_port}]: ')

    host = host_port.split(' ')[0] if host_port else ''
    port = host_port.split(' ')[1] if host_port else 0

    server_handler = UdpServerSocketHandler(host, port)
    server_handler.connect_server()

    message_counter = 0
    while True:
        data, address = server_handler.show_client_message()
        if data == b'exit':
            break

        server_handler.send_message(f'[{message_counter}] OK ::: {data}', address)
        message_counter += 1

    server_handler.close_socket()
