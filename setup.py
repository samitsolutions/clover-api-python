#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    'requests'
]

tests_require = [
    'pytest',
    ]

setup(
    name='clover-py',
    version='0.0.3',
    author='Yash B',
    author_email='yash@samitsolutions.com',
    license='MIT',
    url='https://github.com/samitsolutions/clover-api-python',
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    description='An unofficial Python client for the Clover API',
    download_url='https://github.com/samitsolutions/clover-api-python/archive/master.zip',
    keywords=['clover', 'api'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
