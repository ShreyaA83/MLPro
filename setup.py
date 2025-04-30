## Setup.py is used to install the package
from setuptools import setup, find_packages

setup(
    name= 'MLPro',
    version= '0.0.1',
    author= 'Shreya',
    packages=find_packages(),
    install_requires=['numpy', 'seaborn', 'pandas', 'matplotlib', 'scikit-learn'],
    
)