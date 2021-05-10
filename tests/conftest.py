import csv
import pytest
import re
import time

pytest_plugins = ["pytester"]

"""Method for calculating test run times"""
def pytest_runtest_call(item):
    startTime = time.time()
    print(item.runtest())
    elapsedTime = time.time() - startTime
    seconds = f"Operation took {elapsedTime} seconds"
    return item.add_report_section("call", "Elapsed Time", seconds)

"""Adds testplan option to pytest"""
def pytest_addoption(parser):
    testplan = parser.getgroup('testplan')
    testplan.addoption("--testplan",
        action="store",
        default=None,
        help="Generate a .csv file containing the test's metadata and exit without running tests."
    )

"""The method for writing test plans to .csv file"""
def pytest_collection_modifyitems(session, config, items):
    path = config.getoption('testplan')
    if path:
        # Generate test plan .csv file and exit without running tests
        with open(path, mode='w') as fd:
            writer = csv.writer(fd, delimiter=',', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["title", "description", "markers"])
            for item in items:
                if item.cls:
                    title = f"{item.module.__name__}.py::{item.cls.__name__}::{item.name}"
                else:
                    title = f"{item.module.__name__}.py::{item.name}"
                description = re.sub('\n+', '\n', item.obj.__doc__.strip())
                markers = ','.join([m.name for m in item.iter_markers()])

                writer.writerow([title, description, markers])

        pytest.exit(f"Generated test plan: {path}")