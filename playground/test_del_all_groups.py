# -*- coding: utf-8 -*-
from model.group import Group


# pre-conditions - create some records to delete
def test_add_dummy_groups(app):
    names = ['one', 'two', 'three', 'four', 'five']
    for i in range(5):
        app.group.create(Group(group_name=names[i]))


# test methods
def test_delete_all_groups(app):
    app.group.delete_all()
