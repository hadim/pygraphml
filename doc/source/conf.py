#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import io
import re
from datetime import date
import alabaster

sys.path.insert(0, os.path.abspath("../../"))

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


extensions = [
    'sphinx.ext.autodoc',
    'alabaster'
]

# The suffix of source filenames.
source_suffix = '.rst'

master_doc = 'index'

# General information about the project.
project = 'PyGraphML'
copyright = '2014-{}, Hadrien Mary'.format(date.today().year)

# The short X.Y version.
version = find_version("..", "..", "pygraphml", "__init__.py")

# The full version, including alpha/beta/rc tags.
release = version

pygments_style = 'sphinx'
html_theme = 'alabaster'
html_theme_path = [alabaster.get_path()]
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
    ]
}

html_theme_options = {
    'github_user': 'hadim',
    'github_repo': 'pygraphml',
    'github_button': False,
    'travis_button': True
}
