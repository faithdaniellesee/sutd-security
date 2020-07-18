from debug import *
from zoodb import *
import rpclib

sockname = "/authsvc/sock"
#c = rpclib.client_connect(sockname)

def login(username, password):
    data = {}
    data['username'] = username
    data['password'] = password
    c = rpclib.client_connect(sockname)
    return c.call('login', **data)

def register(username, password):
    data = {}
    data['username'] = username
    data['password'] = password
    c = rpclib.client_connect(sockname)
    return c.call('register',**data)

def check_token(username, token):
    data = {}
    data['username'] = username
    data['token'] = token
    c = rpclib.client_connect(sockname)
    return c.call('check_token',**data)