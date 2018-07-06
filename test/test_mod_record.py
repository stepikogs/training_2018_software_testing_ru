# -*- coding: utf-8 -*-
from model.record import Record
from random import randrange


# test methods
def test_modify_random_record(app):
    app.record.provide()
    old_rec = app.record.get_list()
    index = randrange(len(old_rec))
    record = Record(firstname='modified_again', lastname='modified')
    record.id = old_rec[index].id
    app.record.modify_by_index(index=index, upd_record=record)
    assert len(old_rec) == app.record.count()
    new_rec = app.record.get_list()
    old_rec[index] = record
    assert sorted(old_rec, key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)


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
