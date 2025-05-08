import socket 

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"  

LOCAL_IPV4 = get_local_ip()

FAST_API_URL = f"http://{LOCAL_IPV4}:2814"
DJANGO_URL = f"http://{LOCAL_IPV4}:1974"