#!/usr/bin/env python2

import rpclib
import sys
import bank
from debug import *
from sqlalchemy.orm import class_mapper
import auth_client

def serialize(model):
    cols = [i.key for i in class_mapper(model.__class__).columns]
    return dict((i, getattr(model, i)) for i in cols)
    
class BankRpcServer(rpclib.RpcServer):
    # def rpc_transfer(self, sender, recipient, zoobars):
    #     return bank.transfer(sender, recipient, zoobars)

#exercise 8
    def rpc_transfer(self, sender, recipient, zoobars, token):
        assert (auth_client.check_token(sender, token)), ValueError()
        return bank.transfer(sender, recipient, zoobars)
        
    def rpc_balance(self, username):
        return bank.balance(username)

    def rpc_get_log(self, username):
#        return bank.get_log(username)
        return [serialize(log) for log in bank.get_log(username)]

    def rpc_new_account(self, username):
        return bank.new_account(username)
        
(_, dummy_zookld_fd, sockpath) = sys.argv

s = BankRpcServer()
s.run_sockpath_fork(sockpath)