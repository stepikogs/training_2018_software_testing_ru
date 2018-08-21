# -*- coding: utf-8 -*-
from model.group import Group
import pytest


# test methods
def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I create %s group' % group):
        app.group.create(group)
    with pytest.allure.step('the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(app.group.get_list(), key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
