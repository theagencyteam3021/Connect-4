import socket
import math

ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ROBOT_IP = '10.30.21.100'
ROBOT_PORT = 30002

DEBUG = True

ur.connect((ROBOT_IP, ROBOT_PORT))
if DEBUG:
    print(f'Connected to UR robot at {ROBOT_IP}:{ROBOT_PORT}.')

def send_cmd(cmd):
    '''
    Make sure robot is in remote mode before running. If it ever changes mode, you need to reconnect.
    '''
    if DEBUG:
        print(f'Executing `{cmd}`')
    ur.send(f'{cmd}\n'.encode())
    ur.recv(1024)

def movej_degrees(target, a=1.0, v=0.1):
    '''
    target position is in degrees. [base, shoulder, elbow, wrist 1, wrist 2, wrist 3] 
    acceleration is in radians/sec^2. velocity is in radians/sec
    '''
    radians = [0 for i in target]
    for i, degs in enumerate(target):
        radians[i] = math.radians(degs)
    send_cmd(f'movej({radians}, a={a}, v={v})')

def sock_connect():
    '''
    This runs by default when this module is imported. Run again if the connection drops (like if ur gets put in local mode)
    '''
    ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ur.connect((ROBOT_IP, ROBOT_PORT))

if __name__ == '__main__':
    s = input()
    while s.lower() != 'q' and s.lower() != 'quit':
        send_cmd(s)
        s = input()