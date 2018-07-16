__author__ = 'George Stepiko'
from model.record import Record
import re
from random import randrange


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
    # app.record.delete_all()
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
    assert record_from_home._phones_from_home == homepage_like_set(record_from_edit, record_from_edit._phones)


''' commented out as has been not refactored with backward checks yet.
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
'''


def test_compare_homepage_properties_with_edit_page_values_for_random_record(app):
    # provide record if there is no record on the page
    app.record.provide(record=Record(firstname='John',  # i use one word for names
                                     lastname='Smith',
                                     address='111 Jeegurda street apt 234 Another YE 00000 DFR',
                                     home='+11111111111',  # mobile has been intentionally not set
                                     work='1 333 333 3333',
                                     phone2='1-444-444-4444',
                                     email='user1@domain.name',  # email 2 has been intentionally not set
                                     email3='user3@domain.name'))
    # set random index to take record from list of existing records
    record_index = randrange(app.record.count())
    # get text properties from home page table for random record
    record_from_home = app.record.get_list()[record_index]
    # get all the fields from edit page for the record selected (names and phones included as requested)
    record_from_edit = app.record.get_info_from_edit(record_index, htmlized=True)
    # assert names
    assert record_from_home.firstname == record_from_edit.firstname
    assert record_from_home.lastname == record_from_edit.lastname
    # assert address
    print('home: ', record_from_home.address)
    assert record_from_home.address == record_from_edit.address
    # assert phones (backward check here)
    assert record_from_home._phones_from_home == homepage_like_set(record_from_edit,
                                                                   set_to_arrange=record_from_edit._phones)
    # assert emails (backward check here)
    assert record_from_home._emails_from_home == homepage_like_set(record_from_edit,
                                                                   set_to_arrange=record_from_edit._emails)


# service methods
def clear_chars(raw_string):
    return re.sub('[() -]', '', raw_string)


def homepage_like_set(recorded, set_to_arrange):
    # phone_types = ('home', 'mobile', 'work', 'phone2')
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear_chars(x) if set_to_arrange == recorded._phones else x,
                                filter(lambda x: x is not None,
                                       [getattr(recorded, element) for element in set_to_arrange]))))
