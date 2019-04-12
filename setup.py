from setuptools import setup
import os
import shutil
import sys

if os.geteuid() != 0:
    print("This command must be run as root. Aborting.")
    sys.exit(1)

if os.environ['BOARD'] != 'Pynq-Z2':
    print("Only supported on a Pynq-Z2 Board")
    exit(1)

setup(
	name = "sensehat",
	version = 1.0,
	url = 'https://github.com/xupsh/pynq-sense-hat',
	license = 'BSD 3-Clause License',
	author = "Jin Yongwei",
	author_email = "yongweij@xilinx.com",

	include_package_data = True,
	packages = ['sensehat'],
	package_data = {
	'' : ['*.bit','*.tcl','*.py','*.bin','*.txt', '*.cpp', '*.h', '*.sh'],
	},
	description = "Sense HAT for PYNQ",
    install_requires=[
        'pynq','numpy'
    ],
)

WORK_DIR = os.path.dirname(os.path.realpath(__file__))

shutil.copy2(WORK_DIR + "/sensehat/rpc.py","/usr/local/lib/python3.6/dist-packages/pynq/lib/pynqmicroblaze/rpc.py")

if 'install' in sys.argv:
    if os.path.isdir(os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/pynq-sense-hat/"):
        shutil.rmtree(os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/pynq-sense-hat/")
    shutil.copytree(WORK_DIR + "/boards/Pynq-Z2/notebooks/",os.environ["PYNQ_JUPYTER_NOTEBOOKS"]+"/pynq-sense-hat/")