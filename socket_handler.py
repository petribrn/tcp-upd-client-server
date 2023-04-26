import socket
import configs


class ClientSocketHandler:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.socket_instance : socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    @property
    def socket_instance(self):
        return self.socket_instance

    @property
    def host(self):
        return self.host

    @property
    def port(self):
        return self.port
    
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
        print(f'Server reply......: {response}')

    def close_connection(self):
        """
        close_connection 

        Closes client socket connection to server
        """        
        self.socket_instance.close()

class ServerSocketHandler:
    def __init__(self, host: str, port: int) -> None:
        self.host = configs.default_server_host if not host else host
        self.port = configs.default_server_port if not port else port
        self.socket_instance : socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print('<<< Socket created >>>')

    @property
    def instance(self):
        return self.socket_instance

    @property
    def host(self):
        return self.host

    @property
    def port(self):
        return self.port
    
    def connect_server(self):
        """
        connect_server

        Binds server running on 'host' at 'port', listenning to 2 maximum clients
        simultaneously. Prints address of client connected.

        Returns:
            tuple: socket connection object, address (tuple of host/ip)
        """        
        self.socket_instance.bind((self.host, self.port))
        print('<<< Socket bind complete >>>')
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
            address (_type_): client address tuple (host/ip)
        """
        print(f'Message [{address[0]}:{address[1]}]: {data}')


      