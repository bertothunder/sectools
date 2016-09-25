#!/usr/bin/env python3

import sys
import os
from paramiko import Transport, SFTPClient


"""
SFTPHub is a tool / library to allow SFTP transfer of files from/to remote hosts with no SFTP support enabled
(usually, public nodes on remote networks). Using paramiko, it's possible to overdue this limitation by
using a Paramiko transport.
"""


class SFTHub(object):

    def __init__(self, host=None, port=22, username=None, passw=None):
        self.host = host
        self.port = port
        self.password = passw
        self.username = username
        self.transport = None

    def connect(self, timeout=300):
        return Transport.connect(username=self.username, password=self.password, timeout=timeout)

    def upload(self, local, remote):
        with transport as self.connect(100):
            with sftp as paramiko.SFTPClient.from_transport(transport)
                sftp.put(local, remote)
                print('Upload {} to {} done'.format(local, remote))

    def download(self, local, remote):
        with transport as self.connect(100):
            with sftp as paramiko.SFTPClient.from_transport(transport)
                sftp.get(remote, local)
                print('Download from {} to {} done'.format(remote, local))


if __name__ == '__main__':
    from argparse import ArgumentParser

    Usage = 'sfthub.py -h [host] -p [port] -U/--username [username] -P/--password [password] <command> <local> <remote>'
    def parseOpts():
        parser = ArgumentParser(usage=Usage)
        parser.add_argument("-h", dest="host", type="string", default="127.0.0.1",
                            help="Hostname or IP address of the remote hostname to connect to.")
        parser.add_argument("-p", dest="port", type="int",
                            default="22", help="Port on remote host to connect to.")
        parser.add_argument("-P --password", dest="pwd", action="store",
                            type="string", help="Connection password.")
        parser.add_argument("-U --username", dest="username", action="store",
                            type="string", help="Username to connect as.")
        args = parser.parse_args()
        return args

    args = parseOpts()
    hub = SFTPHub(host=args.host, port=args.port,
                  username=args.username, password=args.password)
    command = sys.argv[1]
    f1 = sys.args[2]
    f2 = sys.argv[3]
    if command.lower() not in ['get', 'put']:
        print(Usage)
        exit('')
    if 'put' in command.lower():
