import os
import io
import re

from setuptools import setup
from setuptools import find_packages


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


setup(name='pygraphml',
      version=find_version("pygraphml", "__init__.py"),
      author='Hadrien Mary',
      author_email='hadrien.mary@gmail.com',
      description='Small library to parse GraphML files in Python',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='https://github.com/hadim/pygraphml/',
      packages=find_packages(),
      classifiers=[
              'Development Status :: 5 - Production/Stable',
              'Intended Audience :: Developers',
              'Natural Language :: English',
              'License :: OSI Approved :: BSD License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.4',
        ])
