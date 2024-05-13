"""
    this file runs pytest with test_dataframe_converters.py as the argument.The subprocess module
     is used to run a command and wait for it to finish


    """

import subprocess

subprocess.run(['pytest', 'test_dataframe_converters.py'])
