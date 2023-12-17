import os
import re

from setuptools import setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        os.system("playwright install")
        install.run(self)


with open(os.path.join("stock_clue", "__init__.py")) as init:
    source = init.read()
    m = re.search("__version__ = '(.*)'", source, re.M)
    __version__ = m.groups()[0]

setup(
    name="stock-clue",
    author="Kang Hangoo",
    version=__version__,
    description="Easy tool for get stock clue",
    url="https://github.com/kgcrom/stock-clue",
    keywords="stock dart finance",
    license="MIT License",
    cmdclass={
        "install": CustomInstallCommand,
    },
)
