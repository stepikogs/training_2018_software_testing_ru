# -*- coding: utf-8 -*-
from model.group import Group
from random import choice


# test methods
def test_modify_random_group(app, db, check_ui):
    app.group.provide()
    old_groups = db.get_group_list()
    group = choice(old_groups)
    donor = Group(group_name='modified_name')
    donor.id = group.id
    app.group.modify_by_id(upd_group=donor, group_id=group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    # replace original group to use updated one for comparison
    old_groups[old_groups.index(group)] = donor
    assert old_groups == new_groups
    if check_ui:
        # todo it should return sorted lists if 'raw' parameter is false
        assert sorted(app.group.get_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_web(app, db, check_ui):
    app.group.provide()
    # take web list intentionally...
    old_groups = app.group.get_list()
    group = Group(group_name='modified_name')
    group.id = old_groups[0].id
    # ...as we need 'first-in-web' group to modify
    app.group.modify_first(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(app.group.get_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
