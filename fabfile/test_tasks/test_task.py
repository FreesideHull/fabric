from fabric.api import *
from fedora import install

def test_install_nano():
    install('nano')