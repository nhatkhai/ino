#!/usr/bin/env python
# -*- coding: utf-8 -*-
# run following command to install this module:
#   python setup.py install
#
# run following command to uninstall this module:
#   python setup.py uninstall
# OR
#   cat install_*.txt | xargs rm -vrf 

from setuptools import setup
import sys

# Check for uninstall in argument and do uninstall
i=0
for e in sys.argv:
    if e=='uninstall':
        print "running uninstall"
        import glob
        import os
        for a in glob.glob('install_*_%s.txt' % sys.platform):
            for f in file(a).read().split('\n'):
                if os.path.isfile(f):
                    print "Remove ", f
                    os.remove(f)
        sys.argv.pop(i)
    else:
        i += 1
if len(sys.argv)<=1: quit()

install_requires = open("requirements.txt").read().split('\n')
readme_content = open("README.rst").read()

def gen_data_files(package_dir, subdir):
    import os.path
    results = []
    for root, dirs, files in os.walk(os.path.join(package_dir, subdir)):
        results.extend([os.path.join(root, f)[len(package_dir)+1:] for f in files])
    return results

ino_package_data = gen_data_files('ino', 'make') + gen_data_files('ino', 'templates')


# Look for install and --record install_*.txt file into argument for
# installation record
__version__ = '0.3.8'
for i, e in enumerate(sys.argv):
    if e=='install':
        # Import to verify all dependencies are satisfy, and obtain __version__
        try:
            import ino.runner
            sys.argv.insert(i+1,'--record')
            sys.argv.insert(i+2,'install_%s_%s.txt' % (__version__, sys.platform))
        except ImportError as e:
            print "Require module is not found: ", e.message
            quit()
        break

setup(
    name='ino',
    version=__version__,
    description='Command line toolkit for working with Arduino hardware',
    long_description=readme_content,
    author='Victor Nakoryakov, Amperka Team',
    author_email='victor@amperka.ru',
    license='MIT',
    keywords="arduino build system",
    url='http://inotool.org',
    packages=['ino', 'ino.commands'],
    scripts=['bin/ino'],
    package_data={'ino': ino_package_data},
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Embedded Systems",
    ],
)
