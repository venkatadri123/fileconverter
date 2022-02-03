from setuptools import find_packages, setup
setup(
    name='filesconverter',
    packages=find_packages(include=['filesconverter']),
    version='1.6.0',
    description='File Converted Library',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.1.2'],
    test_suite='tests'
)