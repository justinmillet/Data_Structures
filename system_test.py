# Name: Justin Millet
# ONID Email: milletj@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Assignment 0: Introduction and Environment Setup
# Due Date: April 12th
# Description: Test to make sure Python 3.7 is installed

import sys

cur_version = sys.version_info
if cur_version >= (3, 7):
    print("This is an acceptable version of Python, version " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
else:
    print("Your Python version is too low, it needs to be 3.7 or greater and this is " + str(cur_version[0]) + '.' + str(cur_version[1]) + '.')
