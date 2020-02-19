from setuptools import setup, find_packages

setup(
    name='predict',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA analyse_predict team 26',
    long_description=open('README.md').read(),
    install_requires=[                      # Add project dependencies here
        "pandas>=0.20.0" ,'numpy'                   # example: pandas version 0.20 or greater                          
    ],
    url='https://github.com/vuks01/predict',
    author='Team26',
    author_email='vukeyasa@gmail.com'
)