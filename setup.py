"""
This module (setup.py) will be used to build and distribute python package

"""
from setuptools import find_packages, setup

# setuptools : A package that provide tools for packaging python project i.e. setup
# setuptools is already installed while creating environment
# find_packages, setup : functions , setuptools : module

from typing import List

hyphone_e_dot='-e.'

def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path,'r') as file_obj:

        requirements=file_obj.readlines() # ex: ['Hello! Welcome to demofile.txt\n', 'This file is for testing purposes.\n']

        requirements=[req.replace("\n","") for req in requirements]

    if hyphone_e_dot in requirements:

            requirements.remove(hyphone_e_dot)

    return requirements


setup(

#Metadata information about project , it will be created as a new package

    name='Fault Detection',
    version='0.0.1',
    author='Harsh Arora',
    author_email='harsharora1004@gmail.com',
    install_requirements=get_requirements('requirements.txt'), # a list of elements
    packages=find_packages()

)


# for install setup.py : python setup.py install