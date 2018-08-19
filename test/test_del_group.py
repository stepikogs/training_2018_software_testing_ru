# -*- coding: utf-8 -*-
from model.group import Group
from random import choice


# test methods
def test_delete_random_group(app, db, check_ui):
    app.group.provide()
    old_groups = db.get_group_list()
    group = choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        # fixme does not work with multi and traveling spaces
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)


# we can not use db here as we work with the first group in WEB!
def test_delete_first_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    app.group.delete_first()
    new_groups = app.group.get_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[0:1] = []
    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_list(), key=Group.id_or_max)


def test_delete_all_groups(app, db, check_ui):
    app.group.provide(requested=3)
    app.group.delete_all()
    assert len(db.get_group_list()) == 0
    if check_ui:
        assert len(app.group.get_list()) == 0
