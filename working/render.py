import subprocess

# TODO: completely detach from nexrender.
def render(nexscript):
    subprocess.call(['node', nexscript])
