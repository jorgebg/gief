from setuptools import setup

import gief


setup(
  name = 'gief',
  description = gief.__doc__,
  version = gief.__version__,
  packages = ['gief'],
  scripts = ['scripts/gief'],
  install_requires = ['flask==0.11', 'werkzeug==0.16.0'],
  url = 'https://github.com/jorgebg/gief',
  author = gief.__author__,
  author_email = gief.__author_email__,
  license = gief.__license__,
  keywords = ['http', 'upload', 'server', 'file']
)
