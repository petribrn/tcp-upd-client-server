from handlers.tcp_socket_handler import TcpClientSocketHandler
import general.configs as configs
import general.tools as tools

"""
        client_method

        Start interaction with server on a socket connection and
        keeps exchanging messages until 'exit' is provided.
"""


def start_tcp_client():
    print("<--------------CLIENT-------------->")
    print("<-----DEFINE HOST ADDRESS/PORT----->")
    server_info = input("Host/IP Port [Default: {} {}]: ".format(configs.default_client_host, configs.default_client_port))
    
    host, port = tools.define_host_port(server_info)

    client_handler = TcpClientSocketHandler(host, port)
    client_handler.connect()

    while True:
        msg = input("Message to send...: ")
        

        server_response = client_handler.send_message(msg)
        if 'EXIT OK' in server_response:
            break
        client_handler.show_server_response(server_response)

    client_handler.close_socket()


if __name__ == "__main__":
    start_tcp_client()
