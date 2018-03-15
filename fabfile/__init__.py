from fabric.api import *
from fabric.contrib.files import append

env.roledefs = {
    'desktops': ['fs-desktop-01', 'fs-desktop-02', 'fs-desktop-03'],
    'servers': ['ipa', 'docker', 'fs-web-02']
}

def install_vscode():
    sudo('rpm --import https://packages.microsoft.com/keys/microsoft.asc')

    append('/etc/yum.repos.d/vscode.repo', '[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\n'
                                'enabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc')
    sudo('dnf install -y code')
    sudo('dnf install -y mono-devel')
    sudo('dnf copr -y enable @dotnet-sig/dotnet')
    sudo('dnf install -y dotnet-sdk-2.0')
    sudo('dnf install -y dotnet-runtime-2.0')

def selinux():
    sudo('setsebool -P use_nfs_home_dirs 1')

def install_discord():
    sudo('dnf copr -y enable tcg/discord')
    sudo('dnf install -y Discord-installer')
    sudo('systemctl enable discord-installer')
    sudo('systemctl start discord-installer')


def install_nvidia():
    sudo('dnf install -y https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm' 
         'https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm')
    sudo('dnf install -y xorg-x11-drv-nvidia akmod-nvidia')
    sudo('dnf install -y xorg-x11-drv-nvidia-cuda')

def install_steam():
    sudo('dnf install -y steam')

def install_nano():
    sudo('dnf install -y nano')

def install_nodejs():
	sudo('dnf install -y nodejs')

def install_tldr():
	sudo('npm install --global tldr')

def update():
    sudo('dnf -y update')

def dconf():
    append('/etc/dconf/profile/user','service-db:keyfile/user')

def install_neovim():
    sudo('dnf install -y neovim')
    sudo('dnf install -y python-neovim')
    sudo('dnf install -y python3-neovim')

