#Used to create a ML application as a package
from setuptools import setup, find_packages #find_packages finds all the packages in the entire ML library

#setup is the metadata information about the entire project
setup(
  name = 'Akshi NLP project',
  version = '0.0.1', # can update the versions as it goes forward
  author = 'Akshi',
  author_email = 'akshitha.3022@gmail.com',
  packages = find_packages(),
  install_requires = ['pandas','numpy','seaborn'],
  
  

)
