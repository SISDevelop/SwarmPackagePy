import codecs
from setuptools import setup, find_packages
import SwarmPackagePy

with codecs.open('DESCRIPTION.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='SwarmPackagePy',
    version=SwarmPackagePy._version_,
    packages=find_packages(),
    description='Library of swarm optimization algorithms.',
    long_description=long_description,
    author='SISDevelop',
    author_email='swarm.team.dev@gmail.com',
    url='https://github.com/SISDevelop/SwarmPackagePy',
    license='none',

    keywords='swarm algorithms, python',
    install_requires=['numpy', 'matplotlib>=2.0.0', 'pandas', 'pytest'],
    platforms='Unix, Windows'

)
