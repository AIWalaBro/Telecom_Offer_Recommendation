from setuptools import find_packages,setup
from typing import List

HYPERN_E_DOT = "-e ."

'''
this function will read the path of requiremnts.txt
'''
requirements = []
def get_requirements(filepath:str)->List[str]:
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements ]
        
        # it is return for "-e ." comes in setup.py files and once again
        # it will triggered out and we dont wann that while running this function.
        if "-e ." in requirements:
            requirements.remove(HYPERN_E_DOT)
    return requirements
        
    

'''
create a meta deta, build a pypy package thats why we create the setup.py file
so anybody can run it in thier local.
'''
setup(
    name = "Telecome Industry Offer Recommender System",
    version = "0.0.1",
    author = "Bharatbhushan",
    author_email = "aiwalabro@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
    )