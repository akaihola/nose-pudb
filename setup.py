from setuptools import setup, find_packages
import re
version = None
for line in open("./nosepudb/__init__.py"):
    m = re.search("__version__\s+=\s+(.*)", line)
    if m:
        version = m.group(1).strip()[1:-1] # quotes
        break
assert version


setup(
    name='nose-pudb',
    version=version,
    description=('A Nose plugin for dropping the test runner into pdb '
                 'when it encounters an error.'),
    long_description=file('README.rst').read(),
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    install_requires=['nose', 'pudb'],
    entry_points="""
    [nose.plugins.0.10]
    nosepudb = nosepudb:Pudb
    """,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing'
        ],
)
