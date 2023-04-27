import general.configs as configs

def define_host_port(server_info):
    """
    define_host_port 

    Defines host and port to be used by client/server connection based on
    user's input or default parameters.

    Args:
        server_info (str): user's input for server_info host/port

    Returns:
        tuple: (host:str, port: int)
    """    
    if server_info:
        server_info = server_info.split()
        host = server_info[0]
        port = int(server_info[1])
    else: 
        host = configs.default_client_host
        port = configs.default_client_port

    return host, port