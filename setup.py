import os
from setuptools import setup, find_packages

VERSION = __import__("djracula").__version__

CLASSIFIERS = [
    'Development Status :: 1 - Planning',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Natural Language :: English',
]

setup(
    name='djracula',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A dark theme for django admin',
    url='https://github.com/Djracula/djracula',
    author='Akash Jain, Taranjeet Singh',
    author_email='akashjain993@gmail.com, reachtotj@gmail.com',
    classifiers=CLASSIFIERS,
    install_requires=[]
)
