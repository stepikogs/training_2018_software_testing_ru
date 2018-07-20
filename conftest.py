__author__ = 'George Stepiko'
import pytest
from fixture.application import Application
import json
import os.path

fixture = None
target = None


@pytest.fixture  # (scope='session')
def app(request):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption('--target'))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])
    fixture.session.ensure_login(username=target['username'], password=target['password'])
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finik():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(finik)
    return fixture


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--target', action='store', default='target.json')
    # parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/')
