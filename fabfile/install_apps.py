from fabric.api import *
from fedora import install

def install(command):
    sudo('dnf -y install ' + command)


def install_nano():
    install('nano')