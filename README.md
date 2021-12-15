# File Type Guesser
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
