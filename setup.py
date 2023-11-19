import subprocess

from setuptools import setup
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        subprocess.check_call("playwright install".split())
        install.run(self)


setup(
    cmdclass={
        "install": PostInstallCommand,
    },
)
