#!/usr/bin/env python3
from PyInquirer import prompt
from platform import system
from subprocess import call

questions = [
    dict(type='input', name='ip', message='What is the ip of the machine you are trying to ping?'),
    dict(type='input', name='pings', message='How many times do you want to ping?')
]

def clear():
    command = 'cls' if 'windows' in system().lower() else 'clear'
    call(command)

def ping(address, n=1):
    flag = '-n' if 'windows' in system().lower() else '-c'
    cmd = ["ping", flag, n, address]
    return call(cmd) == 0

def main():
    clear()
    answers = prompt(questions)
    success = ping(answers['ip'], answers['pings'])
    if not success:
        print("Had some issues pinging {}.".format(answers['ip']))


if __name__ == "__main__":
    main()