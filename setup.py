from setuptools import find_packages, setup ##basic setup 
from typing import List ## for the list used in function

''' 
    Function to return the list of requirements
'''
##declaring constant for the end -e . in requirements.txt
HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    


## meta data
setup(
    name='mlproject',
    version='0.0.1',
    author='Maya',
    author_email='smiyamaya@gmail.com',
    packages=find_packages(),
   # install_requires=['pandas','numpy','seaborn']   ## not feesible for so many libraries
   install_requires = get_requirements('requirements.txt')
)