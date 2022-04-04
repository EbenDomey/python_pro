from re import S


start = True

while True:
    commands = input('>> ').lower()

    if commands == 'start':
        if start:
            print('Car has started')
            start = False
        elif not start:
            print('Car has already started')
    elif commands == 'stop':
        if not start:
            print('Car has stopped')
            start = True
        elif start:
            print('Car has already stopped')
    else:
        print('Err: command not found')
