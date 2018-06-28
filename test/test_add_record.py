# -*- coding: utf-8 -*-
from model.record import Record


def test_add_def_record(app):
    app.record.create(Record())


def test_add_group_wrong_attributes(app):
    # preparation phase
    rcrd = Record(firstname="name_assigned",
                  bday=23,
                  jeegurda='incorrect',
                  lastname='lastname_assigned')
    # creation phase
    app.record.create(rcrd)


def test_add_record_with_photo_only(app):
    # prepare record with photo
    rcrd = Record(photo="C:\\Users\\python\\PycharmProjects\\training_2018_software_testing_ru\\playground\\239005.jpg")
    # create it
    app.record.create(rcrd)


def test_add_record_with_photo(app):
    # prepare record with photo
    rcrd = Record(photo="C:\\Users\\python\\PycharmProjects\\training_2018_software_testing_ru\\playground\\239005.jpg",
                  firstname='me is having photo',
                  bday=23,
                  bmonth=7,
                  byear=1976,
                  jeegurda='ignore it')
    # create it
    app.record.create(rcrd)


def test_add_empty_record(app):
    app.record.create(Record(firstname="",
                             lastname="",
                             middlename="",
                             nickname="",
                             title="",
                             company="",
                             address="",
                             home="",
                             mobile="",
                             work="",
                             fax="",
                             email="",
                             email2="",
                             email3="",
                             homepage="",
                             byear="",
                             ayear="",
                             address2="",
                             phone2="",
                             notes=""
                             ))


def test_add_record(app):
    app.record.create(Record(firstname="testname",
                             lastname="testlast",
                             middlename="testmid",
                             nickname="testnick",
                             title="testtitle",
                             company="testcompany",
                             address="testaddr",
                             home="testphone",
                             mobile="testmob",
                             work="testwork",
                             fax="testfax",
                             email="tesmmail1",
                             email2="testmail2",
                             email3="testmail3",
                             homepage="testpage",
                             bday=12,  # the twelfth
                             bmonth=2,   # of February
                             byear="1986",
                             aday=13,  # the thirteenth
                             amonth=8,   # of August
                             ayear="2003",
                             address2="testsecaddr",
                             phone2="testhomesec",
                             notes="testnotes"
                             ))
