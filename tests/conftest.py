pytest_plugins = ["pytester"]

def pytest_addoption(parser):
    testplan = parser.getgroup('testplan')
    testplan.addoption("--testplan",
        action="store",
        default=None,
        help="Generate a .csv file containing the test's metadata and exit without running tests."
    )
