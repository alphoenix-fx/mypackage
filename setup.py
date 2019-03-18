from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/alphoenix_the_wiz/mypackage',
    author='Alfred Maboa',
    author_email='alfimaboa@gmail.com'
)
