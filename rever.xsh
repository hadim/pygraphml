$PROJECT = 'pygraphml'

$ACTIVITIES = ['version_bump', 'tag', 'push_tag', 'pypi', 'conda_forge', 'ghrelease']

$VERSION_BUMP_PATTERNS = [('pygraphml/__init__.py', '__version__\s*=.*', "__version__ = '$VERSION'"),
                          ('setup.py', 'version\s*=.*,', "version='$VERSION',")
                          ]

$PUSH_TAG_REMOTE = 'git@github.com:hadim/pygraphml.git'
$GITHUB_ORG = 'hadim'
$GITHUB_REPO = 'pygraphml'

$CONDA_FORGE_FEEDSTOCK = 'pygraphml-feedstock'
$CONDA_FORGE_SOURCE_URL = 'https://pypi.io/packages/source/p/pygraphml/pygraphml-$VERSION.tar.gz'
