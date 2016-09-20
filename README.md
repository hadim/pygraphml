# pygraphml

[![Build Status](https://travis-ci.org/hadim/pygraphml.svg?branch=master)](https://travis-ci.org/hadim/pygraphml)
[![DOI](https://zenodo.org/badge/4163/hadim/pygraphml.svg)](https://zenodo.org/badge/latestdoi/4163/hadim/pygraphml)
[![PyPI version](https://img.shields.io/pypi/v/pygraphml.svg?maxAge=2591000)](https://pypi.org/project/pygraphml/)

`pygraphml` is a small Python library designed to parse GraphML file. To
see specification about GraphML, see http://graphml.graphdrawing.org/

Documentation and tutorial are available at http://hadim.github.io/pygraphml/. A notebook is also available [here](example.ipynb).

# Requirements

- Python > 2.7 and > 3.4
- NetworkX (http://networkx.lanl.gov/): only for the visualization

# Install

`pip install pygraphml`

Or you can use Anaconda and `conda-forge` :

```
conda config --add channels conda-forge
conda install pygraphml
```

# How to cite

If you use this library for your research, don't forget to cite it : [![DOI](https://zenodo.org/badge/4163/hadim/pygraphml.svg)](https://zenodo.org/badge/latestdoi/4163/hadim/pygraphml).

# License

Under BSD license. See [LICENSE](LICENSE).

# Authors

- Hadrien Mary <hadrien.mary@gmail.com>
- Nick Hamilton <n.hamilton@imb.uq.edu.au>

# How to release a new version

- Modify version number in `pygraphml/__init__.py`
- Commit and push changes
- Make Github release
- Create and upload packages : `python setup.py sdist bdist_wheel uploadl`
