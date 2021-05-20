"""Set up file for pytest plugin"""
#!/usr/bin/env python3

from setuptools import setup


setup(
    name='runtime_and_report',
    version='0.0.1',
    description='A pytest plugin to determine runtimes of pytests and also report the pytest results to a .csv file.',
    url='https://github.com/allegheny-computer-science-203-s2021/pytest-runtime-and-report',
    author='Zack Devers, Wesley Long, Peter Snipes, Abigail Waryanka, Kai lani Woodard',
    author_email='deversz@allegheny.edu,longw@allegheny.edu, snipesp@allegheny.edu, waryankaa@allegheny.edu, woodardk@allegheny.edu',
    license='MIT',
    py_modules=['plugin'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['pytest-plugin = pytestplugin.plugin', ], },
)
