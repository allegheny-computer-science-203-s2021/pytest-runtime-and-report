"""Set up file for pytest plugin"""
#!/usr/bin/env python3

from setuptools import setup


setup(
    # name='pytest-plugin',
    # version='0.1.0',
    # description='A pytest plugin to ....',
    # url='https://github.com/allegheny-computer-science-203-s2021/pytest-runtime-and-report',
    # author='Zack Devers, Wesley Long, Peter Snipes, Abigail Waryanka, Kai lani Woodard',
    # license='MIT',
    # py_modules=['plugin'],
    # install_requires=['pytest'],
    # entry_points={'pytest11': ['pytest-plugin = pytestplugin.plugin', ], },

    name="myproject",
    packages=["myproject"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["name_of_plugin = myproject.pluginmodule"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
