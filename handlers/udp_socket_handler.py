import general.configs as configs
import socket

class UdpClientSocketHandler:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

        # STREAM constant for TCP connections
        self.socket_instance: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self):
        """
        connect 

        Init connection to server running on 'host' address at 'port'.
        """
        self.socket_instance.connect((self.host, self.port))

    def send_message(self, msg: str):
        """
        send_message _summary_

        Sends message input by user and waits for server response.

        Args:
            msg (str): user message to send directly to server

        Returns:
            str: server's response to sent message
        """
        self.socket_instance.sendto(msg, (self.host, self.port))
        data, address = self.socket_instance.recvfrom(1024)

        return data
    
    def show_server_response(self, response: str):
        """
        show_server_response 

        Print to stdout the server's response to client previous sent message

        Args:
            response (str): server's response
        """        
        print('Server reply......: {}'.format(response.decode()))

    def close_socket(self):
        """
        close_socket

        Closes client TCP socket
        """        
        self.socket_instance.close()

class UdpServerSocketHandler:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        # DGRAM constant for UDP transmission
        self.socket_instance: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("<<< Socket created >>>")

    def connect_server(self):
        """
        connect_server

        Binds server running on 'host' at 'port', listening to 2 maximum clients
        simultaneously. Prints address of client.
        """
        self.socket_instance.bind((self.host, self.port))
        print("<<< Socket bind complete >>>")

    def show_client_message(self):
        """
        show_client_message

        Shows message received from client

        Returns:
            tuple: socket object, address (tuple of host/port)
        """
        data, address = self.socket_instance.recvfrom(1024)
        if data != b"exit":
            print("Message [{}:{}]: {}".format(address[0], address[1], data.decode()))

        return data, address

    def send_message(self, msg: str, address):
        """
        send_message _summary_

        Sends message input by user and waits for server response.

        Args:
            msg (str): user message to send directly to server
            address (_type_): socket host and port
        """
        self.socket_instance.sendto(msg.encode(), address)

    def close_socket(self):
        """
        close_socket

        Closes server UDP socket
        """
        self.socket_instance.close()
