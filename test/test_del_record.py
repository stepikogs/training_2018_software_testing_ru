# -*- coding: utf-8 -*-
from random import randrange


# test methods
def test_delete_random_record(app):
    app.record.provide()
    old_rec = app.record.get_list()
    index = randrange(len(old_rec))
    app.record.delete_by_index(index)
    assert len(old_rec) - 1 == app.record.count()
    new_rec = app.record.get_list()
    old_rec[index:index+1] = []
    assert old_rec == new_rec


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
