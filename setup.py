#!/usr/bin/env python

import re
import io
import os.path


from setuptools import setup

def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()

def find_version(*file_paths):

    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setup(name='bbpyutils',
      version=find_version('bb', '__init__.py'),
      description='Various internal Bakken Baeck utilities',
      packages=['bb'],
      install_requires = []
     )
