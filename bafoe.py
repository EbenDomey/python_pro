start = True
stop = True

while True:
    command = input('>> ').lower()
    if command == 'start':
        if start:
            print('Car has started')
            start = False
        elif not start and command == 'start':
            print('Car has already started')
    elif command == 'stop':
        if stop:
            print('Car has stopped')
            stop = False
        elif not stop and command == 'stop':
            print('Car has already stopped')
    else:
        print('Err: command not found')
        break