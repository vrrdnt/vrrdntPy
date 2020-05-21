import subprocess


# Run nexrender. https://github.com/inlife/nexrender
def render(nexscript):
    subprocess.call(['node', nexscript])
