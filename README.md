# 🐍 Python Password Cracker | 2023 - 2024 CSHS Cybersecurity

## Required Guidelines -
##### ‣ Regular usage of Git or some other version control software ⊰ ✗ ⊱ 3 points
##### ‣ Able to load dataset of at least the top 10K most common password ⊰ ✓ ⊱ 4 points
##### ‣ Implement random combinations (with an order) password cracking ⊰ ✓ ⊱ 10 points
##### ‣ Implement brute force dictionary attack password cracking ⊰ ✓ ⊱ 10 points
##### ‣ Able to run program via command line with various arguments ⊰ ✓ ⊱ 4 points
##### ‣ Able to add arguments when running program via command line ⊰ ✓ ⊱ 4 points
##### ‣ Implement the following types of password cracking; MD5, BCrypt, and SHA256 ⊰ ✓ ⊱ 5 points per
##### ‣ Included README.md file with dependencies and commands/arguments to run ⊰ ✓ ⊱ 1 point

## Dependencies -
##### ‣ requests library ⊰ｉ⊱ https://pypi.org/project/requests/
##### ‣ os library ⊰ｉ⊱ https://docs.python.org/3/library/os.html
##### ‣ zipfile library ⊰ｉ⊱ https://docs.python.org/3/library/zipfile.html
##### ‣ tqdm library ⊰ｉ⊱ https://pypi.org/project/tqdm/
##### ‣ hashlib library ⊰ｉ⊱ https://docs.python.org/3/library/hashlib.html
##### ‣ bcrypt library ⊰ｉ⊱ https://pypi.org/project/bcrypt/
##### ‣ itertools library ⊰ｉ⊱ https://docs.python.org/3/library/itertools.html

## Command Line Arguments -
##### ‣ --help ⊰ｉ⊱ When ran (via program) prints all information listed here
##### ‣ --action ⊰ｉ⊱ str : Actions to perform out of; bfd (zf), bf (zf & l), sha256 (p), md5 (p), and bCrypt (p & r)
##### ‣ --zipfile ⊰ｉ⊱ str : Path of zipfile in need of cracking
##### ‣ --password ⊰ｉ⊱ str : Password to be hashed and compare/contrasted with other hashes
##### ‣ --length ⊰ｉ⊱ int : Length of password to be brute forced (no greater than 4 digits)
##### ‣ --rounds ⊰ｉ⊱ int : Number of rounds for bcrypt hashing (recommend no greater than 8)