from setuptools import find_packages,setup
from typing import List

HYPHEN_E='-e .'

'''
This function will return the list of requirements
'''
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as Obj:
      requirements=Obj.readlines()
      requirements=[req.replace('\n','') for req in requirements]

      if(HYPHEN_E in requirements):
          requirements.remove(HYPHEN_E)
          
      return requirements


setup(name='mlprojects',
      version='0.0.1',
      author='Vishesh',
      author_email='visheshkush342@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements('requirements.txt'),
     )