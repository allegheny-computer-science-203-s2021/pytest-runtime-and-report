"""Set up file for pytest plugin"""
#!/usr/bin/env python3

from setuptools import setup


setup(
    name='pytest-plugin',
    version='0.1.0',
    description='A pytest plugin to ....',
    url='https://github.com/allegheny-computer-science-203-s2021/pytest-runtime-and-report',
    author='Zack Devers, Wesley Long, Peter Snipes, Abigail Waryanka, Kai\'lani Woodard,'
    author_email=', solisa@allegheny.edu, donizk@allegheny.edu, leek3@allegheny.edu, shinomiyaa@allegheny.edu',
    license='MIT',
    py_modules=['plugin'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['pytest-plugin = pytestplugin.plugin', ], },
)
