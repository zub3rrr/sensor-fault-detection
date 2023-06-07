from setuptools import find_packages,setup
from typing import List

# def get_requirements()->List[str]:
#   """Returns a list of requirements.txt"""
#   requirement_list:List[str] = []
  
#   """
#   Write a code so that it returns a list of strings from requirements.txt
#   """
   
#   return requirement_list

requirements_path = r'./requirements.txt'
def read_requirements_file(file_path):
    with open(file_path, 'r') as file:
        requirements = file.read().splitlines()
    return requirements



setup(
  name="sensor",
  author="Zuber Ahmed",
  version="0.0.1",
  author_email="xuberswork@gmail.com",
  # packages=find_packages(),   
  install_requires=read_requirements_file(requirements_path),  
)

# #or else employ using -e . in requirements.txt
