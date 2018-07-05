# -*- coding: utf-8 -*-


# test methods
def test_delete_first_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    app.group.delete_first()
    new_groups = app.group.get_list()
    assert len(old_groups) - 1 == len(new_groups)


def test_delete_all_groups(app):
    app.group.provide(count=3)
    app.group.delete_all()
    new_groups = app.group.get_list()
    # no groups left as result
    assert len(new_groups) == 0
