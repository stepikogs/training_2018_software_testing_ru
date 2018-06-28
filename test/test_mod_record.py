# -*- coding: utf-8 -*-
from model.record import Record


# test methods
def test_modify_first_record(app):
    app.session.login(username="admin", password="secret")
    app.record.modify_first(Record(firstname='modified'))
    app.record.modify_first(Record(firstname='modified_again', lastname='modified'))
    app.session.logout()
