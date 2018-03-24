import app
from fabric.api import task


@task
def all():
    app.nano()
    app.neovim()
    app.android_studio()
    app.vscode()
    app.okular()
    app.texstudio()
    app.svn()
    app.discord()
    app.nvidia()
    app.steam()
    app.nano()
