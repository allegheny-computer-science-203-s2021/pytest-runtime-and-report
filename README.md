# pytest-runtime-and-report

## Table Of Contents
- [Introduction](#Introduction)
- [Objectives](#Objectives)
- [Learning](#Learning)
- [Organizing Test Cases by Runtime](#Organizing-Test-Cases-by-Runtime)
- [Producing a CSV File](#Producing-a-CSV-File)

## Introduction

[Pytest-Runtime-and-Report](https://test.pypi.org/project/runtime-and-report/0.0.1/) is a pytest plugin that sorts the pytests by runtime and then executes them from shortest to longest. It also produces a csv file with the results from running the test cases.

## Objectives

Our main goal was to create the `pytest` plugin tool under the name of Pytest Runtime and Report. The purpose of this program was to create a plugin that would utilize the `durations` method within `pytest` and create dictionary in a `.json` file with the tests names and IDs in order for the user of the plugin to be able to reorder test cases based on the data provided.

## Installation

In order to install the plugin either install from TestPyPI or clone the repository.

To install from TestPyPI:

```bash
pip install -i https://test.pypi.org/simple/ runtime-and-report==0.0.1
```

To clone repository:

```bash
git clone git@github.com:allegheny-computer-science-203-s2021/pytest-runtime-and-report.git
```


## Learning

If you would like to better understand how we completed these issues and how to complete something similar to this take a look at these links that helped us through completing this project.
[Implementing-Execution-Time-Calculations](https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution)
[Organizing-Test-Cases-by-Runtime-Calculations](https://pytest-ordering.readthedocs.io/en/develop/)
[Make-Plugin-Installable-by-Others](https://docs.pytest.org/en/stable/writing_plugins.html)
[Develop-a-Proper-Set-of-Test-Cases](https://realpython.com/python-testing/)

## Organizing Test Cases by Runtime

Being able to calculate execution times is crucial to being able to achieve our goal, which is ordering tests to execute based on quickest execution times. We are attempting to use a hook function to calculate runtime. However, the runtime must be calculated within conftest.py or test_plugin.py to achieve our goal for this project.

Once the runtimes are calculated, we plan to tag each case similar to how [pytest-ordering](https://pypi.org/project/pytest-order/) tags the test cases. However, we plan to tag them with runtimes, and then run them from least to greatest.

## Producing a CSV File

The feature that makes our pytest plugin special is the fact that after the test cases are run, the reports are neatly placed into a comma-separated value sheet (.csv file) to save for later reference. This is particularly useful for keeping documentation of what needs improved or of simply tracking successes.
