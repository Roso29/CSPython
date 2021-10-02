import argparse
from cspython.ServerLib import Server

def GetArgs():
    parser = argparse.ArgumentParser(description='Handler chat server arguments.')
    parser.add_argument('--username', type=str, default = '', help='If left blank, will be requested by system on startup.')
    parser.add_argument('--port', type=int, default=8888, help='Port to communicate on.')
    parser.add_argument('--hosting',action='store_true', help='If used, host the server on this machine.')
    parser.add_argument('--server_addr', type=str, default='', help='Address of hosting server to connect to.')

    args = parser.parse_args()
    return args

def ConflictingArgs(args):
    print(args)
    doArgsConflict = (not args.hosting) and args.server_addr==''
    return doArgsConflict