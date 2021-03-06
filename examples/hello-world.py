import sys

from pynomator.ssh_shell import SshShell
from pynomator.controller import Controller

s = SshShell("192.168.31.140", username="user", password="password").start()
ctrlr = Controller(s).start()

ctrlr.send("echo 'Hello World!'")
response = ctrlr.recv()
sys.stdout.write(ctrlr.motd + ctrlr.prompt + ctrlr.sent_data + response)
