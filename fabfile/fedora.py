from fabric.api import sudo


def install(command):
    sudo('dnf -y install ' + command)
