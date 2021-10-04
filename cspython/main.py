from cspython.SysLib import System
from cspython.ArgHandler import ConflictingArgs, GetArgs

if __name__ == '__main__':
    args = GetArgs()
    if ConflictingArgs(args):
        print("If not hosting a server, a server address must be connected to.")
        exit()
    chatSystem = System(args.hosting, args.port, args.server_addr, args.username)
    chatSystem.StartChatThreads()