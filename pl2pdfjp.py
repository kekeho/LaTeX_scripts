#!/usr/bin/env python3
import re
import subprocess
import sys


def JapaneseMarkToEnglishStyle(fileObj):
    """
    The file needs to be opened in w+ mode.
    [WARNING:] In this function, error handling when there is no file is not described.
    """

    fileStr = fileObj.read()
    returnStr = fileStr.replace('、', ', ').replace('。', '. ')
    return returnStr


def latexToPdfCompile(filename):
    """
    Compile LaTeX file to PDF with platex/dvipdfmx 
    """
    subprocess.call('platex ' + filename, shell=True)
    subprocess.call('dvipdfmx ' + filename.replace('.tex', '.dvi'), shell=True)


if __name__ == '__main__':
    # openのmodeをr+とかw+にしてもなんか動きおかしくね?
    # だから無理やり2回開いている
    try:
        file = open(sys.argv[1], mode='r')

    except FileNotFoundError:
        print('file not found')

    else:
        replacedStr = JapaneseMarkToEnglishStyle(file)

    finally:
        file.close()

    try:
        file = open(sys.argv[1], mode='w')

    except IOError:
        print('cannot write something...')

    else:
        file.write(replacedStr)
        
    finally:
        file.close()
        
    
    latexToPdfCompile(sys.argv[1])