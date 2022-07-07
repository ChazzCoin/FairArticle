from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairArticle',
    version='1.0.2',
    description='Article Provider for Sources, Categorizer, Utils and more.',
    url='https://github.com/chazzcoin/FairArticle',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    package_data={
        'fopResources': ['*.txt', '*.csv']
    },
    install_requires=['FCoRE~=1.0.3', 'fairweb~=3.1.1'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)