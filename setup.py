from setuptools import find_packages, setup
from typing import List

E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this functin will return list of reqiurements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace ('\n', '') for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)

    return requirements

setup(
    name='mlproject',
    version='1.0',
    packages=find_packages(),
    author='Twisha',
    install_requires=get_requirements('requirements.txt')
    
)
