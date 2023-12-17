from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='vineet',
    author_email='vineetkukreti34@gmal.com',
    install_requires=get_requirements('requirememts.txt'),
    # this function will read content from the file requiremnet.txt  and this function will return the list of all 
    packages=find_packages()

)