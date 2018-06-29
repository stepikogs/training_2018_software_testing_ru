# -*- coding: utf-8 -*-
from model.record import Record


# test methods
def test_modify_first_record(app):
    app.record.provide()
    # modify one field
    app.record.modify_first(Record(firstname='modified'))
    # modify two fields
    app.record.modify_first(Record(firstname='modified_again', lastname='modified'))
