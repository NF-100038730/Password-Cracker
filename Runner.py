#argparse import for command line interaction
from argparse import ArgumentParser, Namespace

#PasswordCrack import for calling of functions to crack passwords
from PasswordCrack import *

#Setting up actual ArgumentParser class from argparse import
parser = ArgumentParser()
parser.usage = 'Password cracker'
#Declaring the various arguments that can be taken in via add_argument() method from argparse import
parser.add_argument('--action', type=str, help="str : Actions to perform out of; 'bfd' (zf), 'bf' (zf & l), 'sha256' (p), 'md5' (p), and 'bCrypt' (p & r)")
parser.add_argument('--zipfile', type=str, help='str : Path of zipfile in need of cracking')
parser.add_argument('--password', type=str, help='str : Password to be hashed and compare/contrasted with other hashes')
parser.add_argument('--length', type=int, help='int : Length of password to be brute forced (no greater than 4 digits)')
parser.add_argument('--rounds', type=int, help='int : Number of rounds for bcrypt hashing (recommend no greater than 8)')
args: Namespace = parser.parse_args()

#Checking the various acceptable actions in comparison to the inputted action
#If an accepted action is found to have been inputted then it will call the corresponding function from PasswordCrack
if args.action == 'bfd':
    bfd(args.zipfile)
elif args.action == 'bf':
    bf(args.zipfile, args.length)
elif args.action == 'sha256':
    sha256(args.password)
elif args.action == 'md5':
    md5(args.password)
elif args.action == 'bCrypt':
    bCrypt(args.password, args.rounds)
else:
    print("Sorry, it seems you haven't inputted a necessary and proper action. If in need of assistance run the '--help' command or refer to the README")