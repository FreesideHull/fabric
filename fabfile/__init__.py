from fabric.api import *
from fabric.contrib.files import append
from fedora import install
import install_apps
import test_tasks
env.roledefs = {
    'desktops': ['fs-desktop-01', 'fs-desktop-02', 'fs-desktop-03'],
    'servers': ['ipa', 'docker', 'fs-web-02']
}

def selinux():
    sudo('setsebool -P use_nfs_home_dirs 1')

def update():
    sudo('dnf -y update')

def dconf():
    append('/etc/dconf/profile/user','service-db:keyfile/user')

def deploy_ff_policy():
    with cd('/usr/lib64/firefox/'):
        put('distFiles/firefox/distribution.ini', 'distribution/', use_sudo=True)