# -*- coding: utf-8 -*-
from random import randrange


# test methods
def test_delete_random_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    app.group.delete_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index: index+1] = []
    assert old_groups == new_groups


def test_delete_first_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    app.group.delete_first()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_list()
    old_groups[0:1] = []
    assert old_groups == new_groups


def test_delete_all_groups(app):
    app.group.provide(requested=3)
    app.group.delete_all()
    assert app.group.count() == 0
