import os
import io

from setuptools import setup
from setuptools import find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


setup(name='pygraphml',
      version='2.4.2',
      author='Hadrien Mary',
      author_email='hadrien.mary@gmail.com',
      description='Library to parse GraphML files in Python',
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
