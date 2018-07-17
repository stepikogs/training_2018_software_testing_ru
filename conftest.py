__author__ = 'George Stepiko'
import pytest
from fixture.application import Application

fixture = None


@pytest.fixture  # (scope='session')
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    base_url = request.config.getoption('--baseUrl')
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    elif not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username="admin", password="secret")
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
    parser.addoption('--baseUrl', action='store', default='http://localhost/addressbook/')
