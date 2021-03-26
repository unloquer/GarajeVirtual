#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
from setuptools import setup, find_packages
from tools.tools import writetxt
setup(
	name='garajeVirtual',
	version='1.0.0',
	license='GPLv3',
	author_email='unloquer@gmail.com',
	author='Unloquer',
	description='script for generate a virtual meeting to linking the physical space with virtual space  ',
	url='',
	packages=find_packages(),
    install_requires=['python-telegram-bot', 'selenium'],
    include_package_data=True,
	)
#create files 
PATH = "files/"
writetxt(PATH+"auth.txt","here you gmail account  for meets")
writetxt(PATH+"token.txt","telegram bot token here")
writetxt(PATH+"meetactual.txt")
print("remeber add you private data telegram bot token and you google account\n\ttelegram token\t->files/token.txt\n\tgmail account\t->files/auth.txt")