#deals with shit
from __future__ import print_function
from Custom import *
import Pyro4
import Pyro4.naming
import Pyro4.core
import socket
import time
import select
import sys

def main():
    # sys.excepthook = Pyro4.util.excepthook
    serverPort=50611
    Pyro4.config.SERIALIZERS_ACCEPTED = {'json','marshal','serpent','pickle'}
    server1=Server(serverPort,False)
    store=Store()
    Pyro4.Daemon.serveSimple(
    {
        server1: "server",
        Item: "item",
        Order:"order",
        store:'Store'
    },
    ns=False,host='localhost',port=serverPort)


if __name__=="__main__":
    main()
