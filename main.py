#!/usr/bin/env cached-nix-shell
#! nix-shell -p python310 -i "python3.10" --quiet

import sys
import os

def encryptFile(fileName: str) -> None:
    sourceFile = open(fileName, 'r')
    tempFile = open('temp.txt', 'w')
    byte = sourceFile.read(1)
    while byte:
        byte = ord(byte)
        byte += 1
        tempFile.write(chr(byte))
        byte = sourceFile.read(1)
    sourceFile.close()
    tempFile.close()
    sourceFile = open(fileName, 'w')
    tempFile = open('temp.txt', 'r')
    byte = tempFile.read(1)
    while byte:
        sourceFile.write(byte)
        byte = tempFile.read(1)
    sourceFile.close()
    tempFile.close()
    os.remove('temp.txt')

def decryptFile(filename: str) -> None:
    sourceFile = open(filename, 'rb')
    tempFile = open('temp.txt', 'w')
    byte = sourceFile.read(1)
    while byte:
        byte = ord(byte)
        byte -= 1
        tempFile.write(chr(byte))
        byte = sourceFile.read(1)
    sourceFile.close()
    tempFile.close()
    sourceFile = open(filename, 'w')
    tempFile = open('temp.txt', 'r')
    byte = tempFile.read(1)
    while byte:
        sourceFile.write(byte)
        byte = tempFile.read(1)
    sourceFile.close()
    tempFile.close()
    os.remove('temp.txt')


def encryptDir(directoryName: str) -> None:
    for filename in os.listdir(directoryName):
        fileName = directoryName + "/" + filename
        if os.path.isfile(fileName):
            encryptFile(fileName)
            print(fileName + " encriptado!!")
        elif os.path.isdir(fileName):
            encryptDir(fileName)

def decryptDir(directoryName: str) -> None:
    for filename in os.listdir(directoryName):
        fileName = directoryName + "/" + filename
        if os.path.isfile(fileName):
            decryptFile(fileName)
            print(fileName + " decriptado!")
        elif os.path.isdir(fileName):
            decryptDir(fileName)

def main():
    directoryName = input("Insira o diretório a ser encriptado: ")
    encryptDir(directoryName)
    directoryName = input("Insira o diretório a ser decriptado: ")
    decryptDir(directoryName)

if __name__ == '__main__':
    main()
