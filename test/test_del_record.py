# -*- coding: utf-8 -*-


# test methods
def test_delete_first_record(app):
    app.record.provide()
    old_rec = app.record.get_list()
    app.record.delete_first()
    new_rec = app.record.get_list()
    assert len(old_rec) - 1 == len(new_rec)
    old_rec[0:1] = []
    assert old_rec == new_rec


def test_delete_all_records(app):
    app.record.provide(requested=3)
    app.record.delete_all()
    new_rec = app.record.get_list()
    # no groups left
    assert len(new_rec) == 0
