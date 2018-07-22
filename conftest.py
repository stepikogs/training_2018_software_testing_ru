__author__ = 'George Stepiko'
import pytest
from fixture.application import Application
import json
import jsonpickle
import os.path
import importlib

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


def pytest_generate_tests(metafunc):
    for our_fixture in metafunc.fixturenames:
        if our_fixture.startswith('data_'):
            testdata = load_from_module(our_fixture[5:])
            metafunc.parametrize(our_fixture, testdata, ids=[str(x) for x in testdata])
        elif our_fixture.startswith('json_'):
            testdata = load_from_json(our_fixture[5:])
            metafunc.parametrize(our_fixture, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module('data.%s' % module).testdata


def load_from_json(jsonFile):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/%s.json' % jsonFile)) as source:
        return jsonpickle.decode(source.read())
