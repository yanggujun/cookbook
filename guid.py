import uuid
import sys
from tkinter import Tk

def gen_guids(num, fmt):
    guids = ''
    if fmt == 'd':
        for i in range(0, num):
            guid = str(uuid.uuid4())
            guids += guid + '\n'
            print(guid)
    elif fmt == 'hex':
        for i in range(0, num):
            guid = uuid.uuid4().hex
            guids += guid + '\n'
            print(guid)
    # single quoted
    elif fmt == 'sq':
        for i in range(0, num):
            guid = '\'' + str(uuid.uuid4()) + '\''
            guids += guid + '\n'
            print(guid)
    # double quoted
    elif fmt == 'dq':
        for i in range(0, num):
            guid = '"' + str(uuid.uuid4()) + '"'
            guids += guid + '\n'
            print(guid)
    # upper case guid
    elif fmt == 'u':
        for i in range(0, num):
            guid = str(uuid.uuid4()).upper()
            guids += guid + '\n'
            print(guid)
    # upper case hex
    elif fmt ==  'uh':
        for i in range(0, num):
            guid = uuid.uuid4().hex.upper()
            guids += guid + '\n'
            print(guid)
    # upper case single quoted
    elif fmt == 'usq':
        for i in range(0, num):
            guid = '\'' + str(uuid.uuid4()).upper() + '\''
            guids += guid + '\n'
            print(guid)
    # upper case double quoted
    elif fmt == 'udq':
        for i in range(0, num):
            guid = '"' + str(uuid.uuid4()).upper() + '"'
            guids += guid + '\n'
            print(guid)
    return guids

arg_count = len(sys.argv)

if arg_count == 1:
    gen_guids(1, 'd')
elif arg_count == 2:
    id_num = int(sys.argv[1])
    gen_guids(id_num, 'd')
elif arg_count == 3:
    id_num = int(sys.argv[1])
    fmt = sys.argv[2]
    gen_guids(id_num, fmt)
