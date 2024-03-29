#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PLAGUE: Time Wanderer - Setup.

Setup PLAGUE: Time Wanderer.
"""
import sys
import os
import stat
import pkgutil
import glob
import zipfile
import tarfile
import platform
import shutil
from urllib.request import urlopen, Request

try:
    shutil.rmtree("setup-env")
except FileNotFoundError:
    pass
os.mkdir("setup-env")
os.chdir("setup-env")


def load_requirements(requirements):
    """Load requirements."""
    to_install = requirements
    installed = list()
    for module in pkgutil.iter_modules():
        if module.name in to_install:
            to_install.remove(module.name)
            installed.append(module.name)
    return to_install, installed


def download(url, destination):
    if not url.startswith("http"):
        raise RuntimeError("Incorrect and possibly insecure protocol in url")
    httprequest = Request(url)
    response = urlopen(httprequest)
    with open(destination, 'wb') as destination:
        destination.write(response.read()
                          )


def detect_python():
    """Detect Python installation."""
    print("Detecting: Python...", end=" ", flush=True)
    test = os.system("python3 --version > " + os.devnull)
    if test == 0:
        print("Done.")
        return "python3"
    test = os.system("py -3 --version > " + os.devnull)
    if test == 0:
        print("Done.")
        return "py -3"
    print("Done.")
    print("/!\\ Python installation not found !")
    print("    Please verify that Python is installed and launchable with 'python3' command")
    stop()


def detect_pip(python):
    """Detect pip installation."""
    print("Detecting: pip...", end=" ", flush=True)
    test = os.system(python + " -m pip --version > " + os.devnull)
    print("Done.")
    if test == 0:
        return
    print("Downloading: https://bootstrap.pypa.io/get-pip.py...", end=" ", flush=True)
    download("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
    print("Done.")
    print("Installing: pip...", end=" ", flush=True)
    test = os.system(python + " get-pip.py > " + os.devnull)
    print("Done.")
    if test != 0:
        print("/!\\ Failed to install pip.")
        stop()


def install_requirements(requirements, python):
    """Install missing requirements."""
    for requirement in requirements:
        print("Downloading: https://pypi.org/simple/{0}/...".format(requirement), end=" ", flush=True)
        for retry in range(3):
            test = os.system(python + " -m pip download --prefer-binary " + requirement + " > " + os.devnull)
            if test == 0:
                break
            if retry == 0:
                print()
            print("Failed to download, retrying (" + str(retry + 1) + "/3)")
        if retry == 2:
            print("\n/!\\ Failed to download", requirement)
            stop()
        print("Done.")
    for wheel in glob.glob("*.whl"):
        print("Installing:", wheel + "...", end=" ", flush=True)
        test = os.system(python + " -m pip install --no-dependencies " + wheel + " > " + os.devnull)
        if test != 0:
            print("\n/!\\ Failed to install", wheel)
        print("Done.")
    for targz in glob.glob("*.tar.gz"):
        print("Unpacking:" , targz + "...", end=" ", flush=True)
        file = tarfile.open(targz)
        file.extractall(path="./setup-{0}/".format(targz[:-7]))
        file.close()
        print("Done.")
        print("Installing:", targz[:-7] + "...", end=" ", flush=True)
        os.chdir("setup-" + targz[:-7])
        double: bool = True
        try:
            os.chdir(targz[:-7])
        except FileNotFoundError:
            double: bool = False
        os.system(python + " setup.py build > " + os.devnull)
        os.system(python + " setup.py install > " + os.devnull)
        os.chdir("..")
        if double:
            os.chdir("..")
        print("Done.")


def install_plague(python):
    print("Downloading: https://codeload.github.com/Group-of-PLAGUE-Time-Wanderer/PLAGUE-Time-Wanderer/zip/refs/heads/main...", end=" ", flush=True)
    download("https://codeload.github.com/Group-of-PLAGUE-Time-Wanderer/PLAGUE-Time-Wanderer/zip/refs/heads/main", "plague.zip")
    print("Done.")
    print("Unpacking: plague.zip...", end=" ", flush=True)
    system = platform.system()
    with zipfile.ZipFile("plague.zip", 'r') as zip_ref:
        if system == "Linux":
            zip_ref.extractall("/usr/lib/plague-time-wanderer/")
        elif system == "Windows":
            zip_ref.extractall("C:/Program Files (x86)/PLAGUE Time Wanderer/")
        else:
            print()
            print("/!\\ Unindentified or unsupported OS.")
            stop()
    print("Done.")
    print("Installing: PLAGUE: Time Wanderer...", end=" ", flush=True)
    if system == "Linux":
        with open("/usr/bin/plague", "w") as file:
            file.write("#!/usr/bin/sh\ncd /usr/lib/plague-time-wanderer/PLAGUE-Time-Wanderer-main/\n" + python + " start.py")
            st = os.stat('/usr/bin/plague')
            os.chmod('/usr/bin/plague', st.st_mode | stat.S_IEXEC)
    elif system == "Windows":
        with open("C:/Program Files (x86)/Crocrodile/plague.bat") as file:
            file.write("cd C:/Program Files (x86)/PLAGUE Time Wanderer/PLAGUE-Time-Wanderer-main/\n" + python + " start.py")
    print("Done.")


def install(requirements):
    """Install Plague."""
    python = detect_python()
    detect_pip(python)
    install_requirements(requirements, python)
    install_plague(python)


def stop():
    """Stop installation."""
    print("Installation canceled.")
    sys.exit(1)


requirements = ["pygame", "sentry", "pip"]


print("Welcome in PLAGUE: Time Waderer setup program !")

print("Loading requirements...", end=" ", flush=True)
to_install, installed = load_requirements(requirements)
print("Done.")

print()
print("Installed packages:")
print("   ", "\t".join(installed))
print("Packages to install:")
print("   ", "\t".join(to_install))
continuation = input("Continue ? [Y/n] ").lower()
if continuation in ("y", "yes", ""):
    install(to_install)
elif continuation in ("n", "no"):
    print("Canceling...")
    stop()
else:
    print("Bad answer. Canceling...")
    stop()
