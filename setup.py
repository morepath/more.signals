"""
more.signals
-----
Signals for Morepath.
"""

import io
from setuptools import (
    setup,
    find_packages
    )


version = '0.1.0.dev0'

long_description = '\n'.join((
    io.open('README.md', encoding='utf-8').read(),
    io.open('CHANGES', encoding='utf-8').read()
    ))

install_requires = [
    'morepath',
    'blinker'
    ]

tests_require = [
    'pytest',
    'coverage',
    'pytest-cov',
    'webtest'
    ]

docs_require = [
    'sphinx',
    'docutils'
    ]


setup(
    name='more.signals',
    version=version,
    url='https://github.com/blaflamme/more.signals',
    license='BSD',
    author='Blaise Laflamme',
    author_email='blaise@laflamme.org',
    description='Events for Morepath',
    long_description=long_description,
    keywords='morepath events signals blinker',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        ],
    namespace_packages=['more'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'docs': docs_require
        },
    test_suite='more.signals'
    )
