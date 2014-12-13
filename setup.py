import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(name='pygraphml',
    version='2.0',
    author='Hadrien Mary',
    author_email='hadrien.mary@gmail.com',
    description='Small library to parse GraphML files in Python',
    long_description=read('README.md'),
    url='https://github.com/hadim/pygraphml/',
    packages=['pygraphml'],
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
            'Programming Language :: Python :: 3.3',
        ],)
