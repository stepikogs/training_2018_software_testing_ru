# -*- coding: utf-8 -*-
from model.record import Record
from random import choice


# test methods
def test_modify_random_record(app, db, check_ui):
    app.record.provide()
    old_rec = db.get_record_list()
    record = choice(old_rec)
    donor = Record(firstname='modified_again', lastname='modified')
    donor.id = record.id
    app.record.modify_by_id(upd_record=donor, rec_id=record.id)
    new_rec = db.get_record_list()
    assert len(old_rec) == len(new_rec)
    old_rec[old_rec.index(record)] = donor
    assert old_rec == new_rec
    if check_ui:
        assert sorted(app.record.get_list(), key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)


# this test has been intentionally not updated yet.
def test_modify_first_record(app):
    app.record.provide()
    old_rec = app.record.get_list()
    record = Record(firstname='modified_again', lastname='modified')
    record.id = old_rec[0].id
    app.record.modify_first(record)
    assert len(old_rec) == app.record.count()
    new_rec = app.record.get_list()
    old_rec[0] = record
    assert sorted(old_rec, key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)
