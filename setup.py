from setuptools import setup, find_packages
import os

current = os.getcwd()

setup(
    name='FairArticle',
    version='4.3.0',
    description='Article Provider for Sources, Categorizer, Utils and more.',
    url='https://github.com/chazzcoin/FairArticle',
    author='ChazzCoin',
    author_email='chazzcoin@gmail.com',
    license='BSD 2-clause',
    packages=find_packages(),
    package_dir={'res': 'FAui'},
    package_data={
        'FAui': ['*', '*.ui']
    },
    install_requires=['fairweb>=4.1.1', 'fairresources>=4.0.3', 'nltk>=3.5'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)