# Freeside-Fabfiles

[![Build Status](https://ci.freeside.co.uk/api/badges/FreesideHull/Freeside-Fabfiles/status.svg)](https://ci.freeside.co.uk/FreesideHull/Freeside-Fabfiles)

> The official _Fabfile_ for Freeside.

A _FabFile_ is a configuration file for [fabric](http://www.fabfile.org/) a way of automatically deploying commands on many machines at once. If you'd like some software installed or a configuration changed on the Freeside machines, then it's the _Fabfile_ in this repository that you'll want to edit! See the instructions below for more details.


## Architecture
We use [Drone](https://drone.io/) as our continuous integration server. On every push , it pulls it down and checks the configuration with a tool called [Flake8](http://flake8.pycqa.org/en/latest/), to ensure there aren't any syntactical errors etc. Then, if it's ok and the push was to the `master` branch, it will automatically wake up the PCs in the Freeside lab, and deploy any updates to them.


## Setup
Simply run the following sequence of commands:

```bash
git clone https://github.com/FreesideHull/Freeside-Fabfiles
cd Freeside-Fabfiles
virtualenv .venv
. ./.venv/bin/activate
pip3 install -r requirements.txt
```

Make sure you pay attention to the output, in case an error is thrown.


## Usage
Using the fabric _FabFile_ in this repository is easy. Here's how:

Run a task:
```bash
$ fab -H comma,seperated,hosts taskname 
```

List tasks
```bash
$ fab -l
```

Example usage:
```bash
$ fab -H fs-desktop01 install.app.neovim
```

Running multiple tasks in a collection:
```bash
# Installs all desktop apps
$ source hosts
$ fab -H "$desktops" $(fab --complete | grep "desktop.install")
```


## Contributing
Want some software installing on the Freeside computers? You've come to the right place! Here's a simple guide on how to request software to be installed:

1. Make sure you're logged into your GitHub account.
2. Take a look at [`fabfile/desktop/install.py`](https://github.com/FreesideHull/Freeside-Fabfiles/blob/master/fabfile/desktop/install.py).
3. Press the edit button in the top-right.
4. Figure out how to install the software you want on a standard _Fedora_ machine.
5. Add a new function to the _Fabfile_ in the same vein that the existing ones that installs the software you want. We prefer it if the software is available through `dnf`, _Fedora_'s official package manager. That way it stays up-to-date automatically!
6. Click _Propose File Change_ at the bottom of the page and follow it through to submit a _Pull Request_ for your changes.
7. Take a look at [`fabfile/desktop/__init__.py`](https://github.com/FreesideHull/Freeside-Fabfiles/blob/master/fabfile/desktop/__init__.py). 
8. Add a task to the `all()` function that calls your new install function.
9. Create a _Pull Request_ for this as before.
10. Once your pull requests are accepted, then your software will get installed automatically within a few minutes!
