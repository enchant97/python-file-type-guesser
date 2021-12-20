# File Type Guesser
[![Test](https://github.com/enchant97/python-file-type-guesser/actions/workflows/python-test.yml/badge.svg)](https://github.com/enchant97/python-file-type-guesser/actions/workflows/python-test.yml)
![PyPI](https://img.shields.io/pypi/v/file-type-guesser)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/file-type-guesser)
![PyPI - Downloads](https://img.shields.io/pypi/dm/file-type-guesser)
![License MIT](https://img.shields.io/github/license/enchant97/python-file-type-guesser)
![Open Issues](https://img.shields.io/github/issues/enchant97/python-file-type-guesser)
![Line Count](https://img.shields.io/tokei/lines/github/enchant97/python-file-type-guesser)
![Last Commit](https://img.shields.io/github/last-commit/enchant97/python-file-type-guesser)

Guess a file's type from its content and extension.

This is intended to be a pure Python implementation of something like [python-magic](https://pypi.org/project/python-magic/). This means it should work on all platforms that can run Python as it does not require external binaries like libmagic.

> This project currently is not heavily tested and not fully feature complete

## Example Of Use

```python
from pathlib import Path
from file_type_guesser import guess_file

path = Path("README.md")
guess = guess_file(path)
print(guess)
```

```
ContentGuess(category=<FileTypes.TEXT: 1>, extention='md', content_ext='md')
```
