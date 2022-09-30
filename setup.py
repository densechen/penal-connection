from setuptools import find_packages, setup
from penal_connection import __version__

with open('requirements.txt', 'r') as f:
    requirements = [l.strip() for l in f.readlines()]

setup(
    name='penal_connection',
    version=__version__,
    description='Penal Connection',
    packages=find_packages(exclude=[]),
    author='densechen',
    author_email='densechen@foxmail.com',
    license='Apache License v2',
    include_package_date=True,
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)