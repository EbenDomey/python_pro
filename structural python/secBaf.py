start = True # Start the game with a boolean value true


while True: # While the game is running
    command = input('>> ').lower()
    if command == 'start':
        if start: # If game is running and user just typed in start
            print('Car has started')
            start = False # Set start to false so it doesn't run again
        elif not start and command == 'start': # If game is running and user typed in start again
            print('Car has already started')
    elif command == 'stop':
        if not start: # If game is running and user typed in stop
            print('Car has stopped')
            start = True # Set start to true so it doesn't run again in this block
        elif start and command == 'stop': # If game is running and user typed in stop again
            print('Car has already stopped')
    else:
        print('Err: command not found')
        break
