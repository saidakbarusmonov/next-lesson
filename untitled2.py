command = ''
started = False
while True:
    command = input('''
>>> ''')
    if command == 'start':
        if started:
            print('car has already been started')
        else:
            started = True
            print('car has been running')
    elif command == 'stop':
        if not started:
            print('car has already been stapped')
        else:
            started = False
            print('car stopped')
    elif command == 'quit':
        break
    else:
        print('i didnt understand that')
