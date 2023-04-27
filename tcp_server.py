from handlers.tcp_socket_handler import TcpServerSocketHandler
import general.configs as configs
import general.tools as tools

"""
        server_method

        Handle first message received from client on a socket connection and
        answer it sending another one back.
        Keeps this behavior for every message sent by client.
"""


def start_tcp_server():
    print("<--------------SERVER-------------->")
    print("<-----DEFINE HOST ADDRESS/PORT----->")
    server_info = input(f"Host/IP Port [Default: {configs.default_server_host} {configs.default_server_port}]: ")
    
    host, port = tools.define_host_port(server_info)

    server_handler = TcpServerSocketHandler(host, port)
    connection, address = server_handler.bind_server()

    message_counter = 0
    while True:
        data = connection.recv(1024).decode()

        server_handler.show_client_message(data, address)
        connection.send(f"[{message_counter}] OK ::: {data}".encode())
        message_counter += 1


if __name__ == "__main__":
    start_tcp_server()
