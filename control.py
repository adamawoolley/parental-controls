from subprocess import call, check_output
from json import loads

def import_settings():
    with open('settings.txt', 'r') as file:
        return loads(file.read())

def control():
    while True:
        checks = import_settings()
        for user in checks:
            for line in check_output(f'ps -u {user}', shell=True).decode('utf-8').split('\n')[1:-1]:
                if line.split()[3] in checks[user]:
                    call(f'kill {line.split()[0]}', shell=True)

if __name__ == '__main__':
    control()
