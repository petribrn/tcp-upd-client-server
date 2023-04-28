# -*- coding: future_fstrings -*-
from handlers.udp_socket_handler import UdpServerSocketHandler
import general.configs as configs
import general.tools as tools


def server_method():
    print("<-----DEFINE HOST ADDRESS/PORT----->")
    server_info = input(f"Host/IP Port [Default: {configs.default_server_host} {configs.default_server_port}]: ")

    host, port = tools.define_host_port(server_info)

    server_handler = UdpServerSocketHandler(host, port)
    server_handler.connect_server()

    message_counter = 0
    while True:
        data, address = server_handler.show_client_message()
        if data == b"exit":
            break

        server_handler.send_message(f"[{message_counter}] OK ::: {data.decode()}", address)
        message_counter += 1

    server_handler.close_socket()


if __name__ == "__main__":
    server_method()