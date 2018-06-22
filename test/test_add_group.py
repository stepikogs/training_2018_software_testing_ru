# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


# test methods
def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="",
                           header="",
                           footer=""))
    app.session.logout()


def test_add_def_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group())
    app.session.logout()


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="testgroup",
                           header="testheader",
                           footer="testfooter"))
    app.session.logout()
