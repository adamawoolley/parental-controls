from subprocess import call

filename = '/etc/systemd/system/parental-controls.service'
file_contents = '''
Description=A program that enables parental controls

Wants=network.target
After=syslog.target network-online.target

[Service]
Type=simple
ExecStart=python3.7 /etc/parental-controls/control.py
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
'''
with open(filename, 'w+') as file:
    file.seek(0)
    file.write(file_contents)
call(['systemctl', 'daemon-reload'])
call(['systemctl', 'enable', 'parental-controls'])
call(['systemctl', 'start', 'parental-controls'])
call(['mkdir', '/etc/parental-controls'])
call(['mv', 'control.py', '/etc/parental-controls/control.py'])
call(['mv', 'settings.txt', '/etc/parental-controls/settings.txt'])
call(['mv', 'parent.py', '/usr/bin/parent.py'])
call(['chmod', '+x', '/usr/bin/parent.py'])
