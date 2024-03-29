#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "numpy"
]

test_requirements = ['pytest>=3', ]

setup(
    author="Jacopo Abramo",
    author_email='jacopo.abramo@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="A NumPy circular buffer for fast image storing and indexing.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='np_image_buffer',
    name='np_image_buffer',
    packages=find_packages(include=['np_image_buffer', 'np_image_buffer.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jacopoabramo/np_image_buffer',
    version='0.1.1',
    zip_safe=False,
)
