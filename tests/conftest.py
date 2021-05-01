pytest_plugins = ["pytester"]

def pytest_addoption(parser):
    testplan = parser.getgroup('testplan')
    testplan.addoption("--testplan",
        action="store",
        default=None,
        help="Generate a .csv file containing the test's metadata and exit without running tests."
    )

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
                description = re.sub('\n\s+', '\n', item.obj.__doc__.strip())
                markers = ','.join([m.name for m in item.iter_markers()])

                writer.writerow([title, description, markers])

        pytest.exit(f"Generated test plan: {path}")
