from fabric.api import sudo, cd, put, env, task
from fabric.contrib.files import append
import desktop
import os


env.password = os.environ['SSH_PASSWORD']
env.roledefs = {
    'desktops': ['fs-desktop-01', 'fs-desktop-02', 'fs-desktop-03'],
    'servers': ['ipa', 'docker', 'fs-web-02']
}


@task
def selinux():
    sudo('setsebool -P use_nfs_home_dirs 1')


@task
def update():
    sudo('dnf -y update')


@task
def dconf():
    append('/etc/dconf/profile/user', 'service-db:keyfile/user', use_sudo=True)
    append('/etc/dconf/profile/gdm', 'user-db:user'
           'system-db:gdm'
           'file-db:/usr/share/gdm/greeter-dconf-defaults', use_sudo=True)
    sudo('mkdir /etc/dconf/db/gdm.d')
    append('/etc/dconf/db/gdm.d/00-login-screen', '[org/gnome/login-screen]'
           'disable-user-list=true', use_sudo=True)
    sudo('dconf update')


@task
def deploy_ff_policy():
    with cd('/usr/lib64/firefox/'):
        put('distFiles/firefox/distribution.ini', 'distribution/',
            use_sudo=True)


@task
def wol_setup():
    append('/etc/sysconfig/network-scripts/ifcfg-eno1',
           'ETHTOOL_OPTIONS="wol g"')
