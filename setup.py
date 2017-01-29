"""
A gevent-based concurrent uploader for glacier using Boto3
"""

from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='GreenGlacier',

    version='1.0.0',
    description='A gevent-based concurrent uploader for glacier using Boto3',
    long_description=long_description,
    url='https://github.com/hopkiw/GreenGlacier',
    author='Liam Hopkins',
    author_email='we.hopkins@gmail.com',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Archiving',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='boto3 aws glacier upload network backup archive',

    py_modules=["greenglacier"],

    install_requires=['gevent', 'retrying'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage', 'pytest'],
    }
)
