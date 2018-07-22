# -*- coding: utf-8 -*-
from model.record import Record


# test methods
def test_add_record(app, json_records):
    record = json_records
    old_rec = app.record.get_list()
    app.record.create(record)
    assert len(old_rec) + 1 == app.record.count()
    new_rec = app.record.get_list()
    old_rec.append(record)
    assert sorted(old_rec, key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)
