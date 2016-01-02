'''
Creating the needed environments for creating the pre-compiled distribution on Windods:

1. Download:

* conda32 at C:\tools\Miniconda32

* conda64 at C:\tools\Miniconda

Create the environments:

C:\tools\Miniconda32\Scripts\conda create -y -f -n py27_32 python=2.7 cython numpy nose ipython pip
C:\tools\Miniconda32\Scripts\activate py27_32
pip install "django>=1.7,<1.8"
pip install -U "pip>=1.4" "setuptools>=0.9" "wheel>=0.21" twine
deactivate

C:\tools\Miniconda32\Scripts\conda create -y -f -n py34_32 python=3.4 cython numpy nose ipython pip
C:\tools\Miniconda32\Scripts\activate py34_32
pip install "django>=1.9"
pip install -U "pip>=1.4" "setuptools>=0.9" "wheel>=0.21" twine
deactivate

C:\tools\Miniconda32\Scripts\conda create -y -f -n py35_32 python=3.5 cython numpy nose ipython pip
C:\tools\Miniconda32\Scripts\activate py35_32
pip install "django>=1.9"
pip install -U "pip>=1.4" "setuptools>=0.9" "wheel>=0.21" twine
deactivate

C:\tools\Miniconda\Scripts\conda create -y -f -n py27_64 python=2.7 cython numpy nose ipython pip
C:\tools\Miniconda\Scripts\activate py27_64
pip install "django>=1.7,<1.8"
pip install -U "pip>=1.4" "setuptools>=0.9" "wheel>=0.21" twine
deactivate

C:\tools\Miniconda\Scripts\conda create -y -f -n py34_64 python=3.4 cython numpy nose ipython pip
C:\tools\Miniconda\Scripts\activate py34_64
pip install "django>=1.9"
pip install -U "pip>=1.4" "setuptools>=0.9" "wheel>=0.21" twine
deactivate

C:\tools\Miniconda\Scripts\conda create -y -f -n py35_64 python=3.5 cython numpy nose ipython pip
C:\tools\Miniconda\Scripts\activate py35_64
pip install "django>=1.9"
pip install -U "pip>=1.4" "setuptools>=0.9" "wheel>=0.21" twine
deactivate


'''

from __future__ import unicode_literals
import os
import subprocess


python_installations = [
    r'C:\tools\Miniconda32\envs\py27_32\python.exe',
    r'C:\tools\Miniconda32\envs\py34_32\python.exe',
    r'C:\tools\Miniconda32\envs\py35_32\python.exe',

    r'C:\tools\Miniconda\envs\py27_64\python.exe',
    r'C:\tools\Miniconda\envs\py34_64\python.exe',
    r'C:\tools\Miniconda\envs\py35_64\python.exe',
]

root_dir = os.path.dirname(os.path.dirname(__file__))
def list_binaries():
    for f in os.listdir(os.path.join(root_dir, '_pydevd_bundle')):
        if f.endswith('.pyd'):
            yield f

def main():
    from generate_code import generate_dont_trace_files
    from generate_code import generate_cython_module

    # First, make sure that our code is up to date.
    generate_dont_trace_files()
    generate_cython_module()

    for python_install in python_installations:
        assert os.path.exists(python_install)

    from build import remove_binaries
    remove_binaries()

    for f in list_binaries():
        raise AssertionError('Binary not removed: %s' % (f,))

    for python_install in python_installations:
        subprocess.check_call([
            python_install, os.path.join(root_dir, 'build', 'build.py'), '--no-remove-binaries'])


if __name__ == '__main__':
    main()

