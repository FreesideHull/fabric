from fabric.api import sudo, cd, put, env, task
from fabric.contrib.files import append
import install

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
    append('/etc/dconf/profile/user', 'service-db:keyfile/user')


@task
def deploy_ff_policy():
    with cd('/usr/lib64/firefox/'):
        put('distFiles/firefox/distribution.ini', 'distribution/',
            use_sudo=True)
