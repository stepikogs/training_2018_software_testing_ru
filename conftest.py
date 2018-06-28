__author__ = 'George Stepiko'
import pytest
from fixture.application import Application

fixture = None


@pytest.fixture  # (scope='session')
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    elif not fixture.is_valid():
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def finik():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(finik)
    return fixture
