import subprocess

def create_token():
    cmd = "openssl rand -hex 32"
    return subprocess.getoutput(cmd)
