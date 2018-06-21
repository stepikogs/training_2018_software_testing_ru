# -*- coding: utf-8 -*-
import pytest
from classes.record import Record
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_record(app):
    app.login(username="admin", password="secret")
    app.create_record(Record(firstname="testname",
                             lastname="testlast",
                             midname="testmid",
                             nickname="testnick",
                             title="testtitle",
                             company="testcompany",
                             address="testaddr",
                             phone="testphone",
                             mobile="testmob",
                             work="testwork",
                             fax="testfax",
                             mail1="tesmmail1",
                             mail2="testmail2",
                             mail3="testmail3",
                             page="testpage",
                             bday=12,  # the twelfth
                             bmon=2,  # of February
                             byear="1986",
                             aday=13,  # the thirteenth
                             amon=8,  # of August
                             ayear="2003",
                             second_address="testsecaddr",
                             second_phone="testhomesec",
                             notes="testnotes"
                             ))
    app.logout()


def test_add_def_record(app):
    app.login(username="admin", password="secret")
    app.create_record(Record())
    app.logout()


def test_add_empty_record(app):
    app.login(username="admin", password="secret")
    app.create_record(Record(firstname="",
                             lastname="",
                             midname="",
                             nickname="",
                             title="",
                             company="",
                             address="",
                             phone="",
                             mobile="",
                             work="",
                             fax="",
                             mail1="",
                             mail2="",
                             mail3="",
                             page="",
                             byear="",
                             ayear="",
                             second_address="",
                             second_phone="",
                             notes=""
                             ))
    app.logout()
