__author__ = 'George Stepiko'
from model.record import Record
import re


def test_phones_on_home_page(app):
    """
    preconditions:
    1. delete all the records as first record (previous tests leftover) could have no phones at all
    2. create new record with all the four phones defined

    steps
    1. read record attributes from its row on home page table
    2. read record attributes from its edit page
    3. compare two records by phones

    expectations
    phones must be identical

    """
    # according to task we work with the first record in list for ths test
    record_index = 0

    # preconditions
    # delete all the records
    app.record.delete_all()
    # provide record with all the phones inside
    app.record.provide(record=Record(firstname='dummyfirstname',  # i use one word for names
                                     lastname='dummylastname',
                                     home='11111111111',  # as format is not verified - 10 digits here
                                     mobile='12222222222',
                                     work='13333333333',
                                     phone2='14444444444'))

    # test starts here
    # get fields from home page
    record_from_home = app.record.get_list()[record_index]
    # get all the fields from edit page for the record selected (names and phones included as requested)
    record_from_edit = app.record.get_info_from_edit(record_index)
    # print('final TEST out')  # debug print
    # print(record_from_edit)  # debug print
    assert record_from_home.home == record_from_edit.home
    assert record_from_home.mobile == record_from_edit.mobile
    assert record_from_home.work == record_from_edit.work
    assert record_from_home.phone2 == record_from_edit.phone2


def test_phones_on_home_page_spec_chars(app):
    """
    preconditions:
    1. delete all the records as first record (previous tests leftover) could have no phones at all
    2. create new record with all the four phones defined

    steps
    1. read record attributes from its row on home page table
    2. read record attributes from its edit page
    3. compare two records by phones

    expectations
    phones must be identical

    """
    # according to task we work with the first record in list for ths test
    record_index = 0

    # preconditions
    # delete all the records
    app.record.delete_all()
    # provide record with all the phones inside
    app.record.provide(record=Record(firstname='dummyfirstname',  # i use one word for names
                                     lastname='dummylastname',
                                     home='+11111111111',
                                     mobile='1(222)2222222',
                                     work='1 333 333 3333',
                                     phone2='1-444-444-4444'))

    # test starts here
    # get fields from home page
    record_from_home = app.record.get_list()[record_index]
    # get all the fields from edit page for the record selected (names and phones included as requested)
    record_from_edit = app.record.get_info_from_edit(record_index)
    # print('final TEST out')  # debug print
    # print(record_from_edit)  # debug print
    assert record_from_home.home == clear_chars(record_from_edit.home)
    assert record_from_home.mobile == clear_chars(record_from_edit.mobile)
    assert record_from_home.work == clear_chars(record_from_edit.work)
    assert record_from_home.phone2 == clear_chars(record_from_edit.phone2)


def test_phones_on_record_view_page(app):
    """
        preconditions:
        1. delete all the records as first record (previous tests leftover) could have no phones at all
        2. create new record with all the four phones defined

        steps
        1. read record attributes from its row on home page table
        2. read record attributes from its edit page
        3. compare two records by phones

        expectations
        phones must be identical

        """
    # according to task we work with the first record in list for ths test
    record_index = 0

    # preconditions
    # delete all the records
    app.record.delete_all()
    # provide record with all the phones inside
    app.record.provide(record=Record(firstname='dummyfirstname',  # i use one word for names
                                     lastname='dummylastname',
                                     home='+11111111111',
                                     mobile='1(222)2222222',
                                     work='1 333 333 3333',
                                     phone2='1-444-444-4444'))

    # test starts here
    # get fields from home page
    record_from_view = app.record.get_phones_from_view(record_index)
    # get all the fields from edit page for the record selected (names and phones included as requested)
    record_from_edit = app.record.get_info_from_edit(record_index)
    # print('final TEST out')  # debug print
    # print(record_from_edit)  # debug print
    assert record_from_view.home == record_from_edit.home
    assert record_from_view.mobile == record_from_edit.mobile
    assert record_from_view.work == record_from_edit.work
    assert record_from_view.phone2 == record_from_edit.phone2


# service methods
def clear_chars(str):
    return re.sub('[() -]', '', str)
