__author__ = 'George Stepiko'
from random import choice
from fixture.orm import OrmFixture

orm_base = OrmFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_record_with_group(app, db):
    # preconditions: 1 group and 1 record required
    app.group.provide()
    app.record.provide()
    # get groups ant take random one
    acceptor = choice(db.get_group_list())
    # get records and take one
    donor = choice(db.get_record_list())
    print(donor)
    # get current 'in group' records (supposed to be empty but...)
    in_group = orm_base.get_records_in_group(acceptor)
    assert donor not in in_group  # is False
    # add record to group
    app.record.add_record_to_group_by_ids(record=donor, group=acceptor)
    # assertions
    in_group = orm_base.get_records_in_group(acceptor)
    assert donor in in_group  # is True
    # postconditions: delete it from group
    app.record.remove_record_from_group_by_ids(record=donor, group=acceptor)
    # postcondition assertions
    in_group = orm_base.get_records_in_group(acceptor)
    assert donor not in in_group  # is False
