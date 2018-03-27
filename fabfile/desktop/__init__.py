import install
from fabric.api import task


@task
def all():
    install.nano()
    install.neovim()
    install.android_studio()
    install.vscode()
    install.okular()
    install.texstudio()
    install.svn()
    install.discord()
    install.nvidia()
    install.steam()
    install.qutebrowser()
    install.nodejs()
    install.xonotic()
    install.supertuxkart()
    install.rpmfusion()
    install.ffmpeg()
    install.nvidia()
