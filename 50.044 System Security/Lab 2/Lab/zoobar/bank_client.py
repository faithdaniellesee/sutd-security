from debug import *
from zoodb import *
import rpclib

sockname = "/banksvc/sock"
c = rpclib.client_connect(sockname)

def transfer(sender, recipient, zoobars, token):
    data = {}
    data['sender'] = sender
    data['recipient'] = recipient
    data['zoobars'] = zoobars
    data['token'] = token
    return c.call('transfer', **data)

def balance(username):
    data = {}
    data['username'] = username
    return c.call('balance',**data)

def get_log(username):
    data = {}
    data['username'] = username
    return c.call('get_log',**data)
    
def new_account(username):
    data = {}
    data['username'] = username
    return c.call('new_account',**data)