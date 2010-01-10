import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
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
    author='Antti Kaihola',
    author_email='akaihol+python@ambitone.com',
    maintainer='Antti Kaihola',
    maintainer_email='akaihol+python@ambitone.com',
    version=version,
    url='http://github.com/akaihola/nose-pudb',
    description=('A Nose plugin for dropping the test runner into pdb '
                 'when it encounters an error.'),
    long_description=file('README.rst').read(),
    keywords = ('test unittest doctest automatic discovery nose plugin '
                'debugger pudb'),
    zip_safe=False,
    packages=['nosepudb'],
    install_requires=['nose', 'pudb'],
    entry_points="""
    [nose.plugins.0.10]
    nosepudb = nosepudb:Pudb
    """,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Debuggers',
        ],
)
