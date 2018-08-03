# -*- coding: utf-8 -*-
from model.record import Record


# test methods
def test_add_record(app, db, json_records, check_ui):
    record = json_records
    old_rec = db.get_record_list()
    app.record.create(record)
    new_rec = db.get_record_list()
    assert len(old_rec) + 1 == len(new_rec)
    old_rec.append(record)
    assert sorted(old_rec, key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)
    if check_ui:
        assert sorted(app.record.get_list(), key=Record.id_or_max) == sorted(new_rec, key=Record.id_or_max)
