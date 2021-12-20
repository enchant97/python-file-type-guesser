Quick Start
===========

Install
-------

::

    pip install file-type-guesser


Guess File
-----------
Code:
::

    from pathlib import Path
    from file_type_guesser import guess_file

    path = Path("README.md")
    guess = guess_file(path)
    print(guess)

Output:
::

    ContentGuess(category=<FileTypes.TEXT: 1>, extention='md', content_ext='md')
