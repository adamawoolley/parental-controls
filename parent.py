#! /usr/bin/python3.7

from sys import argv
from json import loads, dumps

use = ''''''

def add(user, program):
    with open('/etc/parental-controls/settings.txt', 'r+') as file:
        settings = loads(file.read())
        if user in settings:
                settings[user].append(program)
        else:
            settings[user] = [program]
        file.seek(0)
        file.write(dumps(settings))

def remove(user, program=False):
    with open('/etc/parental-controls/settings.txt', 'r+') as file:
        settings = loads(file.read())
        if not program:
            settings.pop(user, None)
        else:
            try:
                del settings[user][settings[user].index(program)]
            except:
                print('That program or user is not in the settings file')
        file.seek(0)
        file.write(dumps(settings))
        file.truncate()

def change_settings():
    if '-a' in argv:
        add(argv[argv.index('-a') + 1], argv[argv.index('-a') + 2])
    elif '--add' in argv:
        add(argv[argv.index('--add') + 1], argv[argv.index('--add') + 2])
    elif '-r' in argv:
        user = argv[argv.index('-r') + 1]
        try:
            program = argv[argv.index('-r') + 2]
        except:
            program = False
        remove(user, program)
    elif '--remove' in argv:
        user = argv[argv.index('--remove') + 1]
        try:
            program = argv[argv.index('--remove') + 2]
        except:
            program = False
        remove(user, program)
    else:
        print(use)

if __name__ == '__main__':
    change_settings()
