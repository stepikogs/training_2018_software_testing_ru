# -*- coding: utf-8 -*-
from random import choice
from model.record import Record
import time


# test methods
def test_delete_random_record(app, db, check_ui):
    app.record.provide()
    old_rec = db.get_record_list()
    # old_rec = app.record.get_list()
    # index = randrange(len(old_rec))
    record = choice(old_rec)
    app.record.delete_by_id(record.id)
    time.sleep(1)  # todo temp solution. here we should wait 'Record deleted' message
    new_rec = db.get_record_list()
    assert len(old_rec) - 1 == len(new_rec)
    old_rec.remove(record)
    # todo still does not work with multi and traveling spaces
    assert old_rec == new_rec
    if check_ui:
        assert sorted (new_rec, key=Record.id_or_max) == sorted(app.record.get_list(), key=Record.id_or_max)


# the rest of tests have been intentionally not updated to use db... yet
def test_delete_first_record(app):
    app.record.provide()
    old_rec = app.record.get_list()
    app.record.delete_first()
    assert len(old_rec) - 1 == app.record.count()
    new_rec = app.record.get_list()
    old_rec[0:1] = []
    assert old_rec == new_rec


def test_delete_all_records(app):
    app.record.provide(requested=3)
    app.record.delete_all()
    # no groups left
    assert app.record.count() == 0
