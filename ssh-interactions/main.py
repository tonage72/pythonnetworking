from paramiko import SSHClient
from paramiko.client import AutoAddPolicy

def main():
    with SSHClient() as client:
        client.set_missing_host_key_policy(AutoAddPolicy())
        client.connect('192.168.0.110', key_filename='/home/david/.ssh/id_ecdsa.pub')
        stdin, stdout, stderr = client.exec_command('ls /')
        output = stdout.read()
        print(output.decode())

if __name__ == '__main__':
    main()