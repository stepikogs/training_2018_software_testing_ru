# -*- coding: utf-8 -*-
from model.record import Record


# pre-conditions - get some records to delete
def test_add_dummy_records(app):
    for i in range(5):
        app.record.create(Record(firstname="name_of_"+str(i)))


# test methods
def test_delete_all_records(app):
    app.record.delete_all()