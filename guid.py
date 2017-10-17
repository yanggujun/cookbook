import uuid
import sys

arg_count = len(sys.argv)

if arg_count == 1:
    print(str(uuid.uuid4()))
elif arg_count == 2:
    id_num = int(sys.argv[1])
    if id_num > 0:
        for i in range(0, id_num):
            print(str(uuid.uuid4()))
elif arg_count == 3:
    id_num = int(sys.argv[1])
    fmt = sys.argv[2]
    if fmt == 'hex':
        for i in range(0, id_num):
            print(uuid.uuid4().hex)
    # single quoted
    elif fmt == 'sq':
        for i in range(0, id_num):
            print('\'' + str(uuid.uuid4()) + '\'')
    # double quoted
    elif fmt == 'dq':
        for i in range(0, id_num):
            print('"' + str(uuid.uuid4()) + '"')
    elif fmt == 'u':
        for i in range(0, id_num):
            print(str(uuid.uuid4()).upper())
    # upper case hex
    elif fmt ==  'uh':
        for i in range(0, id_num):
            print(uuid.uuid4().hex.upper())
    # upper case single quoted
    elif fmt == 'usq':
        for i in range(0, id_num):
            print('\'' + str(uuid.uuid4()).upper() + '\'')
    # upper case double quoted
    elif fmt == 'udq':
        for i in range(0, id_num):
            print('"' + str(uuid.uuid4()).upper() + '"')

