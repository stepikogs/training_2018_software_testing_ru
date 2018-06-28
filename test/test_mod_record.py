# -*- coding: utf-8 -*-
from model.record import Record


# test methods
def test_modify_first_record(app):
    app.record.provide()
    app.record.modify_first(Record(firstname='modified'))
    app.record.modify_first(Record(firstname='modified_again', lastname='modified'))
