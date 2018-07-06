# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


# test methods
def test_modify_random_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    index = randrange(len(old_groups))
    group = Group(group_name='modified_name')
    group.id = old_groups[index].id
    app.group.modify_by_index(upd_group=group, index=index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group(app):
    app.group.provide()
    old_groups = app.group.get_list()
    group = Group(group_name='modified_name')
    group.id = old_groups[0].id
    app.group.modify_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
