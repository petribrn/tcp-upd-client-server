class UdpServerSocketHandler:
    def __init__(self, host: str, port: int) -> None:
        self.host = configs.default_server_host if not host else host
        self.port = configs.default_server_port if not port else port

        # DGRAM constant for TCP connections
        self.socket_instance: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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

        Binds server running on 'host' at 'port', listening to 2 maximum clients
        simultaneously. Prints address of client.
        """
        self.socket_instance.bind((self.host, self.port))
        print('<<< Socket bind complete >>>')
        self.socket_instance.listen(2)

    def show_client_message(self):
        """
        show_client_message

        Shows message received from client

        Returns:
            tuple: socket object, address (tuple of host/port)
        """
        data, address = self.socket_instance.recvfrom(1024)
        if data != b'exit':
            print(f'Message [{address[0]}:{address[1]}]: {data}')

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
