# -*- coding: utf-8 -*-


# test methods
def test_delete_first_group(app):
    app.group.provide()
    app.group.delete_first()


def test_delete_all_groups(app):
    app.group.provide(count=3)
    app.group.delete_all()
