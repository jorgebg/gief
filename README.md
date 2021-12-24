# gief

[![Pypy](https://img.shields.io/pypi/v/gief.svg)](https://pypi.python.org/pypi/gief)
[![Build Status](https://travis-ci.org/jorgebg/gief.svg)](https://travis-ci.org/jorgebg/gief)
[![Requirements Status](https://requires.io/github/jorgebg/gief/requirements.svg?branch=master)](https://requires.io/github/jorgebg/gief/requirements/?branch=master)
[![Coverage Status](https://coveralls.io/repos/jorgebg/gief/badge.svg)](https://coveralls.io/r/jorgebg/gief)
[![MIT License](https://img.shields.io/pypi/l/gief.svg)](https://github.com/jorgebg/gief/blob/master/LICENSE)


Instant HTTP file uploading server.

## Requirements
* Python 2.7+ or Python 3.4+

## Install
```
sudo pip install gief
```

## Usage
```
usage: gief [-h] [-H HOST] [-p PORT] [path]

positional arguments:
  path                  Folder where files will be uploaded to (CWD by default)

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST
  -p PORT, --port PORT

```

Alternatively:

```
python -m gief
```

### Examples
```
mkdir /tmp/gief
gief /tmp/gief
```
