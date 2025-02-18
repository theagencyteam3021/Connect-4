import socket
import math

class URSocket:
    def __init__(self, robot_ip = '10.30.21.100', robot_port = 30002, debug = False):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ROBOT_IP = robot_ip
        self.ROBOT_PORT = robot_port
        self.DEBUG = debug 

    def sock_connect(self):
        '''
        This runs by default when this module is imported. Run again if the connection drops (like if ur gets put in local mode)
        '''
        self.sock.connect((self.ROBOT_IP, self.ROBOT_PORT))
        if self.DEBUG:
            print(f'Connected to UR robot at {self.ROBOT_IP}:{self.ROBOT_PORT}.')

    def send_cmd(self, cmd):
        '''
        Make sure robot is in remote mode before running. If it ever changes mode, you need to reconnect.
        '''
        if self.DEBUG:
            print(f'Executing `{cmd}`')
        self.sock.send(f'{cmd}\n'.encode())
        self.sock.recv(1024)

    def movej_degrees(self, target, a=1.0, v=0.1):
        '''
        target position is in degrees. [base, shoulder, elbow, wrist 1, wrist 2, wrist 3] 
        acceleration is in radians/sec^2. velocity is in radians/sec
        '''
        radians = [0 for i in target]
        for i, degs in enumerate(target):
            radians[i] = math.radians(degs)
        self.send_cmd(f'movej({radians}, a={a}, v={v})')



if __name__ == '__main__':
    sock = URSocket(debug=True)
    sock.sock_connect()
    cmd = input()
    while cmd != 'q':
        sock.send_cmd(cmd)
