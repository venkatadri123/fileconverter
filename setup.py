from setuptools import find_packages, setup
setup(
    name='file_converter',
    packages=find_packages(include=['file_converter']),
    version='0.6.0',
    description='File Converted Library',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.1.2'],
    test_suite='tests'
)