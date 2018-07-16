# -*- coding: utf-8 -*-
from model.record import Record
import pytest
import random
import string


def random_string(prefix, maxlength, phone=False):
    symbols = string.digits + ' +-()asd' if phone else string.ascii_letters + string.digits  # + ' '*10
    # fixme: work with multi-space
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [
   Record(
       firstname=random_string('firstname', 10),
       lastname=random_string('lastname', 10),
       home=random_string('', 10, phone=True),
       email=random_string('n', 10)+'@'+random_string('d', 8)+'.morg',
       address=random_string('address: ', 50),
       bmonth=random.randrange(13),
   )
   for i in range(5)
] + \
[
   Record(firstname="name_assigned",
          bday=23,
          jeegurda='incorrect',
          lastname='lastname_assigned'),
   Record(firstname="name_assigned",
          bday=23,
          jeegurda='incorrect',
          lastname='lastname_assigned'),
   Record(
       photo="C:\\Users\\python\\PycharmProjects\\training_2018_software_testing_ru\\playground\\239005.jpg"),
   Record(
       photo="C:\\Users\\python\\PycharmProjects\\training_2018_software_testing_ru\\playground\\239005.jpg",
       firstname='me is having photo',
       bday=23,
       bmonth=7,
       byear=1976,
       jeegurda='ignore it'),
   Record(),
   Record(firstname="",
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
          notes=""),
   Record(firstname="testname",
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
          bmonth=2,  # of February
          byear="1986",
          aday=13,  # the thirteenth
          amonth=8,  # of August
          ayear="2003",
          address2="testsecaddr",
          phone2="testhomesec",
          notes="testnotes"
          )
]


@pytest.mark.parametrize('record', testdata, ids=[repr(x) for x in testdata])
def test_add_record(app, record):
    old_rec = app.record.get_list()
    app.record.create(record)
    assert len(old_rec) + 1 == app.record.count()
    new_rec = app.record.get_list()
    old_rec.append(record)
    assert sorted(old_rec, key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)
