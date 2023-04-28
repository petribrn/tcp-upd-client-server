# -*- coding: future_fstrings -*-
import socket

class TcpClientSocketHandler:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

        # STREAM constant for TCP connections
        self.socket_instance: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        self.socket_instance.send(msg.encode())
        response = self.socket_instance.recv(1024).decode()

        return response
    
    def show_server_response(self, response: str):
        """
        show_server_response 

        Print to stdout the server's response to client previous sent message

        Args:
            response (str): server's response
        """        
        print(f"Server reply......: {response}")

    def close_socket(self):
        """
        close_socket

        Closes client TCP socket
        """        
        self.socket_instance.close()


class TcpServerSocketHandler:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

        # STREAM constant for TCP connections
        self.socket_instance: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("<<< Socket created >>>")
    
    def bind_server(self):
        """
        connect_server

        Binds server running on 'host' at 'port', listening to 2 maximum clients
        simultaneously. Prints address of client connected.

        Returns:
            tuple: socket connection object, address (tuple of host/port)
        """        
        self.socket_instance.bind((self.host, self.port))
        print("<<< Socket bind complete >>>")
        self.socket_instance.listen(2)
        
        connection, address = self.socket_instance.accept()
        print(f'Connected to......: {address[0]}:{address[1]}')

        return connection, address

    def show_client_message(self, data: str, address):
        """
        show_client_message

        Shows message received from client

        Args:
            data (str): data payload received 
            address (_type_): client address tuple (host/port)
        """
        print(f"Message [{address[0]}:{address[1]}]: {data}")

    def close_socket(self):
        """
        close_socket

        Closes server TCP socket
        """
        self.socket_instance.close()
