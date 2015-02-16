import socks
import socket
import urllib2

def create_sock_connection(address, timeout=None, source_address=None):
    sock = sock.socksocket()
    sock.connect(address)
    return sock

#To set default socks proxy:
#    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, addr, port(int))

def patch_socket_module():
    socket.socket = socks.socksocket
    socket.create_connection = create_socket_connection

'''import socks
import socket
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "192.168.78.1", 9050)

    # patch the socket module
socket.socket = socks.socksocket
socket.create_connection = create_connection

import urllib2
print urllib2.urlopen('http://am4wuhz3zifexz5u.onion/Library/English/Physics/').'''
