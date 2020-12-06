from setuptools import setup, find_packages
from seconds.version import __version__

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='seconds',
    version=__version__,
    description=
    'Seconds is a utility package to transform seconds to minutes, hours, etc. and vice versa quickly, easily, understandable by humans and without external dependencies!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NTBBloodbath/Seconds',
    author='NTBBloodbath',
    author_email='bloodbathalchemist@protonmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    zip_safe=False)
