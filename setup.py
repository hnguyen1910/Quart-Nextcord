"""
Quart-Nextcord
-------------

An Discord OAuth2 quart extension.
"""

import re

from setuptools import setup, find_packages


def __get_version():
    with open("quart_nextcord/__init__.py") as package_init_file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', package_init_file.read(), re.MULTILINE).group(1)


requirements = [
    'Quart',
    'pyjwt',
    'oauthlib',
    'Async-OAuthlib',
    'cachetools',
    'nextcord',
]


setup(
    name='Quart-Nextcord',
    version=__get_version(),
    url='https://github.com/hnguyen1910/Quart-Nextcord',
    license='MIT',
    author='HNTin',
    author_email='tin@ti.nz.eu.org',
    description='Discord OAuth2 extension for Quart.',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
