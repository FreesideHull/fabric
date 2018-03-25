from fabric.api import sudo, run, task
from fabric.contrib.files import append
from ..fedora import install


@task
def nano():
    install('nano')


@task
def neovim():
    install('neovim python-neovim python3-neovim')


@task
def android_studio():
    version = '3.0.1.0'
    release = 'android-studio-ide-171.4443003-linux.zip'
    install('qemu-kvm android-tools libstdc++.i686 zlib.i686')
    run('wget https://dl.google.com/dl/android/studio/ide-zips/{}/{}'
        .format(version, release))
    sudo('unzip -q {} -d /opt/'.format(release))
    run('rm -r {}'.format(release))
    append('/usr/local/share/applications/android-studio.desktop',
           '[Desktop Entry]'
           '\nType=Application'
           '\nName=Android Studio'
           '\nIcon=/opt/android-studio/bin/studio.png'
           '\nExec=env _JAVA_OPTIONS=-Djava.io.tmpdir=/var/tmp'
           '/opt/android-studio/bin/studio.sh'
           '\nTerminal=false'
           '\nCategories=Development;IDE;', use_sudo=True)


@task
def vscode():
    sudo('rpm --import https://packages.microsoft.com/keys/microsoft.asc')

    append('/etc/yum.repos.d/vscode.repo', '[code]\nname=Visual Studio Code'
           '\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\n'
           'enabled=1\ngpgcheck=1'
           '\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc',
           use_sudo=True)
    install('code')
    install('mono-devel')
    sudo('dnf copr -y enable @dotnet-sig/dotnet')
    install('dotnet-sdk-2.0')
    install('dotnet-runtime-2.0')


@task
def okular():
    install('okular')


@task
def texstudio():
    install('texlive-scheme-full texstudio')


@task
def svn():
    install('svn')


@task
def discord():
    sudo('dnf copr -y enable tcg/discord')
    install('Discord-installer')
    sudo('systemctl enable discord-installer')
    sudo('systemctl start discord-installer')


@task
def nvidia():
    install('https://download1.rpmfusion.org/free/fedora/'
            'rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm')
    install('xorg-x11-drv-nvidia akmod-nvidia')
    install('xorg-x11-drv-nvidia-cuda')


@task
def steam():
    install('steam')


@task
def qutebrowser():
    install('qutebrowser')
