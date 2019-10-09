from invoke import task, Exit, run as local
from fabric import Connection
from fabric.transfer import Transfer
from patchwork.files import append

import wget

from ..fedora import install

import os


def nano(c):
    install(c, "nano")


@task
def htop(c):
    install(c, "htop")


@task
def neovim(c):
    install(c, "neovim python-neovim python3-neovim")


@task
def android_studio(c):
    version = "3.2.1.0"
    release = "android-studio-ide-181.5056338-linux.zip"

#    install(c, "qemu-kvm android-tools libstdc++.i686 zlib.i686")
    print("Downloading Android Studio, this might take a while")
    if os.path.isfile(release) is False:
        wget.download(
            "https://dl.google.com/dl/android/studio/ide-zips/{}/{}".format(
                version, release
            )
        )
    c.put(release, remote='/tmp/')
    c.sudo("unzip -q /tmp/{} -d /opt/".format(release))
    c.run("rm -r /tmp/{}".format(release))

    append(
        "/usr/local/share/applications/android-studio.desktop",
        "[Desktop Entry]"
        "\nType=Application"
        "\nName=Android Studio"
        "\nIcon=/opt/android-studio/bin/studio.png"
        "\nExec=env _JAVA_OPTIONS=-Djava.io.tmpdir=/var/tmp "
        "/opt/android-studio/bin/studio.sh"
        "\nTerminal=false"
        "\nCategories=Development;IDE;",
        use_sudo=True,
    )


@task
def vscode(c):
    # dotnet repo
    c.sudo("rpm --import https://packages.microsoft.com/keys/microsoft.asc")
    c.sudo("wget -q https://packages.microsoft.com/config/fedora/27/prod.repo")
    c.sudo("mv prod.repo /etc/yum.repos.d/microsoft-prod.repo")
    c.sudo("chown root:root /etc/yum.repos.d/microsoft-prod.repo")
    
    # VC Code repo
    append(
        "/etc/yum.repos.d/vscode.repo",
        "[code]\nname=Visual Studio Code"
        "\nbaseurl=https://packages.microsoft.com/yumrepos/vscode/\n"
        "enabled=1\ngpgcheck=1"
        "\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc",
        use_sudo=True,
    )

    install(c, "code")  # VS Code itself
    install(c, "mono-devel")
    install(c, "mono-addins-devel")  # msbuild

    c.sudo("dnf copr -y disable @dotnet-sig/dotnet")

    install(c, "dotnet-sdk-2.1")
    install(c, "dotnet-runtime-2.1")
    

@task
def okular(c):
    install(c, "okular")


@task
def texstudio(c):
    install(c, "texlive-scheme-full texstudio")


@task
def svn(c):
    install(c, "svn")


@task
def discord(c):
    c.sudo("dnf copr -y enable tcg/discord")
    install(c, "Discord-installer")
    c.sudo("systemctl enable discord-installer")
    c.sudo("systemctl start discord-installer")


@task
def rpmfusion(c):
    install(
        c,
        "https://download1.rpmfusion.org/free/fedora/"
        "rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm "
        "https://download1.rpmfusion.org/nonfree/fedora/"
        "rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm",
    )


@task
def ffmpeg(c):
    install(c, "ffmpeg")


@task
def nvidia(c):
    c.sudo(
        "dnf config-manager --add-repo="
        "https://negativo17.org/repos/"
        "fedora-nvidia.repo"
    )
    install(
        c,
        "nvidia-settings kernel-devel dkms-nvidia vulkan.i686 "
        "nvidia-driver-libs.i686",
    )


@task
def qutebrowser(c):
    install(c, "qutebrowser")


@task
def nodejs(c):
    install(c, "nodejs")


@task
def sshguard(c):
    install(c, "autoconf automake byacc flex gcc python-docutils")
    with c.cd("/tmp"):
        sshguardurl = ("https://sourceforge.net/projects/"
                       "sshguard/files/latest/"
                       "download?source=files"
                       )
        c.run("wget '" + sshguardurl + "' -O sshguard.tar.gz")
        c.run("tar -xzf sshguard.tar.gz")
        with c.cd('sshguard-2.1.0'):
            c.run("./configure --prefix='/usr/local/'")
            c.run("make")

#
# Games
#


@task
def steam(c):
    steamrepourl = "https://negativo17.org/repos/fedora-steam.repo"
    c.sudo(
        "dnf config-manager --add-repo=" + steamrepourl
    )
    install(c, "steam")


@task
def xonotic(c):
    install(c, "xonotic")


@task
def supertuxkart(c):
    install(c, "supertuxkart")
