# -*- coding: utf-8 -*-


# test methods
def test_delete_first_record(app):
    app.record.provide()
    app.record.delete_first()


def test_delete_all_records(app):
    app.record.provide(count=3)
    app.record.delete_all()
