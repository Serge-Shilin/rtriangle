import pytest

HELP_TEXT = 'Input only integer'


def pytest_addoption(parser):
    parser.addoption('--x0', action='store', default=0, help=HELP_TEXT)
    parser.addoption('--y0', action='store', default=0, help=HELP_TEXT)
    parser.addoption('--x1', action='store', default=0, help=HELP_TEXT)
    parser.addoption('--y1', action='store', default=4, help=HELP_TEXT)
    parser.addoption('--x2', action='store', default=5, help=HELP_TEXT)
    parser.addoption('--y2', action='store', default=0, help=HELP_TEXT)


@pytest.fixture(scope='module')
def coordinates(request):
    x0 = request.config.getoption('--x0')
    y0 = request.config.getoption('--y0')
    x1 = request.config.getoption('--x1')
    y1 = request.config.getoption('--y1')
    x2 = request.config.getoption('--x2')
    y2 = request.config.getoption('--y2')
    return {'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2}

