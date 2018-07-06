# -*- coding: utf-8 -*-
from model.record import Record


# test methods
def test_modify_first_record(app):
    app.record.provide()
    old_rec = app.record.get_list()
    record = Record(firstname='modified_again', lastname='modified')
    record.id = old_rec[0].id
    app.record.modify_first(record)
    new_rec = app.record.get_list()
    assert len(old_rec) == len(new_rec)
    old_rec[0] = record
    assert sorted(old_rec, key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)
