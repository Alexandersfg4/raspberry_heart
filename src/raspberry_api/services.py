import subprocess


class Service:
    CMD = 'systemctl'
    START = 'start'
    RESTART = 'restart'
    STOP = 'stop'
    STATUS = 'status'

    def __init__(self, name: str):
        self.name = name

    def restart(self):
        status = subprocess.run([self.CMD, self.RESTART, self.name], capture_output=True)
        return status

