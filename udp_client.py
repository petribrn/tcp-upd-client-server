from handlers.udp_socket_handler import UdpClientSocketHandler
import general.configs as configs
import general.tools as tools

"""
        client_method

        Start interaction with server by socket and
        keeps exchanging messages until 'exit' is provided.
"""


def client_method():
    print("<-----DEFINE HOST ADDRESS/PORT----->")
    server_info = input("Host/IP Port [Default: {} {}]: ".format(configs.default_client_host, configs.default_client_port))
    
    host, port = tools.define_host_port(server_info)

    client_handler = UdpClientSocketHandler(host, port)

    while True:
        msg = input("Message to send...: ")
        if msg.strip().lower() == "exit":
            break

        server_response = client_handler.send_message(msg.encode())
        client_handler.show_server_response(server_response)

    client_handler.close_socket()


if __name__ == "__main__":
    client_method()
