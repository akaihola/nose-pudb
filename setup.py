#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='nose-pudb',
    author='Antti Kaihola',
    maintainer='Antoine Dechaume',
    version=open('VERSION').read().strip(),
    url='https://github.com/AntoineD/nose-pudb',
    download_url='https://pypi.python.org/pypi/nose-pudb',
    py_modules=['nose_pudb'],
    install_requires=['nose', 'pudb'],
    entry_points={
        'nose.plugins.0.10': [
            'nose_pudb=nose_pudb:Pudb'
        ]
    },
    description='A nose plugin for dropping into pudb on test errors or failures.',
    long_description=open('README.rst').read(),
    keywords='test unittest nose plugin debugger pudb',
    platforms=['POSIX'],
    license='GNU Library or Lesser General Public License (LGPL)',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Environment :: Plugins',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers',
    ],
)
