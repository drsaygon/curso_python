import subprocess

cmd = ['dir', '/w']

proc = subprocess.run (cmd, shell=True)

print(proc.args)

