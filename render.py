import subprocess


def render(nexscript):
    subprocess.call(['node', nexscript])
