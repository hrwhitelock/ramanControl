### setup file for raman control package
### uses py2exe, so only usable on windows

from distutils.core import setup
import py2exe

setup(console=['ramanControl.py'])