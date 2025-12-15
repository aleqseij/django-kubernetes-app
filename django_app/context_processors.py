import socket
import os

def get_hostname():
    return socket.gethostname()

def pod_info_context(request):
    return {
        'pod_hostname': get_hostname(),
        'pod_ip': os.getenv('POD_IP', '127.0.0.1'),
    }
