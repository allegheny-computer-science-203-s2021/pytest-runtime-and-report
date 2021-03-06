import csv
import pytest
import re
import json

pytest_plugins = ["pytester"]
test_runtime = {}

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

"""Record test name and test duration in a list, and export to json"""
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    for reps in terminalreporter.stats.values():
        for rep in reps:
            if rep.when == "call":
                test_runtime[rep.nodeid] = rep.duration
    print("\nExported test runtimes to test_times.json")
    with open("test_times.json", "w") as outfile:
        json.dump(test_runtime, outfile, indent=4)