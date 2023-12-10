#Request import for internet interaction
import requests

#OS import for pathways
import os
from os import getcwd

#Zipfile import for zip interaction
import zipfile

#TQDM import for loading process display
from tqdm import tqdm

#Hashlib import for various hashing
import hashlib

#Bcrypt import for Bcrypt hashing
import bcrypt

#Itertools import for cartesian product
import itertools

#Getting raw list of 10k most common passwords for reference and cracking
r = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt')
#Creating pathway to imbedded text document passwdList
passwdListPath = os.path.join(getcwd(), 'passwdList')

#Writing most recent r text to passwdList via write() method
def updateList():
    f = open(passwdListPath,  'w')
    f.write(r.text)
    f.close()

#Brute Force Dictionary attack
def bfd(zipPath):
    #Declaring output variable in correctPasswd and status for output determination
    correctPasswd = '[+] Password found: '
    status = True
    #Creating ZipFile class object out of inputted zipfile pathway via ZipFile() method from zipfile import
    inpZip = zipfile.ZipFile(zipPath)
    #Opening passwdList in read binary mode to read through each passwd
    with open(passwdListPath, 'rb') as passwdList:
        for passWd in tqdm(passwdList, total=10000, unit='passwds'):
            #Isolating the password from any potential lines breaks and such
            passWd = passWd.strip()
            #Trying to extract contents of inpZip by inputting passwords from passwdList
            #If successful then the correct password is saved to correctPasswd
            #If not successful then continue trying other passwords
            try:
                inpZip.extractall(pwd=passWd)
                correctPasswd += passWd.decode()
                status = False
            except:
                continue
    #Checking status to determine output
    if status == True:
        print('[!] Password not found.')
    else:
        print(correctPasswd)  

#Brute Force attack
def bf(zipPath, length):
    #Creating list of characters (a-z and 0-9)
    alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
    #Creating list to hold every combination of alphanumeric
    combos = []
    #Creating every combination of alphanumeric based upon inputted length and then appending them to combos via product() method from itertools import
    for c in itertools.product(alphanumeric, repeat=length):
        combos.append(bytes(''.join(str(x) for x in c), 'utf-8'))

    #Declaring output variable in correctPasswd and status for output determination
    correctPasswd = '[+] Password found: '
    status = True
    #Creating ZipFile class object out of inputted zipfile pathway via ZipFile() method from zipfile import
    inpZip = zipfile.ZipFile(zipPath)
    #Going through every combination in combos
    for combo in tqdm(combos, total=len(combos), unit='combos'):
        #Trying to extract contents of inpZip by inputting combinations from combos
        #If successful then the correct combo is saved to correctPasswd
        #If not successful then continue trying other combos
        try:
            inpZip.extractall(pwd=combo)
            correctPasswd += combo.decode()
            status = False
        except:
            continue
    #Checking status to determine output  
    if status == True:
        print('[!] Password not found.')
    else:
        print(correctPasswd)

#SHA256 crack
def sha256(inpPasswd):
    #Hashing inputted password via sha256() >> update() methods from hashlib import
    sha256InpPasswd = hashlib.sha256()
    sha256InpPasswd.update(inpPasswd.strip().encode())
    #Declaring output variable in correctPasswd and status for output determination
    correctPasswd = '[+] Password found: '
    status = True
    #Opening passwdList in read mode to read through each passwd
    with open(passwdListPath, 'r') as passwdList:
        for passwd in tqdm(passwdList, total=10000, unit='passwds'):
            #Hashing each passwd from passwdList via sha256() >> update() methods from hashlib import to compare to sha256InpPasswd
            sha256 = hashlib.sha256()
            sha256.update(passwd.strip().encode())
            #Checking if md5 is equal to md5InpPasswd
            if sha256InpPasswd.hexdigest() == sha256.hexdigest():
                #Given the correct password is found changing output value and output determination to correct values
                status = False
                correctPasswd += passwd.strip()
    #Checking status to determine output
    if status == True:
        print('[!] Password not found.')
    else:
        print(correctPasswd)

#MD5 crack
def md5(inpPasswd):
    #Hashing inputted password via md5() >> update() methods from hashlib import
    md5InpPasswd = hashlib.md5()
    md5InpPasswd.update(inpPasswd.strip().encode())
    #Declaring output variable in correctPasswd and status for output determination
    correctPasswd = '[+] Password found: '
    status = True
    #Opening passwdList in read mode to read through each passwd
    with open(passwdListPath, 'r') as passwdList:
        for passwd in tqdm(passwdList, total=10000, unit='passwds'):
            #Hashing each passwd from passwdList via md5() >> update() methods from hashlib import to compare to md5InpPasswd
            md5 = hashlib.md5()
            md5.update(passwd.strip().encode())
            #Checking if md5 is equal to md5InpPasswd
            if md5InpPasswd.hexdigest() == md5.hexdigest():
                #Given the correct password is found changing output value and output determination to correct values
                status = False
                correctPasswd += passwd.strip()
    #Checking status to determine output
    if status == True:
        print('[!] Password not found.')
    else:
        print(correctPasswd)

#bCrypt crack
def bCrypt(inpPassword, rounds):
    #Hashing inputted password with given rounds via hashpw() method from bcrypt import
    hashedInp = bcrypt.hashpw(inpPassword.encode(), bcrypt.gensalt(rounds))
    #Declaring output variable in correctPasswd and status for output determination
    correctPasswd = '[+] Password found: '
    status = True
    #Opening passwdList in read binary mode to read through each passwd and compare with inputted password
    with open(passwdListPath, 'rb') as passwdList:
        for passwd in tqdm(passwdList, total=10000, unit='passwds'):
            #Checking if the given sole passwd is equivlent to hashedInp with its salt via checkpw() method from bcrypt import
            if bcrypt.checkpw(passwd.strip(), hashedInp):
                #Given the correct password is found changing output value and output determination to correct values
                status = False
                correctPasswd += passwd.decode()
    #Checking status to determine output            
    if status == True:
        print('[!] Password not found.')
    else:
        print(correctPasswd)
